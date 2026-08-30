# 🤖 AI Interview Mistake Analyzer

An AI-powered interview practice application that analyzes candidate answers and provides structured feedback to help users improve their technical and HR interview performance.

The system combines **NLP-based analysis, concept coverage, answer-quality scoring, and Llama 3.2 AI feedback** to identify mistakes, missing concepts, and areas for improvement.

---

## 🚀 Project Overview

Interview preparation is an important part of getting a job. However, candidates often struggle to understand:

* Whether their answer is relevant
* Which important concepts they missed
* How good their answer is
* What mistakes they made
* How they can improve their answer
* What a better interview answer looks like

The **AI Interview Mistake Analyzer** helps automate this process.

A user selects a job domain and interview type, receives interview questions, submits an answer, and gets detailed AI-powered feedback.

The system can provide:

* Relevance score
* Concept coverage score
* Overall answer quality
* Covered concepts
* Missing concepts
* NLP-based feedback
* Improvement suggestions
* AI-generated interview feedback
* Better sample answers using Llama 3.2

---

## 🎯 Project Objective

The main objective of this project is to build an intelligent interview-practice assistant that can:

1. Provide job-specific interview questions.
2. Randomly select interview questions.
3. Support technical and HR interview types.
4. Analyze candidate answers using NLP.
5. Measure answer relevance.
6. Detect important concepts covered in the answer.
7. Identify missing concepts.
8. Calculate overall answer quality.
9. Classify the answer based on its quality.
10. Generate improvement suggestions.
11. Provide AI-powered feedback using Llama 3.2.
12. Help candidates improve their interview communication and technical explanations.

---

## 🔄 Project Workflow

```text
                    User
                      │
                      ▼
             Select Job Domain
                      │
                      ▼
             Select Interview Type
                      │
                      ▼
             Start New Interview
                      │
                      ▼
          Random Interview Question
                      │
                      ▼
              Display Question
                      │
                      ▼
             Candidate Answer
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       Submit Answer       Skip Question
             │                 │
             ▼                 ▼
        Text Processing    Next Question
             │
             ▼
       TF-IDF Similarity
             │
             ▼
       Relevance Analysis
             │
             ▼
       Concept Coverage
             │
        ┌────┴────┐
        │         │
        ▼         ▼
    Covered     Missing
    Concepts    Concepts
        │         │
        └────┬────┘
             ▼
      Answer Quality Score
             │
             ▼
      Answer Classification
             │
             ▼
      Mistake Analysis
             │
             ▼
     Improvement Suggestions
             │
             ▼
        Llama 3.2 Analysis
             │
             ▼
       AI Interview Feedback
             │
             ▼
      Better Sample Answer
             │
             ▼
        Next Question
```

---

## 🧠 Key Features

### 1. 🎯 Job Domain Selection

Users can select the type of role they are preparing for.

Supported domains include:

* AI/ML Engineer
* Data Analyst
* Python Developer
* Frontend Developer
* Data Scientist

---

### 2. 💼 Interview Type Selection

The application supports different interview formats:

* Technical Interview
* HR Interview

---

### 3. 🎲 Random Question Selection

Interview questions are selected randomly from the available questions for the selected job domain and interview type.

This makes every interview session more dynamic and prevents users from repeatedly receiving the same question.

---

### 4. 🔢 Interview Progress Tracking

The application tracks the number of questions completed during an interview.

Example:

```text
Question 1 / 10
Question 2 / 10
Question 3 / 10
...
Question 10 / 10
```

---

### 5. 💬 Candidate Answer Input

Users can enter their interview answer directly into the application.

The submitted answer is then processed and analyzed by the NLP pipeline.

---

### 6. 📊 Relevance Score

The system calculates how relevant the candidate's answer is to the expected concepts of the interview question.

Example:

```text
Relevance Score: 72.50%
```

---

### 7. 🧠 Concept Coverage Analysis

The system checks whether important expected concepts are present in the candidate's answer.

Example:

```text
Expected Concepts:
- precision
- recall
- true positive
- false positive
- false negative
- F1 score
```

The system identifies:

```text
Covered Concepts:
✓ precision
✓ recall
✓ F1 score

Missing Concepts:
✗ true positive
✗ false positive
✗ false negative
```

---

### 8. ❌ Mistake Detection

The application identifies missing concepts and weaknesses in the candidate's response.

This helps the candidate understand exactly what was missing from their answer.

---

### 9. 🏆 Answer Classification

The answer is classified according to its overall quality.

Possible classifications include:

* Strong Answer
* Good Answer
* Average Answer
* Weak Answer
* Major Improvement Needed

---

### 10. 💡 NLP Feedback

The NLP-based analyzer generates feedback based on the concepts missing from the candidate's answer.

Example:

```text
Your answer is missing some important concepts.

You should discuss:
precision, recall, true positive, false positive,
false negative, and F1 score.
```

---

### 11. 🎯 Improvement Suggestions

The system provides specific suggestions for improving the candidate's answer.

Example:

```text
• Learn and explain the concept of precision.
• Learn and explain the concept of recall.
• Explain the difference between false positive and false negative.
• Explain how F1 score combines precision and recall.
```

---

### 12. 🤖 Llama 3.2 AI Feedback

The project uses **Llama 3.2** through Ollama to provide deeper AI-powered analysis.

The AI evaluates:

* What the candidate did well
* What is missing
* What is incorrect
* Explanation of mistakes
* Specific improvement suggestions
* A better sample answer
* Additional interview tips

Example:

