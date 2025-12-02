from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
import os

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature = 0.2,
)

#定义工具
tool = TavilySearch(
    max_results=4,
    tavily_api_key = "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",
)

model_with_tools = model.bind_tools([tool])

question = "香港大火调查进展如何"

#定义消息列表 
messages = [
    SystemMessage(content="你是一个新闻搜索专家，请根据用户的问题搜索相关新闻"),
    HumanMessage(content=question)
]

ai_msg = model_with_tools.invoke(messages)
messages.append(ai_msg)


tool_message = []

for tool_call in ai_msg.tool_calls:
    tool_result = tool.invoke(tool_call["args"])

    tool_msg = ToolMessage(
        content = str(tool_result),
        tool_call_id = tool_call["id"],
    )

    tool_message.append(tool_msg)
    messages.append(tool_msg)

final_msg = model.invoke(messages).content

print(final_msg)
