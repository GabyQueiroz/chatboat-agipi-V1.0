import requests

from src.llm.llm_client import LLMClient


class OllamaClient(LLMClient):
    def __init__(self, base_url: str = "http://127.0.0.1:11434", model: str = "phi3:mini", timeout: int = 20):
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.timeout = timeout

    def is_available(self) -> bool:
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=3)
            response.raise_for_status()
            models = response.json().get("models", [])
            return any(model.get("name", "").split(":")[0] == self.model.split(":")[0] for model in models)
        except requests.RequestException:
            return False

    def generate_response(self, prompt: str) -> str:
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.1,
            "options": {
                "num_predict": 220,
                "num_ctx": 2048,
            },
        }
        try:
            response = requests.post(url, json=payload, timeout=self.timeout)
            response.raise_for_status()
            return response.json()["response"].strip()
        except requests.exceptions.ConnectionError as exc:
            raise RuntimeError(
                f"Nao foi possivel conectar ao Ollama em {self.base_url}. "
                f"Confirme se o servico esta em execucao e se o modelo '{self.model}' esta disponivel."
            ) from exc
        except requests.exceptions.Timeout as exc:
            raise RuntimeError(
                f"O Ollama demorou mais de {self.timeout}s para responder com o modelo '{self.model}'."
            ) from exc
        except requests.exceptions.HTTPError as exc:
            details = ""
            try:
                details = response.json().get("error", "")
            except ValueError:
                details = response.text
            raise RuntimeError(
                f"Ollama retornou erro ao usar o modelo '{self.model}'. {details}".strip()
            ) from exc
