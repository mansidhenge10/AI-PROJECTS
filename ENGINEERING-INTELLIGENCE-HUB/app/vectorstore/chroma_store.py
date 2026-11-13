
import hashlib

import chromadb
from app.config import CHROMA_DB_PATH


class ChromaStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_PATH)
        )

    def get_collection(self):
        return self.client.get_or_create_collection(
            name="engineering_knowledge",
            metadata={"hnsw:space": "cosine"}
        )

    def add_documents(self, chunks, embeddings, metadatas):
        if not chunks:
            return

        if not (len(chunks) == len(embeddings) == len(metadatas)):
            raise ValueError(
                "Chunks, embeddings and metadata counts must match."
            )

        ids = []

        for chunk, metadata in zip(chunks, metadatas):
            source = metadata.get("source", "unknown")
            chunk_index = metadata.get("chunk_index", 0)

            unique_text = f"{source}:{chunk_index}:{chunk}"

            chunk_id = hashlib.sha256(
                unique_text.encode("utf-8")
            ).hexdigest()

            ids.append(chunk_id)

        collection = self.get_collection()

        collection.upsert(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, query_embedding, top_k=5):
        collection = self.get_collection()

        total = collection.count()

        if total == 0:
            return []

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=min(top_k, total)
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        return [
            {
                "text": document,
                "metadata": metadata,
                "distance": distance
            }
            for document, metadata, distance
            in zip(documents, metadatas, distances)
        ]
