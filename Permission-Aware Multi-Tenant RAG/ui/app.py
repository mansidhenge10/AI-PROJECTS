
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from src.auth.users import USERS
from src.rag.pipeline import generate_answer


app = FastAPI(
    title="Permission-Aware Multi-Tenant RAG API",
    description="Secure RAG API with tenant and role-based access control",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    username: str = Field(min_length=1)
    question: str = Field(min_length=1, max_length=2000)


@app.get("/")
def home():
    return {
        "message": "Permission-Aware Multi-Tenant RAG API is running"
    }


@app.post("/query")
def query_rag(request: QueryRequest):

    username = request.username.strip()
    question = request.question.strip()

    if not username:
        raise HTTPException(
            status_code=400,
            detail="Username cannot be empty"
        )

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    if username not in USERS:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user = USERS[username]

    try:
        result = generate_answer(
            query=question,
            user=user
        )

        return {
            "username": username,
            "tenant_id": user["tenant_id"],
            "role": user["role"],
            "question": question,
            "answer": result["answer"],
            "sources": result["sources"]
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An internal error occurred while processing the query."
        )
