def evaluate_resume(sections):
    """
    Evaluate resume sections and identify
    strengths and areas for improvement.
    """

    important_sections = [
        "summary",
        "skills",
        "education",
        "experience",
        "projects",
        "certifications"
    ]

    strengths = []
    improvements = []

    for section in important_sections:

        if section in sections:
            strengths.append(
                f"{section.title()} section is present."
            )
        else:
            improvements.append(
                f"Consider adding a {section.title()} section."
            )

    return {
        "strengths": strengths,
        "improvements": improvements
    }