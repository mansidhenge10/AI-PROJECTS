import streamlit as st


def show_ats_resume_template(
    resume_text="",
    resume_skills=None,
    missing_skills=None
):

    # ==================================================
    # DEFAULT VALUES
    # ==================================================

    if resume_skills is None:
        resume_skills = []

    if missing_skills is None:
        missing_skills = []


    # ==================================================
    # SESSION STATE
    # ==================================================

    if "resume_generated" not in st.session_state:

        st.session_state[
            "resume_generated"
        ] = False


    # ==================================================
    # ATS RESUME EDITOR
    # ==================================================

    st.divider()

    st.header(
        "📄 ATS-Friendly Resume Editor"
    )

    st.info(
        "Create a clean, professional and ATS-friendly "
        "resume for the selected job."
    )


    # ==================================================
    # ATS TIPS
    # ==================================================

    with st.expander(
        "💡 ATS Resume Tips"
    ):

        st.write(
            "✓ Use a simple single-column layout."
        )

        st.write(
            "✓ Use standard section headings."
        )

        st.write(
            "✓ Include relevant job keywords."
        )

        st.write(
            "✓ Avoid excessive graphics and tables."
        )

        st.write(
            "✓ Use measurable achievements."
        )

        st.write(
            "✓ Only mention skills you genuinely have."
        )


    # ==================================================
    # PERSONAL INFORMATION
    # ==================================================

    st.subheader(
        "👤 Personal Information"
    )


    col1, col2 = st.columns(2)


    with col1:

        name = st.text_input(
            "Full Name",
            placeholder="e.g. Mansi Dhenge",
            key="resume_name"
        )


        email = st.text_input(
            "Email",
            placeholder="e.g. yourname@gmail.com",
            key="resume_email"
        )


        phone = st.text_input(
            "Phone",
            placeholder="e.g. +91 XXXXX XXXXX",
            key="resume_phone"
        )


    with col2:

        location = st.text_input(
            "Location",
            placeholder="e.g. Nagpur, Maharashtra",
            key="resume_location"
        )


        linkedin = st.text_input(
            "LinkedIn",
            placeholder="https://linkedin.com/in/username",
            key="resume_linkedin"
        )


        github = st.text_input(
            "GitHub",
            placeholder="https://github.com/username",
            key="resume_github"
        )


    # ==================================================
    # PROFESSIONAL SUMMARY
    # ==================================================

    st.subheader(
        "📝 Professional Summary"
    )


    summary = st.text_area(
        "Write your professional summary",
        height=130,
        placeholder=(
            "AI Engineer with experience in Python, "
            "Machine Learning, NLP and Generative AI..."
        ),
        key="resume_summary"
    )


    # ==================================================
    # TECHNICAL SKILLS
    # ==================================================

    st.subheader(
        "🛠️ Technical Skills"
    )


    default_skills = ", ".join(
        skill.title()
        for skill in resume_skills
    )


    skills = st.text_area(
        "Technical Skills",
        value=default_skills,
        height=120,
        placeholder=(
            "Python, Machine Learning, NLP, "
            "SQL, PyTorch, TensorFlow..."
        ),
        key="resume_skills"
    )


    # ==================================================
    # EXPERIENCE
    # ==================================================

    st.subheader(
        "💼 Work Experience"
    )


    experience = st.text_area(
        "Work Experience",
        height=220,
        placeholder=(
            "AI Engineer Intern | Company Name | Location\n"
            "Jan 2025 – Jun 2025\n\n"
            "• Developed machine learning solutions using Python.\n"
            "• Built REST APIs using FastAPI.\n"
            "• Improved application performance by X%."
        ),
        key="resume_experience"
    )


    # ==================================================
    # PROJECTS
    # ==================================================

    st.subheader(
        "🚀 Projects"
    )


    projects = st.text_area(
        "Projects",
        height=250,
        placeholder=(
            "AI Interview Mistake Analyzer\n"
            "Python | NLP | Machine Learning | Streamlit\n\n"
            "• Developed an AI-powered interview analysis system.\n"
            "• Used NLP techniques to analyze candidate answers.\n"
            "• Implemented TF-IDF based concept extraction.\n\n"
            "Brain Tumor Detection\n"
            "Python | Deep Learning | CNN\n\n"
            "• Built an image classification model for brain tumor detection."
        ),
        key="resume_projects"
    )


    # ==================================================
    # EDUCATION
    # ==================================================

    st.subheader(
        "🎓 Education"
    )


    education = st.text_area(
        "Education",
        height=130,
        placeholder=(
            "Master of Computer Applications (MCA)\n"
            "University / College Name\n"
            "2025"
        ),
        key="resume_education"
    )


    # ==================================================
    # CERTIFICATIONS
    # ==================================================

    st.subheader(
        "🏆 Certifications"
    )


    certifications = st.text_area(
        "Certifications",
        height=130,
        placeholder=(
            "Machine Learning Certificate — Platform — 2026\n"
            "Generative AI Certificate — Platform — 2026"
        ),
        key="resume_certifications"
    )


    # ==================================================
    # ACHIEVEMENTS
    # ==================================================

    st.subheader(
        "🏅 Achievements"
    )


    achievements = st.text_area(
        "Achievements",
        height=120,
        placeholder=(
            "• Achievement or award\n"
            "• Competition / Hackathon\n"
            "• Academic achievement"
        ),
        key="resume_achievements"
    )


    # ==================================================
    # GENERATE ATS RESUME
    # ==================================================

    st.divider()


    generate_button = st.button(
        "📄 GENERATE ATS RESUME",
        use_container_width=True
    )


    if generate_button:

        # --------------------------------------------------
        # VALIDATION
        # --------------------------------------------------

        if not name.strip():

            st.warning(
                "⚠️ Please enter your full name."
            )

            st.stop()


        if not email.strip():

            st.warning(
                "⚠️ Please enter your email."
            )

            st.stop()


        if not summary.strip():

            st.warning(
                "⚠️ Please enter a professional summary."
            )

            st.stop()


        if not skills.strip():

            st.warning(
                "⚠️ Please enter your technical skills."
            )

            st.stop()


        # --------------------------------------------------
        # SAVE RESUME
        # --------------------------------------------------

        st.session_state[
            "generated_resume"
        ] = {

            "name": name,

            "email": email,

            "phone": phone,

            "location": location,

            "linkedin": linkedin,

            "github": github,

            "summary": summary,

            "skills": skills,

            "experience": experience,

            "projects": projects,

            "education": education,

            "certifications": certifications,

            "achievements": achievements
        }


        st.session_state[
            "resume_generated"
        ] = True


        st.success(
            "✅ ATS-friendly resume generated!"
        )


    # ==================================================
    # RESUME PREVIEW
    # ==================================================

    if st.session_state.get(
        "resume_generated",
        False
    ):

        resume = st.session_state[
            "generated_resume"
        ]


        st.divider()

        st.header(
            "👀 Resume Preview"
        )


        # ==================================================
        # PREVIEW
        # ==================================================

        st.markdown(
            f"""
# {resume["name"]}

**{resume["email"]}**  
**{resume["phone"]}**  
**{resume["location"]}**

{resume["linkedin"]}  
{resume["github"]}

---

## PROFESSIONAL SUMMARY

{resume["summary"]}

---

## TECHNICAL SKILLS

{resume["skills"]}

---

## WORK EXPERIENCE

{resume["experience"]}

---

## PROJECTS

{resume["projects"]}

---

## EDUCATION

{resume["education"]}

---

## CERTIFICATIONS

{resume["certifications"]}

---

## ACHIEVEMENTS

{resume["achievements"]}
"""
        )


        # ==================================================
        # ATS CHECK
        # ==================================================

        st.divider()

        st.subheader(
            "🤖 ATS Resume Check"
        )


        ats_checks = {

            "Name is present":
                bool(resume["name"].strip()),

            "Email is present":
                bool(resume["email"].strip()),

            "Professional Summary":
                bool(resume["summary"].strip()),

            "Technical Skills":
                bool(resume["skills"].strip()),

            "Work Experience":
                bool(resume["experience"].strip()),

            "Projects":
                bool(resume["projects"].strip()),

            "Education":
                bool(resume["education"].strip()),

            "Certifications":
                bool(resume["certifications"].strip())
        }


        for check, status in ats_checks.items():

            if status:

                st.write(
                    f"✅ {check}"
                )

            else:

                st.write(
                    f"⚠️ {check}"
                )


        # ==================================================
        # TEXT DOWNLOAD
        # ==================================================

        resume_text_output = f"""
{resume["name"]}

{resume["email"]} | {resume["phone"]} | {resume["location"]}
{resume["linkedin"]}
{resume["github"]}

PROFESSIONAL SUMMARY
{resume["summary"]}

TECHNICAL SKILLS
{resume["skills"]}

WORK EXPERIENCE
{resume["experience"]}

PROJECTS
{resume["projects"]}

EDUCATION
{resume["education"]}

CERTIFICATIONS
{resume["certifications"]}

ACHIEVEMENTS
{resume["achievements"]}
"""


        st.download_button(
            label="📥 DOWNLOAD RESUME",
            data=resume_text_output,
            file_name="ATS_Resume.txt",
            mime="text/plain",
            use_container_width=True
        )