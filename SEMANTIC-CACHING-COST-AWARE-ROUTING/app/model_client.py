
import requests
from app.config import OLLAMA_BASE_URL


def generate_response(model, query):
    url = f"{OLLAMA_BASE_URL}/api/generate"

    payload = {
        "model": model,
        "prompt": query,
        "stream": False
    }

    response = requests.post(
        url,
        json=payload,
        timeout=180
    )

    response.raise_for_status()
    result = response.json()

    prompt_tokens = result.get("prompt_eval_count", 0)
    completion_tokens = result.get("eval_count", 0)
    total_duration = result.get("total_duration", 0)

    total_tokens = prompt_tokens + completion_tokens

    return {
        "answer": result["response"],
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": total_tokens,
        "total_duration": total_duration,
        "inference_time_seconds": round(
            total_duration / 1_000_000_000, 3
        ),
        "actual_api_cost": 0.0
    }
