import requests


def generate_feedback(resume_text, job_description):
    """
    Generate short AI resume feedback.
    """

    prompt = f"""
Compare this resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Reply with EXACTLY 4 short lines.

Format:
💚 Good: [one short positive sentence]
⚠️ Add: [2-4 important missing skills]
📌 Improve: [one simple action]
⭐ Priority: [one most important action]

Rules:
- Maximum 4 lines
- Maximum 15 words per line
- Very simple English
- No paragraphs
- No numbering
- No detailed analysis
- No candidate name
- No strengths section
- No weaknesses section
- No overall recommendation
- Do not repeat the resume
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0
            }
        }
    )

    response.raise_for_status()

    result = response.json()

    return result["response"].strip()