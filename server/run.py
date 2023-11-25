import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from instructions import black_cat_instructions
from functions import get_city_for_date, get_qa
from dall_e_3 import get_dalle_image
from assistant import create_assistant, create_thread, get_completion


# 创建 FastAPI 实例
app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的来源列表
    allow_credentials=True,
    allow_methods=["*"],  # 允许的方法
    allow_headers=["*"],  # 允许的头部
)

# 定义数据模型
class ChatMessage(BaseModel):
    message: str
    thread_id: str
    
DEBUG = True

# 创建 Assistant
assistant_id = create_assistant(
    name="好奇的黑猫",
    instructions=black_cat_instructions,
    model="gpt-4-1106-preview",
    tools=[
        {
            "type": "retrieval"  # 知识检索
        },
        {
            "type": "code_interpreter"  # 代码解释器
        },
        {
            "type": "function",  # 用于获取当前日期所在城市的函数
            "function": {
                "name": "get_city_for_date",
                "description": "根据传入的日期获取对应的城市.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date_str": {
                            "type": "string",
                            "description": "用于获取对应城市的日期，格式为YYYY-MM-DD."
                        },
                    },
                    "required": ["date_str"]
                }
            }
        },
        {
            "type": "function",  # 用于获取问题和答案的函数
            "function": {
                "name": "get_qa",
                "description": "获取黑猫好奇的问题和答案，返回包含问题和答案的字典.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "Category of curiosity."
                        },
                    },
                    "required": []
                }
            }
        },
        {
            "type": "function",  # 用于获取图片
            "function": {
                "name": "get_dalle_image",
                "description": "根据传入的prompt生成图片.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "prompt": {
                            "type": "string",
                            "description": "Prompt of DALL-E 3."
                        },
                    },
                    "required": ["prompt"]
                }
            }
        }
    ],
    files=["../data/knowledge.txt"],
    debug=DEBUG
)

# 创建函数调用列表
funcs = [get_city_for_date, get_qa, get_dalle_image]


@app.get("/create_thread")
async def create_thread_endpoint():
    # 创建 Thread
    thread_id = create_thread(debug=DEBUG)
    return {"thread_id": thread_id}

@app.post("/chat")
async def chat_endpoint(request: ChatMessage):
    # 处理请求，返回响应
    message = main(request.message, request.thread_id, debug=DEBUG)
    if isinstance(message, dict) and "image" in message.keys():
        return {
            "message": "",
            "image": message["image"]
        }
    return {
        "message": message,
        "image": ""
    }

def main(query, thread_id, debug=False):
    # 根据输入获取回答
    message = get_completion(assistant_id, thread_id, query, funcs, debug)
    return message


if __name__ == "__main__":
    uvicorn.run(app, port=8000)