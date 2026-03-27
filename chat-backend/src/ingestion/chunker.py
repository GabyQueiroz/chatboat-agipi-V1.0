import os
import pymupdf.layout
import pymupdf4llm
import pickle
from typing import List, Dict

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Divide o texto em janelas deslizantes."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def save_documents(documents: List[Dict[str, str]], cache_path: str = "data/processed/documents_cache.pkl") -> None:
    """Salva os documentos processados em um arquivo de cache."""
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, 'wb') as f:
        pickle.dump(documents, f)
    print(f"[CHUNKER] Documentos salvos em cache: {cache_path}")


def load_documents(cache_path: str = "data/processed/documents_cache.pkl") -> List[Dict[str, str]] | None:
    """Carrega os documentos do cache se existirem."""
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'rb') as f:
                documents = pickle.load(f)
            print(f"[CHUNKER] Documentos carregados do cache: {cache_path}")
            return documents
        except Exception as e:
            print(f"[CHUNKER] Erro ao carregar cache: {e}")
            return None
    return None


def process_documents(docs_path: str) -> List[Dict[str, str]]:
    """Lê os arquivos e retorna uma lista de dicionários com metadados."""
    documents = []
    for root, dirs, files in os.walk(docs_path):
        if len(files) > 0:
            for file in files:
                filename, file_ext = os.path.splitext(file)
                if file_ext.lower() in ['.txt', '.pdf']:
                    try:
                        filepath = os.path.abspath(os.path.join(root, file))
                        
                        # Workaround para o limite MAX_PATH no Windows
                        if os.name == 'nt' and not filepath.startswith('\\\\?\\'):
                            filepath = '\\\\?\\' + filepath

                        print(f"[CHUNKER] Processing file: {filepath}")
                        content = pymupdf4llm.to_text(filepath)
                        chunks = chunk_text(content)
                        num_chunks = 0
                        for i, chunk in enumerate(chunks):
                            documents.append({
                                "id": f"{filename}_chunk_{i}",
                                "source": filepath,
                                "text": chunk
                            })
                            num_chunks += 1
                        print(f"[CHUNKER] Extracted {num_chunks} chunks from {file}")
                    except FileNotFoundError:
                        print(f"[CHUNKER] Arquivo não encontrado: {file_ext}")
                        continue

    return documents

if __name__ == "__main__":
    docs_path = "data/raw"

    processed_docs = process_documents(docs_path)
    save_documents(processed_docs)
    print(f"[CHUNKER - MAIN] Processed {len(processed_docs)} document chunks.:\n")