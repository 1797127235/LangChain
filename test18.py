from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# 示例选择器 - 这里先用静态 examples 列表，不使用动态选择器
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "sad", "output": "happy"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples,                 # 所有可选示例
    embeddings=GoogleGenerativeAIEmbeddings(  # 用来度量相似度的嵌入模型（需要 GOOGLE_API_KEY）
        model="models/text-embedding-004",
    ),
    vectorstore_cls=FAISS,             # 存放向量的向量库实现
    k=2,                               # 每次按相似度选出几个示例
    input_keys=["input"],             # 输入里用来算相似度的字段名
)

# 单条示例的模板：描述一组输入/输出
example_prompt = PromptTemplate.from_template("输入: {input}\n输出: {output}")

# Few-shot 提示模板：由 prefix + 若干（动态选择的）示例 + suffix 拼接而成
few_shot_prompt = FewShotPromptTemplate(
    example_selector=selector,         # 使用相似度选择器来选示例
    example_prompt=example_prompt,     # 每条示例的格式
    prefix="给出每个输入的反义词",       # 所有示例前面的说明文字
    suffix="输入: {adjective}\n输出:",  # 所有示例后面的最终输入
    input_variables=["adjective"],    # 外部需要传入的变量名
)

if __name__ == "__main__":
    # 测试一下：给一个形容词，让模板帮我们生成带 few-shot 示例的 prompt
    prompt_text = few_shot_prompt.format(adjective="happy")
    print(prompt_text)
