import re


# Skill database for AI / Software / Data roles
SKILLS = {
    # Programming
    "python",
    "java",
    "c++",
    "javascript",
    "typescript",
    "sql",

    # Machine Learning
    "machine learning",
    "deep learning",
    "supervised learning",
    "unsupervised learning",
    "reinforcement learning",

    # AI / NLP
    "artificial intelligence",
    "natural language processing",
    "nlp",
    "computer vision",
    "generative ai",
    "large language model",
    "llm",
    "rag",
    "retrieval augmented generation",

    # Frameworks / Libraries
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "pandas",
    "numpy",
    "nltk",
    "spacy",
    "opencv",

    # GenAI / AI tools
    "langchain",
    "langgraph",
    "ollama",
    "openai",
    "hugging face",

    # Backend
    "fastapi",
    "flask",
    "django",
    "rest api",

    # Databases
    "mysql",
    "postgresql",
    "mongodb",
    "redis",

    # DevOps / Cloud
    "docker",
    "kubernetes",
    "git",
    "github",
    "aws",
    "azure",
    "google cloud",

    # Data
    "data analysis",
    "data visualization",
    "statistics",
    "power bi",
    "tableau"
}


def extract_skills(text):
    """
    Extract known skills from text.
    """

    text = text.lower()

    found_skills = set()

    for skill in SKILLS:

        # Escape special characters in skill names
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found_skills.add(skill)

    return sorted(found_skills)