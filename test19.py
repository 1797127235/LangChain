from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader,UnstructuredMarkdownLoader

Document(
    #内容
    page_content= "狗是哺乳动物，有四条腿，会叫，会跳，会咬人",
    #元数据字典
    metadata={"source":"https://www.google.com"}
    #元数据属性可以包含：文档源，与其他文档的关系以及其他属性信息
)




# #加载文档 PDF（test19.py 与 docs 在同一级目录）
# loader = PyPDFLoader(file_path="./docs/test1.pdf")

# #生成文档列表
# docs = loader.load()

# print(f"PDF文档页数:{len(docs)}\n")
# print(f"第一页文本的内容是：{docs[-1].page_content}")



#加载Markdown

md_loader =  UnstructuredMarkdownLoader("./docs/CAS.md")
docs = md_loader.load()
print(f"Markdown文档页数:{len(docs)}\n")
print(f"第一页文本的内容是：{docs[-1].page_content}")