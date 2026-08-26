import pandas as pd

from src.text_processor import process_answer
from src.tfidf_analyzer import calculate_similarity
from src.llm_feedback import generate_llm_feedback

from src.evaluation import (
    calculate_relevance_score,
    calculate_concept_coverage,
    calculate_answer_quality
)

from src.mistake_analyzer import (
    analyze_answer_quality,
    generate_feedback,
    generate_improvement_suggestions
)


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("data/interview_questions.csv")


print("=" * 60)
print("AI INTERVIEW MISTAKE ANALYZER")
print("=" * 60)

print("\nTotal questions:", len(df))


# ============================================================
# JOB DOMAIN
# ============================================================

domains = df["job_domain"].dropna().unique()

print("\nJob Domains:")

for i, domain in enumerate(domains, start=1):
    print(f"{i}. {domain}")


while True:
    try:
        domain_choice = int(input("\nEnter your choice: "))

        if 1 <= domain_choice <= 5:
            break

        print("Please enter a number between 1 and 5.")

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

selected_domain = domains[domain_choice - 1]


# ============================================================
# INTERVIEW TYPE
# ============================================================

interview_types = df[
    df["job_domain"] == selected_domain
]["interview_type"].dropna().unique()


print("\nInterview Types:")

for i, interview_type in enumerate(interview_types, start=1):
    print(f"{i}. {interview_type}")


type_choice = int(input("\nEnter your choice: "))

selected_type = interview_types[type_choice - 1]


# ============================================================
# FILTER QUESTIONS
# ============================================================

filtered_questions = df[
    (df["job_domain"] == selected_domain)
    &
    (df["interview_type"] == selected_type)
]


# ============================================================
# RANDOM QUESTION
# ============================================================

question = filtered_questions.sample(n=1).iloc[0]


print("\nCategory:", question["category"])
print("Difficulty:", question["difficulty"])

print("\nQuestion:")
print(question["question"])


# ============================================================
# CANDIDATE ANSWER
# ============================================================

candidate_answer = input("\nYour Answer:\n\n> ")


# ============================================================
# STEP 1 — TEXT PROCESSING
# ============================================================

processed_tokens = process_answer(candidate_answer)

print("\nProcessed Answer:")
print(processed_tokens)


# ============================================================
# STEP 2 — EXPECTED CONCEPTS
# ============================================================

expected_concepts = str(
    question["expected_concepts"]
).split(";")


expected_concepts = [
    concept.strip().lower()
    for concept in expected_concepts
    if concept.strip()
]


print("\nExpected Concepts:")
print(expected_concepts)


# ============================================================
# STEP 3 — SIMILARITY
# ============================================================

similarity_score = calculate_similarity(
    expected_concepts,
    candidate_answer
)


print("\nSimilarity Score:")
print(round(similarity_score, 4))


# ============================================================
# STEP 4 — RELEVANCE SCORE
# ============================================================

relevance_score = calculate_relevance_score(
    similarity_score
)


print("\nRelevance Score:")
print(relevance_score, "%")


# ============================================================
# STEP 5 — CONCEPT COVERAGE
# ============================================================

coverage_score, covered_concepts, missing_concepts = (
    calculate_concept_coverage(
        expected_concepts,
        candidate_answer
    )
)


print("\nConcept Coverage:")
print(coverage_score, "%")


# ============================================================
# COVERED CONCEPTS
# ============================================================

print("\nCovered Concepts:")

if covered_concepts:

    for concept in covered_concepts:
        print("✓", concept)

else:
    print("None")


# ============================================================
# MISSING CONCEPTS
# ============================================================

print("\nMissing Concepts:")

if missing_concepts:

    for concept in missing_concepts:
        print("✗", concept)

else:
    print("None")


# ============================================================
# STEP 6 — ANSWER QUALITY
# ============================================================

answer_quality = calculate_answer_quality(
    relevance_score,
    coverage_score
)


print("\nAnswer Quality Score:")
print(answer_quality, "%")


# ============================================================
# STEP 7 — ANSWER CLASSIFICATION
# ============================================================

evaluation = analyze_answer_quality(
    answer_quality
)


print("\nEvaluation:")
print(evaluation)


# ============================================================
# STEP 8 — FEEDBACK
# ============================================================

feedback = generate_feedback(
    missing_concepts
)


print("\nFeedback:")
print(feedback)


# ============================================================
# STEP 9 — IMPROVEMENT SUGGESTIONS
# ============================================================

suggestions = generate_improvement_suggestions(
    missing_concepts
)


print("\nImprovement Suggestions:")

for suggestion in suggestions:
    print("-", suggestion)


# ============================================================
# STEP 10 — AI LLM FEEDBACK
# ============================================================

print("\n" + "=" * 60)
print("AI INTERVIEW COACH — LLAMA 3.2")
print("=" * 60)

llm_feedback = generate_llm_feedback(
    question["question"],
    candidate_answer,
    answer_quality,
    missing_concepts
)

print("\n" + llm_feedback)


# ============================================================
# COMPLETE
# ============================================================

print("\n" + "=" * 60)
print("INTERVIEW ANALYSIS COMPLETE")
print("=" * 60)