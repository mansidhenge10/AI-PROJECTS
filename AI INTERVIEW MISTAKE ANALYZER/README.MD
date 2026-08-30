# 🤖 AI Interview Mistake Analyzer

An **AI-powered interview practice and answer analysis application** that helps candidates improve their technical and HR interview performance.

The application analyzes candidate answers using **Natural Language Processing (NLP), TF-IDF similarity, concept coverage, answer-quality scoring, speech-to-text, and Llama 3.2** to identify missing concepts, weaknesses, mistakes, and areas for improvement.

---

## 🚀 Project Overview

Interview preparation can be difficult because candidates often do not know:

* Whether their answer is relevant
* Which important concepts they missed
* How complete their answer is
* What mistakes they made
* How they can improve their response
* How a stronger interview answer could be structured

The **AI Interview Mistake Analyzer** provides an interactive environment where users can select a job domain and interview type, receive random interview questions, submit answers using **text or microphone**, and receive detailed AI-powered feedback.

### The application provides:

* 🎯 Job-specific interview questions
* 💼 Technical and HR interview modes
* 🎲 Random question selection
* 📝 Text-based answers
* 🎙️ Microphone-based answers
* 🗣️ Speech-to-text using Whisper
* 📊 Relevance scoring
* 🧠 Concept coverage analysis
* ❌ Missing concept detection
* 🏆 Answer-quality classification
* 💡 NLP-based feedback
* 🎯 Personalized improvement suggestions
* 🤖 Llama 3.2 AI feedback
* 📖 Better sample answer generation
* 📈 Interview performance summary
* 🔢 Interview progress tracking
* ⏭️ Question skipping
* 🔄 New interview sessions

---

# 🎯 Project Objective

The main objective is to build an intelligent interview-practice assistant that combines **traditional NLP techniques with modern Generative AI**.

The system is designed to:

1. Provide job-specific interview questions.
2. Support technical and HR interviews.
3. Randomly select interview questions.
4. Accept text and voice-based answers.
5. Convert spoken answers into text using Whisper.
6. Analyze answers using NLP techniques.
7. Measure answer relevance.
8. Detect expected concepts covered by the candidate.
9. Identify missing concepts.
10. Calculate an overall answer-quality score.
11. Classify the candidate's answer.
12. Generate improvement suggestions.
13. Provide deeper feedback using Llama 3.2.
14. Generate a better sample interview answer.
15. Track performance across multiple questions.

---

# ✨ Key Features

## 1. 🎯 Job Domain Selection

Users can select the role they are preparing for.

Supported job domains:

* AI/ML Engineer
* Data Analyst
* Python Developer
* Frontend Developer
* Data Scientist

---

## 2. 💼 Interview Type Selection

The application supports:

* Technical Interview
* HR Interview

This allows the question selection and analysis process to adapt to different interview situations.

---

## 3. 🎲 Random Interview Questions

Questions are selected randomly from the available questions for the selected:

* Job domain
* Interview type

This makes each interview session more dynamic.

---

## 4. 🔢 Interview Progress Tracking

The application tracks interview progress.

Example:

```text
Question 1 / 10
Question 2 / 10
Question 3 / 10
...
Question 10 / 10
```

It also tracks:

* Answered questions
* Skipped questions
* Average scores

---

## 5. 📝 Text Answer Mode

Candidates can type their interview answer directly into the Streamlit interface.

The answer is then passed through the NLP and AI analysis pipeline.

---

## 6. 🎙️ Microphone Answer Mode

Candidates can record their answer using the browser microphone.

The recorded audio is processed using **OpenAI Whisper** to convert speech into text.

```text
Microphone
    ↓
Audio Recording
    ↓
Whisper Speech-to-Text
    ↓
Transcribed Answer
    ↓
NLP Analysis
    ↓
AI Feedback
```

This allows the application to support both written and spoken interview practice.

---

## 7. 🗣️ Speech-to-Text with Whisper

The project integrates **Whisper** for automatic speech recognition.

Whisper converts the recorded interview response into text before sending it through the answer-analysis pipeline.

This creates a complete voice-answer workflow:

```text
Candidate Speech
       ↓
Audio Input
       ↓
Whisper
       ↓
Transcribed Text
       ↓
Text Processing
       ↓
Answer Analysis
```

---

## 8. 📊 Relevance Score

The system calculates how closely the candidate's answer relates to the expected concepts of the question.

Example:

```text
Relevance Score: 75.20%
```

A higher score indicates that the response is more closely related to the expected answer concepts.

---

## 9. 🧠 Concept Coverage Analysis

The system checks whether important concepts expected for the question are present in the candidate's answer.

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

The system can identify:

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

## 10. ❌ Mistake Detection

The application identifies missing concepts and weaknesses in the candidate's response.

Instead of only giving a score, the system shows **what the candidate should improve**.

