# 🤖 AI Engineering  Projects

### A collection of practical AI, Machine Learning, NLP, Generative AI, and LLM-based projects built to develop real-world AI Engineering skills.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)](https://scikit-learn.org/)
[![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green)](https://www.nltk.org/)
[![Generative AI](https://img.shields.io/badge/Generative%20AI-LLM-purple)](https://huggingface.co/)
[![Projects](https://img.shields.io/badge/Projects-2-orange)](https://github.com/)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/)

---

## 🚀 About This Repository

Welcome to my **AI Engineering Projects** repository!

This repository contains practical AI projects that I am building while developing my skills in:

* Artificial Intelligence
* Machine Learning
* Natural Language Processing
* Generative AI
* Large Language Models
* AI Application Development

Instead of learning AI only through theory, I focus on **learning by building real-world applications**.

Each project is designed to strengthen different areas of the AI Engineering workflow, including:

* Python programming
* Machine Learning
* Natural Language Processing
* Text processing
* LLM integration
* Prompt Engineering
* AI application development
* REST APIs
* Software development
* Problem solving

These projects represent my progression from **traditional NLP and Machine Learning toward modern Generative AI and AI Engineering**.

---

# 📂 Projects

| sr.no       | Project                           | Description                                                                                                                                            | Key Technologies                             |
| -------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| 🧑‍💻 01 | **Auto Code Reviewer**            | An AI-powered application that automatically analyzes source code, identifies potential issues, and provides explanations and improvement suggestions. | Python, LLM, Hugging Face, NLP, FastAPI      |
| 🤖 02    | **AI Interview Mistake Analyzer** | An AI-powered application that analyzes interview answers and provides feedback on mistakes, missing concepts, and areas for improvement.              | Python, NLP, NLTK, TF-IDF, Scikit-learn, LLM |
| 🤖 03 | **AI Resume Analyzer** | An AI-powered application that analyzes resumes, extracts skills and important information, compares resumes with job descriptions, and provides ATS-style scoring, missing skills, and AI-powered improvement suggestions. | Python, NLP, NLTK, TF-IDF, Scikit-learn, Streamlit, LLM |
| 🧑‍💻 04 | Permission-Aware Multi-Tenant RAG | A secure Retrieval-Augmented Generation application that retrieves information while enforcing tenant-level and role-based access permissions. | Python, FastAPI, ChromaDB, LangChain, Ollama, Llama 3.2, Hugging Face |
| ⚡ 05 | Semantic Caching & Cost-Aware Routing | An intelligent LLM optimization system that uses semantic caching and cost-aware model routing to reduce redundant model calls, improve response efficiency, and monitor application performance. | Python, FastAPI, Streamlit, SQLite, Sentence Transformers, Ollama, Llama 3.2, Qwen 2.5 |

---

# 🧑‍💻 01. Auto Code Reviewer

An **AI-powered code review application** designed to automatically analyze source code and provide useful feedback to developers.

The application uses AI and Large Language Models to identify potential problems, explain detected issues, and suggest improvements.

### ✨ Features

* Source code input
* Automatic code analysis
* Potential issue detection
* Code quality analysis
* Error explanation
* Improvement suggestions
* AI-generated code review
* Structured feedback
* Code improvement recommendations
* Support for multiple programming languages

### 🛠️ Technologies Used

```text
Python
Large Language Models
Hugging Face
NLP
Prompt Engineering
FastAPI
REST API
```

### 🔄 Project Workflow

```text
Source Code
     │
     ▼
Code Input
     │
     ▼
Code Analysis
     │
     ▼
Issue Detection
     │
     ▼
LLM Processing
     │
     ▼
AI Code Review
     │
     ▼
Suggestions & Explanation
```

### 🎯 Goal

The goal of this project is to demonstrate how **Large Language Models can be integrated into practical developer tools** to automatically analyze source code and provide meaningful feedback.

---
# 🤖 02. AI Interview Mistake Analyzer

An **AI-powered interview preparation and answer analysis application** that helps candidates practice **technical and HR interviews** and receive intelligent feedback on their answers.

The application supports both **text and microphone-based answers**. Microphone responses are automatically converted into text using **Whisper**, after which the system evaluates the answer using **NLP techniques, TF-IDF, concept coverage, similarity analysis, and Llama 3.2-based AI feedback**.

The goal is to provide candidates with actionable feedback on **answer relevance, concept coverage, answer quality, missing concepts, and areas for improvement**.

---

## ✨ Features

### 🎯 Interview Practice

* Job-domain based interview questions
* Technical interview questions
* HR interview questions
* Random question selection
* 10-question interview sessions
* Question progress tracking
* Skip question functionality
* Start a new interview anytime

### 📝 Multiple Answer Methods

Candidates can choose how they want to answer each question:

* 📝 **Text Answer**
* 🎙️ **Microphone Answer**

The selected answer method continues throughout the interview until the candidate chooses to change it.

### 🎙️ Speech-to-Text

Microphone answers are processed using **OpenAI Whisper locally**.

Workflow:

```text
Microphone
    ↓
Audio Recording
    ↓
Whisper Speech-to-Text
    ↓
Transcribed Answer
    ↓
Answer Analysis
```

Whisper runs locally, so the project does not require an OpenAI API key for speech-to-text.

### 🧠 NLP Analysis

The application performs several NLP operations:

* Text cleaning
* Tokenization
* Stopword removal
* Lemmatization
* TF-IDF analysis
* Cosine similarity
* Expected concept extraction
* Concept coverage analysis
* Missing concept detection

### 📊 Answer Evaluation

Each submitted answer is evaluated using:

* **Relevance Score**
* **Concept Coverage Score**
* **Answer Quality Score**
* Covered concepts
* Missing concepts
* Answer classification

### 🤖 Llama 3.2 AI Feedback

The project uses **Llama 3.2** to provide AI-powered feedback on the candidate's answer.

The LLM analyzes the answer and provides feedback about:

* Answer quality
* Technical correctness
* Missing information
* Explanation quality
* Areas for improvement

### 💡 Personalized Suggestions

The system generates improvement suggestions based on the concepts missing from the candidate's answer.

### 📈 Interview Summary

After completing the interview, the application displays:

* Total questions
* Number of answered questions
* Number of skipped questions
* Average relevance score
* Average concept coverage
* Average answer quality
* Answer-quality performance graph
* Overall interview performance

---

# 🔄 Complete Project Workflow

```text
                    ┌──────────────────────┐
                    │   Start Interview    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Select Job Domain    │
                    │ & Interview Type     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Interview Question │
                    └──────────┬───────────┘
                               │
                               ▼
                  ┌───────────────────────────┐
                  │ Choose Answer Method      │
                  │                           │
                  │ 📝 Text   │   🎙️ Mic     │
                  └────────────┬──────────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌────────────────┐          ┌────────────────┐
        │   Text Answer  │          │ Audio Recording│
        └───────┬────────┘          └───────┬────────┘
                │                           │
                │                           ▼
                │                  ┌─────────────────┐
                │                  │ Whisper Speech  │
                │                  │   to Text       │
                │                  └────────┬────────┘
                │                           │
                └─────────────┬─────────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Text Preprocessing  │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ TF-IDF Analysis     │
                   │ & Similarity        │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Concept Coverage    │
                   │ & Missing Concepts  │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Answer Quality      │
                   │ Evaluation          │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Llama 3.2 AI        │
                   │ Feedback             │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Improvement         │
                   │ Suggestions         │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Next Question       │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Interview Summary   │
                   │ & Performance Graph│
                   └─────────────────────┘
```

---

# 🧠 Answer Evaluation Pipeline

The project combines **traditional NLP techniques with Generative AI**.

```text
Candidate Answer
       │
       ▼
Text Cleaning
       │
       ▼
Tokenization
       │
       ▼
Stopword Removal
       │
       ▼
Lemmatization
       │
       ▼
TF-IDF
       │
       ▼
Similarity Analysis
       │
       ▼
Concept Coverage
       │
       ├──────────────► Covered Concepts
       │
       └──────────────► Missing Concepts
                              │
                              ▼
                       Llama 3.2 Analysis
                              │
                              ▼
                     AI-Powered Feedback
```

---

# 📊 Scoring System

The application evaluates answers using three major metrics.

### Relevance Score

Measures how closely the candidate's answer relates to the expected concepts of the question.

### Concept Coverage

Measures how many important concepts from the expected answer were covered.

### Answer Quality

Combines the evaluation results to provide an overall assessment of the candidate's answer.

The application then classifies the answer based on its quality score.

```text
80%+  → Excellent
60–79% → Good
40–59% → Average
Below 40% → Needs Improvement
```

---

# 🎙️ Text & Voice Interview Architecture

One of the main features of this project is supporting two different input methods.

### Text Mode

```text
Question
   ↓
Candidate types answer
   ↓
Submit
   ↓
NLP Analysis
   ↓
Llama 3.2 Analysis
   ↓
Feedback
   ↓
Next Question
```

### Microphone Mode

```text
Question
   ↓
Candidate speaks
   ↓
Audio Recording
   ↓
Whisper
   ↓
Speech-to-Text
   ↓
Transcribed Answer
   ↓
NLP Analysis
   ↓
Llama 3.2 Analysis
   ↓
Feedback
   ↓
Next Question
```

Both methods use the **same answer-analysis pipeline** after the answer becomes text.

---
# 📄 03. AI Resume Analyzer

An **AI-powered resume analysis application** designed to analyze resumes, extract important information, and compare candidate profiles with job descriptions.

The application uses **NLP, Machine Learning, and Large Language Models** to evaluate resume content, identify relevant skills, detect missing skills, calculate an ATS-style match score, and provide actionable recommendations for improving the resume.

### ✨ Features

* Resume upload support for PDF and DOCX
* Automatic resume text extraction
* Resume section detection
* NLP-based text preprocessing
* Automatic skill extraction
* Job description analysis
* Resume and job description comparison
* ATS-style resume scoring
* Matched skill identification
* Missing skill detection
* Keyword analysis
* Resume strengths and weaknesses
* AI-generated resume feedback
* Resume improvement suggestions
* Job-specific recommendations

### 🛠️ Technologies Used

```text
Python
Streamlit
NLP
NLTK
Scikit-learn
TF-IDF
PyMuPDF
python-docx
Machine Learning
Large Language Models
Ollama
Llama 3.2
```

### 🔄 Project Workflow

```text
Resume Upload
      │
      ▼
PDF / DOCX Text Extraction
      │
      ▼
Text Preprocessing
      │
      ▼
Resume Section Detection
      │
      ▼
Skill & Keyword Extraction
      │
      ▼
Job Description Analysis
      │
      ▼
Resume ↔ Job Matching
      │
      ▼
ATS-Style Score
      │
      ▼
Matched & Missing Skills
      │
      ▼
LLM Analysis
      │
      ▼
AI Feedback & Recommendations
```
## 🔐 04. Permission-Aware Multi-Tenant RAG

A Retrieval-Augmented Generation (RAG) application designed to provide secure, context-aware responses while enforcing tenant-based and role-based access control.

The application allows multiple tenants to store and retrieve their own documents. Before retrieving information, the system applies access permissions based on the user's tenant and role.

This helps prevent users from accessing documents that they are not authorized to view.

### ✨ Features

- Multi-tenant document management
- Tenant-based data isolation
- Role-based access control
- Permission-aware document retrieval
- Document ingestion and processing
- Vector embeddings for semantic search
- ChromaDB vector database integration
- Context-aware information retrieval
- LLM-powered answer generation
- Ollama local LLM integration
- Audit logging for application activities
- FastAPI-based backend

### 🛠️ Technologies Used

- Python
- FastAPI
- ChromaDB
- LangChain
- Ollama
- Llama 3.2
- Hugging Face
- Sentence Transformers
- Vector Embeddings
- Retrieval-Augmented Generation (RAG)
- Role-Based Access Control (RBAC)

### 🔄 Project Workflow

```text
User Login
    │
    ▼
User Identity & Role
    │
    ▼
Tenant Identification
    │
    ▼
Access Permission Validation
    │
    ▼
User Query
    │
    ▼
Permission-Based Retrieval Filter
    │
    ▼
ChromaDB Vector Search
    │
    ▼
Relevant Document Retrieval
    │
    ▼
Context Generation
    │
    ▼
Ollama - Llama 3.2
    │
    ▼
AI-Generated Response
    │
    ▼
Audit Logging
```

### 🔒 Security & Access Control

The application implements access restrictions using:

- Tenant-level document isolation
- Role-based document permissions
- Access filtering before document retrieval
- Controlled retrieval of authorized information

This ensures that retrieved context is restricted according to the configured tenant and role permissions.

### 🎯 Project Goal

The goal of this project is to demonstrate how Retrieval-Augmented Generation can be combined with multi-tenant architecture and access-control mechanisms to build more secure AI-powered applications.

It demonstrates practical concepts in RAG architecture, vector databases, semantic search, LLM integration, API development, and permission-aware information retrieval.

---
### 🎯 Goal

The goal of this project is to demonstrate how **NLP, Machine Learning, and Large Language Models can be combined to build an intelligent career-focused application** that analyzes resumes and helps candidates understand how well their profile matches a target job.

---
# 🛠️ Technologies Used

## 🐍 Programming

* Python 3

## 🧠 Natural Language Processing

* NLTK
* Scikit-learn
* TF-IDF
* Cosine Similarity
* Tokenization
* Stopword Removal
* Lemmatization
* Text Processing

## 🤖 Generative AI

* Llama 3.2
* Large Language Models
* Prompt Engineering
* Generative AI

## 🎙️ Speech Processing

* OpenAI Whisper
* Speech-to-Text
* Local audio processing

## 🌐 Web Application

* Streamlit

## 📊 Data Processing

* Pandas
* CSV

## 🔧 Development Tools

* Git
* GitHub
* VS Code
* Python Virtual Environment

---

# 📁 Project Structure

```text
AI INTERVIEW MISTAKE ANALYZER/
│
├── data/
│   └── interview_questions.csv
│
├── src/
│   ├── __init__.py
│   ├── text_processor.py
│   ├── tfidf_analyzer.py
│   ├── evaluation.py
│   ├── mistake_analyzer.py
│   └── llm_analyzer.py
│
├── ui/
│   └── app.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> `venv/` should remain local and should **not** be uploaded to GitHub.

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/mansidhenge10/AI-PROJECTS.git
```

Navigate to the project:

```bash
cd AI-PROJECTS
cd "AI INTERVIEW MISTAKE ANALYZER"
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

For speech-to-text support:

```bash
pip install openai-whisper
```

Whisper also requires **FFmpeg** to process audio files.

Verify Whisper:

```bash
python -c "import whisper; print('Whisper installed successfully')"
```

Verify FFmpeg:

```bash
ffmpeg -version
```

---

# ▶️ Run the Application

From the project root:

```bash
python -m streamlit run ui/app.py
```

Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🎯 How to Use

### Step 1 — Start Interview

Select:

* Job Domain
* Interview Type

Then click:

```text
🚀 Start New Interview
```

### Step 2 — Select Answer Method

Choose:

```text
📝 Answer with Text
```

or

```text
🎙️ Answer with Microphone
```

### Step 3 — Answer the Question

For text mode, type your answer.

For microphone mode, record your answer and allow Whisper to convert your speech into text.

### Step 4 — Submit

The system analyzes the answer using the NLP and AI pipeline.

### Step 5 — Review Feedback

You receive:

* Relevance score
* Concept coverage
* Answer quality
* Covered concepts
* Missing concepts
* NLP feedback
* Improvement suggestions
* Llama 3.2 feedback

### Step 6 — Continue

Click:

```text
➡️ Next Question
```

and continue the interview until all questions are completed.

### Step 7 — View Final Results

At the end, the application displays an interview summary and performance graph.

---

# 📌 Example

### Interview Question

```text
What is overfitting and how can you prevent it?
```

### Candidate Answer

```text
Overfitting happens when a machine learning model learns
the training data too closely and performs poorly on
unseen data. It can be reduced using regularization,
cross-validation, dropout, and more training data.
```

The system can identify concepts such as:

```text
✓ Training data
✓ Unseen data
✓ Regularization
✓ Cross-validation
✓ Dropout

```

and then generate AI-powered feedback using Llama 3.2.

---

# 🎯 Project Goal

The goal of this project is to combine **traditional Natural Language Processing, Machine Learning techniques, Speech-to-Text, and Generative AI** to build an intelligent interview preparation system.

Instead of only checking whether an answer was submitted, the application attempts to understand:

* What concepts the candidate mentioned
* What important concepts were missing
* How relevant the answer was
* How complete the answer was
* How the candidate can improve

---

# 💡 Key Learning Outcomes

Through this project, the following concepts were implemented:

* Building an end-to-end AI application
* NLP text preprocessing
* TF-IDF vectorization
* Similarity analysis
* Concept extraction
* Rule-based evaluation
* Speech-to-text integration
* Local Whisper model integration
* LLM integration
* Prompt engineering
* Streamlit application development
* Session-state management
* Interactive interview workflows
* Performance visualization
* Git and GitHub project management

---



---

# 🏆 Project Status

```text
✅ Project Completed — Version 1.0
```

The current version supports an end-to-end interview experience using **Text or Microphone input → Whisper Speech-to-Text → NLP Analysis → Llama 3.2 Feedback → Performance Evaluation**.





```

---

# 🛠️ Tech Stack

## 🐍 Programming

**Python 3**

## 🧠 Machine Learning & NLP

* Scikit-learn
* NLTK
* TF-IDF
* Cosine Similarity
* Text Processing

## ✨ Generative AI

* Large Language Models
* Prompt Engineering
* Hugging Face
* AI-powered Applications

## ⚡ Backend & APIs

* FastAPI
* REST APIs

## 🔧 Development Tools

* Git
* GitHub
* VS Code
* Jupyter Notebook

---

# 🧠 Skills Demonstrated

Through these projects, I am developing practical skills in:

```text
Python
   ↓
Machine Learning
   ↓
Natural Language Processing
   ↓
LLMs
   ↓
Prompt Engineering
   ↓
AI Application Development
   ↓
REST APIs
   ↓
AI Engineering 🚀
```

---

# 📈 Learning Journey

My current learning journey follows this progression:

```text
Python
   │
   ▼
Advanced Python
   │
   ▼
Machine Learning
   │
   ▼
NLP
   │
   ▼
Deep Learning
   │
   ▼
Generative AI
   │
   ▼
Large Language Models
   │
   ▼
AI Application Development
   │
   ▼
AI Engineering
```
## ⚡ 05. Semantic Caching & Cost-Aware Routing

An intelligent LLM optimization application designed to reduce redundant Large Language Model (LLM) calls, improve response efficiency, and optimize model selection using semantic caching and cost-aware routing.

The application uses semantic similarity to identify previously answered queries and retrieve cached responses instead of generating new responses every time. It also uses an intelligent model router to select an appropriate language model based on query complexity.

The system integrates local LLMs through Ollama and provides performance monitoring through a dashboard to track cache hits, token usage, response latency, and request metrics.

### ✨ Features

**🧠 Semantic Caching**
- Semantic similarity-based query matching
- Persistent cache storage using SQLite
- Sentence Transformer embeddings
- Similarity threshold-based cache validation
- Cache hit and cache miss detection
- Reuse of previously generated responses
- Reduced redundant LLM calls

**🎯 Cost-Aware Model Routing**
- Intelligent model selection
- Query complexity-based routing
- Lightweight model selection for simple queries
- Advanced model selection for complex queries
- Small model routing using Llama 3.2
- Advanced model routing using Qwen 2.5
- Optimized LLM request handling

**⚡ Performance Optimization**
- Reduced unnecessary model inference
- Faster responses for cached queries
- Semantic query matching
- Intent-aware cache validation
- Efficient request processing

**📊 Performance Monitoring Dashboard**

The application provides a Streamlit dashboard to monitor:

- Total requests
- Cache hits
- Cache hit rate
- Cache misses
- Average response latency
- Prompt token usage
- Completion token usage
- Total token consumption
- Request performance metrics

**🔍 Request Analysis**
- Query processing
- Cache lookup
- Semantic similarity calculation
- Model routing decisions
- LLM response generation
- Cache storage
- Request metrics tracking

### 🛠️ Technologies Used

**🐍 Programming**
- Python 3

**🧠 Semantic Search & Embeddings**
- Sentence Transformers
- all-MiniLM-L6-v2
- Semantic Similarity
- Vector Embeddings

**🤖 Generative AI**
- Large Language Models (LLMs)
- Ollama
- Llama 3.2
- Qwen 2.5
- Prompt Engineering

**🌐 Backend & API**
- FastAPI
- REST API
- Uvicorn

**🗄️ Database & Storage**
- SQLite
- Persistent Semantic Cache

**📊 Dashboard & Monitoring**
- Streamlit
- Performance Metrics
- Token Usage Tracking
- Latency Monitoring

**🧪 Testing**
- Pytest
- API Testing
- Cache Testing
- Model Router Testing
- Metrics Testing

### 🔄 Complete Project Workflow

```text
             User Query
                  │
                  ▼
          Query Preprocessing
                  │
                  ▼
          Semantic Cache Lookup
                  │
                  ▼
        Generate Query Embedding
                  │
                  ▼
       Calculate Semantic Similarity
                  │
                  ▼
          Cache Match Found?
                  │
           ┌──────┴──────┐
           │             │
          YES            NO
           │             │
           ▼             ▼
     Retrieve Cached   Query Complexity
        Response          Analysis
           │             │
           │             ▼
           │       Intelligent Model
           │            Router
           │             │
           │       ┌─────┴─────┐
           │       │           │
           │       ▼           ▼
           │   Small Model  Advanced Model
           │   Llama 3.2    Qwen 2.5
           │       │           │
           │       └─────┬─────┘
           │             │
           │             ▼
           │       LLM Processing
           │             │
           │             ▼
           │       Generate Response
           │             │
           │             ▼
           │       Store in Semantic
           │            Cache
           │             │
           └──────┬──────┘
                  │
                  ▼
           Return Response
                  │
                  ▼
         Record Request Metrics
                  │
                  ▼
       Update Monitoring Dashboard
```

### 🧠 Semantic Caching Pipeline

The project uses semantic similarity to identify queries with similar meanings, even when their wording is different.

```text
          Incoming User Query
                  │
                  ▼
          Text Preprocessing
                  │
                  ▼
       Sentence Transformer Model
             (all-MiniLM-L6-v2)
                  │
                  ▼
           Query Embedding
                  │
                  ▼
        Compare with Cached
             Embeddings
                  │
                  ▼
        Similarity Calculation
                  │
                  ▼
         Similarity Threshold
                  │
           ┌──────┴──────┐
           │             │
           ▼             ▼
       Cache Hit      Cache Miss
           │             │
           ▼             ▼
     Return Stored    Generate New
       Response         Response
                         │
                         ▼
                    Store Result
                         │
                         ▼
                    Return Answer
```

The application uses a configurable semantic similarity threshold of 0.90 to validate cache matches. Intent-aware validation helps avoid reusing responses for queries that are semantically similar but require different answers.

### 🎯 Cost-Aware Model Routing

The model router selects a suitable LLM based on the complexity of the incoming query.

**Small Model Route**

- Model: Llama 3.2
- Used for simple queries
- Suitable for straightforward questions
- Helps avoid unnecessary advanced model calls

**Advanced Model Route**

- Model: Qwen 2.5 (3B)
- Used for more complex queries
- Suitable for queries requiring more detailed reasoning
- Provides an advanced processing route

### 📊 Monitoring & Performance Metrics

The dashboard helps analyze application performance through:

**Cache Hit Rate**

Measures the percentage of requests answered using previously cached responses.

**Average Latency**

Measures the average time required to process requests and generate responses.

**Token Usage**

Tracks prompt tokens, completion tokens, and total token consumption.

**Request Metrics**

Records request counts, cache hits, cache misses, latency, and model usage.

Since the application uses local Ollama models, the actual local API inference cost is zero. The cost-aware routing logic focuses on reducing unnecessary model calls and optimizing resource usage rather than reporting paid API savings.

### 🔄 Request Processing Architecture

**Cache Hit Scenario**

```text
User Query
    ↓
Semantic Cache Lookup
    ↓
Similarity Match
    ↓
Retrieve Cached Response
    ↓
Return Response
```

**Cache Miss Scenario**

```text
User Query
    ↓
Semantic Cache Lookup
    ↓
No Matching Response
    ↓
Query Complexity Analysis
    ↓
Model Router
    ↓
Select Appropriate LLM
    ↓
Ollama Model Processing
    ↓
Generate Response
    ↓
Store Response in Cache
    ↓
Return Response
```

### 🧪 Testing

The project includes automated tests using Pytest to validate:

- Semantic cache functionality
- Cache hit and cache miss handling
- API endpoints
- Model routing decisions
- Performance metrics
- Request processing

**Test Result:** 10 tests passed successfully.

### 🎯 Project Goal

The goal of this project is to demonstrate how semantic caching, sentence embeddings, intelligent model routing, and performance monitoring can be combined to build efficient and optimized LLM-powered applications.

It demonstrates practical concepts in semantic search, vector embeddings, Generative AI, model routing, API development, database management, and LLM performance optimization.
---


---

# 🎯 Career Goal

My goal is to become an **AI Engineer** capable of transforming real-world problems into reliable and useful AI-powered applications.

My current learning path:

**Python → Machine Learning → NLP → Generative AI → LLMs → AI Engineering**

---

# 👩‍💻 About Me

I am building my technical skills through **consistent learning and hands-on project development**.

My current areas of interest include:

* 🐍 Python
* 🤖 Artificial Intelligence
* 🧠 Machine Learning
* 💬 Natural Language Processing
* ✨ Generative AI
* 🦙 Large Language Models
* ⚡ AI Engineering

I believe in learning through:

> **Learn → Build → Debug → Improve → Deploy**

---

# ⭐ Repository Status

**Status:** 🚀 Actively Maintained

This repository currently contains **2 AI Engineering projects** and will be expanded as I build more advanced applications.

---


