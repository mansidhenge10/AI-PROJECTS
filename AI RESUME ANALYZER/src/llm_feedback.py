import requests


def generate_feedback(resume_text, job_description):
    """
    Generate short, simple and user-friendly resume feedback.
    """

    prompt = f"""
You are a simple resume assistant.

Compare the resume with the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Give ONLY a very short answer.

Use EXACTLY this format:

💚 Good:
One short sentence about what is already good.

⚠️ Add:
Mention the 2 or 3 most important things missing.

📌 Improve:
Give ONE simple action the candidate should take.

⭐ Priority:
Give ONE most important thing to do first.

IMPORTANT RULES:
- Use very simple English.
- Maximum 4 lines of feedback.
- Each line must be short.
- Do not write paragraphs.
- Do not explain anything.
- Do not write strengths.
- Do not write weaknesses.
- Do not write missing skills as a numbered list.
- Do not write an overall recommendation.
- Do not repeat the resume.
- Do not suggest unrelated skills.
- If something already exists in the resume, do not say it is missing.
- Focus on practical actions.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1
            }
        }
    )

    response.raise_for_status()

    result = response.json()

    return result["response"]