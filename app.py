
import streamlit as st
from pathlib import Path
from loaders import load_file
from splitters import chunk_docs
from vector_store import store
from qa_chain import build_qa

st.title("📄💬 Ask-Your-Document")

uploaded = st.file_uploader("Upload a PDF or Word file", type=["pdf", "docx", "doc"])
if uploaded:
    temp_path = Path("temp") / uploaded.name
    temp_path.parent.mkdir(exist_ok=True)
    temp_path.write_bytes(uploaded.getvalue())

    with st.spinner("Reading & indexing..."):
        docs = load_file(temp_path)
        chunks = chunk_docs(docs)
        vectordb = store(chunks, persist_dir=f"db/{uploaded.name}")
        qa = build_qa(vectordb)
    st.success("Document ready! Ask away ⬇️")
    if "chat" not in st.session_state:
        st.session_state.chat = []
    user_q = st.text_input("Your question")
    if user_q:
        with st.spinner("Thinking..."):
            resp = qa(user_q)
        answer = resp["result"]
        sources = [s.metadata['source'] for s in resp["source_documents"]]
        st.markdown(f"**Answer:** {answer}")
        with st.expander("Show sources"):
            st.write(sources)
