from pathlib import Path
from datetime import datetime


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "audit.log"


def log_audit(
    user,
    query,
    sources,
    status
):
    """
    Record an audit event for every RAG query.
    """

    LOG_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    username = user.get("username", "unknown")
    tenant_id = user.get("tenant_id", "unknown")
    role = user.get("role", "unknown")

    source_text = ", ".join(sources) if sources else "-"

    log_entry = (
        f"{timestamp} | "
        f"USER: {username} | "
        f"TENANT: {tenant_id} | "
        f"ROLE: {role} | "
        f"QUESTION: {query} | "
        f"SOURCES: {source_text} | "
        f"STATUS: {status}\n"
    )

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(log_entry)