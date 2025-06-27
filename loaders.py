# loaders.py
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader

def load_file(path):
    if path.suffix.lower() == ".pdf":
        return PyPDFLoader(str(path)).load()
    elif path.suffix.lower() in (".docx", ".doc"):
        return Docx2txtLoader(str(path)).load()
    else:
        raise ValueError("Unsupported file type")
