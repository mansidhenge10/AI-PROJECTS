import re


# Common resume section names
SECTION_PATTERNS = {
    "summary": [
        "summary",
        "professional summary",
        "career summary",
        "profile",
        "objective",
        "career objective"
    ],

    "skills": [
        "skills",
        "technical skills",
        "core skills",
        "key skills",
        "technical expertise"
    ],

    "education": [
        "education",
        "academic background",
        "educational background",
        "qualifications"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "professional certifications"
    ],

    "achievements": [
        "achievements",
        "accomplishments",
        "awards"
    ],

    "contact": [
        "contact",
        "contact information"
    ]
}


def detect_section_heading(line):
    """
    Check whether a line is a resume section heading.
    Returns the section name if found.
    """

    cleaned_line = line.strip().lower()

    # Remove common heading characters
    cleaned_line = re.sub(r"[:\-|]", "", cleaned_line)
    cleaned_line = cleaned_line.strip()

    for section, headings in SECTION_PATTERNS.items():

        for heading in headings:

            if cleaned_line == heading:
                return section

    return None


def detect_sections(text):
    """
    Detect resume sections and store their content.
    """

    sections = {}

    current_section = None

    lines = text.splitlines()

    for line in lines:

        line = line.strip()

        if not line:
            continue

        detected_section = detect_section_heading(line)

        if detected_section:

            current_section = detected_section

            if current_section not in sections:
                sections[current_section] = []

        elif current_section:

            sections[current_section].append(line)

    # Convert lists into strings
    for section in sections:

        sections[section] = "\n".join(
            sections[section]
        )

    return sections