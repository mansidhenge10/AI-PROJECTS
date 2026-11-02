from pathlib import Path

from src.ingestion.metadata import DocumentMetadata


DOCUMENT_METADATA = {
    "tenant_a/engineering.txt": DocumentMetadata(
        tenant_id="tenant_a",
        document_type="engineering",
        allowed_roles=["engineer"],
        source="engineering.txt"
    ),

    "tenant_a/hr.txt": DocumentMetadata(
        tenant_id="tenant_a",
        document_type="hr",
        allowed_roles=["hr"],
        source="hr.txt"
    ),

    "tenant_b/finance.txt": DocumentMetadata(
        tenant_id="tenant_b",
        document_type="finance",
        allowed_roles=["finance"],
        source="finance.txt"
    ),

    "tenant_b/engineering.txt": DocumentMetadata(
        tenant_id="tenant_b",
        document_type="engineering",
        allowed_roles=["engineer"],
        source="engineering.txt"
    )
}


def load_documents():
    documents = []

    data_path = Path("data")

    for file_path in data_path.rglob("*.txt"):
        relative_path = file_path.relative_to(data_path)
        key = str(relative_path).replace("\\", "/")

        metadata = DOCUMENT_METADATA.get(key)

        if metadata is None:
            continue

        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "text": text,
            "metadata": metadata
        })

    return documents