from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable
from typing import Iterator
import os

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)

parser = StrOutputParser()


class SentenceSplitter(Runnable):
    # 非流式：上一环节给的是一个完整字符串
    def invoke(self, input: str, config=None, **kwargs):
        sentences = []
        buffer = input 
        while "。" in buffer:
            sentence, buffer = buffer.split("。", 1)
            sentence = sentence.strip()
            if sentence:
                sentences.append(sentence + "。")
        buffer = buffer.strip()
        if buffer:
            sentences.append(buffer)
        return sentences

    # 流式：使用 _transform 方法处理上游的流式输出
    def _transform(self, input: Iterator[str], run_manager=None, **kwargs) -> Iterator[str]:
        buffer = ""
        for chunk in input:
            buffer += chunk
            # 只要还存在一个 '。' 就切一次
            while "。" in buffer:
                sentence, buffer = buffer.split("。", 1)
                sentence = sentence.strip()
                if sentence:
                    yield sentence + "。"

        # 结束后还有残余内容（没有句号结尾的最后一段）
        buffer = buffer.strip()
        if buffer:
            yield buffer


splitter = SentenceSplitter()

# 正确的链：模型 → 字符串解析 → 句子切分
chain = model | parser | splitter

# 流式打印每一句
for sentence in chain.stream("怎么评价中共？从多个角度分析一下，比如历史、意识形态、组织结构、执政方式等。"):
    print("[一句]", sentence)