---

## 11. 🏆 Answer Classification

The answer is classified according to its overall quality.

Possible classifications include:

* Strong Answer
* Good Answer
* Average Answer
* Weak Answer
* Major Improvement Needed

The classification is based on the calculated answer-quality score.

---

## 12. 💡 NLP Feedback

The NLP analysis generates feedback based on missing concepts.

Example:

```text
Your answer is missing some important concepts.

You should discuss:
precision, recall, true positive,
false positive, false negative,
and F1 score.
```

---

## 13. 🎯 Improvement Suggestions

The application generates actionable suggestions based on the candidate's weaknesses.

Example:

```text
• Explain precision clearly.
• Explain recall and its purpose.
• Explain false positives and false negatives.
• Explain how F1 score combines precision and recall.
```

---

## 14. 🤖 Llama 3.2 AI Feedback

The project uses **Llama 3.2 through Ollama** for deeper AI-powered interview analysis.

The LLM evaluates:

* What the candidate did well
* Missing information
* Incorrect information
* Explanation of mistakes
* Improvement suggestions
* Interview communication
* Better sample answer
* Additional interview tips

Example structure:

```text
1. What the candidate did well

2. What is missing or incorrect

3. Explanation of mistakes

4. Specific improvement suggestions

5. Better sample answer
```

---

## 15. ⏭️ Skip Question

Candidates can skip questions they do not know.

The application tracks skipped questions separately from answered questions.

---

## 16. ➡️ Next Question

After submitting an answer and receiving feedback, candidates can continue to the next question.

---

## 17. 🔄 New Interview

Users can start a new interview session.

The application resets:

* Question progress
* Answer statistics
* Scores
* Previous analysis
* Interview state

---

## 18. 📈 Interview Performance Summary

After completing the interview, the application displays:

* Total questions
* Answered questions
* Skipped questions
* Average relevance
* Average concept coverage
* Average answer quality
* Answer-quality graph
* Overall performance classification

Example:

```text
Total Questions       : 10
Answered              : 8
Skipped               : 2

Average Relevance     : 76.40%
Average Coverage      : 70.25%
Average Quality       : 73.32%
```

---

# 🔄 Complete Project Workflow

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
            Random Question
                      │
                      ▼
              Display Question
                      │
                      ▼
             Choose Answer Mode
                ┌─────┴─────┐
                │           │
                ▼           ▼
              Text       Microphone
                │           │
                │           ▼
                │        Audio Input
                │           │
                │           ▼
                │        Whisper
                │           │
                │           ▼
                │     Speech-to-Text
                │           │
                └─────┬─────┘
                      ▼
              Candidate Answer
                      │
                      ▼
             Text Preprocessing
                      │
                      ▼
              TF-IDF Analysis
                      │
                      ▼
            Similarity Calculation
                      │
                      ▼
             Relevance Analysis
                      │
                      ▼
             Concept Coverage
                ┌─────┴─────┐
                │           │
                ▼           ▼
             Covered      Missing
             Concepts     Concepts
                │           │
                └─────┬─────┘
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
                Llama 3.2
                      │
                      ▼
             AI Interview Feedback
                      │
                      ▼
              Better Sample Answer
                      │
                      ▼
                Next Question
                      │
                      ▼
              Interview Summary
```

---

# 🧠 NLP Pipeline

The project combines multiple NLP techniques to evaluate candidate answers.

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
Stopword Handling
       │
       ▼
Lemmatization
       │
       ▼
TF-IDF
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
Answer Quality
       │
       ▼
Feedback Generation
```

---

# 📊 Answer Evaluation

The system evaluates candidate answers using multiple metrics.

### Relevance

Measures how closely the candidate's answer relates to the expected concepts.

### Concept Coverage

Measures how many important expected concepts were included in the answer.

### Answer Quality

Combines the evaluation results into an overall answer-quality score.

Example:

```text
Relevance Score     : 75.20%
Concept Coverage    : 66.67%
Answer Quality      : 71.79%
```

---

# 🤖 AI Analysis Architecture

The project combines traditional NLP with a local LLM.

```text
                    Candidate Answer
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
        NLP Analysis                Llama 3.2
              │                         │
       ┌──────┼──────┐                  │
       │      │      │                  │
       ▼      ▼      ▼                  ▼
   Relevance Coverage Quality      AI Analysis
       │      │      │                  │
       └──────┴──────┘                  │
              │                         │
              ▼                         ▼
       Structured Analysis      Deep AI Feedback
              │                         │
              └──────────┬──────────────┘
                         ▼
                  Final Feedback
```

---

