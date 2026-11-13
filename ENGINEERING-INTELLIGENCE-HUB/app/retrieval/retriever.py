
from app.embeddings.embedder import TextEmbedder
from app.vectorstore.chroma_store import ChromaStore


class EngineeringRetriever:
    def __init__(self):
        self.embedder = TextEmbedder()
        self.vector_store = ChromaStore()

    def retrieve(self, query, top_k=5, max_distance=0.65):
        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        query_embedding = self.embedder.generate_query_embedding(
            query.strip()
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        relevant_results = [
            result for result in results
            if result["distance"] <= max_distance
        ]

        return [
            {
                "content": result["text"],
                "source": result["metadata"].get("source", "Unknown"),
                "chunk_index": result["metadata"].get("chunk_index"),
                "distance": result["distance"],
            }
            for result in relevant_results
        ]
