
from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL


class TextEmbedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def generate_embeddings(self, texts):
        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return embeddings.tolist()

    def generate_query_embedding(self, query):
        return self.generate_embeddings([query])[0]
