from src.retrieval.vector_store import get_vector_store


collection = get_vector_store()

result = collection.get(
    include=["documents", "metadatas"]
)

print(f"Total documents in ChromaDB: {len(result['ids'])}")

for metadata in result["metadatas"]:
    print("\n----------------------------")
    print("Tenant:", metadata["tenant_id"])
    print("Document Type:", metadata["document_type"])
    print("Allowed Roles:", metadata["allowed_roles"])
    print("Source:", metadata["source"])