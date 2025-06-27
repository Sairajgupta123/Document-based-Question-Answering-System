# 📄💬 Document-Based Question-Answering App

Ask questions about any PDF or Word file and get precise, cited answers — powered by embeddings, vector search, and an OpenAI chat model, all wrapped in a Streamlit UI.

---

## ✨ Features
| Capability | Details |
|------------|---------|
| **Upload documents** | Drag-and-drop PDF (`.pdf`) or Word (`.docx`, `.doc`). |
| **Automatic chunking & embedding** | Text split into overlapping chunks, then embedded with `text-embedding-3-small` (or `text-embedding-ada-002`). |
| **Vector store** | ChromaDB (default) or FAISS stores embeddings locally for fast similarity search. |
| **Context-aware answers** | Most relevant chunks are fed into GPT (default **`gpt-3.5-turbo`** for the free tier) to generate an answer plus cited sources. |
| **Streamlit UI** | Minimal, responsive interface: upload → index → ask → read answer & sources. |
| **Configurable** | Swap models, tweak chunk/overlap sizes, or switch vector store with one line. |

---

## 🏗️ Architecture

