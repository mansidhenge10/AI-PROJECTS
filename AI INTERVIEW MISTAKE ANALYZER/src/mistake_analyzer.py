def analyze_answer_quality(answer_quality):
    """
    Classify the candidate's answer
    based on the overall quality score.
    """

    if answer_quality >= 80:
        return "Strong Answer"

    elif answer_quality >= 60:
        return "Good Answer - Needs Minor Improvement"

    elif answer_quality >= 40:
        return "Average Answer - Needs Improvement"

    else:
        return "Weak Answer - Major Improvement Needed"


def generate_feedback(missing_concepts):
    """
    Generate feedback based on missing concepts.
    """

    if not missing_concepts:
        return "Excellent! You covered all the important concepts."

    feedback = (
        "Your answer is missing some important concepts. "
        "You should discuss: "
    )

    feedback += ", ".join(missing_concepts) + "."

    return feedback


def generate_improvement_suggestions(missing_concepts):
    """
    Generate suggestions to help the candidate
    improve their interview answer.
    """

    if not missing_concepts:
        return [
            "Your answer is complete.",
            "Keep practicing for clarity and confidence."
        ]

    suggestions = []

    for concept in missing_concepts:

        if concept == "regularization":
            suggestions.append(
                "Explain how regularization helps prevent overfitting."
            )

        elif concept == "cross validation":
            suggestions.append(
                "Mention cross-validation as a technique for evaluating model performance."
            )

        elif concept == "data augmentation":
            suggestions.append(
                "Explain how data augmentation can provide more varied training examples."
            )

        else:
            suggestions.append(
                f"Learn and explain the concept of {concept}."
            )

    return suggestions