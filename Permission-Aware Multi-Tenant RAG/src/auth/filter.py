def filter_documents(documents, user):
    """
    Return only documents the user is allowed to access.
    """

    filtered_documents = []

    for document in documents:
        metadata = document["metadata"]

        # Check tenant
        if metadata.tenant_id != user["tenant_id"]:
            continue

        # Check role
        if user["role"] not in metadata.allowed_roles:
            continue

        filtered_documents.append(document)

    return filtered_documents