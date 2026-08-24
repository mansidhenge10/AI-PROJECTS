import json


class ReportGenerator:

    def __init__(self):
        pass

    # --------------------------------------------------
    # CREATE COMPLETE REPORT
    # --------------------------------------------------

    def generate_report(self, code, findings, score_report):

        report = {
            "project": "Code Auto Reviewer",

            "review_status": "COMPLETE",

            "summary": {
                "overall_score": score_report["overall_score"],
                "total_issues": score_report["total_issues"],
                "high_issues": score_report["high_issues"],
                "medium_issues": score_report["medium_issues"],
                "low_issues": score_report["low_issues"]
            },

            "category_scores": score_report["category_scores"],

            "findings": findings,

            "code": code
        }

        return report

    # --------------------------------------------------
    # SAVE JSON REPORT
    # --------------------------------------------------

    def save_json(self, report, filename="review_report.json"):

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )

        return filename

    # --------------------------------------------------
    # CREATE HUMAN READABLE REPORT
    # --------------------------------------------------

    def generate_text_report(self, report):

        lines = []

        lines.append("=" * 60)
        lines.append("             CODE AUTO REVIEW REPORT")
        lines.append("=" * 60)

        lines.append("")
        lines.append(
            f"Review Status : {report['review_status']}"
        )

        lines.append(
            f"Overall Score : "
            f"{report['summary']['overall_score']} / 100"
        )

        lines.append("")

        # Summary
        lines.append("--------------- SUMMARY ---------------")

        lines.append(
            f"Total Issues  : "
            f"{report['summary']['total_issues']}"
        )

        lines.append(
            f"High Issues   : "
            f"{report['summary']['high_issues']}"
        )

        lines.append(
            f"Medium Issues : "
            f"{report['summary']['medium_issues']}"
        )

        lines.append(
            f"Low Issues    : "
            f"{report['summary']['low_issues']}"
        )

        lines.append("")

        # Category scores
        lines.append(
            "----------- CATEGORY SCORES -----------"
        )

        for category, score in report[
            "category_scores"
        ].items():

            lines.append(
                f"{category:<20}: {score} / 100"
            )

        lines.append("")

        # Findings
        lines.append(
            "--------------- FINDINGS --------------"
        )

        if not report["findings"]:

            lines.append(
                "No issues found. Great job!"
            )

        else:

            for index, finding in enumerate(
                report["findings"],
                start=1
            ):

                lines.append("")

                lines.append(
                    f"Issue #{index}"
                )

                lines.append(
                    f"Category   : "
                    f"{finding['category']}"
                )

                lines.append(
                    f"Severity   : "
                    f"{finding['severity']}"
                )

                lines.append(
                    f"Line       : "
                    f"{finding['line']}"
                )

                lines.append(
                    f"Title      : "
                    f"{finding['title']}"
                )

                lines.append(
                    f"Message    : "
                    f"{finding['message']}"
                )

                lines.append(
                    f"Suggestion : "
                    f"{finding['suggestion']}"
                )

                lines.append("-" * 60)

        return "\n".join(lines)