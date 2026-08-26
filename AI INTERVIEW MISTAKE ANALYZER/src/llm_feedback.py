import ollama

from src.prompt_manager import SYSTEM_PROMPT


def generate_llm_feedback(
    question,
    candidate_answer,
    answer_quality,
    missing_concepts
):
    """
    Generate AI-based interview feedback
    using a local Ollama LLM.
    """

    # Convert missing concepts into readable text
    if missing_concepts:
        missing_text = ", ".join(missing_concepts)
    else:
        missing_text = "None"

    # Create the prompt for the LLM
    user_prompt = f"""
Interview Question:
{question}

Candidate Answer:
{candidate_answer}

Answer Quality Score:
{answer_quality}%

Missing Concepts:
{missing_text}

Please analyze the candidate's answer.

Provide the following:

1. What the candidate did well
2. What needs improvement
3. Specific improvement advice
4. An improved interview answer

Keep the feedback clear, professional,
and suitable for a real job interview.
"""

    # Send the prompt to Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    # Return the AI response
    return response["message"]["content"]


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":

    question = "What is overfitting?"

    candidate_answer = """
    Overfitting happens when a model learns
    the training data too closely.
    """

    answer_quality = 55.0

    missing_concepts = [
        "regularization",
        "cross validation"
    ]

    feedback = generate_llm_feedback(
        question,
        candidate_answer,
        answer_quality,
        missing_concepts
    )

    print("\n========================================")
    print("AI INTERVIEW COACH FEEDBACK")
    print("========================================")

    print(feedback)