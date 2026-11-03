import sqlite3
from app.monitoring.metrics import initialize_database, save_metric
from app.config import DATABASE_PATH


def test_metrics_database_initialization():
    initialize_database()

    connection = sqlite3.connect(DATABASE_PATH)

    tables = connection.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='request_metrics'
    """).fetchone()

    connection.close()

    assert tables is not None


def test_save_metric():
    initialize_database()

    test_data = {
        "query": "pytest test query",
        "source": "ollama",
        "model": "llama3.2:latest",
        "route": "fast",
        "similarity": None,
        "prompt_tokens": 10,
        "completion_tokens": 20,
        "total_tokens": 30,
        "latency_ms": 100,
        "inference_time_seconds": 0.1,
        "actual_api_cost": 0.0
    }

    save_metric(test_data)

    connection = sqlite3.connect(DATABASE_PATH)

    result = connection.execute("""
        SELECT query, total_tokens
        FROM request_metrics
        WHERE query = ?
    """, ("pytest test query",)).fetchone()

    connection.close()

    assert result == ("pytest test query", 30)