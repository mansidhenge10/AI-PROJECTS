import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")


# Initialize NLP tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    """
    Clean the candidate's answer.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def tokenize_text(text):
    """
    Convert text into individual words.
    """

    return word_tokenize(text)


def remove_stopwords(tokens):
    """
    Remove common English stopwords.
    """

    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return filtered_tokens


def lemmatize_tokens(tokens):
    """
    Convert words into their base form.
    """

    lemmatized_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return lemmatized_tokens


def process_answer(answer):
    """
    Complete answer-processing pipeline.
    """

    cleaned = clean_text(answer)

    tokens = tokenize_text(cleaned)

    filtered_tokens = remove_stopwords(tokens)

    lemmatized = lemmatize_tokens(filtered_tokens)

    return lemmatized