# AI Semantic Cache & Cost-Aware Model Routing

An intelligent LLM infrastructure system that reduces redundant model inference through semantic caching and routes queries using a heuristic-based complexity scoring system.

## Project Overview

This project combines semantic search, persistent caching, and cost-aware model routing to improve the efficiency of Large Language Model applications.

Instead of sending every query directly to an LLM, the system first checks whether a semantically similar query already exists in its cache. If a suitable result is found, it returns the cached response. Otherwise, it selects a model based on query complexity and generates a new response using Ollama.

## Key Features

- **Semantic Caching:** Stores query embeddings and generated responses in SQLite.
- **Intent-Aware Validation:** Checks query intent before accepting a semantic cache match.
- **Cost-Aware Routing:** Uses heuristic complexity scoring to select a configured model.
- **Local LLM Inference:** Integrates with Ollama for local model execution.
- **Token Tracking:** Records prompt, completion, and total tokens.
- **Performance Monitoring:** Tracks latency, inference duration, cache hits, and model usage.
- **REST API:** Provides endpoints through FastAPI.
- **Analytics Dashboard:** Visualizes request statistics and system performance using Streamlit.
- **Automated Testing:** Uses Pytest to verify core components.

## System Architecture

```text
              User Query
                   |
                   v
             FastAPI Backend
                   |
                   v
             AI Engine
                   |
                   v
             Semantic Cache
                   |
             +-----+-----+
             |           |
          Cache Hit   Cache Miss
             |           |
             v           v
        Cached Answer  Model Router
                         |
                  +------+------+
                  |             |
               Fast Model   Advanced Model
                  |             |
                  +------+------+
                         |
                         v
                    Ollama LLM
                         |
                         v
                  Generated Answer
                         |
                         v
                  Update Cache
                         |
                         v
                  Save Metrics
                         |
                         v
                    User Response

             Streamlit Dashboard
                  |
             SQLite Metrics
```

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend API | FastAPI |
| Dashboard | Streamlit |
| Database | SQLite |
| Embeddings | Sentence Transformers |
| Similarity Search | NumPy |
| LLM Runtime | Ollama |
| Models | Llama 3.2, Qwen 2.5 3B |
| Testing | Pytest |
| Data Processing | Pandas |

## Project Structure

```text
SEMANTIC-CACHING-COST-AWARE-ROUTING/
│
├── app/
│   ├── cache/
│   │   └── semantic_cache.py
│   ├── router/
│   │   └── model_router.py
│   ├── monitoring/
│   │   └── metrics.py
│   ├── config.py
│   ├── engine.py
│   ├── main.py
│   └── model_client.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── metrics.db
│
├── tests/
│   ├── test_api.py
│   ├── test_cache.py
│   ├── test_metrics.py
│   └── test_router.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mansidhenge10/SEMANTIC-CACHING-COST-AWARE-ROUTING.git
cd SEMANTIC-CACHING-COST-AWARE-ROUTING
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Start Ollama

Install Ollama and pull the required models:

```bash
ollama pull llama3.2
ollama pull qwen2.5:3b
```

Start the Ollama service:

```bash
ollama serve
```

Keep the Ollama service running in a separate terminal.

### 5. Start the FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

API documentation:

http://127.0.0.1:8000/docs

### 6. Start the Streamlit Dashboard

Open another terminal, activate the virtual environment, and run:

```bash
python -m streamlit run dashboard/app.py
```

## API Usage

### Health Check

**Endpoint:**

`GET /health`

### Process a Query

**Endpoint:**

`POST /query`

Example request:

```json
{
  "query": "Explain machine learning"
}
```

The API returns the generated or cached answer along with information such as:

- Response source
- Selected model
- Routing decision
- Cache similarity
- Prompt tokens
- Completion tokens
- Total tokens
- Request latency
- Inference duration
- Actual local API cost

## Model Routing Strategy

The system uses heuristic-based complexity scoring.

Simple queries are routed to the configured fast model:

`llama3.2:latest`

More complex queries are routed to the configured advanced model:

`qwen2.5:3b`

Routing considers query length, reasoning keywords, technical keywords, and multiple questions.

## Semantic Caching Strategy

The system uses the `all-MiniLM-L6-v2` embedding model.

Query embeddings are normalized and stored in SQLite. Cosine similarity is calculated using the dot product of normalized embeddings.

Cache validation considers:

1. Semantic similarity threshold.
2. Query intent compatibility.
3. Existing cached responses.

The current similarity threshold is 0.90.

## Performance Monitoring

The dashboard tracks:

- Total requests
- Cache hits and cache hit rate
- Average request latency
- Model usage
- Prompt and completion tokens
- Total token usage
- Model inference duration
- Actual local API cost
- Request history

Local Ollama inference has no per-request API charge. Electricity and hardware costs are not included.

## Automated Testing

Run the complete test suite:

```bash
python -m pytest -v
```

**Latest test results: 10 passed**

| Test Module | Passed |
|---|---:|
| API | 3 |
| Semantic Cache | 2 |
| Metrics | 2 |
| Model Router | 3 |
| Total | 10 |

## Future Improvements

- Improve semantic cache accuracy using larger evaluation datasets.
- Develop more robust intent classification.
- Explore adaptive similarity thresholds.
- Implement advanced model-routing strategies.
- Add cache eviction and expiration policies.
- Introduce production-ready monitoring and benchmarking.
- Compare local inference performance across different models.
---

