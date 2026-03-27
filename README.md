# Chatbot RAG — AGIPI/UEPG

Chatbot com pipeline RAG (Retrieval-Augmented Generation) usando FastAPI no backend e React + Vite no frontend.



## Pré-requisitos

- Python 3.10+
- Node.js 18+
- [Ollama](https://ollama.com) instalado e rodando localmente (ou outra LLM — veja a seção abaixo)

---

## Backend

### 1. Estrutura esperada

```
backend/
├── src/
│   ├── api/
│   │   └── main.py
│   ├── core/
│   │   └── rag_pipeline.py
│   ├── llm/
│   │   ├── llm_client.py       # Interface abstrata
│   │   └── ollama_client.py    # Implementação Ollama
│   ├── retrieval/
│   │   ├── embeddings.py
│   │   └── vector_db.py
│   └── ingestion/
│       └── chunker.py
├── data/
│   └── raw/                    # Base de dados (PDFs)
├── requirements.txt
└── pyproject.toml
```

### 2. Criar e ativar ambiente virtual

```bash
cd chat-backend
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# ou
.venv\Scripts\activate           # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Adicionar documentos

Coloque os arquivos PDF a serem indexados dentro de `data/raw/`. O sistema gera os embeddings e o índice FAISS automaticamente na primeira execução.

### 5. Rodar o servidor

```bash
fastapi dev
```

O servidor ficará disponível em `http://localhost:8000`.

> **Nota:** Na primeira execução, o processamento dos documentos e geração de embeddings pode levar alguns minutos. As execuções seguintes usam o índice em cache em `data/index/`.

---

## Frontend

### 1. Instalar dependências

```bash
cd chat-frontend
npm install
```

### 2. Rodar em modo de desenvolvimento

```bash
npm run dev
```

A interface ficará disponível em `http://localhost:5173`.

> O frontend espera o backend em `http://localhost:8000`. Se necessário, ajuste a URL base no código do frontend.

---

## Adicionando uma nova LLM

O backend usa o padrão de interface abstrata (`LLMClient`) para desacoplar a lógica do pipeline da LLM utilizada. Para integrar uma nova LLM, siga os passos:

### 1. Crie um novo arquivo em `src/llm/`

```python
# src/llm/minha_llm_client.py

from src.llm.llm_client import LLMClient

class MinhaLLMClient(LLMClient):
    def __init__(self, api_key: str, model: str = "nome-do-modelo"):
        self.api_key = api_key
        self.model = model

    def generate_response(self, prompt: str) -> str:
        # Implemente aqui a chamada à API da sua LLM
        # Deve retornar a resposta como string
        ...
        return resposta
```

A única obrigação é implementar o método `generate_response(prompt: str) -> str`.

### 2. Use o novo cliente em `main.py`

Substitua a instância do `OllamaClient`:

```python
# Antes
from src.llm.ollama_client import OllamaClient
llm = OllamaClient(model="llama3")

# Depois
from src.llm.minha_llm_client import MinhaLLMClient
llm = MinhaLLMClient(api_key="sua-chave", model="nome-do-modelo")
```

O `RAGPipeline` aceita qualquer objeto que implemente `LLMClient`, sem nenhuma outra alteração necessária.

### Exemplos de integrações comuns

| LLM | Biblioteca sugerida |
|---|---|
| OpenAI / GPT | `openai` |
| Google Gemini | `google-generativeai` |
| Anthropic Claude | `anthropic` |
| Groq | `groq` |
| Qualquer OpenAI-compatible | `openai` com `base_url` customizada |

Instale a biblioteca correspondente e adicione-a ao `requirements.txt`.

---

## Build de produção (frontend)

```bash
cd frontend
npm run build
```

Os arquivos estáticos serão gerados em `frontend/dist/` e podem ser servidos por qualquer servidor web estático ou pelo próprio FastAPI com `StaticFiles`.