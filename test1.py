"""Google Generative AI + LangChain 入门示例."""

from __future__ import annotations

import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI



def main() -> None:
    api_key = os.getenv("GOOGLE_API_KEY")

    llm = ChatGoogleGenerativeAI(
        # model="gemini-3-pro-preview",
        model = "gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.2,
    )

    messages = [
        SystemMessage(content="你是一个问题解决专家"),
        HumanMessage(content="加入我一晚没睡觉，但我明天有一上午的课我该怎么办")
    ]

    #定义输出解析器
    parser = StrOutputParser()

    #定义链
    chain = llm | parser

    print('开始调用')
    text = chain.invoke(messages)
    print("=== 模型回复 ===")
    print(text)


if __name__ == "__main__":
    main()