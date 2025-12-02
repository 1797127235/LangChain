from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional,TypedDict,Annotated
from langchain_core.messages import HumanMessage,SystemMessage
import os

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature = 0.2,
)

for chunk in model.stream("写一段关于春天的作文，1000字"):
    print(chunk.content, end="", flush=True)

