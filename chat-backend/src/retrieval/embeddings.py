from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.dimension = self.model.get_sentence_embedding_dimension()


    def embed_texts(self, texts: list[str]):
        if not texts:
            return np.empty((0, self.dimension), dtype=np.float32)
        
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        embeddings = np.asarray(embeddings, dtype=np.float32)

        if embeddings.ndim == 1:
            embeddings = np.expand_dims(embeddings, axis=0)
            
        return embeddings