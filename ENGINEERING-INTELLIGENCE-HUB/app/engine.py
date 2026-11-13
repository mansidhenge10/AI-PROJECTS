
from app.ingestion.pipeline import IngestionPipeline
from app.retrieval.retriever import EngineeringRetriever
from app.generation.answer_generator import AnswerGenerator


class EngineeringIntelligenceEngine:
    def __init__(self):
        self.ingestion = IngestionPipeline()
        self.retriever = EngineeringRetriever()
        self.generator = AnswerGenerator()

    def ingest_document(self, file_path, original_filename=None):
        return self.ingestion.ingest(
            file_path,
            original_filename=original_filename
        )

    def ask_question(self, question, top_k=5):
        if not question or not question.strip():
            raise ValueError("Please enter a valid question.")

        retrieved_chunks = self.retriever.retrieve(
            query=question,
            top_k=top_k
        )

        if not retrieved_chunks:
            return {
                "answer": (
                    "No relevant engineering information was found "
                    "in the uploaded documents."
                ),
                "sources": [],
                "retrieved_chunks": 0,
            }

        context = "\n\n".join(
            f"Source: {item['source']}\n{item['content']}"
            for item in retrieved_chunks
        )

        answer = self.generator.generate_answer(
            question=question,
            context=context
        )

        sources = list(
            dict.fromkeys(
                item["source"] for item in retrieved_chunks
            )
        )

        return {
            "answer": answer,
            "sources": sources,
            "retrieved_chunks": len(retrieved_chunks),
        }
