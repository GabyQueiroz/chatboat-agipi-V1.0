from pathlib import Path

from src.ingestion.chunker import (
    build_source_manifest,
    process_documents,
    save_documents,
    save_source_manifest,
)
from src.retrieval.embeddings import Embedder
from src.retrieval.vector_db import VectorStore


ROOT_DIR = Path(__file__).resolve().parent
DATA_DIR = ROOT_DIR / "data"
INDEX_CACHE_PATH = DATA_DIR / "index" / "faiss_index.bin"
METADATA_CACHE_PATH = DATA_DIR / "processed" / "faiss_metadata.pkl"
DOCS_CACHE_PATH = DATA_DIR / "processed" / "documents_cache.pkl"
MANIFEST_CACHE_PATH = DATA_DIR / "processed" / "source_manifest.pkl"

RAW_SOURCE_DIRS = [
    str(ROOT_DIR / "data" / "raw"),
    r"C:\Users\gabri\OneDrive\Documentos\UEPG\IA_AGIPI\DOCUMENTOS EPITEC PROF. LIVIO-20260409T232820Z-3-001",
]
FAQ_XLSX_PATH = r"C:\Users\gabri\OneDrive\Documentos\UEPG\IA_AGIPI\faq_agipi_ageuni_documentos.xlsx"


def main() -> None:
    print("[REBUILD] Montando manifest...")
    manifest = build_source_manifest(RAW_SOURCE_DIRS, FAQ_XLSX_PATH)
    print(f"[REBUILD] Itens de origem detectados: {len(manifest)}")

    print("[REBUILD] Processando documentos...")
    documents = process_documents(RAW_SOURCE_DIRS, FAQ_XLSX_PATH)
    print(f"[REBUILD] Chunks gerados: {len(documents)}")

    print("[REBUILD] Salvando caches de documentos...")
    save_documents(documents, str(DOCS_CACHE_PATH))
    save_source_manifest(manifest, str(MANIFEST_CACHE_PATH))

    print("[REBUILD] Gerando embeddings...")
    embedder = Embedder()
    embeddings = embedder.embed_texts([doc["text"] for doc in documents])

    print("[REBUILD] Construindo indice vetorial...")
    vector_store = VectorStore(dimension=embedder.dimension)
    vector_store.add_documents(embeddings, documents)
    vector_store.save(str(INDEX_CACHE_PATH), str(METADATA_CACHE_PATH))

    faq_count = sum(1 for doc in documents if doc.get("doc_type") == "faq")
    doc_count = sum(1 for doc in documents if doc.get("doc_type") == "document")
    print(
        "[REBUILD] Finalizado com "
        f"{faq_count} entradas de FAQ e {doc_count} chunks documentais."
    )


if __name__ == "__main__":
    main()
