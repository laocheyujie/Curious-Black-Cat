from instructions import black_cat_instructions
from functions import get_city_for_date, get_qa
from dall_e_3 import get_dalle_image
from assistant import create_assistant, create_thread, get_completion


def main(debug=False):
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
    )

    # 创建 Thread
    thread_id = create_thread()

    # 创建函数调用列表
    funcs = [get_city_for_date, get_qa, get_dalle_image]
    # 根据输入获取回答
    while True:
        user_input = input("你：")
        message = get_completion(assistant_id, thread_id, user_input, funcs, debug)
        print("小黑：", message)


if __name__ == "__main__":
    debug = True
    main(debug)