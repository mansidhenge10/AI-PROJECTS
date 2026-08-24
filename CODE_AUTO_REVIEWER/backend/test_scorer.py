from api.ast_analyzer import ASTAnalyzer
from api.rule_engine import RuleEngine
from api.scorer import CodeQualityScorer


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


# -------------------------------
# AST ANALYSIS
# -------------------------------

analyzer = ASTAnalyzer()

ast_result = analyzer.analyze(code)


# -------------------------------
# RULE ENGINE
# -------------------------------

engine = RuleEngine()

findings = engine.run(ast_result)


# -------------------------------
# CODE QUALITY SCORER
# -------------------------------

scorer = CodeQualityScorer()

report = scorer.generate_report(findings)


# -------------------------------
# PRINT REPORT
# -------------------------------

print("\n================================")
print("       CODE QUALITY REPORT")
print("================================")

print(
    f"\nOverall Score : "
    f"{report['overall_score']} / 100"
)

print(
    f"Total Issues  : "
    f"{report['total_issues']}"
)

print(
    f"High Issues   : "
    f"{report['high_issues']}"
)

print(
    f"Medium Issues : "
    f"{report['medium_issues']}"
)

print(
    f"Low Issues    : "
    f"{report['low_issues']}"
)


print("\n---------- CATEGORY SCORES ----------")

for category, score in report["category_scores"].items():

    print(
        f"{category:<18}: {score} / 100"
    )

print("================================")