from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.auth.users import USERS
from src.rag.pipeline import generate_answer


# Create FastAPI application
app = FastAPI(
    title="Permission-Aware Multi-Tenant RAG API",
    description="Secure RAG API with tenant and role-based access control",
    version="1.0.0"
)


# Request model
class QueryRequest(BaseModel):
    username: str
    question: str


# Health check endpoint
@app.get("/")
def home():
    return {
        "message": "Permission-Aware Multi-Tenant RAG API is running"
    }


# RAG query endpoint
@app.post("/query")
def query_rag(request: QueryRequest):

    # Check whether user exists
    if request.username not in USERS:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Get authenticated user
    user = USERS[request.username]

    # Generate secure RAG answer
    result = generate_answer(
        query=request.question,
        user=user
    )

    return {
        "username": request.username,
        "tenant_id": user["tenant_id"],
        "role": user["role"],
        "question": request.question,
        "answer": result["answer"],
        "sources": result["sources"]
    }