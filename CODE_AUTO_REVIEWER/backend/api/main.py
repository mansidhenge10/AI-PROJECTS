from fastapi import FastAPI

app = FastAPI(
    title="Code Auto Reviewer",
    description="AI-powered Python code review system",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Code Auto Reviewer API is running"
    }