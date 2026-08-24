from api.rules import (
    check_risky_calls,
    check_dictionary_access,
    check_bare_exceptions,
    check_type_hints,
     check_print_usage,
      check_long_functions
)


class RuleEngine:

 def run(self, ast_result):
    findings = []

    findings.extend(
        check_risky_calls(ast_result)
    )

    findings.extend(
        check_dictionary_access(ast_result)
    )

    findings.extend(
        check_bare_exceptions(ast_result)
    )
    findings.extend(
    check_type_hints(ast_result)
)
    findings.extend(
        check_print_usage(ast_result)
    )
    findings.extend(
        check_long_functions(ast_result)
    )
    return findings