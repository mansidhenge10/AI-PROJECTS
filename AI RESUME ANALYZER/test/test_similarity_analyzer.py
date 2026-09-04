import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.similarity_analyzer import calculate_similarity


resume_text = """
AI Engineer with experience in Python, Machine Learning,
NLP, FastAPI and Docker. Developed AI applications.
"""

job_description = """
We are looking for an AI Engineer with experience in
Python, Machine Learning, NLP and FastAPI.
"""


score = calculate_similarity(
    resume_text,
    job_description
)

print("Resume-Job Similarity:")
print(f"{score}%")