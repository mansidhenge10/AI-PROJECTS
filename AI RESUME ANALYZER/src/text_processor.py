import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# English stopwords
stop_words = set(stopwords.words("english"))

# Lemmatizer
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    """Clean resume text."""

    # Convert to lowercase
    text = text.lower()

    # Remove email addresses
    text = re.sub(r'\S+@\S+', ' ', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\S+', ' ', text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def preprocess_text(text):
    """Complete NLP preprocessing."""

    # Step 1: Clean
    text = clean_text(text)

    # Step 2: Tokenize
    tokens = word_tokenize(text)

    # Step 3: Remove stopwords
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # Step 4: Lemmatize
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return tokens