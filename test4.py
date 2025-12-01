from typing import Type
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

# --- 第一步：定义 Schema (这是给 LLM 看的说明书) ---
class FlightSearchInput(BaseModel):
    """这里定义 LLM 必须提取哪些参数"""
    
    origin: str = Field(
        description="出发城市的机场代码，例如 PEK, SHA, NYC"
    )
    destination: str = Field(
        description="目的城市的机场代码，例如 HND, LHR"
    )
    date: str = Field(
        description="出发日期，必须是 YYYY-MM-DD 格式"
    )
    cabin: str = Field(
        default="economy",
        description="舱位等级，可选值: economy, business, first。如果不指定默认为 economy"
    )

# --- 第二步：定义 Tool (这是实际干活的逻辑) ---
class FlightSearchTool(BaseTool):
    name: str = "search_flights"
    description: str = "当用户想要查询机票价格或航班时刻表时使用此工具"
    args_schema: Type[BaseModel] = FlightSearchInput  # <--- 关键：把上面的 Schema 绑定到这里

    def _run(self, origin: str, destination: str, date: str, cabin: str = "economy"):
        # 这里写真实的 API 调用逻辑，我们用 print 模拟
        print(f"DEBUG: 正在查询数据库 -> {origin} to {destination} on {date} ({cabin})")
        
        # 模拟返回结果
        return f"查询成功：{date} 从 {origin} 飞往 {destination} 的 {cabin} 舱位最低价为 ¥3500。"

# --- 第三步：实例化工具 ---
tool = FlightSearchTool()

# 让我们看看 LangChain 自动生成的 Schema 是什么样子的
print("=== LLM 看到的 JSON Schema ===")
print(tool.args)

# --- 第四步：测试工具 ---
result = tool.invoke({"origin": "PEK", "destination": "HND", "date": "2025-12-01"})
print("=== LLM 返回的 JSON ===")
print(result)