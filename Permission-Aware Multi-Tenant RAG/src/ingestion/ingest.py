from src.retrieval.secure_retriever import secure_search
from src.rag.llm import get_llm


def generate_answer(query, user):
    """
    Generate an answer using only documents
    that the user is authorized to access.
    """

    # Secure retrieval
    results = secure_search(
        query=query,
        user=user,
        top_k=3
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    # No authorized documents found
    if not documents:
        return {
            "answer": "I could not find any information you are authorized to access.",
            "sources": []
        }

    # Build context
    context_parts = []

    for document, metadata in zip(documents, metadatas):

        context_parts.append(
            f"Source: {metadata['source']}\n"
            f"Content:\n{document}"
        )

    context = "\n\n---\n\n".join(context_parts)

    # Secure RAG prompt
    prompt = f"""
You are a secure enterprise AI assistant.

Answer the user's question using ONLY the provided context.

IMPORTANT SECURITY RULES:
1. Never use information outside the provided context.
2. Never invent information.
3. Do not reveal information from documents the user is not authorized to access.
4. If the answer is not present in the authorized context, say exactly:
"I don't have enough authorized information to answer this."

Context:
{context}

User Question:
{query}

Answer:
"""

    # Generate answer
    llm = get_llm()

    response = llm.invoke(prompt)

    answer = response.content.strip()

    # Do not expose sources when access is denied
    if "I don't have enough authorized information" in answer:
        sources = []
    else:
        sources = [
            metadata["source"]
            for metadata in metadatas
        ]

    return {
        "answer": answer,
        "sources": sources
    }