from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from config.models.embeddings import get_embeddings


def create_vector_db():
    from pathlib import Path

    sample_path = Path(__file__).resolve().parent / "data" / "sample.txt"
    if not sample_path.exists():
        raise FileNotFoundError(f"{sample_path} does not exist")

    with sample_path.open("r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        raise ValueError(f"{sample_path} is empty")

    docs = [Document(page_content=text, metadata={"source": "data/sample.txt"})]
    embeddings = get_embeddings()

    db = InMemoryVectorStore(embeddings)
    db.add_documents(documents=docs)

    return db


def retrieve_docs(query, db, k=3):
    return db.similarity_search(query=query, k=k)