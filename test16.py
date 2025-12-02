from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import Runnable, RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, FewShotChatMessagePromptTemplate
import os

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)

#少样本提示词模板
examples = [
    {"text": "hi what is your name?","output": "你好你叫什么名字"},
    {"text": "hi what is your age?","output": "你好你多大了"}
]

examples_prompt_template = ChatPromptTemplate(
    [
        ("user","{text}"),
        ("ai","{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples = examples,
    example_prompt = examples_prompt_template,
    
)

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","将文本从{language_from}翻译成{language_to}"),
        #示例
        few_shot_prompt,
        ("user","{text}"),
    ]
)



chain = chat_prompt_template | model
chain.invoke({
    "language_from":"英文",
    "language_to":"中文",
    "text":"hi what is your name?"
}).pretty_print()




