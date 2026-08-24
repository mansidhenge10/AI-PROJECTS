from code_analyzer import analyze_code


code = """
def get_user(id):
    password = "admin123"
    return database.get(id)
"""


issues = analyze_code(code)


print("\n==============================")
print("STATIC CODE ANALYSIS")
print("==============================")

for issue in issues:
    print(f"\nCategory   : {issue['category']}")
    print(f"Severity   : {issue['severity']}")
    print(f"Line       : {issue['line']}")
    print(f"Title      : {issue['title']}")
    print(f"Message    : {issue['message']}")
    print(f"Suggestion : {issue['suggestion']}")