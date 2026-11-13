from pathlib import Path
from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def load_document(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {extension}")

    if extension == ".pdf":
        reader = PdfReader(str(path))
        text = "\n".join(
            page.extract_text() or "" for page in reader.pages
        )

    else:
        text = path.read_text(encoding="utf-8")

    if not text.strip():
        raise ValueError("Document contains no extractable text.")

    return {
        "text": text,
        "metadata": {
            "source": path.name,
            "file_type": extension.replace(".", ""),
            "file_path": str(path.resolve()),
        },
    }