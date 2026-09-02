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

from src.skill_extractor import extract_skills


resume_text = """
I am an AI Engineer with experience in Python,
Machine Learning, Deep Learning, NLP and SQL.

I have worked with TensorFlow, PyTorch, Pandas,
NumPy and Scikit-learn.

I have built REST API applications using FastAPI
and deployed applications using Docker.

I also have experience with Git, GitHub and MySQL.
"""


skills = extract_skills(resume_text)


print("Extracted Skills:")
print("------------------")

for skill in skills:
    print("✓", skill)