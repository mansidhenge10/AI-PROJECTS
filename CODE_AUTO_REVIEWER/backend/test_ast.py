from api.ast_analyzer import ASTAnalyzer


code = """
def get_user(user):
    try:
        print("Searching for user")
        name = user["name"]
        result = eval(user["expression"])
        return name
    except:
        return None
"""

analyzer = ASTAnalyzer()

result = analyzer.analyze(code)

print("\n========== SYNTAX TEST ==========\n")
print(result)