import sys
import os


# ==================================================
# PROJECT PATH
# ==================================================

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


# ==================================================
# IMPORTS
# ==================================================

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


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ==================================================
# SESSION STATE
# ==================================================

if "analysis_complete" not in st.session_state:
    st.session_state["analysis_complete"] = False

if "tailor_resume" not in st.session_state:
    st.session_state["tailor_resume"] = False

if "analysis_data" not in st.session_state:
    st.session_state["analysis_data"] = {}


# ==================================================
# HEADER
# ==================================================

st.title("📄 AI Resume Analyzer")

st.write(
    "Analyze your resume, compare it with a job description, "
    "and get clear AI-powered recommendations."
)

st.divider()


# ==================================================
# INPUT SECTION
# ==================================================

col1, col2 = st.columns(2)


# ==================================================
# RESUME UPLOAD
# ==================================================

with col1:

    st.subheader("📤 Upload Resume")

    resume_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"]
    )


# ==================================================
# JOB DESCRIPTION
# ==================================================

with col2:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description",
        height=180,
        placeholder="Paste the job description here..."
    )


st.write("")


# ==================================================
# ANALYZE BUTTON
# ==================================================

analyze_button = st.button(
    "🔍 ANALYZE RESUME",
    use_container_width=True
)


# ==================================================
# ANALYSIS
# ==================================================

if analyze_button:

    # --------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------

    if resume_file is None:

        st.warning(
            "⚠️ Please upload your resume."
        )

        st.stop()


    if not job_description.strip():

        st.warning(
            "⚠️ Please paste the job description."
        )

        st.stop()


    try:

        # ==================================================
        # START ANALYSIS
        # ==================================================

        with st.spinner(
            "Analyzing your resume..."
        ):

            # --------------------------------------------------
            # EXTRACT RESUME TEXT
            # --------------------------------------------------

            resume_text = extract_resume_text(
                resume_file
            )


            # --------------------------------------------------
            # DETECT RESUME SECTIONS
            # --------------------------------------------------

            sections = detect_sections(
                resume_text
            )


            # --------------------------------------------------
            # EXTRACT RESUME SKILLS
            # --------------------------------------------------

            resume_skills = extract_skills(
                resume_text
            )


            # ==================================================
            # ANALYZE JOB DESCRIPTION
            # ==================================================

            job_result = analyze_job_description(
                job_description
            )

            job_skills = job_result[
                "required_skills"
            ]


            # ==================================================
            # COMPARE SKILLS
            # ==================================================

            skill_result = compare_skills(
                resume_skills,
                job_skills
            )


            # ==================================================
            # TEXT SIMILARITY
            # ==================================================

            similarity = calculate_similarity(
                resume_text,
                job_description
            )


            # ==================================================
            # ATS SCORE
            # ==================================================

            ats_score = calculate_ats_score(
                skill_result["match_percentage"],
                similarity,
                sections
            )


            # ==================================================
            # RESUME EVALUATION
            # ==================================================

            evaluation = evaluate_resume(
                sections
            )


        # ==================================================
        # SAVE ANALYSIS RESULTS
        # ==================================================

        st.session_state["analysis_data"] = {

            "resume_text": resume_text,

            "job_description": job_description,

            "sections": sections,

            "resume_skills": resume_skills,

            "job_skills": job_skills,

            "matched_skills":
                skill_result["matched_skills"],

            "missing_skills":
                skill_result["missing_skills"],

            "skill_match":
                skill_result["match_percentage"],

            "similarity":
                similarity,

            "ats_score":
                ats_score,

            "evaluation":
                evaluation
        }


        # ==================================================
        # MARK ANALYSIS COMPLETE
        # ==================================================

        st.session_state[
            "analysis_complete"
        ] = True


        # ==================================================
        # RESET TAILOR STATE
        # ==================================================

        st.session_state[
            "tailor_resume"
        ] = False


        st.success(
            "✅ Resume analysis completed successfully!"
        )


    except Exception as e:

        st.error(
            f"❌ Error during analysis: {e}"
        )

        st.stop()


# ==================================================
# DISPLAY RESULTS
# ==================================================

