AI Interview Mistake Analyzer

An AI-powered interview practice application that helps candidates practice interview questions, evaluate their answers, identify missing concepts, and receive detailed feedback from Llama 3.2.

The project combines NLP techniques, TF-IDF similarity, concept coverage analysis, rule-based evaluation, and a local LLM to provide a complete interview feedback system.

🚀 Features
🎯 Interview Practice
Select a job domain
Select interview type
Start a new interview
Randomly selects interview questions
Supports multiple questions per interview
Displays interview progress
📝 Answer Evaluation
Candidate enters an answer for each question
TF-IDF-based similarity analysis
Relevance score calculation
Expected concept detection
Concept coverage score
Missing concept identification
Overall answer quality score
🤖 AI-Powered Feedback
Uses Llama 3.2 through Ollama
Analyzes the candidate's answer
Identifies strengths and weaknesses
Explains mistakes
Provides improvement suggestions
Generates a better sample answer
📊 Interview Analysis

The application provides:

Relevance Score
Concept Coverage
Answer Quality
Answer classification
Covered concepts
Missing concepts
NLP feedback
Improvement suggestions
Llama 3.2 AI feedback
🎮 Interview Controls
🚀 Start New Interview
📤 Submit Answer
⏭️ Skip Question
➡️ Next Question
🔄 Start New Interview
🧠 How It Works

The application follows this workflow:

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
                    │ Random Question      │
                    │ Selection            │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Candidate Answers    │
                    │ Question             │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                      │
                    ▼                      ▼
             Submit Answer            Skip / Next
                    │                      │
                    ▼                      │
          ┌──────────────────┐             │
          │ TF-IDF Analysis  │             │
          └────────┬─────────┘             │
                   │                       │
                   ▼                       │
          ┌──────────────────┐             │
          │ Concept Coverage │             │
          └────────┬─────────┘             │
                   │                       │
                   ▼                       │
          ┌──────────────────┐             │
          │ Score Evaluation │             │
          └────────┬─────────┘             │
                   │                       │
                   ▼                       │
          ┌──────────────────┐             │
          │ Llama 3.2        │             │
          │ AI Analysis      │             │
          └────────┬─────────┘             │
                   │                       │
                   ▼                       │
          ┌──────────────────┐             │
          │ Detailed         │             │
          │ Feedback         │             │
          └──────────────────┘             │
                   │                       │
                   └───────────────┬───────┘
                                   ▼
                           Next Question
🛠️ Tech Stack
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
Pandas	Dataset handling
NLTK	Natural Language Processing
Scikit-learn	TF-IDF and similarity analysis
Ollama	Local LLM execution
Llama 3.2	AI-powered answer analysis
PyDeck	Data visualization support
Requests	HTTP/API communication
📂 Project Structure
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
│
├── README.md
│
└── .gitignore
📊 Dataset

The project uses an interview-question dataset stored in:

data/interview_questions.csv

The dataset contains interview questions along with information such as:

Job domain
Interview type
Category
Difficulty
Question
Expected concepts

Example:

Job Domain:
AI/ML Engineer

Interview Type:
Technical

Category:
Machine Learning

Difficulty:
Medium

Question:
What is the difference between supervised and unsupervised learning?

Expected Concepts:
labeled data;
unlabeled data;
supervised learning;
unsupervised learning;
prediction;
pattern discovery
🧮 Answer Evaluation

The project evaluates candidate answers using multiple stages.

1. TF-IDF Similarity

The candidate answer is compared with the expected concepts using TF-IDF-based similarity.

This helps determine how closely the answer relates to the expected concepts.

2. Relevance Score

The similarity result is converted into a relevance score.

3. Concept Coverage

The application checks which expected concepts were mentioned in the candidate's answer.

Example:

Expected Concepts:

✓ precision
✓ recall
✓ true positive
✓ false positive
✗ false negative
✗ f1 score
4. Answer Quality

The relevance and concept coverage scores are combined to calculate an overall answer-quality score.

5. Answer Classification

The answer is classified based on the overall score.

For example:

Excellent Answer
Good Answer
Average Answer
Weak Answer
🤖 Llama 3.2 Integration

The project uses Llama 3.2 locally through Ollama.

The LLM analyzes:

What the candidate did well
Missing or incorrect information
Explanation of mistakes
Improvement suggestions
Better sample answer
Additional interview tips

Example workflow:

Candidate Answer
       │
       ▼
   Llama 3.2
       │
       ▼
AI Interview Feedback
       │
       ├── What went well
       ├── Missing information
       ├── Mistakes
       ├── Improvements
       └── Better Answer

Running the LLM locally allows the project to perform AI analysis without sending candidate answers to an external LLM API.

⚙️ Installation
1. Clone the Repository
git clone https://github.com/mansidhenge10/AI-PROJECTS.git

Navigate to the project:

cd "AI INTERVIEW MISTAKE ANALYZER"
2. Create Virtual Environment
python -m venv venv

Activate it on Windows PowerShell:

.\venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt
🦙 Install Ollama

Install Ollama on your system and make sure it is running.

Then download the Llama 3.2 model:

ollama pull llama3.2

Verify that the model is available:

ollama list

You should see:

llama3.2
▶️ Run the Application

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Run Streamlit:

streamlit run ui/app.py

The terminal will provide a local URL similar to:

http://localhost:8502

Open the URL in your browser.

🎯 Using the Application
Step 1 — Select Interview Settings

Choose:

Job Domain
    ↓
AI/ML Engineer

Interview Type
    ↓
Technical
Step 2 — Start Interview

Click:

🚀 Start New Interview

A random interview question will appear.

Step 3 — Answer the Question

Enter your answer in:

💬 Your Answer

You then have three controls:

📤 Submit Answer
⏭️ Skip Question
➡️ Next Question
Step 4 — Submit

Click:

📤 Submit Answer

The application performs NLP analysis and sends the answer to Llama 3.2 for AI feedback.

Step 5 — Review Results

The application displays:

📊 Interview Analysis

Relevance Score
Concept Coverage
Answer Quality

🏆 Answer Classification

✅ Covered Concepts

❌ Missing Concepts

💡 NLP Feedback

🎯 Improvement Suggestions

🤖 Llama 3.2 AI Interview Feedback
🔄 Interview Flow

Each interview contains multiple questions.

Example:

Question 1 / 10
       │
       ▼
Answer
       │
       ├───────────────┐
       │               │
       ▼               ▼
    Submit           Skip
       │               │
       ▼               │
   Analysis            │
       │               │
       └───────┬───────┘
               ▼
        Question 2 / 10
               │
               ▼
        Question 3 / 10
               │
              ...
               │
               ▼
        Question 10 / 10
               │
               ▼
       🎉 Interview Complete
🔐 Privacy

The Llama 3.2 analysis is designed to run locally through Ollama.

Candidate answers are processed locally by the application and local LLM rather than requiring a cloud-based LLM API.
