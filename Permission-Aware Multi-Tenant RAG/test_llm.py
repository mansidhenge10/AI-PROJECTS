from src.rag.llm import get_llm


llm = get_llm()

response = llm.invoke(
    "Explain what RAG means in one simple sentence."
)

print(response.content)