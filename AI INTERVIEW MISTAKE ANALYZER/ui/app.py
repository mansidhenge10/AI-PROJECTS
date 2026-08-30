import streamlit as st
import pandas as pd
import sys
import os
import random
import tempfile


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# IMPORT PROJECT FUNCTIONS
# ============================================================

from src.tfidf_analyzer import calculate_similarity

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

from src.llm_analyzer import analyze_with_llm


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Interview Mistake Analyzer",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================

DEFAULTS = {
    "current_question": None,
    "question_number": 0,
    "total_questions": 10,
    "asked_questions": [],
    "interview_started": False,

    # Answer method
    "answer_method": None,

    # Analysis
    "analysis_done": False,
    "llm_feedback": "",

    # Statistics
    "answered_questions": 0,
    "skipped_questions": 0,

    # Scores
    "relevance_scores": [],
    "coverage_scores": [],
    "quality_scores": [],

    # Final summary
    "interview_finished": False,
}


for key, value in DEFAULTS.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# LOAD QUESTIONS
# ============================================================

questions_path = os.path.join(
    PROJECT_ROOT,
    "data",
    "interview_questions.csv"
)

try:

    questions_df = pd.read_csv(
        questions_path
    )

except Exception as e:

    st.error(
        f"Could not load interview questions.\n\n{e}"
    )

    st.stop()


# ============================================================
# TITLE
# ============================================================

st.title(
    "🤖 AI Interview Mistake Analyzer"
)

st.write(
    "Practice interview questions and get AI-powered "
    "feedback on your answers."
)

st.divider()


# ============================================================
# HELPER: RESET INTERVIEW
# ============================================================

def reset_interview():

    st.session_state["current_question"] = None

    st.session_state["question_number"] = 0

    st.session_state["asked_questions"] = []

    st.session_state["interview_started"] = False

    st.session_state["answer_method"] = None

    st.session_state["analysis_done"] = False

    st.session_state["llm_feedback"] = ""

    st.session_state["answered_questions"] = 0

    st.session_state["skipped_questions"] = 0

    st.session_state["relevance_scores"] = []

    st.session_state["coverage_scores"] = []

    st.session_state["quality_scores"] = []

    st.session_state["interview_finished"] = False


# ============================================================
# HELPER: RESET QUESTION
# ============================================================

def reset_question():

    st.session_state["analysis_done"] = False

    st.session_state["llm_feedback"] = ""


# ============================================================
# GET RANDOM QUESTION
# ============================================================

def get_next_question():

    filtered_questions = questions_df[
        (questions_df["job_domain"] == job_domain)
        &
        (questions_df["interview_type"] == interview_type)
    ]

    if filtered_questions.empty:

        return None


    # --------------------------------------------------------
    # Questions not asked yet
    # --------------------------------------------------------

    available_questions = filtered_questions[
        ~filtered_questions.index.isin(
            st.session_state["asked_questions"]
        )
    ]


    # --------------------------------------------------------
    # If all questions used
    # --------------------------------------------------------

    if available_questions.empty:

        available_questions = filtered_questions


    # --------------------------------------------------------
    # Random question
    # --------------------------------------------------------

    question = available_questions.sample(
        n=1
    ).iloc[0]

    return question


# ============================================================
# START NEXT QUESTION
# ============================================================