```text
1. What the candidate did well

2. What is missing or incorrect

3. Explanation of mistakes

4. Specific improvement suggestions

5. A better sample answer
```

---

### 13. ⏭️ Skip Question

Users can skip a question when they do not know the answer.

The application then moves to the next interview question.

---

### 14. ➡️ Next Question

After submitting an answer and receiving feedback, the user can continue the interview by moving to the next question.

---

### 15. 🔄 New Interview

Users can start a completely new interview session.

The question counter and previous interview state are reset.

---

## 🧩 Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Core programming language      |
| Streamlit    | Web application interface      |
| Pandas       | Dataset and CSV processing     |
| NLTK         | Natural Language Processing    |
| Scikit-learn | TF-IDF and similarity analysis |
| Ollama       | Local LLM execution            |
| Llama 3.2    | AI-powered answer analysis     |
| NumPy        | Numerical processing           |
| Requests     | HTTP/API communication         |

---

## 🧠 NLP Pipeline

The project uses multiple NLP techniques to evaluate candidate answers.

```text
Candidate Answer
       │
       ▼
Text Processing
       │
       ▼
Tokenization
       │
       ▼
Stopword Handling
       │
       ▼
TF-IDF Analysis
       │
       ▼
Similarity Calculation
       │
       ▼
Concept Matching
       │
       ▼
Concept Coverage
       │
       ▼
Answer Quality Score
       │
       ▼
Feedback Generation
```

---

## 📊 Answer Evaluation

The system evaluates an answer using multiple components.

### Relevance

Measures how closely the candidate's answer relates to the expected concepts.

### Concept Coverage

Measures how many important concepts from the expected answer were covered.

### Answer Quality

Combines the evaluation results to produce an overall quality score.

Example:

```text
Relevance Score     : 75.20%
Concept Coverage    : 66.67%
Answer Quality      : 71.79%
```

---

## 🤖 AI Analysis Pipeline

The NLP-based analysis is combined with Llama 3.2 for deeper feedback.

```text
Candidate Answer
       │
       ├──────────────► NLP Analysis
       │                    │
       │                    ├── Relevance
       │                    ├── Concept Coverage
       │                    └── Answer Quality
       │
       └──────────────► Llama 3.2
                            │
                            ├── Strengths
                            ├── Mistakes
                            ├── Missing Information
                            ├── Suggestions
                            └── Better Answer
```

---

## 📁 Project Structure

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
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📄 Dataset

The project uses an interview-question dataset stored in:

```text
data/interview_questions.csv
```

The dataset contains information such as:

* Job domain
* Interview type
* Category
* Difficulty
* Interview question
* Expected concepts

Example:

```text
Job Domain: AI/ML Engineer
Interview Type: Technical
Category: Machine Learning
Difficulty: Medium
Question: What is the difference between precision, recall and F1 score?
Expected Concepts:
precision; recall; true positive; false positive;
false negative; f1 score
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

### 2. Navigate to the project

```bash
cd "AI INTERVIEW MISTAKE ANALYZER"
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Ollama Setup

This project uses Ollama to run Llama 3.2 locally.

Install Ollama and download the model:

```bash
ollama pull llama3.2
```

Verify that the model is available:

```bash
ollama list
```

You should see:

```text
llama3.2
```

---

## ▶️ Running the Project

First activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run the Streamlit application:

```bash
streamlit run ui/app.py
```

The application will open in your browser.

Example:

```text
http://localhost:8501
```

---

## 🖥️ Application Flow

```text
1. Select Job Domain
        ↓
2. Select Interview Type
        ↓
3. Start New Interview
        ↓
4. Receive Random Question
        ↓
5. Write Your Answer
        ↓
6. Submit / Skip
        ↓
7. NLP Analysis
        ↓
8. View Scores
        ↓
9. View Missing Concepts
        ↓
10. View Improvement Suggestions
        ↓
11. Receive Llama 3.2 Feedback
        ↓
12. Continue to Next Question
```

---

## 📊 Example Output

```text
Interview Analysis

Your Submitted Answer:
"Precision is about correct predictions."

Relevance Score:
45.20%

Concept Coverage:
33.33%

Answer Quality:
40.25%

Answer Classification:
Average Answer

Covered Concepts:
✓ precision

Missing Concepts:
✗ recall
✗ false positive
✗ false negative
✗ F1 score

NLP Feedback:
Your answer is missing some important concepts.

Improvement Suggestions:
• Explain recall.
• Explain false positives and false negatives.
• Explain how F1 score combines precision and recall.

Llama 3.2 AI Interview Feedback:
The candidate demonstrated a basic understanding of
precision but did not explain recall or F1 score...
```

---

## 🔮 Future Enhancements

The project can be extended with:

* 🎤 Voice-based interview answers
* 🗣️ Speech-to-text processing
* 🔊 Pronunciation analysis
* ⏱️ Interview timer
* 📈 Interview performance dashboard
* 📊 Performance history
* 🏅 Interview score history
* 🎯 Personalized learning recommendations
* 🧠 More advanced semantic similarity
* 📚 Question difficulty adaptation
* 🎲 Larger interview question database
* 👤 User accounts and authentication
* 📄 Interview performance report generation
* 🌐 Deployment as an online application

---

## 🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Python application development
* Streamlit application development
* Natural Language Processing
* Text preprocessing
* TF-IDF
* Similarity analysis
* Concept extraction
* Text classification
* Evaluation metrics
* LLM integration
* Local LLM deployment
* Prompt engineering
* Session-state management
* CSV dataset processing
* AI-powered feedback generation

---


