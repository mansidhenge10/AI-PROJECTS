
import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer

from app.config import (
    EMBEDDING_MODEL,
    CACHE_SIMILARITY_THRESHOLD,
    DATABASE_PATH
)


class SemanticCache:

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.database_path = DATABASE_PATH
        self.initialize_cache()

    def initialize_cache(self):
        connection = sqlite3.connect(self.database_path)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS semantic_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                answer TEXT NOT NULL,
                embedding BLOB NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        connection.commit()
        connection.close()

    def get_embedding(self, text):
        return self.model.encode(
            text,
            normalize_embeddings=True
        )

    def get_intent(self, query):
        query = query.lower()

        if any(word in query for word in [
            "advantage", "benefit", "disadvantage", "limitation"
        ]):
            return "advantages"

        if any(word in query for word in [
            "invented", "inventor", "founded", "origin", "history"
        ]):
            return "history"

        if any(word in query for word in [
            "application", "applications", "used for", "uses of"
        ]):
            return "applications"

        if any(word in query for word in [
            "compare", "comparison", "difference", "differentiate"
        ]):
            return "comparison"

        if any(word in query for word in [
            "how does", "how do", "how to", "working", "process", "steps"
        ]):
            return "process"

        if any(word in query for word in [
            "what is", "what are", "define", "definition",
            "meaning", "explain"
        ]):
            return "definition"

        return "general"

    def find(self, query):
        query_embedding = self.get_embedding(query)
        query_intent = self.get_intent(query)

        connection = sqlite3.connect(self.database_path)

        rows = connection.execute("""
            SELECT query, answer, embedding
            FROM semantic_cache
        """).fetchall()

        connection.close()

        best_match = None
        best_score = 0

        for cached_query, answer, embedding_blob in rows:

            cached_intent = self.get_intent(cached_query)

            if query_intent != cached_intent:
                continue

            cached_embedding = np.frombuffer(
                embedding_blob,
                dtype=np.float32
            )

            score = float(
                np.dot(query_embedding, cached_embedding)
            )

            if score > best_score:
                best_score = score
                best_match = answer

        if best_match and best_score >= CACHE_SIMILARITY_THRESHOLD:
            return {
                "answer": best_match,
                "similarity": best_score
            }

        return None

    def add(self, query, answer):
        embedding = self.get_embedding(query)

        embedding_blob = embedding.astype(
            np.float32
        ).tobytes()

        connection = sqlite3.connect(self.database_path)

        connection.execute("""
            INSERT INTO semantic_cache (
                query, answer, embedding
            )
            VALUES (?, ?, ?)
        """, (
            query,
            answer,
            embedding_blob
        ))

        connection.commit()
        connection.close()