def move_to_next_question():

    if (
        st.session_state["question_number"]
        >=
        st.session_state["total_questions"]
    ):

        st.session_state["interview_finished"] = True

        st.session_state["current_question"] = None

        return


    next_question = get_next_question()

    if next_question is None:

        st.error(
            "No questions found for this selection."
        )

        return


    st.session_state["current_question"] = next_question

    st.session_state["asked_questions"].append(
        next_question.name
    )

    st.session_state["question_number"] += 1

    reset_question()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header(
        "⚙️ Interview Settings"
    )


    # --------------------------------------------------------
    # Job Domain
    # --------------------------------------------------------

    job_domain = st.selectbox(
        "Select Job Domain",
        [
            "AI/ML Engineer",
            "Data Analyst",
            "Python Developer",
            "Frontend Developer",
            "Data Scientist"
        ]
    )


    # --------------------------------------------------------
    # Interview Type
    # --------------------------------------------------------

    interview_type = st.selectbox(
        "Select Interview Type",
        [
            "Technical",
            "HR"
        ]
    )


    st.divider()


    st.write(
        "### Interview Settings"
    )


    st.write(
        f"**Questions:** "
        f"{st.session_state['total_questions']}"
    )


    if st.session_state["interview_started"]:

        st.write(
            f"**Progress:** "
            f"{st.session_state['question_number']} / "
            f"{st.session_state['total_questions']}"
        )

        st.write(
            f"**Answered:** "
            f"{st.session_state['answered_questions']}"
        )

        st.write(
            f"**Skipped:** "
            f"{st.session_state['skipped_questions']}"
        )


    # --------------------------------------------------------
    # Current Answer Method
    # --------------------------------------------------------

    if st.session_state["answer_method"]:

        st.divider()

        st.write(
            "**Answer Method:**"
        )

        if st.session_state["answer_method"] == "Text":

            st.write(
                "📝 Text"
            )

        else:

            st.write(
                "🎙️ Microphone"
            )


# ============================================================
# START INTERVIEW PAGE
# ============================================================

if (
    not st.session_state["interview_started"]
    and
    not st.session_state["interview_finished"]
):

    st.header(
        "🎯 Start Your Interview"
    )

    st.write(
        "Choose your job domain and interview type "
        "from the sidebar."
    )

    st.write(
        f"**Number of Questions:** "
        f"{st.session_state['total_questions']}"
    )

    st.write(
        "You will choose Text or Microphone after "
        "starting the interview."
    )


    st.divider()


    if st.button(
        "🚀 Start New Interview",
        use_container_width=True
    ):

        filtered_questions = questions_df[
            (questions_df["job_domain"] == job_domain)
            &
            (questions_df["interview_type"] == interview_type)
        ]


        if filtered_questions.empty:

            st.error(
                "No questions found for the selected "
                "Job Domain and Interview Type."
            )

        else:

            # Reset interview statistics

            st.session_state["asked_questions"] = []

            st.session_state["question_number"] = 0

            st.session_state["answered_questions"] = 0

            st.session_state["skipped_questions"] = 0

            st.session_state["relevance_scores"] = []

            st.session_state["coverage_scores"] = []

            st.session_state["quality_scores"] = []

            st.session_state["answer_method"] = None

            st.session_state["analysis_done"] = False

            st.session_state["llm_feedback"] = ""

            st.session_state["interview_finished"] = False

            st.session_state["interview_started"] = True


            # Get first question

            first_question = get_next_question()


            if first_question is not None:

                st.session_state[
                    "current_question"
                ] = first_question

                st.session_state[
                    "asked_questions"
                ].append(
                    first_question.name
                )

                st.session_state[
                    "question_number"
                ] = 1

                st.rerun()

            else:

                st.error(
                    "Unable to load question."
                )


# ============================================================
# INTERVIEW PAGE
# ============================================================

