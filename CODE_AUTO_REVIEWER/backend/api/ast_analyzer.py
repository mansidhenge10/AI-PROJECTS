import ast


class ASTAnalyzer:

    def __init__(self):
        self.functions = []
        self.classes = []
        self.loops = 0
        self.conditions = 0
        self.imports = []
        self.return_statements = 0
        self.function_calls = []
        self.variables = []

        # Risk and quality information
        self.dictionary_accesses = []
        self.risky_calls = []
        self.bare_exceptions = []

    # --------------------------------------------------
    # FUNCTION DETECTION
    # --------------------------------------------------

    def visit_FunctionDef(self, node):

        missing_type_hints = []

        # Check function parameters
        for arg in node.args.args:

            if arg.arg != "self" and arg.annotation is None:
                missing_type_hints.append(arg.arg)

        # Check return type
        return_missing = node.returns is None

        # Get function ending line
        function_end_line = getattr(
            node,
            "end_lineno",
            node.lineno
        )

        # Calculate function length
        function_length = (
            function_end_line - node.lineno + 1
        )

        self.functions.append({
            "name": node.name,
            "line": node.lineno,
            "end_line": function_end_line,
            "length": function_length,
            "arguments": [
                arg.arg for arg in node.args.args
            ],
            "missing_type_hints": missing_type_hints,
            "missing_return_type": return_missing
        })

    # --------------------------------------------------
    # ASYNC FUNCTION DETECTION
    # --------------------------------------------------

    def visit_AsyncFunctionDef(self, node):

        missing_type_hints = []

        for arg in node.args.args:

            if arg.arg != "self" and arg.annotation is None:
                missing_type_hints.append(arg.arg)

        return_missing = node.returns is None

        function_end_line = getattr(
            node,
            "end_lineno",
            node.lineno
        )

        function_length = (
            function_end_line - node.lineno + 1
        )

        self.functions.append({
            "name": node.name,
            "line": node.lineno,
            "end_line": function_end_line,
            "length": function_length,
            "arguments": [
                arg.arg for arg in node.args.args
            ],
            "missing_type_hints": missing_type_hints,
            "missing_return_type": return_missing
        })

    # --------------------------------------------------
    # CLASS DETECTION
    # --------------------------------------------------

    def visit_ClassDef(self, node):

        self.classes.append({
            "name": node.name,
            "line": node.lineno
        })

    # --------------------------------------------------
    # LOOP DETECTION
    # --------------------------------------------------

    def visit_For(self, node):

        self.loops += 1

    def visit_While(self, node):

        self.loops += 1

    # --------------------------------------------------
    # CONDITION DETECTION
    # --------------------------------------------------

    def visit_If(self, node):

        self.conditions += 1

    # --------------------------------------------------
    # IMPORT DETECTION
    # --------------------------------------------------

    def visit_Import(self, node):

        for alias in node.names:
            self.imports.append(alias.name)

    def visit_ImportFrom(self, node):

        for alias in node.names:
            self.imports.append(alias.name)

    # --------------------------------------------------
    # RETURN STATEMENT DETECTION
    # --------------------------------------------------

    def visit_Return(self, node):

        self.return_statements += 1

    # --------------------------------------------------
    # FUNCTION CALL DETECTION
    # --------------------------------------------------

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):

            function_name = node.func.id

            self.function_calls.append({
                "function": function_name,
                "line": node.lineno
            })

            # Detect dangerous functions
            if function_name in ["eval", "exec"]:

                self.risky_calls.append({
                    "function": function_name,
                    "line": node.lineno
                })

        elif isinstance(node.func, ast.Attribute):

            function_name = node.func.attr

            self.function_calls.append({
                "function": function_name,
                "line": node.lineno
            })

    # --------------------------------------------------
    # VARIABLE DETECTION
    # --------------------------------------------------

    def visit_Name(self, node):

        if isinstance(node.ctx, ast.Store):

            self.variables.append(node.id)

    # --------------------------------------------------
    # DICTIONARY ACCESS DETECTION
    # --------------------------------------------------

    def visit_Subscript(self, node):

        if isinstance(node.value, ast.Name):

            key = None

            # Example:
            # user["name"]

            if isinstance(node.slice, ast.Constant):

                key = node.slice.value

            self.dictionary_accesses.append({
                "variable": node.value.id,
                "key": key,
                "line": node.lineno
            })

    # --------------------------------------------------
    # BARE EXCEPTION DETECTION
    # --------------------------------------------------

    def visit_ExceptHandler(self, node):

        if node.type is None:

            self.bare_exceptions.append({
                "line": node.lineno
            })

    # --------------------------------------------------
    # ANALYZE CODE
    # --------------------------------------------------

    def analyze(self, code):

        # Reset previous analysis
        self.functions = []
        self.classes = []
        self.loops = 0
        self.conditions = 0
        self.imports = []
        self.return_statements = 0
        self.function_calls = []
        self.variables = []
        self.dictionary_accesses = []
        self.risky_calls = []
        self.bare_exceptions = []

        # Parse Python code
        try:

            tree = ast.parse(code)

        except SyntaxError as error:

            return {
                "syntax_error": {
                    "message": error.msg,
                    "line": error.lineno,
                    "offset": error.offset
                }
            }

        # Walk through AST
        for node in ast.walk(tree):

            method = getattr(
                self,
                "visit_" + node.__class__.__name__,
                None
            )

            if method:
                method(node)

        # Return complete analysis
        return {
            "functions": self.functions,
            "classes": self.classes,
            "loops": self.loops,
            "conditions": self.conditions,
            "imports": self.imports,
            "return_statements": self.return_statements,
            "function_calls": self.function_calls,
            "variables": self.variables,
            "dictionary_accesses": self.dictionary_accesses,
            "risky_calls": self.risky_calls,
            "bare_exceptions": self.bare_exceptions
        }