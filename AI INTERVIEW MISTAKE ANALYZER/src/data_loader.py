import pandas as pd
from pathlib import Path


def load_questions():
    """Load interview questions from the CSV file."""

    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "data" / "interview_questions.csv"

    df = pd.read_csv(file_path)

    return df


def get_job_domains(df):
    """Get all available job domains."""

    return sorted(df["job_domain"].unique())


def get_interview_types(df):
    """Get all interview types."""

    return sorted(df["interview_type"].unique())


def get_questions(df, job_domain, interview_type):
    """Get questions for a selected job domain and interview type."""

    filtered_questions = df[
        (df["job_domain"] == job_domain)
        & (df["interview_type"] == interview_type)
    ]

    return filtered_questions