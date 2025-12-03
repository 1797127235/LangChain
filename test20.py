#文本分割器
from langchain_text_splitters import CharacterTextSplitter, TokenTextSplitter
from langchain_community.document_loaders import UnstructuredMarkdownLoader

md_loader =  UnstructuredMarkdownLoader("./docs/CAS.md")
data = md_loader.load()

#根据字符长度进行拆分
splitter1 = CharacterTextSplitter(
    separator="\n",
    chunk_size=100, #块的大小
    chunk_overlap=50 #块之间的重叠大小
)



#基于token进行拆分

splitter2 = TokenTextSplitter(
    chunk_size=100,
    chunk_overlap=50
)

# data 是 Document 列表，这里对第一个文档的文本做基于 token 的拆分
chunks = splitter2.split_text(data[0].page_content)

print(f"原始文档页数:{len(data)}\n")
print(f"拆分后的文档块数:{len(chunks)}\n")

for i, chunk in enumerate(chunks, start=1):
    print(f"----- Chunk {i} -----")
    print(chunk)
    print()