# 🧩 Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Core programming language      |
| Streamlit    | Interactive web application    |
| Pandas       | Dataset and CSV processing     |
| NLTK         | Natural Language Processing    |
| Scikit-learn | TF-IDF and similarity analysis |
| NumPy        | Numerical processing           |
| Whisper      | Speech-to-text                 |
| Ollama       | Local LLM execution            |
| Llama 3.2    | AI-powered answer analysis     |
| Requests     | API communication              |
| Git          | Version control                |
| GitHub       | Source-code hosting            |

---

# 🏗️ Project Architecture

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

# 📄 Dataset

The project uses:

```text
data/interview_questions.csv
```

The dataset contains interview information such as:

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

Question:
What is the difference between precision, recall and F1 score?

Expected Concepts:
precision;
recall;
true positive;
false positive;
false negative;
f1 score
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/mansidhenge10/AI-PROJECTS.git
```

## 2. Navigate to the Project

```bash
cd "AI-PROJECTS/AI INTERVIEW MISTAKE ANALYZER"
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Ollama Setup

This project uses **Ollama** to run Llama 3.2 locally.

Install Ollama and download the model:

```bash
ollama pull llama3.2
```

Verify the model:

```bash
ollama list
```

You should see:

```text
llama3.2
```

Make sure Ollama is running before using the LLM analysis feature.

---

# 🎙️ Whisper Setup

Whisper is used for speech-to-text processing.

Verify the installation:

```bash
python -c "import whisper; print('Whisper installed successfully')"
```

The application uses the Whisper model to convert recorded microphone answers into text.

---

# ▶️ Running the Application

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Run Streamlit:

```powershell
streamlit run ui/app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

If Streamlit selects another available port, use the URL displayed in the terminal.

---

# 🖥️ Application Flow

```text
1. Select Job Domain
        ↓
2. Select Interview Type
        ↓
3. Start New Interview
        ↓
4. Receive Random Question
        ↓
5. Choose Text or Microphone
        ↓
6. Submit Answer
        ↓
7. Speech-to-Text (for voice answers)
        ↓
8. NLP Analysis
        ↓
9. Relevance Score
        ↓
10. Concept Coverage
        ↓
11. Answer Quality
        ↓
12. Mistake Detection
        ↓
13. Improvement Suggestions
        ↓
14. Llama 3.2 Feedback
        ↓
15. Better Sample Answer
        ↓
16. Next Question
        ↓
17. Interview Summary
```

---

# 📊 Example Output

```text
==================================================
INTERVIEW ANALYSIS
==================================================

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
Your answer is missing several important concepts.

Improvement Suggestions:
• Explain recall.
• Explain false positives and false negatives.
• Explain how F1 score combines precision and recall.

Llama 3.2 AI Feedback:
The candidate demonstrated a basic understanding
of precision but did not explain recall or F1 score.

Better Sample Answer:
...
```

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

* Python application development
* Streamlit development
* Natural Language Processing
* Text preprocessing
* Tokenization
* Stopword handling
* Lemmatization
* TF-IDF
* Similarity analysis
* Concept matching
* Concept coverage
* Text classification
* Evaluation metrics
* Speech-to-text
* Whisper
* LLM integration
* Llama 3.2
* Ollama
* Prompt engineering
* Session-state management
* CSV dataset processing
* AI-powered feedback generation
* Git and GitHub

---

# 💼 Resume-Relevant Skills Demonstrated

This project demonstrates experience in:

```text
Python
NLP
Machine Learning
Generative AI
LLMs
Llama 3.2
Ollama
Whisper
TF-IDF
Scikit-learn
NLTK
Streamlit
Pandas
Speech-to-Text
Prompt Engineering
AI Application Development
```

---

# 🔮 Future Enhancements

Possible future improvements include:

* 🔊 Pronunciation and speaking analysis
* ⏱️ Real-time interview timer
* 📈 Advanced performance dashboard
* 📊 Persistent performance history
* 🎯 Personalized learning recommendations
* 🧠 Semantic similarity using embeddings
* 📚 Larger interview-question database
* 🎲 Adaptive question difficulty
* 👤 User authentication
* 📄 Downloadable interview reports
* 🌐 Cloud deployment
* 💾 Database integration
* 🎤 Real-time voice interview mode

---

# 👩‍💻 Author

**Mansi Dhenge**

AI Engineer | Python | Machine Learning | NLP | Generative AI

GitHub:
https://github.com/mansidhenge10

---

## ⭐ Project Highlights

> An end-to-end AI interview practice application combining **NLP, Machine Learning, Speech-to-Text, and Generative AI**.

### Core AI Pipeline

```text
Question
   ↓
Candidate Answer
   ↓
Whisper / Text Input
   ↓
NLP Processing
   ↓
TF-IDF Similarity
   ↓
Concept Coverage
   ↓
Answer Quality Scoring
   ↓
Mistake Detection
   ↓
Llama 3.2
   ↓
Personalized AI Feedback
   ↓
Better Interview Answer
```

---

⭐ If you find this project useful, consider giving the repository a star!
