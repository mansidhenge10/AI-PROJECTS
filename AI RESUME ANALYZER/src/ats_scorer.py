def calculate_ats_score(
    skill_match_percentage,
    similarity_percentage,
    sections
):
    """
    Calculate an ATS-style resume score.
    """

    # Skill matching: 50%
    skill_score = skill_match_percentage * 0.50

    # Resume-job similarity: 30%
    similarity_score = similarity_percentage * 0.30

    # Section completeness: 20%
    important_sections = [
        "summary",
        "skills",
        "education",
        "experience",
        "projects"
    ]

    found_sections = 0

    for section in important_sections:
        if section in sections:
            found_sections += 1

    section_percentage = (
        found_sections / len(important_sections)
    ) * 100

    section_score = section_percentage * 0.20

    # Final score
    ats_score = (
        skill_score
        + similarity_score
        + section_score
    )

    return round(ats_score, 2)