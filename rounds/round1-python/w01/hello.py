import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()          # 自动向上找到 D:\agent-journey\.env

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "用一句话解释什么是智能体"}],
)
print(resp.choices[0].message.content)
