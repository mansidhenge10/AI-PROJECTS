import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.section_detector import detect_sections


resume_text = """
PROFESSIONAL SUMMARY

AI Engineer with experience in Python and Machine Learning.

SKILLS

Python
Machine Learning
NLP
SQL

EDUCATION

Master of Computer Applications

EXPERIENCE

AI Developer Intern
Worked on machine learning projects.

PROJECTS

AI Resume Analyzer
AI Interview Mistake Analyzer

CERTIFICATIONS

IBM AI Fundamentals
"""


sections = detect_sections(resume_text)


print("Detected Resume Sections:")
print("--------------------------------")

for section, content in sections.items():

    print(f"\n[{section.upper()}]")
    print(content)