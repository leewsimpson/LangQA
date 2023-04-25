from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings

db = Chroma(persist_directory="data", embedding_function=OpenAIEmbeddings())
llm = OpenAI()
from langchain.chains.question_answering import load_qa_chain

while True:
    query = input("Question: ")
    docs = db.similarity_search(query, top_k=3)
    print(f"Found {len(docs)} documents.  Querying AI...")

    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
    print(result["output_text"])
    print()