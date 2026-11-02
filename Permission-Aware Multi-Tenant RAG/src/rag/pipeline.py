from src.retrieval.secure_retriever import secure_search
from src.rag.llm import get_llm
from src.utils.audit_logger import log_audit


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
        answer = (
            "I could not find any information "
            "you are authorized to access."
        )

        log_audit(
            user=user,
            query=query,
            sources=[],
            status="DENIED"
        )

        return {
            "answer": answer,
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
3. Never reveal information from another tenant.
4. Never reveal information belonging to a role the user does not have.
5. If the answer cannot be found in the authorized context, respond EXACTLY with:

I don't have enough authorized information to answer this.

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

    # Check whether the LLM refused to answer
    refusal_phrases = [
        "I don't have enough authorized information",
        "I do not have enough authorized information",
        "not enough authorized information",
        "cannot provide",
        "can't provide",
        "cannot answer",
        "can't answer"
    ]

    is_refusal = any(
        phrase.lower() in answer.lower()
        for phrase in refusal_phrases
    )

    if is_refusal:

        sources = []

        log_audit(
            user=user,
            query=query,
            sources=[],
            status="DENIED"
        )

    else:

        sources = list(dict.fromkeys(
            metadata["source"]
            for metadata in metadatas
        ))

        log_audit(
            user=user,
            query=query,
            sources=sources,
            status="ALLOWED"
        )

    return {
        "answer": answer,
        "sources": sources
    }