import sqlite3
from app.config import DATABASE_PATH


def initialize_database():
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS request_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT,
            source TEXT,
            model TEXT,
            route TEXT,
            similarity REAL,
            prompt_tokens INTEGER DEFAULT 0,
            completion_tokens INTEGER DEFAULT 0,
            total_tokens INTEGER DEFAULT 0,
            latency_ms REAL,
            inference_time_seconds REAL DEFAULT 0,
            actual_api_cost REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    columns = {
        row[1] for row in connection.execute(
            "PRAGMA table_info(request_metrics)"
        ).fetchall()
    }

    new_columns = {
        "total_tokens": "INTEGER DEFAULT 0",
        "inference_time_seconds": "REAL DEFAULT 0",
        "actual_api_cost": "REAL DEFAULT 0"
    }

    for column, data_type in new_columns.items():
        if column not in columns:
            connection.execute(
                f"ALTER TABLE request_metrics ADD COLUMN {column} {data_type}"
            )

    connection.commit()
    connection.close()


def save_metric(data):
    connection = sqlite3.connect(DATABASE_PATH)

    connection.execute("""
        INSERT INTO request_metrics (
            query, source, model, route, similarity,
            prompt_tokens, completion_tokens, total_tokens,
            latency_ms, inference_time_seconds, actual_api_cost
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("query"),
        data.get("source"),
        data.get("model"),
        data.get("route"),
        data.get("similarity"),
        data.get("prompt_tokens", 0),
        data.get("completion_tokens", 0),
        data.get("total_tokens", 0),
        data.get("latency_ms", 0),
        data.get("inference_time_seconds", 0),
        data.get("actual_api_cost", 0)
    ))

    connection.commit()
    connection.close()