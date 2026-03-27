import faiss
import numpy as np
import pickle
import os

class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []
        self.dimension = dimension

    def add_documents(self, embeddings: np.ndarray, metadata_list: list[dict]):
        if embeddings.size == 0:
            print("Aviso: Nenhum embedding recebido para adicionar ao índice.")
            return

        if embeddings.ndim == 1:
            embeddings = np.expand_dims(embeddings, axis=0)

        self.index.add(embeddings)
        self.metadata.extend(metadata_list)

    
    def search(self, query_embedding: np.ndarray, top_k: int = 3):
        if query_embedding.ndim == 1:
            query_embedding = np.expand_dims(query_embedding, axis=0)

        distances, indices = self.index.search(query_embedding, top_k)
        
        results = []
        for i in indices[0]:
            if i != -1 and i < len(self.metadata):
                results.append(self.metadata[i])
        return results
    
    def save(self, index_path: str, metadata_path: str):
        """Salva o índice FAISS e os metadados em arquivos."""
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        faiss.write_index(self.index, index_path)
        with open(metadata_path, 'wb') as f:
            pickle.dump(self.metadata, f)
        print(f"[VECTORSTORE] Índice salvo em {index_path}")
        print(f"[VECTORSTORE] Metadados salvos em {metadata_path}")
    
    def load(self, index_path: str, metadata_path: str) -> bool:
        """Carrega o índice FAISS e os metadados de arquivos. Retorna True se bem-sucedido."""
        if os.path.exists(index_path) and os.path.exists(metadata_path):
            try:
                self.index = faiss.read_index(index_path)
                with open(metadata_path, 'rb') as f:
                    self.metadata = pickle.load(f)
                print(f"[VECTORSTORE] Índice carregado de {index_path}")
                print(f"[VECTORSTORE] Metadados carregados de {metadata_path}")
                return True
            except Exception as e:
                print(f"[VECTORSTORE] Erro ao carregar índice: {e}")
                return False
        return False