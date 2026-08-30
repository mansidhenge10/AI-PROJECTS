import ollama


def analyze_with_llm(question, candidate_answer):
    """
    Analyze the candidate's interview answer
    using Llama 3.2.
    """

    prompt = f"""
You are an AI interview evaluator.

Analyze the candidate's answer to the interview question.

Interview Question:
{question}

Candidate Answer:
{candidate_answer}

Provide feedback in the following format:

1. What the candidate did well
2. What is missing or incorrect
3. Explanation of mistakes
4. Specific improvement suggestions
5. A better sample answer

Keep the feedback professional, clear,
and suitable for an interview candidate.
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


if __name__ == "__main__":

    question = "What is the difference between WHERE and HAVING in SQL?"

    candidate_answer = """
    WHERE is used to filter rows and HAVING
    is used to filter groups after GROUP BY.
    """

    feedback = analyze_with_llm(
        question,
        candidate_answer
    )

    print("\n===== Llama 3.2 Feedback =====\n")
    print(feedback)