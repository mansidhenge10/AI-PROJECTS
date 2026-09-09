import streamlit as st


def show_ats_resume_template():

    st.divider()

    st.header("📄 ATS-Friendly Resume Builder")

    st.info(
        "Create a clean, professional, ATS-friendly resume "
        "using the information from your analyzed resume."
    )

    # ==================================================
    # PERSONAL INFORMATION
    # ==================================================

    st.subheader("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Full Name",
            placeholder="e.g. Mansi Dhenge"
        )

        email = st.text_input(
            "Email",
            placeholder="e.g. yourname@gmail.com"
        )

        phone = st.text_input(
            "Phone",
            placeholder="e.g. +91 XXXXX XXXXX"
        )

    with col2:
        location = st.text_input(
            "Location",
            placeholder="e.g. Nagpur, Maharashtra"
        )

        linkedin = st.text_input(
            "LinkedIn",
            placeholder="LinkedIn profile"
        )

        github = st.text_input(
            "GitHub",
            placeholder="GitHub profile"
        )

    # ==================================================
    # PROFESSIONAL SUMMARY
    # ==================================================

    st.subheader("📝 Professional Summary")

    summary = st.text_area(
        "Professional Summary",
        height=120,
        placeholder=(
            "Write a 2–4 line professional summary "
            "tailored to the job."
        )
    )

    # ==================================================
    # SKILLS
    # ==================================================

    st.subheader("🛠️ Technical Skills")

    skills = st.text_area(
        "Skills",
        height=100,
        placeholder=(
            "Python, Machine Learning, NLP, SQL, "
            "TensorFlow, PyTorch, FastAPI..."
        )
    )

    # ==================================================
    # EXPERIENCE
    # ==================================================

    st.subheader("💼 Work Experience")

    experience = st.text_area(
        "Experience",
        height=180,
        placeholder=(
            "Job Title | Company | Location | Dates\n"
            "• Achievement or responsibility\n"
            "• Achievement or responsibility\n"
            "• Technologies used"
        )
    )

    # ==================================================
    # PROJECTS
    # ==================================================

    st.subheader("🚀 Projects")

    projects = st.text_area(
        "Projects",
        height=200,
        placeholder=(
            "Project Name\n"
            "• What you built\n"
            "• Technologies used\n"
            "• Result / achievement"
        )
    )

    # ==================================================
    # EDUCATION
    # ==================================================

    st.subheader("🎓 Education")

    education = st.text_area(
        "Education",
        height=120,
        placeholder=(
            "Degree | University / College | Year\n"
            "MCA | XYZ University | 2025"
        )
    )

    # ==================================================
    # CERTIFICATIONS
    # ==================================================

    st.subheader("🏆 Certifications")

    certifications = st.text_area(
        "Certifications",
        height=100,
        placeholder=(
            "Machine Learning Certificate\n"
            "Generative AI Certificate"
        )
    )

    # ==================================================
    # GENERATE BUTTON
    # ==================================================

    if st.button(
        "📄 GENERATE ATS RESUME",
        use_container_width=True
    ):

        st.session_state["generated_resume"] = {

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
            "certifications": certifications
        }

        st.session_state["resume_generated"] = True

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

        st.subheader("👀 Resume Preview")

        st.markdown(
            f"""
            # {resume["name"]}

            **{resume["email"]} | {resume["phone"]} | 
            {resume["location"]}**

            {resume["linkedin"]} | {resume["github"]}

            ---

            ## PROFESSIONAL SUMMARY

            {resume["summary"]}

            ## TECHNICAL SKILLS

            {resume["skills"]}

            ## WORK EXPERIENCE

            {resume["experience"]}

            ## PROJECTS

            {resume["projects"]}

            ## EDUCATION

            {resume["education"]}

            ## CERTIFICATIONS

            {resume["certifications"]}
            """
        )