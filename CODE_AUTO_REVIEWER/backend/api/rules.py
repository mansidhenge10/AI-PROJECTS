def check_risky_calls(ast_result):
    findings = []

    for risky_call in ast_result["risky_calls"]:
        function_name = risky_call["function"]
        line = risky_call["line"]

        if function_name == "eval":
            findings.append({
                "category": "SECURITY",
                "severity": "HIGH",
                "line": line,
                "title": "Dangerous eval() usage",
                "message": (
                    "eval() can execute arbitrary code and may create "
                    "a serious security risk."
                ),
                "suggestion": (
                    "Avoid eval() and use safer alternatives such as "
                    "explicit parsing or controlled mappings."
                )
            })

        elif function_name == "exec":
            findings.append({
                "category": "SECURITY",
                "severity": "HIGH",
                "line": line,
                "title": "Dangerous exec() usage",
                "message": (
                    "exec() can execute dynamically generated Python code "
                    "and may introduce security vulnerabilities."
                ),
                "suggestion": (
                    "Avoid exec() whenever possible and use explicit "
                    "functions or controlled logic instead."
                )
            })

    return findings


def check_dictionary_access(ast_result):
    findings = []

    for access in ast_result["dictionary_accesses"]:
        variable = access["variable"]
        key = access["key"]
        line = access["line"]

        access_text = f'{variable}["{key}"]'

        findings.append({
            "category": "BUG RISK",
            "severity": "MEDIUM",
            "line": line,
            "title": "Unsafe dictionary access",
            "message": (
                f"{access_text} may raise a KeyError "
                "if the key does not exist."
            ),
            "suggestion": (
                f'Consider using {variable}.get("{key}") '
                "or checking whether the key exists first."
            )
        })

    return findings


def check_bare_exceptions(ast_result):
    findings = []

    for exception in ast_result["bare_exceptions"]:
        line = exception["line"]

        findings.append({
            "category": "BEST PRACTICE",
            "severity": "MEDIUM",
            "line": line,
            "title": "Bare except clause",
            "message": (
                "A bare except catches almost every exception and "
                "can hide unexpected programming errors."
            ),
            "suggestion": (
                "Catch specific exceptions such as ValueError, "
                "TypeError, or KeyError."
            )
        })

    return findings
def check_type_hints(ast_result):
    findings = []

    for function in ast_result["functions"]:
        function_name = function["name"]
        line = function["line"]

        missing_arguments = function["missing_type_hints"]
        missing_return = function["missing_return_type"]

        if missing_arguments:
            arguments = ", ".join(missing_arguments)

            findings.append({
                "category": "BEST PRACTICE",
                "severity": "LOW",
                "line": line,
                "title": "Missing type hints",
                "message": (
                    f"Function '{function_name}' has parameters "
                    f"without type hints: {arguments}."
                ),
                "suggestion": (
                    "Add type hints to make the function contract "
                    "clearer and improve readability."
                )
            })

        if missing_return:
            findings.append({
                "category": "BEST PRACTICE",
                "severity": "LOW",
                "line": line,
                "title": "Missing return type hint",
                "message": (
                    f"Function '{function_name}' does not specify "
                    "a return type."
                ),
                "suggestion": (
                    "Add a return type annotation to make the "
                    "function's expected output explicit."
                )
            })

    return findings
def check_print_usage(ast_result):
    findings = []

    for call in ast_result["function_calls"]:

        if call == "print":

            # We don't have the line number yet.
            # We'll improve AST detection in the next step.

            findings.append({
                "category": "BEST PRACTICE",
                "severity": "LOW",
                "line": None,
                "title": "print() used in application code",
                "message": (
                    "print() is commonly used for debugging and basic "
                    "output, but logging is usually better for production "
                    "applications."
                ),
                "suggestion": (
                    "Consider using the Python logging module instead "
                    "of print()."
                )
            })

    return findings
def check_print_usage(ast_result):
    findings = []

    for call in ast_result["function_calls"]:

        if call["function"] == "print":

            findings.append({
                "category": "BEST PRACTICE",
                "severity": "LOW",
                "line": call["line"],
                "title": "print() used in application code",
                "message": (
                    "print() is commonly used for debugging and basic "
                    "output, but logging is usually better for production "
                    "applications."
                ),
                "suggestion": (
                    "Consider using the Python logging module instead "
                    "of print()."
                )
            })

    return findings
def check_long_functions(ast_result):

    findings = []

    MAX_FUNCTION_LINES = 20

    for function in ast_result["functions"]:

        if function["length"] > MAX_FUNCTION_LINES:

            findings.append({
                "category": "MAINTAINABILITY",
                "severity": "MEDIUM",
                "line": function["line"],
                "title": "Function is too long",
                "message": (
                    f"Function '{function['name']}' contains "
                    f"{function['length']} lines of code."
                ),
                "suggestion": (
                    "Consider splitting this function into smaller "
                    "functions with clear responsibilities."
                )
            })

    return findings