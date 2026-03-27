import requests
from src.llm.llm_client import LLMClient

class OllamaClient(LLMClient):
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3"):
        self.base_url = base_url
        self.model = model

    def generate_response(self, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.1
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"]