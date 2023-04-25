from langchain.document_loaders import ConfluenceLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os

loader = ConfluenceLoader(
    url="https://hub.deloittedigital.com.au/wiki/",
    username="leewsimpson",
    api_key=os.environ["CONFLUENCE_API_KEY"]
)

documents = loader.load(space_key="ARC", include_attachments=False, limit=50)

print(f"{len(documents)} documents loaded")

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

print(f"{len(texts)} texts created")

db = Chroma.from_documents(documents=texts, embedding=OpenAIEmbeddings(), persist_directory="data")
db.persist()