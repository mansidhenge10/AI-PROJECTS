
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from app.config import OLLAMA_MODEL, OLLAMA_BASE_URL


class AnswerGenerator:
    def __init__(self):
        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0.2,
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are an AI Engineering Assistant.

            Answer the developer's question using only the
            engineering context provided below.

            Rules:
            1. Give clear and technically accurate answers.
            2. Explain complex concepts in simple language.
            3. If the context does not contain the answer,
               clearly say that the available documents do not
               provide enough information.
            4. Do not invent technical details.
            5. Mention relevant source filenames when possible.

            Engineering Context:
            {context}

            Developer Question:
            {question}

            Answer:
            """
        )

        self.chain = self.prompt | self.llm

    def generate_answer(self, question, context):
        if not context:
            return (
                "I could not find relevant information in the "
                "available engineering documents."
            )

        response = self.chain.invoke(
            {
                "question": question,
                "context": context,
            }
        )

        return response.content
