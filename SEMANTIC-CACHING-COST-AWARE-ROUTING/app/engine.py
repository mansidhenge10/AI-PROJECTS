
import time

from app.cache.semantic_cache import SemanticCache
from app.router.model_router import ModelRouter
from app.model_client import generate_response
from app.monitoring.metrics import initialize_database, save_metric


class AIEngine:

    def __init__(self):
        self.cache = SemanticCache()
        self.router = ModelRouter()
        initialize_database()

    def process_query(self, query):
        start_time = time.perf_counter()

        cached_result = self.cache.find(query)

        if cached_result:
            result = {
                "answer": cached_result["answer"],
                "source": "semantic_cache",
                "similarity": cached_result["similarity"],
                "model": None,
                "route": "cache",
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "total_tokens": 0,
                "total_duration": 0,
                "inference_time_seconds": 0,
                "actual_api_cost": 0.0
            }

        else:
            model, route = self.router.route(query)

            generated = generate_response(model, query)

            self.cache.add(query, generated["answer"])

            result = {
                "answer": generated["answer"],
                "source": "ollama",
                "similarity": None,
                "model": model,
                "route": route,
                "prompt_tokens": generated["prompt_tokens"],
                "completion_tokens": generated["completion_tokens"],
                "total_tokens": generated["total_tokens"],
                "total_duration": generated["total_duration"],
                "inference_time_seconds": generated["inference_time_seconds"],
                "actual_api_cost": generated["actual_api_cost"]
            }

        result["latency_ms"] = round(
            (time.perf_counter() - start_time) * 1000, 2
        )

        save_metric({
            "query": query,
            **result
        })

        return result
