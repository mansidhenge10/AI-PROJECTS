import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.llm_feedback import generate_feedback


resume_text = """
AI Engineer with experience in Python, Machine Learning,
NLP, FastAPI and Docker. Developed AI applications.
"""

job_description = """
We are looking for an AI Engineer with experience in
Python, Machine Learning, NLP, FastAPI and Docker.
"""


feedback = generate_feedback(
    resume_text,
    job_description
)

print("AI RESUME FEEDBACK")
print("==================")
print(feedback)