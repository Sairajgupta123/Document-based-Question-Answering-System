# qa_chain.py
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

def build_qa(vectordb):
    retriever = vectordb.as_retriever(search_type="similarity", k=4)
    return RetrievalQA.from_chain_type(
        llm,
        chain_type="stuff",        # simplest strategy
        retriever=retriever,
        return_source_documents=True  # so we can cite chunks
    )
