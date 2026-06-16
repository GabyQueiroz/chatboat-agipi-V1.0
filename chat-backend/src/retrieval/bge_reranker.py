import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

class BGEReranker:
    def __init__(self, model_name: str = "BAAI/bge-reranker-v2-m3"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(self.device)
        self.model.eval()

    def compute_scores(self, pairs: list[list[str]]) -> list[float]:
        if not pairs:
            return []
        
        with torch.no_grad():
            inputs = self.tokenizer(
                pairs, 
                padding=True, 
                truncation=True, 
                return_tensors="pt", 
                max_length=512
            ).to(self.device)

            scores = self.model(**inputs).logits.view(-1).float()
            probabilities = torch.sigmoid(scores).tolist()
            return probabilities