if (
    st.session_state["interview_started"]
    and
    not st.session_state["interview_finished"]
):


    # ========================================================
    # NEW INTERVIEW
    # ========================================================

    if st.button(
        "🔄 New Interview",
        use_container_width=True
    ):

        reset_interview()

        st.rerun()


    # ========================================================
    # PROGRESS
    # ========================================================

    st.divider()

    st.info(
        f"🔢 Question "
        f"{st.session_state['question_number']} / "
        f"{st.session_state['total_questions']}"
    )


    # ========================================================
    # CURRENT QUESTION
    # ========================================================

    question = st.session_state[
        "current_question"
    ]


    if question is not None:


        # ====================================================
        # QUESTION
        # ====================================================

        st.subheader(
            "📝 Interview Question"
        )

        st.write(
            f"### {question['question']}"
        )

        st.write(
            "**Category:**",
            question["category"]
        )

        st.write(
            "**Difficulty:**",
            question["difficulty"]
        )


        st.divider()


        # ====================================================
        # ANSWER METHOD SELECTION
        # ====================================================

        if st.session_state["answer_method"] is None:

            st.subheader(
                "🎤 Choose Answer Method"
            )

            st.write(
                "How would you like to answer this question?"
            )


            col1, col2 = st.columns(2)


            with col1:

                if st.button(
                    "📝 Answer with Text",
                    use_container_width=True
                ):

                    st.session_state[
                        "answer_method"
                    ] = "Text"

                    st.rerun()


            with col2:

                if st.button(
                    "🎙️ Answer with Microphone",
                    use_container_width=True
                ):

                    st.session_state[
                        "answer_method"
                    ] = "Mic"

                    st.rerun()


            # ------------------------------------------------
            # SKIP BEFORE ANSWER
            # ------------------------------------------------

            st.write("")

            if st.button(
                "⏭️ Skip Question",
                use_container_width=True
            ):

                if (
                    st.session_state["question_number"]
                    <
                    st.session_state["total_questions"]
                ):

                    st.session_state[
                        "skipped_questions"
                    ] += 1

                    move_to_next_question()

                    st.rerun()

                else:

                    st.session_state[
                        "skipped_questions"
                    ] += 1

                    st.session_state[
                        "interview_finished"
                    ] = True

                    st.session_state[
                        "current_question"
                    ] = None

                    st.rerun()


        # ====================================================
        # TEXT ANSWER MODE
        # ====================================================

        elif (
            st.session_state["answer_method"]
            == "Text"
        ):

            st.subheader(
                "📝 Text Answer"
            )

            st.caption(
                "Type your answer below."
            )


            answer_key = (
                f"text_answer_"
                f"{st.session_state['question_number']}"
            )


            candidate_answer = st.text_area(
                "💬 Your Answer",
                placeholder=(
                    "Type your interview answer here..."
                ),
                height=180,
                key=answer_key
            )


            st.write("")


            col1, col2 = st.columns(2)


            # ------------------------------------------------
            # SUBMIT
            # ------------------------------------------------

            with col1:

                submit_clicked = st.button(
                    "📤 Submit Answer",
                    use_container_width=True
                )


            # ------------------------------------------------
            # SKIP
            # ------------------------------------------------

            with col2:

                skip_clicked = st.button(
                    "⏭️ Skip Question",
                    use_container_width=True
                )


            # ------------------------------------------------
            # SKIP
            # ------------------------------------------------

            if skip_clicked:

                if (
                    st.session_state["question_number"]
                    <
                    st.session_state["total_questions"]
                ):

                    st.session_state[
                        "skipped_questions"
                    ] += 1

                    move_to_next_question()

                    st.rerun()

                else:

                    st.session_state[
                        "skipped_questions"
                    ] += 1

                    st.session_state[
                        "interview_finished"
                    ] = True

                    st.session_state[
                        "current_question"
                    ] = None

                    st.rerun()


            # ------------------------------------------------
            # SUBMIT
            # ------------------------------------------------

            if submit_clicked:

                if candidate_answer.strip() == "":

                    st.warning(
                        "⚠️ Please enter your answer first."
                    )

                else:

                    expected_concepts = str(
                        question["expected_concepts"]
                    ).split(";")

                    expected_concepts = [
                        concept.strip().lower()
                        for concept in expected_concepts
                        if concept.strip()
                    ]


                    # ========================================
                    # TF-IDF
                    # ========================================

                    similarity_score = calculate_similarity(
                        expected_concepts,
                        candidate_answer
                    )


                    # ========================================
                    # RELEVANCE
                    # ========================================

                    relevance_score = (
                        calculate_relevance_score(
                            similarity_score
                        )
                    )


                    # ========================================
                    # CONCEPT COVERAGE
                    # ========================================

                    coverage_score, covered, missing = (
                        calculate_concept_coverage(
                            expected_concepts,
                            candidate_answer
                        )
                    )


                    # ========================================
                    # ANSWER QUALITY
                    # ========================================

                    answer_quality = (
                        calculate_answer_quality(
                            relevance_score,
                            coverage_score
                        )
                    )


                    # ========================================
                    # MISTAKE ANALYZER
                    # ========================================

                    quality_label = (
                        analyze_answer_quality(
                            answer_quality
                        )
                    )


                    feedback = generate_feedback(
                        missing
                    )


                    suggestions = (
                        generate_improvement_suggestions(
                            missing
                        )
                    )


                    # ========================================
                    # LLAMA
                    # ========================================

                    llm_feedback = ""

                    with st.spinner(
                        "🤖 Llama 3.2 is analyzing your answer..."
                    ):

                        try:

                            llm_feedback = analyze_with_llm(
                                question["question"],
                                candidate_answer
                            )

                        except Exception as e:

                            llm_feedback = (
                                "Llama 3.2 analysis could not "
                                "be completed.\n\n"
                                f"Error: {str(e)}"
                            )


                    # ========================================
                    # SAVE RESULTS
                    # ========================================

                    st.session_state[
                        "analysis_done"
                    ] = True

                    st.session_state[
                        "submitted_answer"
                    ] = candidate_answer

                    st.session_state[
                        "relevance_score"
                    ] = relevance_score

                    st.session_state[
                        "coverage_score"
                    ] = coverage_score

                    st.session_state[
                        "answer_quality"
                    ] = answer_quality

                    st.session_state[
                        "covered"
                    ] = covered

                    st.session_state[
                        "missing"
                    ] = missing

                    st.session_state[
                        "quality_label"
                    ] = quality_label

                    st.session_state[
                        "feedback"
                    ] = feedback

                    st.session_state[
                        "suggestions"
                    ] = suggestions

                    st.session_state[
                        "llm_feedback"
                    ] = llm_feedback


                    # Add statistics

                    st.session_state[
                        "answered_questions"
                    ] += 1

                    st.session_state[
                        "relevance_scores"
                    ].append(
                        relevance_score
                    )

                    st.session_state[
                        "coverage_scores"
                    ].append(
                        coverage_score
                    )

                    st.session_state[
                        "quality_scores"
                    ].append(
                        answer_quality
                    )


                    st.rerun()


        # ====================================================
        # MICROPHONE MODE
        # ====================================================

        elif (
            st.session_state["answer_method"]
            == "Mic"
        ):

            st.subheader(
                "🎙️ Microphone Answer"
            )

            st.caption(
                "Click the microphone button and speak "
                "your answer."
            )


            audio_value = st.audio_input(
                "🎤 Record your answer"
            )


            if audio_value is not None:

                st.audio(
                    audio_value
                )

                st.success(
                    "🎙️ Audio recorded successfully."
                )

                st.info(
                    "The recorded audio is ready. "
                    "To convert speech into text automatically, "
                    "connect a speech-to-text model such as "
                    "Whisper."
                )


                # --------------------------------------------
                # NOTE
                # --------------------------------------------

                st.warning(
                    "⚠️ Microphone recording is enabled, "
                    "but automatic speech-to-text conversion "
                    "requires a speech recognition model."
                )


            st.write("")


            col1, col2 = st.columns(2)


            with col1:

                if st.button(
                    "📤 Submit Answer",
                    use_container_width=True
                ):

                    if audio_value is None:

                        st.warning(
                            "⚠️ Please record your answer first."
                        )

                    else:

                        st.error(
                            "🎙️ Speech-to-text is not connected yet. "
                            "We need to add Whisper to convert your "
                            "recording into text before analysis."
                        )


            with col2:

                if st.button(
                    "⏭️ Skip Question",
                    use_container_width=True
                ):

                    if (
                        st.session_state["question_number"]
                        <
                        st.session_state["total_questions"]
                    ):

                        st.session_state[
                            "skipped_questions"
                        ] += 1

                        move_to_next_question()

                        st.rerun()

                    else:

                        st.session_state[
                            "skipped_questions"
                        ] += 1

                        st.session_state[
                            "interview_finished"
                        ] = True

                        st.session_state[
                            "current_question"
                        ] = None

                        st.rerun()


            st.write("")


            # ------------------------------------------------
            # CHANGE METHOD
            # ------------------------------------------------

            if st.button(
                "🔄 Change Answer Method",
                use_container_width=True
            ):

                st.session_state[
                    "answer_method"
                ] = None

                st.rerun()


