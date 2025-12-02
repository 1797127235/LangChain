from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import Runnable, RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
import os

#多轮对话

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]



config = {
    "configurable": {
        "session_id": "1"
    }
}

model_with_history = RunnableWithMessageHistory(model,get_session_history)

model_with_history.invoke(
    [
        HumanMessage(content="我是小明你好")
    ],
    config = config
).pretty_print()




model_with_history.invoke(
    [
        HumanMessage(content="请问我是谁")
    ],
    config = config
).pretty_print()


