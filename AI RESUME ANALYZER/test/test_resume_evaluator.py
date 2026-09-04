import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.resume_evaluator import evaluate_resume


sections = {
    "summary": "AI Engineer...",
    "skills": "Python, Machine Learning...",
    "education": "MCA...",
    "projects": "AI Resume Analyzer..."
}


result = evaluate_resume(sections)


print("RESUME STRENGTHS")
print("----------------")

for strength in result["strengths"]:
    print("✓", strength)


print("\nAREAS FOR IMPROVEMENT")
print("---------------------")

for improvement in result["improvements"]:
    print("⚠", improvement)