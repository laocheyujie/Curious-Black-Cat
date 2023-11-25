# Curious Black Cat

<p align="center">
   📺<a href="https://space.bilibili.com/330394387" target="_blank">bilibili</a> • 🌐 <a href="https://github.com/laocheyujie" target="_blank">Github</a> • ▶️ <a href="https://www.youtube.com/channel/UCzuN1k1nnakatRg8kfT4M6A" target="_blank">YouTube</a>
</p>
<p align="center">
    👋 If you like it, please give a little star in the top right corner. ⭐
</p>

_Read this in [Chinese](README.md)._

## Introduction
This is a demonstration of using the OpenAI Assistant API, including complete front-end and back-end code.

## Background
In my childhood, a black cat brought me a lot of joy.

His eyes were like an entire universe, and his black fur would shimmer with a purplish-gold hue under the sunlight, looking particularly beautiful.

This cat was extremely lively, with a loud and piercing meow, full of energy, visible to the neighbors on the hill behind during the day.

Every day after school, as soon as I opened the door, he would run down from the platform of my house to play with me.

Unfortunately, he later accidentally ate rat poison from a neighbor's house and left me too soon.

This project is the "Curious Black Cat" built using OpenAI's Assistant API.

He is full of curiosity about the world and appears in a city in China every day. If I miss him, he can also send me his current picture.

I know that today's technology has a very grand and vast significance for the future, to the extent that people in the future, when reminiscing about their childhood like I do, may fondly remember an AI agent that accompanied them through their childhood.

And on this weekend evening, I just suddenly missed my old friend from my childhood again.

## Usage
### API Key
First, modify the API KEY in `.env`

- OPENAI_API_KEY from [API keys - OpenAI API](https://platform.openai.com/api-keys)
- NINJAS_API_KEY from [API Ninjas](https://api-ninjas.com/profile)

### Server
1. Install anaconda or miniconda: search for installation methods
2. Create a Python virtual environment
```bash
conda create -n cat python=3.11
```
3. Enter the Python virtual environment
```bash
conda activate cat
```
4. Install project dependencies
```bash
cd server
pip install -r requirements.txt
```
5. Start the backend server
```bash
python run.py
```

### Web
1. Install Node.js: search for installation methods
2. Install dependencies
```bash
cd web
npm i
# or
yarn
```
3. Run the frontend web
```bash
npm run dev
# or
yarn dev
```

### Web Usage
Open a browser and enter the address: `127.0.0.1:3000` 

## Caution
If using WSL (Windows Subsystem for Linux), please modify `127.0.0.1`  in the code to the host IP address accordingly.
