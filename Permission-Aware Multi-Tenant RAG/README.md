# Permission-Aware Multi-Tenant RAG API

A secure Retrieval-Augmented Generation (RAG) application built with Python, FastAPI, ChromaDB, Streamlit, and Ollama. It implements tenant-level and role-based document access control to ensure users can retrieve information only from documents they are authorized to access.

## Project Overview

This project demonstrates how to build a multi-tenant RAG system where different organizations (tenants) can securely access their own documents.

Unlike a basic RAG application, this system applies access-control filters before retrieving documents from the vector database.

The application combines semantic search with a locally hosted Large Language Model (LLM) to generate context-aware answers.

## Key Features

- **Multi-Tenant Architecture:** Supports multiple tenants with isolated document access.
- **Role-Based Access Control (RBAC):** Restricts document retrieval according to user roles.
- **Secure Retrieval:** Applies tenant and role filters during vector database queries.
- **Document Ingestion:** Loads documents, splits them into chunks, and generates embeddings.
- **Vector Search:** Uses ChromaDB for persistent vector storage and semantic retrieval.
- **Local LLM Integration:** Uses Ollama with Llama 3.2 to generate answers.
- **FastAPI Backend:** Provides REST API endpoints for RAG queries.
- **Streamlit Frontend:** Provides an interactive interface for testing the application.
- **Audit Logging:** Records access decisions and query activity.
- **Input Validation:** Handles invalid users and empty questions.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Backend | FastAPI |
| Frontend | Streamlit |
| Vector Database | ChromaDB |
| Embeddings | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Large Language Model | Llama 3.2 |
| LLM Runtime | Ollama |
| API Testing | Swagger UI |
| Data Processing | LangChain |
| API Communication | Requests |

## System Architecture

```text
                  User
                   |
                   v
             Streamlit UI
                   |
                   v
              FastAPI
                   |
                   v
          User Identification
                   |
                   v
       Tenant and Role Validation
                   |
                   v
          Secure Document Retrieval
                   |
                   v
               ChromaDB
                   |
                   v
          Relevant Document Chunks
                   |
                   v
            RAG Pipeline
                   |
                   v
              Ollama LLM
              (Llama 3.2)
                   |
                   v
            Generated Answer
                   |
                   v
             User Response

          Audit Logging
```

## Multi-Tenant Access Control

The project uses four demo users belonging to two different tenants.

| Username | Tenant | Role | Document Access |
|---|---|---|---|
| alice | tenant_a | engineer | Engineering |
| emma | tenant_a | hr | HR |
| bob | tenant_b | engineer | Engineering |
| david | tenant_b | finance | Finance |

### Security Implementation

The retrieval process applies two conditions:

1. Tenant ID must match the user's tenant.
2. Allowed role must match the user's role.

Only documents satisfying both conditions can be retrieved.

This prevents users from accessing documents belonging to another tenant or an unauthorized role.

## Project Structure

```text
Permission-Aware Multi-Tenant RAG/
│
├── src/
│   ├── ingestion/
│   │   ├── metadata.py
│   │   ├── loader.py
│   │   └── ingest.py
│   │
│   ├── retrieval/
│   │   ├── vector_store.py
│   │   └── secure_retriever.py
│   │
│   ├── auth/
│   │   ├── users.py
│   │   ├── permissions.py
│   │   └── filter.py
│   │
│   ├── rag/
│   │   ├── llm.py
│   │   └── pipeline.py
│   │
│   └── utils/
│       └── audit_logger.py
│
├── data/
│   ├── tenant_a/
│   ├── tenant_b/
│   └── chroma_db/
│
├── logs/
├── ui/
│   └── app.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mansidhenge10/AI-PROJECTS.git
```

Navigate to the project directory:

```bash
cd "AI-PROJECTS/Permission-Aware Multi-Tenant RAG"
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Install and Configure Ollama

Install Ollama from:

https://ollama.com/

Download the model:

```bash
ollama pull llama3.2
```

### 5. Run Document Ingestion

Run the ingestion script from the project root:

```bash
python -m src.ingestion.ingest
```

This processes the sample documents, generates embeddings, and stores them in ChromaDB.

### 6. Start the FastAPI Backend

```bash
python -m uvicorn app:app --reload
```

Open Swagger UI:

http://127.0.0.1:8000/docs

### 7. Start the Streamlit Frontend

Open another terminal, activate the virtual environment, and run:

```bash
streamlit run ui/app.py
```

The frontend will open in your browser.

## API Documentation

### GET /

Checks whether the API is running.

### POST /query

Accepts a username and question and returns an answer based on authorized documents.

**Example Request:**

```json
{
  "username": "alice",
  "question": "What technologies does the engineering team use?"
}
```

**Example Response:**

```json
{
  "username": "alice",
  "tenant_id": "tenant_a",
  "role": "engineer",
  "question": "What technologies does the engineering team use?",
  "answer": "The engineering team uses Python, FastAPI, and Docker for backend development.",
  "sources": [
    "engineering.txt"
  ]
}
```

## Security Testing

The application was tested with different users and access permissions.

| Test Case | Expected Result |
|---|---|
| Alice accesses tenant_a engineering | Allowed |
| Emma accesses tenant_a HR | Allowed |
| Bob accesses tenant_b engineering | Allowed |
| David accesses tenant_b finance | Allowed |
| Alice attempts to access HR documents | Denied |
| Alice attempts to access tenant_b engineering | Denied |
| Unknown username sends a query | 404 User Not Found |
| Empty question is submitted | Validation error |

The tests demonstrate tenant isolation and role-based document retrieval.

## Important Security Note

This is a portfolio and learning prototype. User identities are simulated through predefined demo accounts. The API currently accepts a username from the request rather than verifying a real authenticated identity.

For production deployment, authentication should be implemented using secure identity verification, such as JWT or OAuth2. Additional protections, including stronger tenant isolation, input controls, and deployment security, would also be required.

## Future Improvements

- JWT-based authentication and authorization.
- Support for PDF, DOCX, and additional document formats.
- Admin dashboard for tenant and user management.
- Advanced retrieval with reranking.
- Semantic caching to reduce repeated LLM calls.
- Cloud deployment and monitoring.
- Automated security and integration tests.

