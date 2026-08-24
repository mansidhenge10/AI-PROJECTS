class CodeQualityScorer:

    def __init__(self):
        # Starting score
        self.max_score = 100

        # Points deducted for each severity
        self.penalties = {
            "HIGH": 15,
            "MEDIUM": 8,
            "LOW": 3
        }

    def calculate_score(self, findings):

        score = self.max_score

        for finding in findings:

            severity = finding.get("severity", "LOW")

            penalty = self.penalties.get(
                severity,
                0
            )

            score -= penalty

        # Score should never go below 0
        score = max(score, 0)

        return score

    def calculate_category_scores(self, findings):

        categories = {
            "SECURITY": 100,
            "BUG RISK": 100,
            "BEST PRACTICE": 100,
            "MAINTAINABILITY": 100
        }

        for finding in findings:

            category = finding.get("category")
            severity = finding.get("severity", "LOW")

            if category in categories:

                penalty = self.penalties.get(
                    severity,
                    0
                )

                categories[category] -= penalty

        # Prevent negative scores
        for category in categories:

            categories[category] = max(
                categories[category],
                0
            )

        return categories

    def generate_report(self, findings):

        overall_score = self.calculate_score(
            findings
        )

        category_scores = self.calculate_category_scores(
            findings
        )

        high = 0
        medium = 0
        low = 0

        for finding in findings:

            severity = finding.get("severity")

            if severity == "HIGH":
                high += 1

            elif severity == "MEDIUM":
                medium += 1

            elif severity == "LOW":
                low += 1

        return {
            "overall_score": overall_score,
            "category_scores": category_scores,
            "total_issues": len(findings),
            "high_issues": high,
            "medium_issues": medium,
            "low_issues": low
        }