# Assistente AGIPI

Aplicação RAG com backend em FastAPI e frontend em React + Vite.

## Estrutura

```text
chat-backend/
chat-frontend/
```

## Backend

```powershell
cd chat-backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m uvicorn src.api.main:app --reload
```

Para reconstruir totalmente o indice com FAQ + documentos externos:

```powershell
cd chat-backend
.venv\Scripts\activate
python rebuild_index.py
```

Variaveis uteis:

- `RAG_RESPONSE_MODE=extractive` para resposta mais rapida
- `RAG_RESPONSE_MODE=hybrid` para usar LLM quando ela estiver disponivel
- `OLLAMA_MODEL=phi3:mini` para um modelo leve no Windows
- `FAQ_XLSX_PATH` para apontar para a planilha FAQ
- `RAW_SOURCE_DIRS` para apontar para uma ou mais pastas documentais

Ao subir, o backend valida se `data/raw` corresponde ao indice em cache. Se não corresponder, ele reprocessa automaticamente.

## Frontend

```powershell
cd chat-frontend
npm install
npm run dev
```

Se quiser apontar para outra API:

```powershell
$env:VITE_API_BASE_URL="http://127.0.0.1:8000"
npm run dev
```

## Publicação

- backend: configure as variaveis do arquivo `chat-backend/.env.example`
- frontend: configure `VITE_API_BASE_URL` com a URL publica da API
- monitore o backend por `GET /health`
