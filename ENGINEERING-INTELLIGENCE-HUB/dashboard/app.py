
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"

st.set_page_config(
    page_title="Engineering Intelligence Hub",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: #0b1120;
    color: #f8fafc;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3 {
    color: #e2e8f0;
}
.stButton button {
    background: #0891b2;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Engineering Intelligence Hub")
st.caption("Your AI-powered engineering knowledge assistant")

st.divider()

if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar: document upload
with st.sidebar:
    st.header("📁 Knowledge Base")
    st.write("Upload engineering documents to build your knowledge base.")

    uploaded_file = st.file_uploader(
        "Upload a document",
        type=["pdf", "txt", "md"]
    )

    if st.button("Upload and Index", use_container_width=True):
        if uploaded_file is None:
            st.warning("Please select a document first.")
        else:
            try:
                with st.spinner("Processing document..."):
                    response = requests.post(
                        f"{API_URL}/upload",
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                uploaded_file.type
                            )
                        },
                        timeout=180
                    )

                if response.ok:
                    result = response.json()
                    st.success("Document indexed successfully!")
                    st.write("Filename:", result["filename"])
                    st.write("Chunks:", result["total_chunks"])
                else:
                    st.error(response.text)

            except requests.RequestException as error:
                st.error(f"Backend connection failed: {error}")

    st.divider()
    st.caption("Supported formats: PDF, TXT, Markdown")

# Main area: AI question and answer
st.subheader("💬 Ask Engineering Assistant")

question = st.text_area(
    "Enter your engineering question",
    placeholder="Example: Explain the architecture of this project...",
    height=120
)

top_k = st.slider(
    "Number of relevant chunks",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Generate Answer", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Searching knowledge and generating answer..."):
                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "question": question,
                        "top_k": top_k
                    },
                    timeout=180
                )

            if response.ok:
                result = response.json()

                st.session_state.history.append({
                    "question": question,
                    "answer": result["answer"],
                    "sources": result["sources"]
                })

            else:
                st.error(response.text)

        except requests.RequestException as error:
            st.error(f"Backend connection failed: {error}")

# Display latest answer
if st.session_state.history:
    latest = st.session_state.history[-1]

    st.divider()
    st.subheader("🤖 AI Response")
    st.markdown(latest["answer"])

    st.subheader("📚 Retrieved Sources")

    if latest["sources"]:
        for source in latest["sources"]:
            st.write(f"📄 {source}")
    else:
        st.info("No sources found.")

# Conversation history
if st.session_state.history:
    st.divider()
    st.subheader("🕘 Conversation History")

    for index, item in enumerate(reversed(st.session_state.history), 1):
        with st.expander(f"Question {index}: {item['question']}"):
            st.write(item["answer"])
            st.write("Sources:", ", ".join(item["sources"]))