# ============================================================
# DISPLAY ANALYSIS
# ============================================================

if (
    st.session_state["analysis_done"]
    and
    not st.session_state["interview_finished"]
):

    st.divider()


    st.subheader(
        "📊 Interview Analysis"
    )


    # ========================================================
    # SUBMITTED ANSWER
    # ========================================================

    st.subheader(
        "💬 Your Submitted Answer"
    )

    st.info(
        st.session_state["submitted_answer"]
    )


    # ========================================================
    # SCORE CARDS
    # ========================================================

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Relevance Score",
            f"{st.session_state['relevance_score']:.2f}%"
        )


    with col2:

        st.metric(
            "Concept Coverage",
            f"{st.session_state['coverage_score']:.2f}%"
        )


    with col3:

        st.metric(
            "Answer Quality",
            f"{st.session_state['answer_quality']:.2f}%"
        )


    # ========================================================
    # CLASSIFICATION
    # ========================================================

    st.subheader(
        "🏆 Answer Classification"
    )


    quality = st.session_state[
        "answer_quality"
    ]

    label = st.session_state[
        "quality_label"
    ]


    if quality >= 80:

        st.success(label)

    elif quality >= 60:

        st.info(label)

    elif quality >= 40:

        st.warning(label)

    else:

        st.error(label)


    # ========================================================
    # COVERED CONCEPTS
    # ========================================================

    st.subheader(
        "✅ Covered Concepts"
    )


    covered = st.session_state[
        "covered"
    ]


    if covered:

        for concept in covered:

            st.write(
                f"✓ {concept}"
            )

    else:

        st.write(
            "No expected concepts were detected."
        )


    # ========================================================
    # MISSING CONCEPTS
    # ========================================================

    st.subheader(
        "❌ Missing Concepts"
    )


    missing = st.session_state[
        "missing"
    ]


    if missing:

        for concept in missing:

            st.write(
                f"✗ {concept}"
            )

    else:

        st.success(
            "All important concepts were covered! 🎉"
        )


    # ========================================================
    # NLP FEEDBACK
    # ========================================================

    st.subheader(
        "💡 NLP Feedback"
    )


    st.write(
        st.session_state["feedback"]
    )


    # ========================================================
    # IMPROVEMENT SUGGESTIONS
    # ========================================================

    st.subheader(
        "🎯 Improvement Suggestions"
    )


    suggestions = st.session_state[
        "suggestions"
    ]


    if suggestions:

        for suggestion in suggestions:

            st.write(
                f"• {suggestion}"
            )

    else:

        st.write(
            "Keep practicing to improve your "
            "interview performance."
        )


    # ========================================================
    # LLAMA FEEDBACK
    # ========================================================

    st.subheader(
        "🤖 Llama 3.2 AI Interview Feedback"
    )


    if st.session_state["llm_feedback"]:

        st.markdown(
            st.session_state["llm_feedback"]
        )

    else:

        st.warning(
            "No Llama 3.2 feedback available."
        )


    # ========================================================
    # NEXT QUESTION
    # ========================================================

    st.divider()


    if (
        st.session_state["question_number"]
        <
        st.session_state["total_questions"]
    ):

        if st.button(
            "➡️ Next Question",
            use_container_width=True
        ):

            move_to_next_question()

            st.rerun()

    else:

        st.session_state[
            "interview_finished"
        ] = True

        st.session_state[
            "current_question"
        ] = None

        st.rerun()


