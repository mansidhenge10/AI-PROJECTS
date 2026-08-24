from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai_reviewer import review_code
from code_analyzer import analyze_code
from code_fixer import fix_code


app = FastAPI(
    title="Code Auto Reviewer",
    description="AI-powered Python code review system",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {
        "message": "AI Code Reviewer API is running"
    }


@app.post("/review")
@app.post("/review")
def review(request: CodeRequest):

    static_issues = analyze_code(request.code)

    ai_result = review_code(
        request.code,
        static_issues
    )

    return {
        "static_analysis": static_issues,
        "ai_review": ai_result
    }
@app.post("/fix")
def fix(request: CodeRequest):

    fixed_code = fix_code(request.code)

    return {
        "fixed_code": fixed_code
    }

    return {
        "fixed_code": fixed_code
    }
    # Step 3: Return both results
    return {
        "static_analysis": static_issues,
        "ai_review": ai_result
    }