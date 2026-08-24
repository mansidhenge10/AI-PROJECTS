from transformers import pipeline


print("Loading AI Code Reviewer model...")

reviewer = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-Coder-0.5B-Instruct"
)


def review_code(code: str, static_issues: list) -> str:

    if not static_issues:
        return "The code looks good. No issues were detected."

    issue_titles = "\n".join(
        f"- {issue['title']}"
        for issue in static_issues
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a concise Python code review assistant. "
                "Your ONLY job is to explain the confirmed issues. "
                "DO NOT repeat the issue list. "
                "DO NOT repeat the category, severity, line, message, "
                "or suggestion. "
                "DO NOT create new issues. "
                "Give one short explanation for each issue. "
                "Maximum 100 words."
            )
        },
        {
            "role": "user",
            "content": (
                "The following issues have already been detected:\n\n"
                + issue_titles
                + "\n\n"
                "Explain why these issues matter and briefly describe "
                "how a developer should fix them. "
                "Do not list the issue details again."
            )
        }
    ]

    result = reviewer(
        messages,
        max_new_tokens=120,
        do_sample=False
    )

    return result[0]["generated_text"][-1]["content"]
def fix_code(code: str, static_issues: list) -> str:

    if not static_issues:
        return code

    issues_text = "\n".join(
        f"- {issue['title']}: {issue['suggestion']}"
        for issue in static_issues
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a conservative Python code fixer.\n"
                "Modify ONLY what is necessary to fix the confirmed issues.\n"
                "Preserve the original program behavior.\n"
                "Do NOT add new functionality.\n"
                "Do NOT add example usage.\n"
                "Do NOT add comments unless necessary.\n"
                "Do NOT add password checks.\n"
                "Do NOT invent imports or variables.\n"
                "Do NOT change unrelated code.\n"
                "Return ONLY the corrected Python code.\n"
                "Do NOT use markdown code fences."
            )
        },
        {
            "role": "user",
            "content": (
                "Original code:\n"
                + code
                + "\n\n"
                "Confirmed issues:\n"
                + issues_text
                + "\n\n"
                "Fix ONLY these confirmed issues."
            )
        }
    ]

    result = reviewer(
        messages,
        max_new_tokens=150,
        do_sample=False
    )

    return result[0]["generated_text"][-1]["content"].strip()