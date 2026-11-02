from src.retrieval.vector_store import get_vector_store, get_embeddings


def secure_search(query, user, top_k=3):
    """
    Search only documents that belong to the user's tenant
    and are accessible to the user's role.
    """

    vector_store = get_vector_store()
    embeddings = get_embeddings()

    query_vector = embeddings.embed_query(query)

    results = vector_store.query(
        query_embeddings=[query_vector],
        n_results=top_k,
        where={
            "$and": [
                {"tenant_id": user["tenant_id"]},
                {"allowed_role": user["role"]}
            ]
        }
    )

    return results