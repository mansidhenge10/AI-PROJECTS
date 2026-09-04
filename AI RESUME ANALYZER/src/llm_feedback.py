import requests


def generate_feedback(resume_text, job_description):
    """
    Generate AI-powered resume feedback using Llama 3.2
    through Ollama.
    """

    prompt = f"""
You are an expert AI resume reviewer.

Analyze the following resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Provide:
1. Resume strengths
2. Weaknesses
3. Missing skills
4. Specific improvement suggestions
5. Overall recommendation

Keep the feedback clear and practical.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    result = response.json()

    return result["response"]