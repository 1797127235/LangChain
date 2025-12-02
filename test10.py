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

class Person(BaseModel):
    '''人'''
    name: Optional[str] = Field(description="人姓名")
    hair_color: Optional[str] = Field(description="人头发颜色")
    skin_color: Optional[str] = Field(description="人皮肤颜色")
    height_in_meters: Optional[float] = Field(description="人身高,单位:米")


structured_model = model.with_structured_output(schema=Person)

message = [
    HumanMessage(content="我是张三,我的头发是棕色的,我的皮肤是黄色的,我的身高是1.8米"),
    SystemMessage(content="你是一个信息提取专家，只从文本提取相关信息，如果你不知道要提取的属性，属性值返回null")
]

res = structured_model.invoke(message)
print(res)
