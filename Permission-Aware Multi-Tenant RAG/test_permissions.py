from src.ingestion.loader import load_documents
from src.auth.users import USERS
from src.auth.filter import filter_documents


documents = load_documents()


def test_user(username):
    user = USERS[username]

    allowed_documents = filter_documents(documents, user)

    print(f"\nUser: {username}")
    print(f"Tenant: {user['tenant_id']}")
    print(f"Role: {user['role']}")

    print("Accessible documents:")

    for document in allowed_documents:
        metadata = document["metadata"]
        print(
            f"  - {metadata.source} "
            f"({metadata.tenant_id}, {metadata.document_type})"
        )


test_user("alice")
test_user("emma")
test_user("bob")
test_user("david")