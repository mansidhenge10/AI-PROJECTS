
import requests


def generate_feedback(
    resume_text,
    job_description,
    matched_skills,
    missing_skills
):
    """
    Generate short, evidence-based AI resume feedback.
    """

    # Convert skill lists into text
    matched_skills_text = ", ".join(matched_skills)

    missing_skills_text = ", ".join(missing_skills)

    # Handle empty lists
    if not matched_skills_text:
        matched_skills_text = "None"

    if not missing_skills_text:
        missing_skills_text = "None"


    # ==================================================
    # PROMPT
    # ==================================================

    prompt = f"""
You are an AI Resume Assistant.

Compare the resume with the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

ACTUAL MATCHED SKILLS:
{matched_skills_text}

ACTUAL MISSING SKILLS:
{missing_skills_text}

Give EXACTLY 4 short lines.

Use this format:

💚 Good: [one short positive sentence]
⚠️ Add: [only actual missing skills]
📌 Improve: [one practical resume improvement]
⭐ Priority: [one most important action]

STRICT RULES:

1. Only use skills from ACTUAL MATCHED SKILLS when discussing matched skills.

2. Only use skills from ACTUAL MISSING SKILLS when discussing missing skills.

3. Never say that a matched skill is missing.

4. Never invent a skill.

5. Never suggest unrelated technologies.

6. Never suggest certifications unless the job description specifically requires them.

7. If ACTUAL MISSING SKILLS is None, say:
No major job-required skills are missing.

8. Give practical resume improvement advice.

9. Maximum 15 words per line.

10. Use very simple English.

11. No paragraphs.

12. No numbering.

13. No candidate name.

14. Exactly 4 lines.

15. Do not repeat the resume.

16. Do not create information that is not present in the resume.
"""


    # ==================================================
    # OLLAMA API
    # ==================================================

    response = requests.post(
        "http://localhost:11434/api/generate",

        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False,

            "options": {
                "temperature": 0
            }
        },

        timeout=120
    )


    # ==================================================
    # ERROR CHECK
    # ==================================================

    response.raise_for_status()


    # ==================================================
    # RESPONSE
    # ==================================================

    result = response.json()

    return result["response"].strip()
