import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from src.ats_scorer import calculate_ats_score


skill_match = 80
similarity = 70

sections = {
    "summary": "AI Engineer...",
    "skills": "Python, Machine Learning...",
    "education": "MCA...",
    "projects": "AI Resume Analyzer...",
    "experience": "AI Engineer..."
}


score = calculate_ats_score(
    skill_match,
    similarity,
    sections
)

print("ATS-Style Resume Score:")
print(f"{score}%")