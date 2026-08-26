import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Interview Mistake Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Interview Mistake Analyzer")

st.write(
    "Practice interview questions and get AI-powered feedback "
    "on your answers."
)

st.divider()

st.subheader("🎯 Start Your Interview")
# ==============================
# LOAD INTERVIEW DATASET
# ==============================

df = pd.read_csv("../data/interview_questions.csv")
# ==============================
# JOB DOMAIN
# ==============================

domains = [
    "AI/ML Engineer",
    "Data Analyst",
    "Python Developer",
    "Frontend Developer",
    "Data Scientist"
]

selected_domain = st.selectbox(
    "Select Job Domain",
    domains
)

st.write("Selected Domain:", selected_domain)


# ==============================
# INTERVIEW TYPE
# ==============================

interview_types = [
    "Technical",
    "HR"
]

selected_type = st.selectbox(
    "Select Interview Type",
    interview_types
)

st.write("Selected Interview Type:", selected_type)
# ==============================
# QUESTION COUNT
# ==============================

st.divider()

st.write(f"📚 Total Interview Questions: {len(df)}")


# ==============================
# FILTER QUESTIONS
# ==============================

filtered_questions = df[
    (df["job_domain"] == selected_domain)
    &
    (df["interview_type"] == selected_type)
]

st.write(
    f"Questions available for this selection: "
    f"{len(filtered_questions)}"
)
# ==============================
# START INTERVIEW
# ==============================

if len(filtered_questions) > 0:

    if st.button("🚀 Start Interview"):

        selected_question = filtered_questions.sample(
            n=1
        ).iloc[0]

        st.session_state["selected_question"] = selected_question


# ==============================
# DISPLAY QUESTION
# ==============================

if "selected_question" in st.session_state:

    question = st.session_state["selected_question"]

    st.divider()

    st.subheader("📝 Interview Question")

    st.write(
        "**Category:**",
        question["category"]
    )

    st.write(
        "**Difficulty:**",
        question["difficulty"]
    )

    st.write(
        "**Question:**"
    )

    st.info(question["question"])
    # ==============================
# CANDIDATE ANSWER
# ==============================

candidate_answer = st.text_area(
    "✍️ Your Answer",
    height=200,
    placeholder="Type your interview answer here..."
)
if st.button("🔍 Analyze My Answer"):

    if candidate_answer.strip():

        st.success("Answer received! Analysis will start next.")

    else:

        st.warning("Please enter your answer first.")