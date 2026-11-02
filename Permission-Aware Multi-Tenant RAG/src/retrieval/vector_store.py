import chromadb

from langchain_huggingface import HuggingFaceEmbeddings


CHROMA_PATH = "data/chroma_db"


# Load the embedding model only once
_embeddings = None


def get_vector_store():
    client = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    collection = client.get_or_create_collection(
        name="multi_tenant_documents"
    )

    return collection


def get_embeddings():
    global _embeddings

    if _embeddings is None:
        print("Loading embedding model...")
        
        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Embedding model loaded.")

    return _embeddings