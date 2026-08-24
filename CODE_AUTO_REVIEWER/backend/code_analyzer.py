import ast


def analyze_code(code: str):
    issues = []

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        issues.append({
            "category": "SYNTAX",
            "severity": "HIGH",
            "line": e.lineno,
            "title": "Syntax Error",
            "message": e.msg,
            "suggestion": "Fix the syntax error before running the code."
        })

        return issues

    # ==========================================
    # FUNCTION ANALYSIS
    # ==========================================

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            # Missing return type
            if node.returns is None:
                issues.append({
                    "category": "BEST PRACTICE",
                    "severity": "LOW",
                    "line": node.lineno,
                    "title": "Missing return type hint",
                    "message": (
                        f"Function '{node.name}' does not specify "
                        "a return type."
                    ),
                    "suggestion": (
                        "Add a return type annotation to make "
                        "the function contract clearer."
                    )
                })

            # Missing parameter type hints
            for argument in node.args.args:

                if argument.annotation is None:
                    issues.append({
                        "category": "BEST PRACTICE",
                        "severity": "LOW",
                        "line": node.lineno,
                        "title": "Missing parameter type hint",
                        "message": (
                            f"Parameter '{argument.arg}' in function "
                            f"'{node.name}' has no type annotation."
                        ),
                        "suggestion": (
                            "Add a type annotation to improve "
                            "code readability."
                        )
                    })

    # ==========================================
    # HARDcoded SECRET ANALYSIS
    # ==========================================

    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):

                    variable_name = target.id.lower()

                    # Only check variables related to secrets
                    if "password" in variable_name or "secret" in variable_name:

                        # ------------------------------------------
                        # Case 1:
                        # password = "admin123"
                        # This IS a hardcoded secret
                        # ------------------------------------------

                        if isinstance(node.value, ast.Constant):

                            if isinstance(node.value.value, str):

                                if node.value.value.strip():

                                    issues.append({
                                        "category": "SECURITY",
                                        "severity": "HIGH",
                                        "line": node.lineno,
                                        "title": "Hardcoded secret",
                                        "message": (
                                            f"Sensitive value is hardcoded "
                                            f"in variable '{target.id}'."
                                        ),
                                        "suggestion": (
                                            "Store sensitive information "
                                            "in environment variables instead."
                                        )
                                    })

                        # ------------------------------------------
                        # Case 2:
                        # password = os.getenv("PASSWORD")
                        # This is NOT a hardcoded secret
                        # ------------------------------------------

                        elif isinstance(node.value, ast.Call):

                            # If value comes from os.getenv()
                            if (
                                isinstance(node.value.func, ast.Attribute)
                                and isinstance(
                                    node.value.func.value,
                                    ast.Name
                                )
                                and node.value.func.value.id == "os"
                                and node.value.func.attr == "getenv"
                            ):
                                # Safe - do not report anything
                                continue

                            # Other function calls are not automatically
                            # considered hardcoded secrets.
                            continue

    return issues