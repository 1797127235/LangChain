import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model

def main():
    # 环境变量准备好
    google_key = os.getenv("GOOGLE_API_KEY")
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")

    # 1. 创建一个“可配置模型”，不指定 model，这样 model 和 model_provider 默认可配置
    base_model = init_chat_model(
        temperature=0.2,   # 其他参数通用
    )

    parser = StrOutputParser()
    chain = base_model | parser

    messages = [
        SystemMessage(content="你是一个问题解决专家"),
        HumanMessage(content="怎么左脚踩右脚上天"),
    ]

    # 2. 调用 Google Gemini
    print("=== Google Gemini ===")
    text_google = chain.invoke(
        messages,
        config={
            "configurable": {
                "model": "gemini-2.5-flash",
                "model_provider": "google_genai",
            },
            "google_api_key": google_key,
        },
    )
    print(text_google)

    # 3. 调用 DeepSeek
    print("=== DeepSeek ===")
    text_deepseek = chain.invoke(
        messages,
        config={
            "configurable": {
                "model": "deepseek-chat",
                "model_provider": "deepseek",
            },
            "api_key": deepseek_key,
            "base_url": "https://api.deepseek.com",
        },
    )
    print(text_deepseek)

if __name__ == "__main__":
    main()
