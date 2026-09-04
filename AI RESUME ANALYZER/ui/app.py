import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import streamlit as st

from src.resume_parser import extract_resume_text
from src.skill_extractor import extract_skills
from src.section_detector import detect_sections
from src.job_analyzer import (
    analyze_job_description,
    compare_skills
)
from src.similarity_analyzer import calculate_similarity
from src.ats_scorer import calculate_ats_score
from src.resume_evaluator import evaluate_resume
from src.llm_feedback import generate_feedback


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume, compare it with a job description, "
    "and get clear AI-powered recommendations."
)

st.divider()


# -----------------------------
# Input Section
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📤 Upload Resume")

    resume_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"]
    )


with col2:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description",
        height=180,
        placeholder="Paste the job description here..."
    )


st.write("")

analyze_button = st.button(
    "🔍 ANALYZE RESUME",
    use_container_width=True
)


# -----------------------------
# Analysis
# -----------------------------

if analyze_button:

    if resume_file is None:

        st.warning("⚠️ Please upload your resume.")

        st.stop()


    if not job_description.strip():

        st.warning(
            "⚠️ Please paste the job description."
        )

        st.stop()


    try:

        with st.spinner("Analyzing your resume..."):

            # Resume text
            resume_text = extract_resume_text(
                resume_file
            )

            # Resume sections
            sections = detect_sections(
                resume_text
            )

            # Resume skills
            resume_skills = extract_skills(
                resume_text
            )

            # Job analysis
            job_result = analyze_job_description(
                job_description
            )

            job_skills = job_result[
                "required_skills"
            ]

            # Skill comparison
            skill_result = compare_skills(
                resume_skills,
                job_skills
            )

            # Text similarity
            similarity = calculate_similarity(
                resume_text,
                job_description
            )

            # ATS score
            ats_score = calculate_ats_score(
                skill_result["match_percentage"],
                similarity,
                sections
            )

            # Resume evaluation
            evaluation = evaluate_resume(
                sections
            )


        st.success(
            "Resume analysis completed successfully!"
        )


        # ==================================================
        # SCORE
        # ==================================================

        st.divider()

        st.subheader("🎯 Your Resume Score")

        score_col1, score_col2, score_col3 = st.columns(3)

        with score_col1:

            st.metric(
                "ATS-Style Score",
                f"{ats_score}/100"
            )


        with score_col2:

            st.metric(
                "Skill Match",
                f'{skill_result["match_percentage"]}%'
            )


        with score_col3:

            st.metric(
                "Job Match",
                f"{similarity}%"
            )


        if ats_score >= 80:

            st.success(
                "🟢 Strong Resume"
            )

        elif ats_score >= 60:

            st.warning(
                "🟡 Needs Some Improvement"
            )

        else:

            st.error(
                "🔴 Needs Improvement"
            )


        # ==================================================
        # MISSING SKILLS
        # ==================================================

        st.divider()

        st.subheader(
            "❌ What You Are Missing"
        )

        missing_skills = skill_result[
            "missing_skills"
        ]


        if missing_skills:

            skill_cols = st.columns(
                min(len(missing_skills), 3)
            )

            for index, skill in enumerate(
                missing_skills
            ):

                with skill_cols[
                    index % len(skill_cols)
                ]:

                    st.error(
                        f"🔴 {skill.title()}"
                    )

        else:

            st.success(
                "🎉 No major missing skills found!"
            )


        # ==================================================
        # WHAT TO DO
        # ==================================================

        st.divider()

        st.subheader(
            "📌 What You Should Do"
        )

        if missing_skills:

            st.write(
                "1️⃣ Add the most important missing skills "
                "from the job description."
            )

            st.write(
                "2️⃣ Add projects that demonstrate "
                "your relevant technical skills."
            )

            st.write(
                "3️⃣ Add measurable results to your "
                "project and experience descriptions."
            )

        else:

            st.write(
                "1️⃣ Tailor your resume to this job."
            )

            st.write(
                "2️⃣ Add measurable achievements."
            )

            st.write(
                "3️⃣ Keep your technical skills clearly visible."
            )


        # ==================================================
        # GOOD THINGS
        # ==================================================

        st.divider()

        st.subheader(
            "✅ What Is Already Good"
        )

        matched_skills = skill_result[
            "matched_skills"
        ]


        for skill in matched_skills[:10]:

            st.write(
                f"✓ {skill.title()}"
            )


        if "experience" in sections:

            st.write(
                "✓ Work experience is present"
            )


        if "projects" in sections:

            st.write(
                "✓ Projects section is present"
            )


        if "education" in sections:

            st.write(
                "✓ Education section is present"
            )


        # ==================================================
        # AI QUICK FEEDBACK
        # ==================================================

        st.divider()

        st.subheader(
            "🤖 AI Quick Feedback"
        )


        with st.spinner(
            "Generating AI feedback..."
        ):

            feedback = generate_feedback(
                resume_text,
                job_description
            )


        st.info(feedback)


        # ==================================================
        # RESUME SECTIONS
        # ==================================================

        st.divider()

        st.subheader(
            "📑 Resume Sections"
        )


        important_sections = [
            "summary",
            "skills",
            "education",
            "experience",
            "projects",
            "certifications"
        ]


        for section in important_sections:

            if section in sections:

                st.write(
                    f"✓ {section.title()}"
                )

            else:

                st.write(
                    f"⚠️ {section.title()}"
                )


        # ==================================================
        # DETAILED ANALYSIS
        # ==================================================

        st.divider()

        with st.expander(
            "🔎 View Detailed AI Analysis"
        ):

            st.write(feedback)


        # ==================================================
        # EXTRACTED TEXT
        # ==================================================

        with st.expander(
            "📄 View Extracted Resume Text"
        ):

            st.text_area(
                "Resume Text",
                resume_text,
                height=400
            )


    except Exception as e:

        st.error(
            f"❌ Error during analysis: {e}"
        )