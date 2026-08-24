import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


class LLMReviewer:

    def __init__(self):

        token = os.getenv("HF_TOKEN")

        if not token:
            raise ValueError(
                "HF_TOKEN not found. "
                "Add your Hugging Face token to .env"
            )

        self.client = InferenceClient(
            api_key=token
        )

        # We can change the model later if needed.
        self.model = "meta-llama/Meta-Llama-3-8B-Instruct"

    def review_code(self, code, findings):

        findings_text = ""

        for index, finding in enumerate(
            findings,
            start=1
        ):

            findings_text += f"""
Issue {index}:
Category: {finding['category']}
Severity: {finding['severity']}
Line: {finding['line']}
Title: {finding['title']}
Message: {finding['message']}
Suggestion: {finding['suggestion']}
"""

        prompt = f"""
You are an expert Python code reviewer.

Review the following Python code.

Use the static-analysis findings as additional
information.

Explain:

1. What is wrong
2. Why it matters
3. How to improve it
4. Safer alternatives
5. Suggested corrected code

Do not invent problems that are not supported
by the code.

PYTHON CODE:
----------------
{code}
----------------

STATIC ANALYSIS FINDINGS:
----------------
{findings_text}
----------------

Return the answer using these sections:

SUMMARY

KEY PROBLEMS

IMPROVEMENT SUGGESTIONS

SUGGESTED CODE

SAFETY NOTES
"""

        response = self.client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional Python "
                        "code reviewer."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model=self.model,
            max_tokens=1000,
            temperature=0.2
        )

        return response.choices[0].message.content