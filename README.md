# 🤖 AI Engineering Projects

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

### 🎯 Goal

The goal of this project is to demonstrate how **NLP, Machine Learning, and Large Language Models can be combined to build an intelligent career-focused application** that analyzes resumes and helps candidates understand how well their profile matches a target job.

The project also demonstrates practical implementation of **document processing, NLP pipelines, skill extraction, text similarity, scoring systems, and LLM-based recommendations**.
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

# 🔮 Future Enhancements

Possible future versions could include:

* 📅 Interview history
* 💾 Persistent performance database
* 📈 Long-term performance tracking
* 🎯 Topic-wise weakness analysis
* 🧠 Adaptive question difficulty
* 🎤 Voice-confidence analysis
* ⏱️ Interview time tracking
* 👁️ Facial-expression analysis
* 📊 Advanced performance dashboard
* 📄 Resume-based interview questions
* 🎯 Personalized interview preparation plans

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

---

# 🔮 Future Plans

This repository will continue to evolve as I develop my AI Engineering skills.

Future projects may include:

* 🔹 RAG Applications
* 🔹 AI Agents
* 🔹 Multi-Agent Systems
* 🔹 Advanced NLP Applications
* 🔹 Voice AI Applications
* 🔹 Computer Vision Applications
* 🔹 LLM Evaluation
* 🔹 AI Automation
* 🔹 AI-powered APIs
* 🔹 Dockerized AI Applications
* 🔹 Cloud Deployment

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


