import os
import requests

from src.llm.llm_client import LLMClient


class GroqClient(LLMClient):
    def __init__(self, api_key: str = None, model: str = "llama3-8b-8192", timeout: int = 20):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1"
        self.model = model
        self.timeout = timeout

        if not self.api_key:
            raise ValueError("GROQ_API_KEY não foi configurada. Obtenha uma em console.groq.com")

    def is_available(self) -> bool:
        if not self.api_key:
            return False
            
        url = f"{self.base_url}/models"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            return True
        except requests.RequestException:
            return False

    def generate_response(self, prompt: str) -> str:
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.1,
            "max_tokens": 1024,
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
            
        except requests.exceptions.ConnectionError as exc:
            raise RuntimeError(
                "Não foi possível conectar à API do Groq. Verifique sua conexão com a internet."
            ) from exc
        except requests.exceptions.Timeout as exc:
            raise RuntimeError(
                f"A API do Groq demorou mais de {self.timeout}s para responder com o modelo '{self.model}'."
            ) from exc
        except requests.exceptions.HTTPError as exc:
            details = ""
            try:
                details = response.json().get("error", {}).get("message", "")
            except ValueError:
                details = response.text
            raise RuntimeError(
                f"A API do Groq retornou erro ao usar o modelo '{self.model}'. {details}".strip()
            ) from exc