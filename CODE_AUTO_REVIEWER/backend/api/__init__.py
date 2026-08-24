def __init__(self):
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