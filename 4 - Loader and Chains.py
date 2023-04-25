from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=C_78DM8fG6E", add_video_info=False)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap=100)
documents = loader.load_and_split(text_splitter)
print(len(documents))

chain = load_summarize_chain(OpenAI(), chain_type="map_reduce")
summary = chain.run(documents)
print(summary)