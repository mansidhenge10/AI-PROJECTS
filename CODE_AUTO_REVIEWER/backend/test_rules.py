from api.ast_analyzer import ASTAnalyzer
from api.rule_engine import RuleEngine

code = """
def get_user(user):

    print("Searching for user")

    value1 = user.get("a")
    value2 = user.get("b")
    value3 = user.get("c")
    value4 = user.get("d")
    value5 = user.get("e")
    value6 = user.get("f")
    value7 = user.get("g")
    value8 = user.get("h")
    value9 = user.get("i")
    value10 = user.get("j")
    value11 = user.get("k")
    value12 = user.get("l")
    value13 = user.get("m")
    value14 = user.get("n")
    value15 = user.get("o")
    value16 = user.get("p")
    value17 = user.get("q")
    value18 = user.get("r")
    value19 = user.get("s")
    value20 = user.get("t")
    value21 = user.get("u")

    return value21
"""

analyzer = ASTAnalyzer()
ast_result = analyzer.analyze(code)

engine = RuleEngine()
findings = engine.run(ast_result)

print("\n========== CODE REVIEW ==========\n")

for finding in findings:
    print(f"Category   : {finding['category']}")
    print(f"Severity   : {finding['severity']}")
    print(f"Line       : {finding['line']}")
    print(f"Title      : {finding['title']}")
    print(f"Message    : {finding['message']}")
    print(f"Suggestion : {finding['suggestion']}")
    print("-" * 50)