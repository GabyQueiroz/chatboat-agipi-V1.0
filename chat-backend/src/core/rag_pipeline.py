
from src.retrieval.embeddings import Embedder
from src.retrieval.vector_db import VectorStore
from src.llm.ollama_client import OllamaClient
import numpy as np

class RAGPipeline:
    def __init__(self, embedder: Embedder, vector_store: VectorStore, llm: OllamaClient):
        self.embedder = embedder
        self.vector_store = vector_store
        self.llm = llm


    def ask(self, user_question: str) -> dict:
        question_vector = self.embedder.embed_texts([user_question])
        relevant_docs = self.vector_store.search(question_vector, top_k=3)

        context_text = "\n\n".join([doc["text"] for doc in relevant_docs])
        sources = list(set([doc["source"] for doc in relevant_docs]))
        prompt = f"""Você é um assistente da útil, amigável e detalhista.Você faz parte da Agência de Inovação e Propriedade Intelectual (AGIPI) da Universidade Estadual de Ponta Grossa (UEPG). Sua função é fornecer informações sobre o contexto de Inovação e Propriedade Intelectual, tirando o máximo de detalhes relevantes possível do contexto, dada a pergunta do usuário.
Responda à pergunta do usuário baseando-se APENAS no contexto abaixo. Se a resposta não estiver no contexto, diga que não sabe. Evite mencionar o contexto quando você souber a resposta.

Contexto:
{context_text}

Pergunta: {user_question}
Resposta:"""
        
        answer = self.llm.generate_response(prompt)

        return {
            "answer": answer,
            "sources": sources
        }