from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_tfidf(texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    return vectorizer, tfidf_matrix


def extract_concepts(expected_concepts):
    concepts = expected_concepts.split(";")

    concepts = [
        concept.strip().lower()
        for concept in concepts
        if concept.strip()
    ]

    return concepts


def calculate_similarity(expected_concepts, candidate_answer):
    expected_text = " ".join(expected_concepts)

    texts = [
        expected_text,
        candidate_answer
    ]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    return similarity[0][0]


if __name__ == "__main__":

    expected = (
        "training data;"
        "generalization;"
        "validation data;"
        "regularization"
    )

    candidate = """
    Overfitting happens when a model learns
    the training data too much.
    """

    concepts = extract_concepts(expected)

    print("Expected Concepts:")
    print(concepts)

    score = calculate_similarity(
        concepts,
        candidate
    )

    print("\nCandidate Answer:")
    print(candidate)

    print("\nSimilarity Score:")
    print(score)