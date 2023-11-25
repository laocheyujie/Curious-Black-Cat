# 好奇的黑猫

<p align="center">
   📺<a href="https://space.bilibili.com/330394387" target="_blank">bilibili</a> • 🌐 <a href="https://github.com/laocheyujie" target="_blank">Github • ▶️ <a href="https://www.youtube.com/channel/UCzuN1k1nnakatRg8kfT4M6A" target="_blank">YouTube</a>
</p>
<p align="center">
    👋 如果喜欢，右上角请给一个小星星 ⭐
</p>

_Read this in [English](README_en.md)._

## 介绍
这是一个 OpenAI Assistance API 的使用演示，包含了前后端完整代码。

## 背景
在我的童年，有一只黑猫给了我很多快乐。

他的眼睛就像装了一整个宇宙，他黑色的毛发在阳光照耀下会泛出一点儿紫金色，特好看。

这个人巨能闹腾，叫声嘹亮刺耳，活力十足，白天邻居在后山上都能看到他。

每天放学后推开门，他就从我家平台上跑下来，找我玩儿。

可惜他后来误吃了邻居家的老鼠药，早早地离开了。

这个项目是用 OpenAI 的 Assistant API 构建的“好奇的黑猫”。

他对世界充满了好奇，每天都会出现在中国的一个城市，如果我想他了，他还可以给我发送他现在的照片。

我知道现在的技术对未来有着非常宏大辽阔的意义，甚至未来的人在像我一样回忆童年时，怀念的可能是陪伴他童年的某个 AI 智能体。

而在这个周末的晚上，我只是突然又想念起我童年的老朋友了。

## 使用
### API Key
首先修改`.env` 的 API KEY

- OPENAI_API_KEY 到 [API keys - OpenAI API](https://platform.openai.com/api-keys) 获取
- NINJAS_API_KEY 到 [API Ninjas](https://api-ninjas.com/profile) 获取

### Server
1. 安装 anaconda 或 miniconda：自行搜索安装方法
2. 创建 Python 虚拟环境
```bash
conda create -n cat python=3.11
```
3. 进入 Python 虚拟环境
```bash
conda activate cat
```
4. 安装项目依赖
```bash
cd server
pip install -r requirements.txt
```
5. 启动后端 server
```bash
python run.py
```

### Web
1. 安装 Node.js：自行搜索安装方法
2. 安装依赖
```bash
cd web
npm i
# or
yarn
```
3. 运行前端 web
```bash
npm run dev
# or
yarn dev
```

### 网页使用
打开浏览器，输入地址：`127.0.0.1:3000` 

## 注意
如果使用 WSL，请在代码中相应地修改 `127.0.0.1` 为主机 IP 地址
