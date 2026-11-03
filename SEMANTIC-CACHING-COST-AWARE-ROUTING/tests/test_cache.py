import numpy as np
from app.cache.semantic_cache import SemanticCache


def test_exact_query_cache_hit(monkeypatch, tmp_path):
    cache = SemanticCache.__new__(SemanticCache)

    cache.database_path = str(tmp_path / "test_cache.db")

    class FakeModel:
        def encode(self, text, normalize_embeddings=True):
            return np.array([1.0, 0.0], dtype=np.float32)

    cache.model = FakeModel()
    cache.initialize_cache()

    cache.add("What is artificial intelligence?", "AI is machine intelligence.")

    result = cache.find("What is artificial intelligence?")

    assert result is not None
    assert result["answer"] == "AI is machine intelligence."
    assert result["similarity"] == 1.0


def test_cache_miss_for_empty_database(tmp_path):
    cache = SemanticCache.__new__(SemanticCache)

    cache.database_path = str(tmp_path / "empty_cache.db")

    class FakeModel:
        def encode(self, text, normalize_embeddings=True):
            return np.array([1.0, 0.0], dtype=np.float32)

    cache.model = FakeModel()
    cache.initialize_cache()

    result = cache.find("What is machine learning?")

    assert result is None