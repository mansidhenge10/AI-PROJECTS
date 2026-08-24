import ast


def fix_code(code: str) -> str:
    """
    Apply safe automatic fixes to Python code.
    """

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return code

    lines = code.splitlines()

    # Fix missing parameter type hints
    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            # Add type hints to parameters that don't have them
            for arg in node.args.args:

                if arg.annotation is None:

                    line_number = node.lineno - 1

                    old_line = lines[line_number]

                    old_name = f"{arg.arg})"

                    if old_name in old_line:
                        new_line = old_line.replace(
                            old_name,
                            f"{arg.arg}: int)"
                        )

                        lines[line_number] = new_line

            # Add return type hint
            if node.returns is None:

                line_number = node.lineno - 1

                old_line = lines[line_number]

                if "):" in old_line:

                    lines[line_number] = old_line.replace(
                        "):",
                        ") -> Any:"
                    )

    # Fix hardcoded password/secret values
    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):

                    name = target.id.lower()

                    if any(
                        keyword in name
                        for keyword in [
                            "password",
                            "secret",
                            "api_key",
                            "token"
                        ]
                    ):

                        line_number = node.lineno - 1

                        lines[line_number] = (
                            "    "
                            + target.id
                            + ' = os.getenv("'
                            + target.id.upper()
                            + '")'
                        )

    fixed_code = "\n".join(lines)

    # Add required import
    if "os.getenv" in fixed_code and "import os" not in fixed_code:

        fixed_code = "import os\n\n" + fixed_code

    # Add Any import when return type is added
    if "-> Any:" in fixed_code and "from typing import Any" not in fixed_code:

        fixed_code = (
            "from typing import Any\n"
            + fixed_code
        )

    return fixed_code