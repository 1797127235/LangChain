from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import Runnable, RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
import os

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)

#提示词模板
#方式1
# prompt = PromptTemplate(
#     template="介绍{city}的历史",
#     input_variables=["city"],
# )

#方式2
prompt = PromptTemplate.from_template("将文本从{language_from}翻译成{language_to}")

#调用实例化模板
res =prompt.invoke({
    "language_from": "中文",
    "language_to": "英文",
})
print(res)


#处理聊天消息模板
chat_prompt = ChatPrompTemplate(
    [
        ("System","将文本从{language_from}翻译成{language_to}"),
        ("user","{text}")
    ]
)






