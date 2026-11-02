from src.auth.users import USERS
from src.rag.pipeline import generate_answer


questions = [
    ("alice", "What technologies does the engineering team use?"),
    ("emma", "How many annual paid leaves do employees receive?"),
    ("bob", "What database does the engineering team use?"),
    ("david", "Who reviews the monthly financial reports?"),

    # Security tests
    ("alice", "How many annual paid leaves do employees receive?"),
    ("david", "What technologies does the engineering team use?")
]

for username, question in questions:

    print("\n===================================")
    print(f"USER: {username}")
    print(f"QUESTION: {question}")
    print("===================================")

    result = generate_answer(
        query=question,
        user=USERS[username]
    )

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")
    for source in result["sources"]:
        print("-", source)