# ============================================================
# FINAL INTERVIEW SUMMARY
# ============================================================

if st.session_state["interview_finished"]:

    st.title(
        "🎉 Interview Completed!"
    )


    st.success(
        "You have completed the interview."
    )


    st.divider()


    # ========================================================
    # SUMMARY STATISTICS
    # ========================================================

    st.subheader(
        "📊 Interview Summary"
    )


    total = st.session_state[
        "total_questions"
    ]

    answered = st.session_state[
        "answered_questions"
    ]

    skipped = st.session_state[
        "skipped_questions"
    ]


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Total Questions",
            total
        )


    with col2:

        st.metric(
            "Answered",
            answered
        )


    with col3:

        st.metric(
            "Skipped",
            skipped
        )


    # ========================================================
    # AVERAGE SCORES
    # ========================================================

    st.subheader(
        "📈 Average Performance"
    )


    relevance_scores = st.session_state[
        "relevance_scores"
    ]

    coverage_scores = st.session_state[
        "coverage_scores"
    ]

    quality_scores = st.session_state[
        "quality_scores"
    ]


    if relevance_scores:

        average_relevance = sum(
            relevance_scores
        ) / len(
            relevance_scores
        )

    else:

        average_relevance = 0


    if coverage_scores:

        average_coverage = sum(
            coverage_scores
        ) / len(
            coverage_scores
        )

    else:

        average_coverage = 0


    if quality_scores:

        average_quality = sum(
            quality_scores
        ) / len(
            quality_scores
        )

    else:

        average_quality = 0


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Average Relevance",
            f"{average_relevance:.2f}%"
        )


    with col2:

        st.metric(
            "Average Concept Coverage",
            f"{average_coverage:.2f}%"
        )


    with col3:

        st.metric(
            "Average Answer Quality",
            f"{average_quality:.2f}%"
        )


    # ========================================================
    # PERFORMANCE CHART
    # ========================================================

    if quality_scores:

        st.subheader(
            "📊 Answer Quality by Question"
        )


        chart_data = pd.DataFrame(
            {
                "Question": list(
                    range(
                        1,
                        len(quality_scores) + 1
                    )
                ),

                "Answer Quality": quality_scores
            }
        )


        chart_data = chart_data.set_index(
            "Question"
        )


        st.line_chart(
            chart_data
        )


    # ========================================================
    # OVERALL PERFORMANCE
    # ========================================================

    st.subheader(
        "🏆 Overall Performance"
    )


    if average_quality >= 80:

        st.success(
            "Excellent performance! 🌟"
        )

        st.write(
            "Your interview answers show strong "
            "concept understanding and relevance."
        )

    elif average_quality >= 60:

        st.info(
            "Good performance! 👍"
        )

        st.write(
            "You have a good foundation, but there "
            "are still some areas to improve."
        )

    elif average_quality >= 40:

        st.warning(
            "Average performance. 📚"
        )

        st.write(
            "Focus on improving concept coverage "
            "and explaining your answers clearly."
        )

    else:

        st.error(
            "Needs improvement. 💪"
        )

        st.write(
            "Practice the important concepts and "
            "try to give more complete explanations."
        )


    st.divider()


    # ========================================================
    # START AGAIN
    # ========================================================

    if st.button(
        "🔄 Start Another Interview",
        use_container_width=True
    ):

        reset_interview()

        st.rerun()