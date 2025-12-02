from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional,TypedDict,Annotated
from langchain_core.messages import HumanMessage,SystemMessage
from typing import List
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


class Date(BaseModel):
    prople: List[Person] = Field(description="人员列表")

structured_model = model.with_structured_output(schema=Date)

messages = [
    SystemMessage(content="你是一个信息提取专家，只从文本中提取信息，你如果不知道，属性值返回null"),
    HumanMessage(content="蓝球场上，身高两米的中锋王伟默契地将球传给一米七的后卫李明，完成一记绝杀")
]

res= structured_model.invoke(messages)
print(res)