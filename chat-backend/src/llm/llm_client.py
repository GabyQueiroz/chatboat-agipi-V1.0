from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> list[str, int]:
        pass

    def is_available(self) -> bool:
        return True
