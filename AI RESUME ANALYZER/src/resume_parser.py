import fitz
from docx import Document


def extract_text_from_pdf(file):
    """Extract text from a PDF resume."""
    text = ""

    pdf_document = fitz.open(stream=file.read(), filetype="pdf")

    for page in pdf_document:
        text += page.get_text()

    pdf_document.close()

    return text


def extract_text_from_docx(file):
    """Extract text from a DOCX resume."""
    text = ""

    document = Document(file)

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_resume_text(file):
    """Extract text based on the uploaded file type."""

    file_name = file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(file)

    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")