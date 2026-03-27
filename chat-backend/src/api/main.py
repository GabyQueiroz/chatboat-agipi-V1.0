from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.core.rag_pipeline import RAGPipeline
from src.retrieval.embeddings import Embedder
from src.retrieval.vector_db import VectorStore
from src.llm.ollama_client import OllamaClient
from src.ingestion.chunker import process_documents, load_documents, save_documents

app = FastAPI(title="Chatbot API")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicialização global
embedder = Embedder()
vector_store = VectorStore(dimension=embedder.dimension)
llm = OllamaClient(model="llama3")

INDEX_CACHE_PATH = "data/index/faiss_index.bin"
METADATA_CACHE_PATH = "data/processed/faiss_metadata.pkl"
DOCS_CACHE_PATH = "data/processed/documents_cache.pkl"

print("Inicializando sistema...")

# Tenta carregar índice do cache
if not vector_store.load(INDEX_CACHE_PATH, METADATA_CACHE_PATH):
    print("Cache não encontrado. Processando documentos...")
    
    # Tenta carregar documentos processados do cache
    docs = load_documents(DOCS_CACHE_PATH)
    if docs is None:
        docs = process_documents("data/raw")
        save_documents(docs, DOCS_CACHE_PATH)
    
    # Gera embeddings e constrói índice
    print("Gerando embeddings...")
    embeddings = embedder.embed_texts([doc["text"] for doc in docs])
    vector_store.add_documents(embeddings, docs)
    
    # Salva o índice para futuras execuções
    vector_store.save(INDEX_CACHE_PATH, METADATA_CACHE_PATH)

print("Pronto!")

pipeline = RAGPipeline(embedder, vector_store, llm)

class QuestionRequest(BaseModel):
    question: str


@app.post("/chat")
async def chat_endpoint(request: QuestionRequest):
    try:
        response = pipeline.ask(request.question)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
