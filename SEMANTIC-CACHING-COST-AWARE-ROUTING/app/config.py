import os

OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
CACHE_SIMILARITY_THRESHOLD = 0.90

SMALL_MODEL = 'llama3.2:latest'
LARGE_MODEL = 'qwen2.5:3b'

EMBEDDING_MODEL = 'all-MiniLM-L6-v2'

DATABASE_PATH = 'data/metrics.db'
