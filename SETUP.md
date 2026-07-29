# Guia de Ambiente — Assistente AGIPI v1.0

Documento de referência para configuração de ambiente de **desenvolvimento** e **produção** do sistema RAG Assistente AGIPI, composto por backend FastAPI, frontend React/Vite, banco de dados PostgreSQL e armazenamento de objetos compatível com S3.

---

## Índice

1. [Visão geral da arquitetura](#1-visão-geral-da-arquitetura)
2. [Pré-requisitos](#2-pré-requisitos)
3. [Ambiente de desenvolvimento](#3-ambiente-de-desenvolvimento)
4. [Referência completa de variáveis de ambiente](#4-referência-completa-de-variáveis-de-ambiente)
5. [Gestão da base de conhecimento](#5-gestão-da-base-de-conhecimento)
6. [Ambiente de produção (Railway)](#6-ambiente-de-produção-railway)
7. [Operação e manutenção](#7-operação-e-manutenção)

---

## 1. Visão geral da arquitetura

O backend, no startup, baixa os documentos do bucket, compara o manifest com o cache e - se houver mudança - reconstrói os embeddings e o índice FAISS. O índice é persistido em volume Docker entre reinicializações.

Para desenvolvimento local, o bucket é implementado através do MinIO, e pode ser gerenciado pela interface web na porta padrão 9001.

---

## 2. Pré-requisitos

### Desenvolvimento local

| Ferramenta | Versão mínima | Instalação |
|---|---|---|
| Docker Desktop | 24.x | https://docs.docker.com/get-docker/ |
| Docker Compose | v2 (embutido no Docker Desktop) | Incluído no Docker Desktop |
| Git | 2.x | https://git-scm.com/ |
| Python | 3.11 | https://www.python.org/ (opcional, apenas para rodar fora do Docker) |
| Node.js | 20.x | https://nodejs.org/ (opcional, apenas para rodar fora do Docker) |

> **PostgreSQL não precisa ser instalado localmente.** O serviço `postgres` no Docker Compose já provisiona uma instância isolada. Instale o PostgreSQL localmente apenas se precisar usar ferramentas de cliente como DBeaver ou psql diretamente na sua máquina.

#### Verificação pós-instalação

```bash
docker --version          # Docker version 24.x.x
docker compose version    # Docker Compose version v2.x.x
git --version             # git version 2.x.x
```

### Produção (Railway)

- Conta na plataforma [Railway](https://railway.app/)
- Chave de API do [Groq](https://console.groq.com/) para o LLM
- Acesso ao repositório Git (GitHub, GitLab ou Bitbucket)

---


## 3. Ambiente de desenvolvimento

### 3.1 Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```

### 3.2 Configurar variáveis de ambiente

Copie o arquivo de exemplo e preencha os valores:

```bash
cp chat-backend/.env.example chat-backend/.env
```

Edite `chat-backend/.env` com as credenciais necessárias. Veja a [seção 5](#5-referência-completa-de-variáveis-de-ambiente) para descrição detalhada de cada variável.

Os valores mínimos para o ambiente de desenvolvimento funcionar são:

```bash
# Credenciais do banco de dados
POSTGRES_USER=postgres
POSTGRES_PASSWORD=uma_senha_segura
POSTGRES_DB=ia_agipi

# Credenciais do MinIO a serem criadas
MINIO_ROOT_USER=minio_admin
MINIO_ROOT_PASSWORD=uma_senha_com_8_ou_mais_caracteres

# Nome do bucket (deve ser igual ao criado pelo minio-init)
S3_BUCKET_NAME=rag-agipi

# Chave do LLM
GROQ_API_KEY=sua_chave_groq
```

> **Atenção:** O MinIO rejeita senhas com menos de 8 caracteres e silenciosamente usa as credenciais padrão `minioadmin:minioadmin`, causando `Access Denied` no `minio-init`. Use sempre senhas com 8+ caracteres.

### 3.3 Subir o ambiente

```bash
docker compose --env-file ./chat-backend/.env up --build
```

Na primeira execução, o Docker irá:
1. Construir as imagens do backend e frontend
2. Baixar as imagens do PostgreSQL e MinIO
3. Criar o banco de dados e aplicar as migrações via Alembic
4. Criar o bucket no MinIO com a estrutura de prefixos (`raw/`, `md/`, `faq/`, `index/`)
5. Iniciar o backend, que no startup verifica o cache e reconstrói o índice FAISS se necessário

A geração de embeddings na **primeira inicialização a frio** (sem cache) pode levar vários minutos dependendo do volume de documentos. Os logs do backend indicam o progresso:

```
[BOOT] Gerando embeddings para N chunks... (pode levar alguns minutos)
[BOOT] Embeddings concluídos.
[BOOT] Índice FAISS salvo.
[BOOT] Sistema pronto com N chunks (X FAQ + Y documentos).
```

O sistema está pronto quando a linha "Sistema pronto" aparecer nos logs.

### 3.4 Verificar o ambiente

```bash
# Saúde do backend
curl http://localhost:8000/health

# Frontend
# Acesse http://localhost:5173 no navegador

# Console web do MinIO
# Acesse http://localhost:9001 no navegador
# Login: valores de MINIO_ROOT_USER e MINIO_ROOT_PASSWORD do .env
```

### 3.5 Comandos úteis

```bash
# Subir em background
docker compose --env-file ./chat-backend/.env up -d

# Ver logs em tempo real de um serviço específico
docker compose --env-file ./chat-backend/.env logs -f backend

# Parar todos os serviços
docker compose --env-file ./chat-backend/.env down

# Parar e remover volumes (limpa banco e bucket — use com cuidado)
docker compose --env-file ./chat-backend/.env down -v

# Reconstruir apenas o backend após mudanças no código
docker compose --env-file ./chat-backend/.env up --build backend

# Verificar se variáveis foram resolvidas corretamente antes de subir
docker compose --env-file ./chat-backend/.env config
```

### 3.6 Rodar fora do Docker (desenvolvimento direto)

Se preferir rodar o backend e frontend diretamente na máquina para desenvolvimento com hot-reload mais ágil, mantenha apenas o PostgreSQL e MinIO no Docker:

```bash
# Sobe apenas a infraestrutura
docker compose --env-file ./chat-backend/.env up -d postgres minio minio-init
```

**Backend:**

```bash
cd chat-backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python -m uvicorn src.api.main:app --reload
```

**Frontend:**

```bash
cd chat-frontend
npm install
npm run dev
```

---

## 4. Referência completa de variáveis de ambiente

Todas as variáveis ficam em `chat-backend/.env`. O arquivo deve existir antes de qualquer `docker compose up`.

### RAG e modelo de embeddings

| Variável | Padrão | Descrição |
|---|---|---|
| `RAG_RESPONSE_MODE` | `extractive` | Modo de resposta: `extractive` (extrai trecho direto, mais rápido), `hybrid` (usa LLM como principal e trecho direto como fallback), `generative` (força LLM) |
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | Modelo de embeddings da HuggingFace. Não altere sem reindexar toda a base |
| `RAW_SOURCE_DIRS` | — | Caminhos locais onde `process_documents` lê os arquivos fonte. Em Docker, aponta para onde o bucket é baixado (ex: `/tmp/rag/raw,/tmp/rag/md`) |
| `FAQ_XLSX_PATH` | — | Caminho local da planilha de FAQ após download do bucket (ex: `/tmp/rag/faq/faq_agipi.xlsx`) |

### LLM — Groq

| Variável | Padrão | Descrição |
|---|---|---|
| `GROQ_API_KEY` | — | **Obrigatório.** Chave de API do Groq. Obtenha em https://console.groq.com/ |
| `GROQ_MODEL` | `llama-3.1-8b-instant` | Modelo do Groq a utilizar |
| `GROQ_TIMEOUT` | `20` | Timeout em segundos para chamadas ao Groq |

### LLM — Ollama (opcional)

Usado apenas em desenvolvimento local com modelo rodando na máquina. Comentado por padrão.

| Variável | Padrão | Descrição |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://127.0.0.1:11434` | Endpoint do Ollama local |
| `OLLAMA_MODEL` | `phi3:mini` | Modelo local a usar |
| `OLLAMA_TIMEOUT` | `20` | Timeout em segundos |

### Banco de dados — PostgreSQL

| Variável | Exemplo | Descrição |
|---|---|---|
| `POSTGRES_USER` | `postgres` | Usuário do banco |
| `POSTGRES_PASSWORD` | — | **Obrigatório.** Senha do banco |
| `POSTGRES_DB` | `ia_agipi` | Nome do banco de dados |
| `DATABASE_URL` | — | String de conexão completa. **Em Docker**, é sobrescrita no compose para usar o hostname do serviço (`@postgres:5432`). Em desenvolvimento local fora do Docker, aponte para `@localhost:5432` |

### Armazenamento de objetos — S3/MinIO

| Variável | Dev (MinIO) | Prod (Railway) | Descrição |
|---|---|---|---|
| `S3_BUCKET_NAME` | `rag-agipi` | `rag-agipi` | Nome do bucket. Deve ser igual ao criado no `minio-init` |
| `S3_ENDPOINT_URL` | `http://minio:9000` | URL do Railway Bucket | Endpoint S3. Em Docker usa o nome do serviço. Em produção, injetado pelo Railway |
| `AWS_ACCESS_KEY_ID` | valor de `MINIO_ROOT_USER` | Injetado pelo Railway | Access key S3. No Docker Compose, é sobrescrita com o valor do MinIO |
| `AWS_SECRET_ACCESS_KEY` | valor de `MINIO_ROOT_PASSWORD` | Injetado pelo Railway | Secret key S3. No Docker Compose, é sobrescrita com o valor do MinIO |
| `AWS_REGION` | `us-east-1` | `us-east-1` | Região S3. MinIO não valida este valor, mas boto3 exige que esteja preenchido |

### MinIO (apenas desenvolvimento local)

| Variável | Exemplo | Descrição |
|---|---|---|
| `MINIO_ROOT_USER` | `minio_admin` | Usuário administrador do MinIO. Mínimo 3 caracteres |
| `MINIO_ROOT_PASSWORD` | — | **Obrigatório.** Senha do MinIO. **Mínimo 8 caracteres** |

### API e CORS

| Variável | Padrão | Descrição |
|---|---|---|
| `ALLOWED_ORIGINS` | `http://localhost:5173,http://127.0.0.1:5173` | Origens permitidas pelo CORS, separadas por vírgula. Em produção, inclua a URL pública do frontend |

---

## 5. Gestão da base de conhecimento

Os documentos fonte (`.md`, `.docx`) e a planilha de FAQ devem ser enviados para o bucket antes da inicialização do backend. O backend compara o estado atual do bucket com o cache local e reprocessa automaticamente se houver diferença.

### Estrutura de prefixos no bucket

```
rag-agipi/
├── raw/      ← documentos DOCX e outros formatos
├── md/       ← documentos Markdown
├── faq/      ← planilha FAQ (.xlsx)
└── index/    ← reservado para cache do índice FAISS (uso interno)
```

### Upload de documentos via console MinIO (desenvolvimento)

1. Acesse `http://localhost:9001` com as credenciais do `.env`
2. Navegue até o bucket `rag-agipi`
3. Faça upload dos arquivos nos prefixos correspondentes (`raw/`, `md/`, `faq/`)
4. Reinicie o backend: `docker compose --env-file ./chat-backend/.env restart backend`

O backend detectará a mudança no manifest via ETag dos objetos e reconstruirá o índice.

### Forçar reindexação manual

```bash
# Dentro do container do backend
docker exec -it chatbot-backend python rebuild_index.py

# Ou reiniciando o serviço (o startup já verifica e reindexar se necessário)
docker compose --env-file ./chat-backend/.env restart backend
```

### Migrações do banco de dados

Sempre que os modelos SQLAlchemy forem alterados:

```bash
# Dentro do container do backend
docker exec -it chatbot-backend alembic revision --autogenerate -m "descricao_da_alteracao"
docker exec -it chatbot-backend alembic upgrade head
```

As migrações também são aplicadas automaticamente a cada startup via `CMD` do Dockerfile (`alembic upgrade head && uvicorn ...`).

---

## 6. Ambiente de produção (Railway)

### 6.1 Serviços a criar no Railway

Crie um novo projeto no Railway e adicione os seguintes serviços:

| Serviço | Tipo no Railway | Observação |
|---|---|---|
| `backend` | Deploy from GitHub repo | Aponta para `chat-backend/` com o Dockerfile do backend |
| `postgres` | PostgreSQL (plugin) | Railway provisiona automaticamente e injeta `DATABASE_URL` |
| `bucket` | Bucket (plugin) | Railway provisiona e injeta as credenciais S3 automaticamente |

O frontend pode ser publicado no Railway também, ou em alternativas como Vercel ou Netlify, que são mais adequadas para aplicações estáticas.

### 6.2 Variáveis de ambiente no Railway

Configure as seguintes variáveis no serviço `backend` pelo painel do Railway em **Variables**:

#### Obrigatórias — configurar manualmente

| Variável | Valor em produção |
|---|---|
| `GROQ_API_KEY` | Chave obtida em https://console.groq.com/ |
| `RAG_RESPONSE_MODE` | `extractive` (ou `hybrid` para usar LLM) |
| `EMBED_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` |
| `ALLOWED_ORIGINS` | URL pública do frontend (ex: `https://seu-app.vercel.app`) |
| `GROQ_MODEL` | `llama-3.1-8b-instant` |
| `GROQ_TIMEOUT` | `20` |

#### Banco de dados — injetadas automaticamente pelo Railway

O plugin PostgreSQL do Railway injeta `DATABASE_URL` automaticamente via **Variable Reference**. Não é necessário configurar manualmente.

Se preferir configurar explicitamente:

| Variável | Valor |
|---|---|
| `DATABASE_URL` | Referência: `${{Postgres.DATABASE_URL}}` |

#### Bucket S3 — injetadas automaticamente pelo Railway

O plugin Bucket do Railway injeta as variáveis abaixo automaticamente via **Variable References**. Configure no serviço `backend`:

| Variável | Variable Reference do Railway |
|---|---|
| `AWS_ACCESS_KEY_ID` | `${{Bucket.AWS_ACCESS_KEY_ID}}` |
| `AWS_SECRET_ACCESS_KEY` | `${{Bucket.AWS_SECRET_ACCESS_KEY}}` |
| `S3_ENDPOINT_URL` | `${{Bucket.BUCKET_ENDPOINT_URL}}` |
| `S3_BUCKET_NAME` | `${{Bucket.BUCKET_NAME}}` |
| `AWS_REGION` | `${{Bucket.BUCKET_REGION}}` |

> As Variable References garantem que, ao rotacionar credenciais ou migrar de serviço, o backend recebe os valores atualizados automaticamente sem edição manual.

#### Caminhos locais de processamento

| Variável | Valor recomendado |
|---|---|
| `RAW_SOURCE_DIRS` | `/tmp/rag/raw,/tmp/rag/md` |
| `FAQ_XLSX_PATH` | `/tmp/rag/faq/faq_agipi.xlsx` |

### 6.3 Upload inicial da base de conhecimento (produção)

O Railway não tem um container de inicialização como o `minio-init`. O upload dos documentos para o bucket de produção deve ser feito manualmente uma vez, usando o AWS CLI ou o console do Railway:

```bash
# Instalar AWS CLI
pip install awscli

# Configurar credenciais (use os valores das variáveis do Railway Bucket)
aws configure set aws_access_key_id     <AWS_ACCESS_KEY_ID>
aws configure set aws_secret_access_key <AWS_SECRET_ACCESS_KEY>
aws configure set default.region        us-east-1

# Upload dos documentos
aws s3 cp ./chat-backend/data/raw/ s3://<BUCKET_NAME>/raw/ \
  --recursive \
  --endpoint-url <S3_ENDPOINT_URL>

aws s3 cp ./chat-backend/data/md/ s3://<BUCKET_NAME>/md/ \
  --recursive \
  --endpoint-url <S3_ENDPOINT_URL>

aws s3 cp ./caminho/para/faq.xlsx s3://<BUCKET_NAME>/faq/faq_agipi.xlsx \
  --endpoint-url <S3_ENDPOINT_URL>
```

Após o upload, o deploy do backend detectará os documentos e construirá o índice automaticamente.

### 6.4 Configuração do frontend em produção

Se o frontend for publicado no Vercel ou Railway, configure a variável de ambiente:

| Variável | Valor |
|---|---|
| `VITE_API_BASE_URL` | URL pública do backend no Railway (ex: `https://chatbot-backend.up.railway.app`) |

### 6.5 Healthcheck de produção

Monitore o backend pelo endpoint:

```
GET https://<sua-url-backend>/health
```

Resposta esperada quando o sistema está pronto:

```json
{
  "status": "ok",
  "index": {
    "ready": true,
    "documents": 1234,
    "faq_entries": 604,
    "document_chunks": 630
  }
}
```

---

## 7. Operação e manutenção

### Atualizar a base de conhecimento

1. Faça upload dos novos arquivos no bucket (prefixo correto)
2. Redeploy do backend no Railway (ou `restart backend` em dev)
3. O backend detecta a mudança via ETag e reprocessa automaticamente

### Roteiro de troubleshooting

**Backend trava durante geração de embeddings (primeiro boot)**
O processo de embeddings é síncrono e pode levar vários minutos. Aguarde os logs `[BOOT] Embeddings concluídos` e `[BOOT] Sistema pronto`. Não interrompa o processo.

**`Access Denied` no minio-init**
A senha de `MINIO_ROOT_PASSWORD` tem menos de 8 caracteres, ou há conflito entre `env_file` e `environment` no compose. Verifique com:
```bash
docker compose --env-file ./chat-backend/.env config | grep MINIO
```

**Variáveis aparecem vazias no compose**
Execute sempre com `--env-file ./chat-backend/.env`. Sem essa flag, o Docker Compose só lê `.env` na raiz do projeto, e as variáveis ficam vazias.

**Índice não atualiza após upload de novos documentos**
O cache local (volumes Docker) ainda está válido. Reinicie o backend ou remova manualmente os arquivos de cache:
```bash
docker exec -it chatbot-backend rm -rf /app/data/processed/ /app/data/index/
docker compose --env-file ./chat-backend/.env restart backend
```

**Erro de migração Alembic no startup**
```bash
docker exec -it chatbot-backend alembic history
docker exec -it chatbot-backend alembic current
docker exec -it chatbot-backend alembic upgrade head
```
