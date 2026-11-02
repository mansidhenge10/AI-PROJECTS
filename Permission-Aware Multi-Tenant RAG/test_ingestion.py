from src.ingestion.loader import load_documents


documents = load_documents()

print(f"Total documents loaded: {len(documents)}")

for document in documents:
    print("\n----------------------------")
    print("Document:")
    print(document["metadata"].source)

    print("Tenant:")
    print(document["metadata"].tenant_id)

    print("Document Type:")
    print(document["metadata"].document_type)

    print("Allowed Roles:")
    print(document["metadata"].allowed_roles)

    print("----------------------------")