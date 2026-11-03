
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import requests

from app.engine import AIEngine


app = FastAPI(
    title="AI Semantic Cache & Cost-Aware Routing API",
    description="LLM API with semantic caching and intelligent model routing",
    version="1.1.0"
)

engine = AIEngine()


class QueryRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        max_length=2000,
        description="Enter a question between 3 and 2000 characters"
    )


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Semantic Cache & Cost-Aware Routing API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Semantic Cache & Cost-Aware Routing API"
    }


@app.post("/query")
def process_query(request: QueryRequest):

    query = request.query.strip()

    if not query:
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty or contain only spaces."
        )

    try:
        result = engine.process_query(query)
        return {
            "status": "success",
            **result
        }

    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Ollama is unavailable. Please start Ollama and try again."
        )

    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=504,
            detail="Model inference timed out. Please try again."
        )

    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=502,
            detail="An error occurred while communicating with Ollama."
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while processing your query."
        )
