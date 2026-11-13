
from pathlib import Path
import tempfile

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel

from app.engine import EngineeringIntelligenceEngine


router = APIRouter()
engine = EngineeringIntelligenceEngine()


class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    allowed_extensions = {".pdf", ".txt", ".md"}

    original_filename = Path(file.filename or "").name
    extension = Path(original_filename).suffix.lower()

    if not original_filename or extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, TXT and Markdown files are supported."
        )

    try:
        content = await file.read()

        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty."
            )

        with tempfile.NamedTemporaryFile(
            suffix=extension,
            delete=False
        ) as temp_file:
            temp_file.write(content)
            temp_path = temp_file.name

        try:
            result = engine.ingest_document(
                temp_path,
                original_filename=original_filename
            )
            return result

        finally:
            Path(temp_path).unlink(missing_ok=True)

    except HTTPException:
        raise
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@router.post("/ask")
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if not 1 <= request.top_k <= 10:
        raise HTTPException(
            status_code=400,
            detail="top_k must be between 1 and 10."
        )

    try:
        return engine.ask_question(
            question=request.question,
            top_k=request.top_k
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
