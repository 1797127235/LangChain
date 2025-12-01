from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from typing import Tuple, List

class AddInput(BaseModel):
    a: int = Field(..., description="第一个数")
    b: int = Field(..., description="第二个数")

def add(a:int,b:int)->Tuple[str,List[int]]:
    return f"({a}) + ({b}) add result is {a+b}", [a,b]


add_tool = StructuredTool.from_function(
    func = add,
    name = "ADD",
    description = "Add two numbers",
    args_schema = AddInput,
    response_format = "content_and_artifact" #内容与工件分离 
)

    '''
        add_tool最后一个参数告诉LangChain,我的函数会返回两个值，请把第一个
        值作为文本喂给LLM，第二个值作为工件存起来不要给LLM看
    '''


res = add_tool.invoke(
    {
        "name": "ADD",
        "args": {"a": 3,"b": 4},
        "type": "tool_call",
        "id": "1",  #必填 将工具调用请求和结果关联起来
    }
)

print(res)




