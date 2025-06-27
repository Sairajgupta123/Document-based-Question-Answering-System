# vector_store.py
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma  # or FAISS

embeddings = OpenAIEmbeddings()            # uses Ada-002 by default

def store(docs, persist_dir="db"):
    vectordb = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    vectordb.persist()
    return vectordb
