import logging
import re
import json
from src.llm.llm_client import LLMClient

logger = logging.getLogger(__name__)

CONTEXTUAL_REFERENCES = {
    "ele", "ela", "eles", "elas", "isso", "esse", "essa", "disso", "dele", "dela",
    "o que ele faz", "o que ela faz", "e ele", "e ela", "como ele funciona",
    "como ela funciona", "qual a funcao dele", "qual a funcao dela", "o que e", "o que e isso",
}


class QueryRewriter:
    def __init__(self, llm: LLMClient, context_triggers: list[str] = CONTEXTUAL_REFERENCES):
        self.llm = llm
        self.contextual_triggers = context_triggers


    def _needs_rewrite(self, question: str) -> bool:
        """
        Decide se a pergunta parece precisar do histórico.
        """
        tokens = re.findall(r'\b\w+\b', question.lower())

        if len(tokens) <= 4:
            return True
        
        if any(word in self.contextual_triggers for word in tokens):
            return True
        
        if question.lower().startswith(("e ", "mas ", "entao ", "o que é", "quem é")):
            return True
        
        return False


    def rewrite(self, user_question: str, history: list[dict[str, str]]) -> str:
        """
        Analisa o histórico da conversa e a última pergunta do usuário para gerar
        uma busca independente.
        """

        question_cleaned = user_question.strip()

        if not history or not self._needs_rewrite(question_cleaned):
            return question_cleaned
        
        formatted_history = ""
        for msg in history[-4:]:  # Considera os últimos 3 turnos completos de conversa
            role = "Usuário" if msg.get("role") == "user" else "Assistente"
            content = msg.get("content", "").strip()
            formatted_history += f"{role}: {content}\n"

        prompt = f"""Você é um especialista em processamento de linguagem natural e busca semântica.
Sua tarefa é analisar o histórico da conversa e a nova pergunta do usuário para gerar uma única pergunta reformulada. 
Esta pergunta reformulada deve ser independente (standalone) e autoexplicativa, contendo todo o contexto necessário para ser buscada em um banco de dados, sem precisar do histórico.

Regras estritas:
1. Identifique o assunto ou entidade (ex: AGEUNI, AGIPI, INPROTEC, NIT, etc.) de que o usuário está falando no histórico e inclua-o na pergunta se ela for vaga (ex: "Onde fica?" -> "Onde fica a AGIPI?").
2. Mantenha os termos técnicos originais da UEPG.
3. Se a nova pergunta já for independente e clara por si só ou não parecer uma pergunta e sim uma afirmação (como "certo", "ok" etc.), retorne-a exatamente como foi digitada pelo usuário.
4. Não adicione nenhuma introdução, explicação ou comentários. Retorne APENAS a pergunta reformulada.
5. Se você não reconhecer algum acrônimo ou sigla, preserve-o no contexto.

Histórico da conversa:
{formatted_history}

Nova Pergunta do Usuário:
{user_question}

Pergunta Reformulada:"""
        
        try:
            rewritten_question = self.llm.generate_response(prompt=prompt).strip()
            if rewritten_question:
                return rewritten_question
        except Exception as exc:
            logger.error(f"[QueryRewriter] Erro ao reescrever query com LLM: {exc}")
        
        return user_question


    def generate_query_plan(self, user_question: str, history: list[dict[str, str]]) -> dict:
        """
        Gera múltiplas estratégias de busca em formato JSON.
        """
        question_cleaned = user_question.strip()
        
        # Estrutura base de fallback
        base_plan = {
            "standalone": question_cleaned,
            "step_back": None,
            "sub_queries": []
        }

        if not history and not self._needs_rewrite(question_cleaned):
            return base_plan
        
        formatted_history = ""
        for msg in history[-4:]:
            role = "Usuário" if msg.get("role") == "user" else "Assistente"
            content = msg.get("content", "").strip()
            formatted_history += f"{role}: {content}\n"

        prompt = f"""Você é um roteador de buscas semânticas especialista na UEPG (AGEUNI, AGIPI, INPROTEC).
Analise o histórico da conversa e a nova pergunta do usuário. Sua tarefa é extrair intenções e gerar variações da pergunta para otimizar a busca no banco de dados vetorial.

Responda ESTRITAMENTE no formato JSON com as seguintes chaves:
- "standalone": A pergunta do usuário reescrita para ser independente e autoexplicativa usando o histórico. Mantenha os termos técnicos.
- "step_back": Uma versão mais ampla e conceitual da pergunta. Útil para recuperar conceitos, políticas ou documentos fundacionais que baseiam a pergunta específica.
- "sub_queries": Uma lista de strings dividindo a pergunta em perguntas menores, APENAS SE a pergunta principal contiver múltiplos pedidos ou for muito complexa (senão, retorne lista vazia).

Histórico da conversa:
{formatted_history}

Nova Pergunta do Usuário:
{user_question}

Retorne APENAS o JSON válido, sem markdown extra ou explicações."""
        
        try:
            response = self.llm.generate_response(prompt=prompt).strip()
            # Limpa caso a LLM retorne blocos de código Markdown
            response = re.sub(r"^```json\n|```$", "", response, flags=re.MULTILINE).strip()
            
            plan = json.loads(response)
            
            # Validação simples
            return {
                "standalone": plan.get("standalone", question_cleaned) or question_cleaned,
                "step_back": plan.get("step_back"),
                "sub_queries": plan.get("sub_queries", [])
            }
        except Exception as exc:
            logger.error(f"[QueryRewriter] Erro ao gerar plano de queries com LLM: {exc}")
        
        return base_plan

