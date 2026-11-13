
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Engineering Intelligence Hub",
    description="AI-powered engineering knowledge assistant using RAG and LLMs.",
    version="1.0.0"
)

app.include_router(router, prefix="/api")


@app.get("/")
def home():
    return {
        "message": "Engineering Intelligence Hub API is running.",
        "status": "healthy"
    }
