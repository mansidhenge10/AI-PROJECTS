
from pathlib import Path

from app.ingestion.document_loader import load_document
from app.ingestion.text_splitter import split_text
from app.embeddings.embedder import TextEmbedder
from app.vectorstore.chroma_store import ChromaStore


class IngestionPipeline:
    def __init__(self):
        self.embedder = TextEmbedder()
        self.vector_store = ChromaStore()

    def ingest(self, file_path, original_filename=None):
        document = load_document(file_path)

        filename = original_filename or Path(file_path).name

        # Preserve the original uploaded filename
        document["metadata"]["source"] = filename

        chunks = split_text(document["text"])

        if not chunks:
            raise ValueError("No text chunks were generated.")

        embeddings = self.embedder.generate_embeddings(chunks)

        metadatas = [
            {
                **document["metadata"],
                "chunk_index": index,
            }
            for index in range(len(chunks))
        ]

        self.vector_store.add_documents(
            chunks=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        return {
            "filename": filename,
            "total_chunks": len(chunks),
            "status": "success",
        }
