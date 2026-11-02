from src.auth.users import USERS
from src.retrieval.secure_retriever import secure_search


query = "What technologies does the engineering team use?"


for username in ["alice", "emma", "bob", "david"]:

    print("\n============================")
    print("USER:", username)
    print("============================")

    results = secure_search(
        query,
        USERS[username]
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    for document, metadata in zip(documents, metadatas):
        print("\nSource:", metadata["source"])
        print("Tenant:", metadata["tenant_id"])
        print("Role:", metadata["allowed_roles"])
        print("Text:", document[:150])