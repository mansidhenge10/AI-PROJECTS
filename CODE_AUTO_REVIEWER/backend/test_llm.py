from api.ast_analyzer import ASTAnalyzer
from api.rule_engine import RuleEngine
from api.llm_reviewer import LLMReviewer


code = """
def get_user(user):

    print("Searching for user")

    name = user["name"]

    result = eval(user["expression"])

    return name
"""


# --------------------------------
# AST ANALYSIS
# --------------------------------

analyzer = ASTAnalyzer()

ast_result = analyzer.analyze(code)


# --------------------------------
# RULE ENGINE
# --------------------------------

engine = RuleEngine()

findings = engine.run(ast_result)


# --------------------------------
# LLM REVIEW
# --------------------------------

reviewer = LLMReviewer()

ai_review = reviewer.review_code(
    code,
    findings
)


# --------------------------------
# OUTPUT
# --------------------------------

print("\n========================================")
print("           AI CODE REVIEW")
print("========================================")

print(ai_review)