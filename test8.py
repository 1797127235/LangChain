from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional,TypedDict,Annotated
import os

model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = os.getenv("GOOGLE_API_KEY"),
    temperature = 0.2,
)

class Joke1(BaseModel):
    setup: str = Field(description="这个笑话的开头")
    punchline: str = Field(description="这个笑话的妙语")
    rating: Optional[int] = Field(description="这个笑话的评分,1-10分")

#Typeddict
class Joke(TypedDict):
    setup: Annotated[str,...,"这个笑话的开头"]
    punchline: Annotated[str,...,"这个笑话的妙语"]
    rating: Optional[Annotated[int,None,"这个笑话的评分,1-10分"]]


model_with_stuctured = model.with_structured_output(Joke)


print(model_with_stuctured.invoke("讲一个笑话"))
