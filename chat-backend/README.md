# Assistente AGIPI - Backend

Aplicação RAG construída com FastAPI, utilizando PostgreSQL como banco de dados relacional e SQLAlchemy/Alembic para gestão de dados e estrutura.

## Configuração e Execução

Siga os passos abaixo para preparar e rodar o ambiente:

```powershell
cd chat-backend
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

Antes de executar a aplicação, certifique-se de configurar o arquivo `.env` na raiz do projeto (mesmo nível da pasta `src`). Exemplo da variável essencial para a conexão com o banco de dados:

```env
DATABASE_URL=postgresql+asyncpg://usuario:senha@localhost:5432/nome_do_banco
```

Para iniciar a API em ambiente de desenvolvimento, utilize o Uvicorn:

```powershell
python -m uvicorn src.api.main:app --reload
```

Outras variáveis de ambiente úteis:

* `RAG_RESPONSE_MODE=extractive` (para resposta mais rápida extraindo trechos diretos)
* `RAG_RESPONSE_MODE=hybrid` (para usar LLM como fallback)
* `RAG_RESPONSE_MODE=generative` (para forçar o uso da LLM na geração de respostas)
* `OLLAMA_MODEL=phi3:mini` (para um modelo leve no Windows)
* `FAQ_XLSX_PATH` (caminho para a planilha de FAQ)
* `RAW_SOURCE_DIRS` (caminho para as pastas documentais)

## Gestão do Banco de Dados Relacional (PostgreSQL + Alembic)

O projeto utiliza SQLAlchemy 2.0 com suporte assíncrono para o mapeamento objeto-relacional (ORM) e o Alembic para o controle de versão do esquema do banco de dados (migrações).

### Como alterar a estrutura do banco de dados (Modelos)

Sempre que for necessário adicionar uma nova tabela, modificar ou remover colunas existentes, o fluxo correto de trabalho com o Alembic é:

1. Modifique as classes Python no arquivo `src/db/models.py` refletindo as alterações desejadas na estrutura.
2. Gere o script de migração automaticamente executando no terminal:
```bash
alembic revision --autogenerate -m "Descricao clara da alteracao"
```
3. Revise o arquivo gerado na pasta `alembic/versions/` para garantir que as instruções SQL geradas pela ferramenta estão corretas.
4. Aplique as modificações definitivas no banco de dados com o comando:
```bash
alembic upgrade head
```


## Gestão do Banco Vetorial (RAG)

Ao iniciar, o backend valida se a pasta `data/raw` corresponde ao índice em cache. Se não corresponder, ele reprocessa automaticamente os chunks e embeddings.

Para forçar a reconstrução total do índice vetorial (FAQ + documentos externos) manualmente:

```powershell
python rebuild_index.py
```

## Avaliação de Métricas (Retrieval)

O sistema possui um script automatizado para medir a assertividade da busca vetorial utilizando as métricas Precision@K, Recall@K, Hit@K e MRR@K.

Para executar os testes de avaliação:

```powershell
python src/evaluation/evaluate_rag.py
```

*Atenção: O script realiza leitura da planilha localizada em `src/evaluation/PERGUNTAS_TESTE.xlsx`. Para garantir a eficácia da avaliação, os documentos listados na coluna correspondente da planilha devem possuir nomenclatura idêntica aos arquivos originais (incluindo extensões).*