import re


# Common resume section names
SECTION_PATTERNS = {

    "summary": [
        "summary",
        "professional summary",
        "career summary",
        "profile",
        "objective",
        "career objective",
        "about me",
        "professional profile"
    ],

    "skills": [
        "skills",
        "technical skills",
        "technical skill",
        "core skills",
        "key skills",
        "technical expertise",
        "skills and technologies",
        "technical knowledge"
    ],

    "education": [
        "education",
        "academic background",
        "educational background",
        "qualifications",
        "academic qualifications",
        "educational qualifications"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history",
        "internship",
        "internships",
        "work experience and internships"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "key projects",
        "technical projects",
        "project experience",
        "projects and experience"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "professional certifications",
        "certification",
        "licenses and certifications"
    ],

    "achievements": [
        "achievements",
        "accomplishments",
        "awards",
        "honors",
        "honors and awards"
    ],

    "contact": [
        "contact",
        "contact information",
        "personal information"
    ]
}


def clean_heading(line):
    """
    Clean a possible resume heading.
    """

    line = line.strip().lower()

    # Remove common heading symbols
    line = re.sub(r"[*#_:|•·\-–—]", " ", line)

    # Remove extra spaces
    line = re.sub(r"\s+", " ", line).strip()

    return line


def detect_section_heading(line):
    """
    Detect whether a line is a resume section heading.
    """

    cleaned_line = clean_heading(line)

    for section, headings in SECTION_PATTERNS.items():

        for heading in headings:

            # Exact match
            if cleaned_line == heading:
                return section

            # Match heading with small extra text
            if cleaned_line.startswith(heading + " "):
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