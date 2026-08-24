from api.ast_analyzer import ASTAnalyzer
from api.rule_engine import RuleEngine
from api.scorer import CodeQualityScorer
from api.report_generator import ReportGenerator


# --------------------------------------------------
# TEST CODE
# --------------------------------------------------

code = """
def get_user(user):

    print("Searching for user")

    name = user["name"]

    result = eval(user["expression"])

    return name
"""


# --------------------------------------------------
# AST ANALYSIS
# --------------------------------------------------

analyzer = ASTAnalyzer()

ast_result = analyzer.analyze(code)


# --------------------------------------------------
# RULE ENGINE
# --------------------------------------------------

engine = RuleEngine()

findings = engine.run(ast_result)


# --------------------------------------------------
# CODE QUALITY SCORE
# --------------------------------------------------

scorer = CodeQualityScorer()

score_report = scorer.generate_report(
    findings
)


# --------------------------------------------------
# REPORT GENERATOR
# --------------------------------------------------

generator = ReportGenerator()

report = generator.generate_report(
    code,
    findings,
    score_report
)


# --------------------------------------------------
# PRINT TEXT REPORT
# --------------------------------------------------

text_report = generator.generate_text_report(
    report
)

print(text_report)


# --------------------------------------------------
# SAVE JSON REPORT
# --------------------------------------------------

filename = generator.save_json(
    report
)

print(
    f"\nJSON report saved as: {filename}"
)