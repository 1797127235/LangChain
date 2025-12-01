from langchain_core.tools import tool
from pydantic import BaseModel,Field


class AddInput(BaseModel):
    '''
    两数相加
    '''
    a: int = Field(..., description="第一个数")
    b: int = Field(..., description="第二个数")

@tool(args_schema=AddInput)
def add(a:int,b:int) -> int:
    # """两数相加
    # Args:
    #     a (int): 第一个数
    #     b (int): 第二个数
    # Returns:
    #     int: 两个数的和
    # """
    return a + b

result = add.invoke({"a": 1, "b": 2})
print(result)
print(add.name)
print(add.description)