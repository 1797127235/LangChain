import os
from typing import Annotated

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import ToolMessage

@tool
def add(
    a: Annotated[int, "第一个参数"],
    b: Annotated[int, "第二个参数"],
):
    '''
    两数相加
    '''
    return a + b


@tool
def multiply(
    a: Annotated[int, "第一个参数"],
    b: Annotated[int, "第二个参数"],
):
    '''
    两数相乘
    '''
    return a * b

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature = 0.2,
)


#绑定工具
tools = [add,multiply]
model_with_tools =  model.bind_tools(tools = tools)
question = "请你先用工具算 2乘以3，再顺便算一下 6加6，一并告诉我两个结果。"

ai_msg = model_with_tools.invoke(question)
print("模型决策:", ai_msg)

#自动执行工具

#第一步：模型决定要调用哪个工具
ai_msg = model_with_tools.invoke(question)

#工具调用信息 此时只会调用一个工具
tool_message = []

for tool_call in ai_msg.tool_calls:
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    if tool_name == "multiply":
        tool_result = multiply.invoke(tool_args)
    elif tool_name == "add":
        tool_result = add.invoke(tool_args)
    else:
        raise ValueError(f"未知工具: {tool_name}")

    print("工具实际执行结果:", tool_result)  # 这里就是 6
    
    tool_message.append(
        ToolMessage(
            content = str(tool_result),
            tool_call_id = tool_call["id"],
        )
    )
    
    final_msg = model_with_tools.invoke(
        [
            HumanMessage(content=question),
            ai_msg,
            *tool_message
        ]
    )
    print("最终回答",final_msg.content)    

    




