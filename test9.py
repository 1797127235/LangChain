from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional,TypedDict,Annotated
import os

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature = 0.2,
)


class Joke(BaseModel):
    '''给用户讲一个笑话'''
    setup: str = Field(description="这个笑话的开头")
    punchline: str = Field(description="这个笑话的妙语")
    rating: Optional[int] = Field(description="这个笑话的评分,1-10分")

class Response(BaseModel):
    '''笑话回复'''
    content: str = Field(description="笑话的回复内容")


class FinalResponse(BaseModel):
    '''最终回复,选择合适的输出结构'''
    joke: Joke = Field(description="用户的笑话")
    response: Response = Field(description="笑话的回复")


model_with_stuctured = model.with_structured_output(FinalResponse)

print(model_with_stuctured.invoke("你是谁"))
