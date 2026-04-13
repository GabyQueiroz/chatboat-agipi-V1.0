import os
import pickle

import faiss
import numpy as np


class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)
        self.metadata: list[dict] = []

    @property
    def document_count(self) -> int:
        return len(self.metadata)

    def add_documents(self, embeddings: np.ndarray, metadata_list: list[dict]) -> None:
        if embeddings.size == 0:
            print("[VECTORSTORE] Nenhum embedding recebido para indexacao.")
            return

        if embeddings.ndim == 1:
            embeddings = np.expand_dims(embeddings, axis=0)

        embeddings = np.asarray(embeddings, dtype=np.float32)
        faiss.normalize_L2(embeddings)
        self.index.add(embeddings)
        self.metadata = list(metadata_list)

    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> list[dict]:
        if self.index.ntotal == 0:
            return []

        if query_embedding.ndim == 1:
            query_embedding = np.expand_dims(query_embedding, axis=0)

        query_embedding = np.asarray(query_embedding, dtype=np.float32)
        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, top_k)
        results = []

        for score, index in zip(scores[0], indices[0]):
            if index == -1 or index >= len(self.metadata):
                continue

            document = dict(self.metadata[index])
            document["score"] = float(score)
            results.append(document)

        return results

    def save(self, index_path: str, metadata_path: str) -> None:
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        faiss.write_index(self.index, index_path)
        with open(metadata_path, "wb") as file:
            pickle.dump(self.metadata, file)
        print(f"[VECTORSTORE] Indice salvo em {index_path}")
        print(f"[VECTORSTORE] Metadados salvos em {metadata_path}")

    def load(self, index_path: str, metadata_path: str) -> bool:
        if not os.path.exists(index_path) or not os.path.exists(metadata_path):
            return False

        try:
            self.index = faiss.read_index(index_path)
            with open(metadata_path, "rb") as file:
                self.metadata = pickle.load(file)
            print(f"[VECTORSTORE] Indice carregado de {index_path}")
            print(f"[VECTORSTORE] Metadados carregados de {metadata_path}")
            return True
        except Exception as exc:
            print(f"[VECTORSTORE] Erro ao carregar indice: {exc}")
            self.index = faiss.IndexFlatIP(self.dimension)
            self.metadata = []
            return False
