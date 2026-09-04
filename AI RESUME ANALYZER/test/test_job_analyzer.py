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

from src.job_analyzer import (
    analyze_job_description,
    compare_skills
)


# Sample job description
job_description = """
We are looking for an AI Engineer with experience in
Python, Machine Learning, NLP, FastAPI and Docker.
Knowledge of SQL and Git is also required.
"""


# Analyze job description
job_result = analyze_job_description(job_description)

job_skills = job_result["required_skills"]


# Sample resume skills
resume_skills = [
    "python",
    "machine learning",
    "nlp",
    "fastapi",
    "sql",
    "git"
]


# Compare skills
result = compare_skills(
    resume_skills,
    job_skills
)


print("JOB REQUIRED SKILLS")
print("-------------------")

for skill in job_skills:
    print("✓", skill)


print("\nMATCHED SKILLS")
print("--------------")

for skill in result["matched_skills"]:
    print("✓", skill)


print("\nMISSING SKILLS")
print("--------------")

for skill in result["missing_skills"]:
    print("✗", skill)


print("\nSKILL MATCH")
print("-----------")

print(
    f"{result['match_percentage']}%"
)