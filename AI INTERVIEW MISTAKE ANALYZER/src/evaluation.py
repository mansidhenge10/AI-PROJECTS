def calculate_relevance_score(similarity_score):
    """
    Convert similarity score into a percentage.
    """

    relevance_score = similarity_score * 100

    return round(relevance_score, 2)


def calculate_concept_coverage(expected_concepts, candidate_answer):
    """
    Calculate how many expected concepts are covered
    by the candidate's answer.

    Supports common variations and equivalent phrases.
    """

    candidate_answer = candidate_answer.lower()

    # Normalize common variations
    candidate_answer = candidate_answer.replace("-", " ")
    candidate_answer = candidate_answer.replace("_", " ")

    covered_concepts = []
    missing_concepts = []

    # Common semantic variations
    concept_variations = {

        "categorical output": [
            "categorical output",
            "categorical",
            "category",
            "class",
            "classes",
            "discrete output",
            "discrete"
        ],

        "continuous output": [
            "continuous output",
            "continuous",
            "continuous value",
            "continuous numerical value",
            "numerical value",
            "numeric value"
        ],

        "prediction": [
            "prediction",
            "predict",
            "predicts",
            "predicted",
            "predicting"
        ],

        "pattern discovery": [
            "pattern discovery",
            "discover patterns",
            "find patterns",
            "finding patterns",
            "hidden patterns",
            "identify patterns",
            "identifying patterns"
        ],

        "generalization": [
            "generalization",
            "generalisation",
            "generalize",
            "generalise",
            "generalizes",
            "generalises"
        ],

     "poor test performance": [
    "poor test performance",
    "poor performance on test data",
    "poor performance on unseen data",
    "performs poorly on test data",
    "performs poorly on unseen data",
    "poorly on unseen data",
    "poor performance on new data"
]
    }


    for concept in expected_concepts:

        concept = concept.lower().strip()

        # Normalize concept
        concept = concept.replace("-", " ")
        concept = concept.replace("_", " ")

        # Check semantic variations
        if concept in concept_variations:

            variations = concept_variations[concept]

            if any(
                variation in candidate_answer
                for variation in variations
            ):
                covered_concepts.append(concept)
            else:
                missing_concepts.append(concept)

        # Special handling for class imbalance
        elif concept == "class imbalance":

            if (
                "class imbalance" in candidate_answer
                or "imbalanced classification" in candidate_answer
                or "imbalanced dataset" in candidate_answer
                or "imbalanced classification dataset" in candidate_answer
            ):
                covered_concepts.append(concept)
            else:
                missing_concepts.append(concept)

        # Special handling for F1 score
        elif concept == "f1 score":

            if (
                "f1 score" in candidate_answer
                or "fscore" in candidate_answer
                or "f 1 score" in candidate_answer
            ):
                covered_concepts.append(concept)
            else:
                missing_concepts.append(concept)

        # Normal concept matching
        else:

            if concept in candidate_answer:
                covered_concepts.append(concept)
            else:
                missing_concepts.append(concept)


    total_concepts = len(expected_concepts)

    if total_concepts == 0:
        coverage_score = 0
    else:
        coverage_score = (
            len(covered_concepts) / total_concepts
        ) * 100


    return (
        round(coverage_score, 2),
        covered_concepts,
        missing_concepts
    )


def calculate_answer_quality(relevance_score, coverage_score):
    """
    Calculate the overall answer quality score.
    """

    answer_quality = (
        (relevance_score * 0.40)
        +
        (coverage_score * 0.60)
    )

    return round(answer_quality, 2)


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    similarity = 0.212

    relevance_score = calculate_relevance_score(similarity)

    print("Similarity Score:", similarity)
    print("Relevance Score:", relevance_score, "%")


    expected_concepts = [
        "training data",
        "poor test performance",
        "generalization",
        "regularization",
        "cross validation",
        "data augmentation"
    ]


    candidate_answer = """
    Overfitting occurs when a machine learning model
    learns the training data too closely, including
    its noise and small details, so it performs very
    well on training data but poorly on unseen data.
    """


    coverage_score, covered, missing = calculate_concept_coverage(
        expected_concepts,
        candidate_answer
    )


    print("\nConcept Coverage:", coverage_score, "%")


    print("\nCovered Concepts:")

    for concept in covered:
        print("✓", concept)


    print("\nMissing Concepts:")

    for concept in missing:
        print("✗", concept)


    answer_quality = calculate_answer_quality(
        relevance_score,
        coverage_score
    )

    print("\nAnswer Quality Score:")
    print(answer_quality, "%")