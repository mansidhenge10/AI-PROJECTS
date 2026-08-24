from ai_reviewer import review_code


code = """
def get_user(id):
    password = "admin123"
    return database.get(id)
"""


result = review_code(code)

print("\n==============================")
print("AI CODE REVIEW")
print("==============================")
print(result)