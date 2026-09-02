import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from src.resume_parser import extract_resume_text

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and analyze it using NLP and AI."
)


st.subheader("📤 Upload Resume")

resume_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


if resume_file is not None:

    st.success(f"Uploaded: {resume_file.name}")

    if st.button("📖 Extract Resume Text"):

        try:

            resume_text = extract_resume_text(resume_file)

            if resume_text.strip():

                st.subheader("📄 Extracted Resume Text")

                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=500
                )

            else:

                st.warning(
                    "No text could be extracted from this resume."
                )

        except Exception as e:

            st.error(f"Error while reading resume: {e}")