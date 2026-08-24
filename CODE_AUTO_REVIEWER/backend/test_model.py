from transformers import pipeline

print("Loading AI model...")

reviewer = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-Coder-0.5B-Instruct"
)

messages = [
    {
        "role": "system",
        "content": "You are an expert Python code reviewer."
    },
    {
        "role": "user",
        "content": """Review this Python code:

def add(a, b):
    return a + b

Give one specific improvement suggestion."""
    }
]

result = reviewer(
    messages,
    max_new_tokens=100,
    do_sample=False
)

print("\nAI REVIEW:")
print(result[0]["generated_text"][-1]["content"])