import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI Interview Mistake Analyzer",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Interview Mistake Analyzer")

st.write(
    "Practice interview questions and get AI-powered feedback "
    "on your answers."
)

st.divider()

# Interview section
st.header("🎯 Start Your Interview")

# Load questions
questions_df = pd.read_csv(
    "data/interview_questions.csv"
)

# Job domain
job_domain = st.selectbox(
    "Select Job Domain",
    [
        "AI/ML Engineer",
        "Data Analyst",
        "Python Developer",
        "Frontend Developer",
        "Data Scientist"
    ]
)

# Interview type
interview_type = st.selectbox(
    "Select Interview Type",
    [
        "Technical",
        "HR"
    ]
)

st.write("### Selected Options")
st.write("**Job Domain:**", job_domain)
st.write("**Interview Type:**", interview_type)

# Start interview
if st.button("🚀 Start Interview"):

    # Filter questions
    filtered_questions = questions_df[
        (questions_df["job_domain"] == job_domain) &
        (questions_df["interview_type"] == interview_type)
    ]

    if len(filtered_questions) == 0:

        st.warning(
            "No questions found for this selection."
        )

    else:

        # Select first question
        question = filtered_questions.iloc[0]

        st.session_state["current_question"] = question

        st.success("Interview started successfully!")


# Show question
if "current_question" in st.session_state:

    question = st.session_state["current_question"]

    st.divider()

    st.subheader("📝 Interview Question")

    st.write(
        question["question"]
    )

    st.write(
        "**Category:**",
        question["category"]
    )

    st.write(
        "**Difficulty:**",
        question["difficulty"]
    )

    # Candidate answer
    candidate_answer = st.text_area(
        "💬 Your Answer",
        placeholder="Type your interview answer here..."
    )

    # Submit answer
    if st.button("📤 Submit Answer"):

        if candidate_answer.strip() == "":

            st.warning(
                "Please enter your answer first."
            )

        else:

            st.success(
                "Answer received! Analysis will start next."
            )