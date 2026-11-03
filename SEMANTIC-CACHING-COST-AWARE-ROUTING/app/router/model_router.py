
from app.config import SMALL_MODEL, LARGE_MODEL


class ModelRouter:

    def route(self, query):
        query_lower = query.lower()
        words = query_lower.split()

        complexity_score = 0

        # 1. Query length
        if len(words) > 20:
            complexity_score += 2
        elif len(words) > 10:
            complexity_score += 1

        # 2. Complex reasoning keywords
        complex_keywords = [
            "analyze", "analyse", "compare", "evaluate",
            "architecture", "implement", "debug",
            "optimize", "design", "reason",
            "step by step", "explain in detail",
            "pros and cons", "trade-offs",
            "advantages and disadvantages"
        ]

        for keyword in complex_keywords:
            if keyword in query_lower:
                complexity_score += 2

        # 3. Technical task keywords
        technical_keywords = [
            "algorithm", "system design", "machine learning",
            "deep learning", "neural network", "database",
            "api integration", "code review", "performance"
        ]

        for keyword in technical_keywords:
            if keyword in query_lower:
                complexity_score += 1

        # 4. Multiple questions
        if query.count("?") > 1:
            complexity_score += 1

        # 5. Select model based on score
        if complexity_score >= 2:
            return LARGE_MODEL, "advanced"

        return SMALL_MODEL, "fast"
