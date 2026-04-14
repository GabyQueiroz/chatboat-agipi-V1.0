import os
import time
import asyncio
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from src.core.rag_pipeline import RAGPipeline
from src.ingestion.chunker import (
    build_source_manifest,
    load_documents,
    load_source_manifest,
    process_documents,
    save_documents,
    save_source_manifest,
)
from src.llm.ollama_client import OllamaClient
from src.llm.groq_client import GroqClient
from src.retrieval.embeddings import Embedder
from src.retrieval.vector_db import VectorStore
from src.api.store import save_session_log

load_dotenv()

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
INDEX_CACHE_PATH = DATA_DIR / "index" / "faiss_index.bin"
METADATA_CACHE_PATH = DATA_DIR / "processed" / "faiss_metadata.pkl"
DOCS_CACHE_PATH = DATA_DIR / "processed" / "documents_cache.pkl"
MANIFEST_CACHE_PATH = DATA_DIR / "processed" / "source_manifest.pkl"

DEFAULT_RAW_DIRS = [
    str(ROOT_DIR / "data" / "raw"),
    os.getenv('RAW_SOURCE_DIRS') or r"C:\Users\gabri\OneDrive\Documentos\UEPG\IA_AGIPI\DOCUMENTOS EPITEC PROF. LIVIO-20260409T232820Z-3-001",
]
DEFAULT_FAQ_PATH = os.getenv('FAQ_XLSX_PATH') or r"C:\Users\gabri\OneDrive\Documentos\UEPG\IA_AGIPI\faq_agipi_ageuni_documentos.xlsx"

RESPONSE_MODE = os.getenv("RAG_RESPONSE_MODE", "extractive").lower()
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
# OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434")
# OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3:mini")
# OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "20"))
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-8b-8192")
GROQ_TIMEOUT = int(os.getenv("GROQ_TIMEOUT", "20"))

FAQ_XLSX_PATH = os.getenv("FAQ_XLSX_PATH", DEFAULT_FAQ_PATH)
RAW_SOURCE_DIRS = [
    item.strip()
    for item in os.getenv("RAW_SOURCE_DIRS", ",".join(DEFAULT_RAW_DIRS)).split(",")
    if item.strip()
]
ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    ).split(",")
    if origin.strip()
]


class QuestionRequest(BaseModel):
    question: str = Field(min_length=2, max_length=1000)
    history: list[dict[str, str]] = Field(default_factory=list)
    user_name: str
    session_id: str


class AppState:
    def __init__(self) -> None:
        self.embedder = Embedder(model_name=EMBED_MODEL)
        self.vector_store = VectorStore(dimension=self.embedder.dimension)
        self.llm = OllamaClient(
            model=GROQ_MODEL,
            timeout=GROQ_TIMEOUT,
        )
        self.pipeline = RAGPipeline(
            embedder=self.embedder,
            vector_store=self.vector_store,
            llm=self.llm,
            response_mode=RESPONSE_MODE,
        )
        self.index_ready = False
        self.last_index_build: dict[str, Any] = {}

    def initialize(self) -> None:
        print("[BOOT] Inicializando sistema...")
        print(f"[BOOT] FAQ: {FAQ_XLSX_PATH}")
        print(f"[BOOT] Pastas fonte: {RAW_SOURCE_DIRS}")

        manifest = build_source_manifest(RAW_SOURCE_DIRS, FAQ_XLSX_PATH)
        cached_manifest = load_source_manifest(str(MANIFEST_CACHE_PATH))
        cache_is_valid = manifest == cached_manifest and self.vector_store.load(
            str(INDEX_CACHE_PATH),
            str(METADATA_CACHE_PATH),
        )

        if not cache_is_valid:
            print("[BOOT] Cache ausente ou desatualizado. Reprocessando base documental...")
            docs = load_documents(str(DOCS_CACHE_PATH))
            if docs is None or manifest != cached_manifest:
                docs = process_documents(RAW_SOURCE_DIRS, FAQ_XLSX_PATH)
                save_documents(docs, str(DOCS_CACHE_PATH))
                save_source_manifest(manifest, str(MANIFEST_CACHE_PATH))

            embeddings = self.embedder.embed_texts([doc["text"] for doc in docs])
            self.vector_store = VectorStore(dimension=self.embedder.dimension)
            self.vector_store.add_documents(embeddings, docs)
            self.vector_store.save(str(INDEX_CACHE_PATH), str(METADATA_CACHE_PATH))
            self.pipeline = RAGPipeline(
                embedder=self.embedder,
                vector_store=self.vector_store,
                llm=self.llm,
                response_mode=RESPONSE_MODE,
            )

        self.index_ready = True
        documents = self.vector_store.metadata
        self.last_index_build = {
            "documents": self.vector_store.document_count,
            "sources": len(manifest),
            "response_mode": RESPONSE_MODE,
            "llm_model": GROQ_MODEL,
            "faq_entries": sum(1 for doc in documents if doc.get("doc_type") == "faq"),
            "document_chunks": sum(1 for doc in documents if doc.get("doc_type") == "document"),
        }
        print(
            f"[BOOT] Sistema pronto com {self.vector_store.document_count} chunks "
            f"({self.last_index_build['faq_entries']} FAQ + {self.last_index_build['document_chunks']} documentos)."
        )

    def health(self) -> dict[str, Any]:
        return {
            "status": "ok" if self.index_ready else "starting",
            "response_mode": RESPONSE_MODE,
            "llm": {
                "provider": "groq",
                "model": GROQ_MODEL,
                "available": self.llm.is_available(),
            },
            "index": {
                "ready": self.index_ready,
                "documents": self.vector_store.document_count,
                "sources": self.last_index_build.get("sources", 0),
                "faq_entries": self.last_index_build.get("faq_entries", 0),
                "document_chunks": self.last_index_build.get("document_chunks", 0),
            },
        }


state = AppState()
state.initialize()

app = FastAPI(title="Chatbot API", version="0.3.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> dict[str, Any]:
    return {
        "name": "Chatbot API",
        "version": app.version,
        "health": "/health",
        "chat": "/chat",
    }


@app.get("/health")
async def health() -> dict[str, Any]:
    return state.health()


@app.post("/chat")
async def chat_endpoint(request: QuestionRequest) -> dict[str, Any]:
    started_at = time.perf_counter()
    request_ts = datetime.now(timezone.utc).isoformat()

    user_name = request.user_name
    session_id = request.session_id

    try:
        print(f"[CHAT] Pergunta recebida: {request.question}")
        response = await asyncio.to_thread(state.pipeline.ask, request.question, request.history)
        elapsed = time.perf_counter() - started_at
        print(f"[CHAT] Resposta gerada em {elapsed:.2f}s")

        response_ts = datetime.now(timezone.utc).isoformat()
        await asyncio.to_thread(
            save_session_log,
            session_id=session_id,
            user_name=user_name,
            request_ts=request_ts,
            question=request.question,
            response_ts=response_ts,
            response=response,
            error=None
        )

        return response
    except Exception as exc:
        elapsed = time.perf_counter() - started_at
        response_ts = datetime.now(timezone.utc).isoformat()
        error_detail = traceback.format_exc()
        print(f"[CHAT] Falha apos {elapsed:.2f}s: {exc}")

        await asyncio.to_thread(
            save_session_log,
            session_id=session_id,
            user_name=user_name,
            request_ts=request_ts,
            question=request.question,
            response_ts=response_ts,
            response=None,
            error=error_detail
        )

        raise HTTPException(status_code=500, detail=str(exc))