if st.session_state["analysis_complete"]:

    # ==================================================
    # LOAD ANALYSIS DATA
    # ==================================================

    data = st.session_state[
        "analysis_data"
    ]


    resume_text = data[
        "resume_text"
    ]

    job_description = data[
        "job_description"
    ]

    sections = data[
        "sections"
    ]

    matched_skills = data[
        "matched_skills"
    ]

    missing_skills = data[
        "missing_skills"
    ]

    skill_match = data[
        "skill_match"
    ]

    similarity = data[
        "similarity"
    ]

    ats_score = data[
        "ats_score"
    ]

    evaluation = data[
        "evaluation"
    ]


    # ==================================================
    # RESUME STRENGTH
    # ==================================================

    if ats_score >= 85 and skill_match >= 80:

        resume_status = "strong"

    elif ats_score >= 70:

        resume_status = "needs_improvement"

    else:

        resume_status = "weak"


    # ==================================================
    # SCORE
    # ==================================================

    st.divider()

    st.subheader(
        "🎯 Your Resume Score"
    )


    score_col1, score_col2, score_col3 = st.columns(3)


    with score_col1:

        st.metric(
            "ATS-Style Score",
            f"{ats_score}/100"
        )


    with score_col2:

        st.metric(
            "Skill Match",
            f"{skill_match}%"
        )


    with score_col3:

        st.metric(
            "Job Match",
            f"{similarity}%"
        )


    # ==================================================
    # SCORE STATUS
    # ==================================================

    if resume_status == "strong":

        st.success(
            "🟢 Strong Resume"
        )

        st.write(
            "Your resume is already strong for this job."
        )


    elif resume_status == "needs_improvement":

        st.warning(
            "🟡 Resume Needs Improvement"
        )

        st.write(
            "Your resume is good, but some areas can "
            "be improved for this job."
        )


    else:

        st.error(
            "🔴 Resume Needs Significant Improvement"
        )

        st.write(
            "Your resume has several areas that should "
            "be improved for this job."
        )


    # ==================================================
    # TAILOR RESUME
    # ==================================================

    # The Tailor option appears ONLY when the
    # resume is not considered strong.

    if resume_status != "strong":

        st.divider()

        st.subheader(
            "✨ Tailor Your Resume"
        )

        st.write(
            "Improve your resume specifically for this "
            "job description."
        )


        if st.button(
            "✨ TAILOR MY RESUME",
            use_container_width=True
        ):

            st.session_state[
                "tailor_resume"
            ] = True


    # ==================================================
    # TAILOR RESULTS
    # ==================================================

    if (
        resume_status != "strong"
        and st.session_state["tailor_resume"]
    ):

        st.divider()

        st.subheader(
            "✨ Resume Tailoring"
        )

        st.info(
            "These suggestions are based on the "
            "job description and your resume."
        )


        # ==================================================
        # MISSING SKILLS
        # ==================================================

        st.markdown(
            "### 🔴 Missing Skills"
        )


        if missing_skills:

            for skill in missing_skills:

                st.write(
                    f"🔴 **{skill.title()}**"
                )

        else:

            st.success(
                "🎉 No major job-required skills are missing."
            )


        # ==================================================
        # WHERE TO ADD
        # ==================================================

        st.markdown(
            "### 📍 Where Should You Add Them?"
        )


        if missing_skills:

            for skill in missing_skills:

                st.write(
                    f"**{skill.title()}** → "
                    f"Skills / Technical Skills section"
                )

        else:

            st.write(
                "No missing skills need to be added."
            )


        # ==================================================
        # PROJECT IMPROVEMENT
        # ==================================================

        st.markdown(
            "### 🚀 Improve Your Projects"
        )


        if missing_skills:

            st.write(
                "If you genuinely know a missing skill, "
                "show evidence of it in a relevant project."
            )


            for skill in missing_skills[:5]:

                st.write(
                    f"📌 **{skill.title()}** → "
                    f"Add truthful evidence of using this "
                    f"skill in a relevant project."
                )

        else:

            st.write(
                "Your required skills are already matched. "
                "Focus on stronger project descriptions."
            )


        # ==================================================
        # WHAT TO WRITE
        # ==================================================

        st.markdown(
            "### ✍️ What Should You Write?"
        )


        if missing_skills:

            st.write(
                "Example wording:"
            )


            for skill in missing_skills[:3]:

                st.code(
                    f"Used {skill.title()} to build "
                    f"and improve a relevant AI/ML project.",
                    language="text"
                )

        else:

            st.write(
                "Add measurable results to your projects."
            )


            st.code(
                "Improved project performance by X% "
                "through optimization and testing.",
                language="text"
            )


        # ==================================================
        # TRUTHFULNESS WARNING
        # ==================================================

        st.caption(
            "⚠️ Only add skills, tools, certifications, "
            "or experience that you genuinely have."
        )


    # ==================================================
    # MISSING SKILLS
    # ==================================================

    st.divider()

    st.subheader(
        "❌ What You Are Missing"
    )


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
    # WHAT YOU SHOULD DO
    # ==================================================

    st.divider()

    st.subheader(
        "📌 What You Should Do"
    )


    if missing_skills:

        st.write(
            "1️⃣ Add the most important missing skills "
            "from the job description if you genuinely know them."
        )

        st.write(
            "2️⃣ Mention those skills in relevant projects "
            "where you have actually used them."
        )

        st.write(
            "3️⃣ Add measurable results to your "
            "project and experience descriptions."
        )

    else:

        st.write(
            "1️⃣ Tailor your resume wording to this job."
        )

        st.write(
            "2️⃣ Add measurable achievements."
        )

        st.write(
            "3️⃣ Keep your strongest technical skills visible."
        )


    # ==================================================
    # WHAT IS ALREADY GOOD
    # ==================================================

    st.divider()

    st.subheader(
        "✅ What Is Already Good"
    )


    if matched_skills:

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


    if "summary" in sections:

        st.write(
            "✓ Summary section is present"
        )


    # ==================================================
    # AI QUICK FEEDBACK
    # ==================================================

    st.divider()

    st.subheader(
        "🤖 AI Quick Feedback"
    )

    st.caption(
        "Simple suggestions based on your resume "
        "and job requirements."
    )


    try:

        with st.spinner(
            "Generating AI feedback..."
        ):

            feedback = generate_feedback(
                resume_text,
                job_description,
                matched_skills,
                missing_skills
            )


        # --------------------------------------------------
        # DISPLAY FEEDBACK
        # --------------------------------------------------

        for line in feedback.splitlines():

            if line.strip():

                st.markdown(
                    f"- {line.strip()}"
                )


    except Exception as e:

        st.warning(
            f"⚠️ AI feedback unavailable: {e}"
        )


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
    # EXTRACTED RESUME TEXT
    # ==================================================

    st.divider()

    with st.expander(
        "📄 View Extracted Resume Text"
    ):

        st.text_area(
            "Resume Text",
            resume_text,
            height=400
        )