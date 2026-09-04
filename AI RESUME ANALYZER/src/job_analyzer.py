from .skill_extractor import extract_skills


def analyze_job_description(job_description):
    """
    Extract required skills from a job description.
    """

    skills = extract_skills(job_description)

    return {
        "job_description": job_description,
        "required_skills": skills
    }


def compare_skills(resume_skills, job_skills):
    """
    Compare resume skills with job-required skills.
    """

    resume_skills = set(resume_skills)
    job_skills = set(job_skills)

    matched_skills = sorted(resume_skills.intersection(job_skills))
    missing_skills = sorted(job_skills - resume_skills)

    if job_skills:
        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100
    else:
        match_percentage = 0

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(match_percentage, 2)
    }