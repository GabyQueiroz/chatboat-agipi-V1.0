import re
import time
import unicodedata
from typing import Any

from src.llm.llm_client import LLMClient
from src.retrieval.embeddings import Embedder
from src.retrieval.vector_db import VectorStore


STOPWORDS = {
    "a", "ao", "aos", "as", "com", "como", "da", "das", "de", "do", "dos", "e",
    "em", "esse", "essa", "esta", "este", "eu", "foi", "ha", "isso", "isto",
    "na", "nas", "no", "nos", "o", "os", "ou", "para", "por", "qual", "que",
    "se", "sem", "ser", "sua", "suas", "suo", "seu", "seus", "um", "uma",
    "sobre", "quais", "onde", "quando", "porque", "por que",
    "ele", "ela", "eles", "elas", "isso", "esse", "essa", "dela", "dele",
}

CONTEXTUAL_REFERENCES = {
    "ele", "ela", "eles", "elas", "isso", "esse", "essa", "disso", "dele", "dela",
    "o que ele faz", "o que ela faz", "e ele", "e ela", "como ele funciona",
    "como ela funciona", "qual a funcao dele", "qual a funcao dela", "o que e", "o que e isso",
}

ACTION_HINTS = {
    "faz", "fazer", "funcao", "funcoes", "atua", "atuacao",
    "serve", "trabalha", "responsavel", "objetivo", "objetivos",
    "papel", "competencia", "competencias", "atribui", "atribuicao",
    "registrar", "registro", "solicitar", "pedido", "criar", "abrir", "iniciar",
}

LOCATION_HINTS = {
    "onde", "local", "localizacao", "localizada", "localizado", "endereco",
    "fica", "ficam", "situada", "situado", "contato", "telefone", "email",
}

DEFINITION_PREFIXES = ("o que e", "quem e")
PRIORITY_ENTITIES = ("ageuni", "agipi", "epitec", "inprotec", "nit", "nits", "software", "patente", "marca")
GENERIC_SUBJECTS = {
    "programa", "agencia", "agencias", "desenvolvimento", "regional", "sustentavel",
    "inovacao", "universidade", "universidades", "documento", "documentos", "projeto",
}

CANONICAL_REPLACEMENTS = (
    (r"\bcriar um registro\b", "registrar"),
    (r"\bcriar o registro\b", "registrar"),
    (r"\bfazer um registro\b", "registrar"),
    (r"\bfazer o registro\b", "registrar"),
    (r"\babrir um registro\b", "registrar"),
    (r"\babrir o registro\b", "registrar"),
    (r"\biniciar um registro\b", "registrar"),
    (r"\biniciar o registro\b", "registrar"),
    (r"\bsolicitar o registro\b", "registrar"),
    (r"\bsolicitar registro\b", "registrar"),
    (r"\bpedido de registro\b", "registro"),
    (r"\bcriar um pedido\b", "solicitar"),
    (r"\bcomo criar\b", "como registrar"),
    (r"\bcomo fazer\b", "como registrar"),
    (r"\bcomo abrir\b", "como registrar"),
    (r"\bcomo iniciar\b", "como registrar"),
    (r"\bcomo solicitar\b", "como registrar"),
)


class RAGPipeline:
    def __init__(
        self,
        embedder: Embedder,
        vector_store: VectorStore,
        llm: LLMClient | None,
        response_mode: str = "extractive",
        min_score: float = 0.25,
    ):
        self.embedder = embedder
        self.vector_store = vector_store
        self.llm = llm
        self.response_mode = response_mode
        self.min_score = min_score
        self.out_of_scope_message = (
            "Desculpe, essa pergunta nao parece fazer parte da base atual do assistente. "
            "Eu consigo ajudar melhor com temas como AGEUNI, AGIPI, EPITEC, NITs, "
            "inovacao universitaria, incubacao, patente, software e documentos institucionais da UEPG."
        )

    def ask(self, user_question: str, history: list[dict[str, str]] | None = None) -> dict[str, Any]:
        history = history or []
        resolved_question, topic = self._resolve_follow_up_question(user_question, history)
        canonical_question = self._canonicalize_question(resolved_question)
        normalized_question = self._normalize_text(canonical_question.lower().strip())

        if normalized_question in {"o que e", "o que e?", "o que e isso", "o que e isso?", "e a", "e o", "e as", "e os"} and not topic:
            return {
                "answer": "Posso te ajudar melhor se voce disser sobre qual tema quer saber. Por exemplo: AGEUNI, AGIPI, INPROTEC ou registro de software.",
                "sources": [],
                "mode": "clarification",
                "resolved_question": resolved_question,
                "timings": {"embedding_ms": 0.0, "retrieval_ms": 0.0, "answer_ms": 0.0},
                "warnings": [],
            }

        if "inprotec" in normalized_question and normalized_question.startswith("o que e"):
            base_faq = self._find_faq_by_question_contains(["inprotec"], ["o que"])
            if base_faq is not None:
                return self._curated_payload(self._format_faq_answer(base_faq["faq_answer"]), [base_faq], "faq")

        if "registro de software" in normalized_question and normalized_question.startswith("o que e"):
            base_faq = self._find_faq_by_question_contains(["registro de software"], ["o que"])
            if base_faq is not None:
                return self._curated_payload(self._format_faq_answer(base_faq["faq_answer"]), [base_faq], "faq")

        if "registrar" in normalized_question and "software" in normalized_question:
            how_faq = self._find_faq_by_question_contains(["software"], ["como registrar", "desenvolvido na universidade", "tramite institucional"])
            if how_faq is not None:
                answer = (
                    f"{self._format_faq_answer(how_faq['faq_answer'])} "
                    "O formulario principal e o 'Formulario de Avaliacao Preliminar de solicitacao de Registro de Software'. "
                    "Voce pode acessar o formulario neste link: "
                    "https://docs.google.com/document/d/1gQiIr4HPmdhOhmApsxPnPzbpgTOnpalY/edit?usp=sharing&ouid=105226628045611786767&rtpof=true&sd=true"
                )
                return self._curated_payload(answer, [how_faq], "faq")

        curated_response = self._build_curated_response(canonical_question, topic)
        if curated_response is not None:
            print(f"[RAG] resposta curada mode={curated_response['mode']}")
            return curated_response

        topic_action_faq = self._find_topic_action_faq(canonical_question, topic)
        if topic_action_faq is not None:
            answer_started_at = time.perf_counter()
            answer = self._format_faq_answer(topic_action_faq["faq_answer"])
            answer_elapsed = time.perf_counter() - answer_started_at
            sources = [self._build_source_payload(topic_action_faq)]
            print("[RAG] resposta FAQ contextual mode=faq")
            return {
                "answer": answer,
                "sources": sources,
                "mode": "faq",
                "resolved_question": resolved_question,
                "timings": {
                    "embedding_ms": 0.0,
                    "retrieval_ms": 0.0,
                    "answer_ms": round(answer_elapsed * 1000, 1),
                },
                "warnings": [],
            }

        direct_document_match = self._find_direct_document_match(canonical_question)
        if direct_document_match is not None:
            answer_started_at = time.perf_counter()
            answer = self._build_extractive_answer(resolved_question, [direct_document_match])
            answer = re.sub(r"^No entanto,\s*", "", answer, flags=re.IGNORECASE)
            normalized_answer = self._normalize_text(answer.lower())
            if "agencia de inovacao e propriedade intelectual (agipi)" in normalized_answer:
                answer = "A AGIPI e a Agencia de Inovacao e Propriedade Intelectual da UEPG, vinculada a AGEUNI."
            answer_elapsed = time.perf_counter() - answer_started_at
            sources = [self._build_source_payload(direct_document_match)]
            print("[RAG] resposta documental direta mode=extractive")
            return {
                "answer": answer,
                "sources": sources,
                "mode": "extractive",
                "resolved_question": resolved_question,
                "timings": {
                    "embedding_ms": 0.0,
                    "retrieval_ms": 0.0,
                    "answer_ms": round(answer_elapsed * 1000, 1),
                },
                "warnings": [],
            }

        direct_faq_match = self._find_direct_faq_match(canonical_question, topic)
        if direct_faq_match is not None:
            answer_started_at = time.perf_counter()
            answer = self._format_faq_answer(direct_faq_match["faq_answer"])
            answer_elapsed = time.perf_counter() - answer_started_at
            sources = [self._build_source_payload(direct_faq_match)]
            print("[RAG] resposta FAQ direta mode=faq")
            return {
                "answer": answer,
                "sources": sources,
                "mode": "faq",
                "resolved_question": resolved_question,
                "timings": {
                    "embedding_ms": 0.0,
                    "retrieval_ms": 0.0,
                    "answer_ms": round(answer_elapsed * 1000, 1),
                },
                "warnings": [],
            }

        embedding_started_at = time.perf_counter()
        question_vector = self.embedder.embed_texts([canonical_question])
        embedding_elapsed = time.perf_counter() - embedding_started_at

        retrieval_started_at = time.perf_counter()
        relevant_docs = self.vector_store.search(question_vector, top_k=10)
        ranked_docs = self._rerank_documents(canonical_question, relevant_docs)
        retrieval_elapsed = time.perf_counter() - retrieval_started_at

        filtered_docs = [doc for doc in ranked_docs if doc.get("score", 0.0) >= self.min_score]
        docs_for_answer = self._choose_docs_for_answer(canonical_question, filtered_docs, ranked_docs)
        best_doc_score = ranked_docs[0].get("score", 0.0) if ranked_docs else 0.0

        if self._is_out_of_scope(canonical_question, docs_for_answer, best_doc_score):
            print("[RAG] pergunta fora de escopo")
            return {
                "answer": self.out_of_scope_message,
                "sources": [],
                "mode": "out_of_scope",
                "resolved_question": canonical_question,
                "timings": {
                    "embedding_ms": round(embedding_elapsed * 1000, 1),
                    "retrieval_ms": round(retrieval_elapsed * 1000, 1),
                    "answer_ms": 0.0,
                },
                "warnings": [],
            }

        answer_started_at = time.perf_counter()
        warnings: list[str] = []
        document_docs = [doc for doc in docs_for_answer if doc.get("doc_type") == "document"]
        faq_docs = [doc for doc in docs_for_answer if doc.get("doc_type") == "faq"]
        faq_match = self._select_faq_match(canonical_question, faq_docs)

        if document_docs:
            answer = self._build_extractive_answer(canonical_question, document_docs[:5])
            mode = "extractive"
        elif faq_match is not None:
            answer = self._format_faq_answer(faq_match["faq_answer"])
            docs_for_answer = [faq_match] + [doc for doc in faq_docs if doc["id"] != faq_match["id"]][:4]
            mode = "faq"
        else:
            answer = self._build_extractive_answer(canonical_question, docs_for_answer[:5])
            mode = "extractive"

        if not docs_for_answer:
            warnings.append("Nao encontrei informacoes suficientes na base para responder com seguranca.")

        if self.response_mode == "hybrid" and self.llm is not None and docs_for_answer:
            try:
                answer = self._build_llm_answer(canonical_question, docs_for_answer, answer)
                mode = "hybrid" if mode != "faq" else "faq+hybrid"
            except Exception as exc:
                warnings.append(str(exc))

        answer_elapsed = time.perf_counter() - answer_started_at
        sources = [self._build_source_payload(doc) for doc in docs_for_answer]

        print(
            "[RAG] tempos "
            f"embedding={embedding_elapsed:.2f}s "
            f"retrieval={retrieval_elapsed:.2f}s "
            f"answer={answer_elapsed:.2f}s "
            f"mode={mode}"
        )

        return {
            "answer": answer,
            "sources": sources,
            "mode": mode,
                "resolved_question": canonical_question,
            "timings": {
                "embedding_ms": round(embedding_elapsed * 1000, 1),
                "retrieval_ms": round(retrieval_elapsed * 1000, 1),
                "answer_ms": round(answer_elapsed * 1000, 1),
            },
            "warnings": warnings,
        }

    def _build_source_payload(self, doc: dict[str, Any]) -> dict[str, Any]:
        return {
            "id": doc["id"],
            "source": doc["source"],
            "title": doc.get("title", doc["source"]),
            "score": round(float(doc.get("score", 0.0)), 4),
            "excerpt": self._excerpt(doc.get("faq_answer") or doc.get("text", "")),
            "category": doc.get("category"),
            "doc_type": doc.get("doc_type", "document"),
        }

    def _canonicalize_question(self, question: str) -> str:
        normalized = self._normalize_text(question.lower().strip())
        for pattern, replacement in CANONICAL_REPLACEMENTS:
            normalized = re.sub(pattern, replacement, normalized)
        normalized = re.sub(r"\s+", " ", normalized).strip()
        return normalized

    def _build_curated_response(self, question: str, topic: str | None) -> dict[str, Any] | None:
        normalized_question = self._normalize_text(question.lower().strip())
        normalized_question = re.sub(r"^(?:e\s+|mas\s+)+", "", normalized_question)
        subject_keywords = self._extract_subject_keywords(normalized_question)
        if not subject_keywords:
            return None

        subject = self._pick_primary_subject(subject_keywords)
        is_definition = any(normalized_question.startswith(prefix) for prefix in DEFINITION_PREFIXES)
        is_action = any(hint in normalized_question for hint in ACTION_HINTS)

        if is_definition and subject == "ageuni":
            base_faq = self._find_faq_by_question_contains(["ageuni"], ["o que", "programa"])
            objective_faq = self._find_faq_by_question_contains(["ageuni"], ["objetivo"])
            if base_faq and objective_faq:
                answer = (
                    f"{self._format_faq_answer(base_faq['faq_answer'])} "
                    f"Em termos praticos, {self._lowercase_first(self._format_faq_answer(objective_faq['faq_answer']))}"
                )
                return self._curated_payload(answer, [base_faq, objective_faq], "faq")

        if is_definition and subject == "agipi":
            cleaned_question = "O que e AGIPI?"
            doc_match = self._find_direct_document_match(cleaned_question)
            services_faq = self._find_faq_by_question_contains(["principais servicos", "servicos oferecidos"], ["agipi"])
            if doc_match:
                answer = "A AGIPI e a Agencia de Inovacao e Propriedade Intelectual da UEPG, vinculada a AGEUNI."
                if services_faq:
                    answer += " Entre os principais servicos da AGIPI estao a gestao da politica de inovacao, a protecao da propriedade intelectual, o apoio a patentes, marcas e software, a transferencia de tecnologia, a incubacao de projetos inovadores e o apoio ao empreendedorismo."
                    return self._curated_payload(answer, [doc_match, services_faq], "extractive")
                return self._curated_payload(answer, [doc_match], "extractive")

        if subject == "agipi" and any(hint in normalized_question for hint in LOCATION_HINTS):
            location_faq = self._find_faq_by_question_contains(["agipi"], ["onde", "localizada"])
            contact_faq = self._find_faq_by_question_contains(["agipi"], ["contato", "email", "telefone"])
            if location_faq:
                answer = "A AGIPI esta localizada no Campus Uvaranas, na Av. General Carlos Cavalcanti, 4748, em Ponta Grossa-PR. Os relatorios tambem indicam o Hub de Inovacao no mesmo endereco."
                if contact_faq and any(term in normalized_question for term in {"contato", "telefone", "email"}):
                    answer += " " + self._lowercase_first(self._format_faq_answer(contact_faq["faq_answer"]))
                    return self._curated_payload(answer, [location_faq, contact_faq], "faq")
                return self._curated_payload(answer, [location_faq], "faq")

        if is_definition and subject == "inprotec":
            base_faq = self._find_faq_by_question_contains(["inprotec"], ["o que"])
            if base_faq:
                answer = self._format_faq_answer(base_faq["faq_answer"])
                return self._curated_payload(answer, [base_faq], "faq")

        if (is_action and "ageuni" in normalized_question) or (topic and self._normalize_text(topic.lower()) == "ageuni" and is_action):
            objective_faq = self._find_faq_by_question_contains(["ageuni"], ["objetivo"])
            innovation_faq = self._find_faq_by_question_contains(["ageuni"], ["promove inovacao"])
            if objective_faq:
                answer = self._format_faq_answer(objective_faq["faq_answer"])
                if innovation_faq:
                    answer += " " + self._lowercase_first(self._format_faq_answer(innovation_faq["faq_answer"])).capitalize()
                return self._curated_payload(answer, [objective_faq] + ([innovation_faq] if innovation_faq else []), "faq")


        return None

    def _curated_payload(self, answer: str, docs: list[dict[str, Any]], mode: str) -> dict[str, Any]:
        sources = [self._build_source_payload(doc) for doc in docs if doc is not None]
        return {
            "answer": answer,
            "sources": sources,
            "mode": mode,
            "resolved_question": "",
            "timings": {
                "embedding_ms": 0.0,
                "retrieval_ms": 0.0,
                "answer_ms": 0.0,
            },
            "warnings": [],
        }

    def _find_faq_by_question_contains(self, required_terms: list[str], optional_terms: list[str]) -> dict[str, Any] | None:
        best_doc = None
        best_score = -1
        for doc in self.vector_store.metadata:
            if doc.get("doc_type") != "faq":
                continue
            faq_question = self._normalize_text(str(doc.get("faq_question", "")).lower())
            if required_terms and not all(term in faq_question for term in required_terms):
                continue
            score = sum(1 for term in optional_terms if term in faq_question)
            if score > best_score:
                best_score = score
                best_doc = doc
        return best_doc

    def _lowercase_first(self, text: str) -> str:
        if not text:
            return text
        return text[0].lower() + text[1:]

    def _resolve_follow_up_question(self, user_question: str, history: list[dict[str, str]]) -> tuple[str, str | None]:
        question = user_question.strip()
        lowered = self._normalize_text(question)

        if not self._looks_contextual(lowered):
            return question, None

        topic = self._extract_recent_topic(history)
        if not topic:
            return question, None

        if any(hint in lowered for hint in ACTION_HINTS):
            return f"O que {topic} faz?", topic

        if lowered in {"o que e", "o que e?", "o que e isso"}:
            return f"O que e {topic}?", topic

        if any(lowered.startswith(prefix) for prefix in ["onde ", "onde?", "qual o endereco", "qual endereco", "como entrar em contato", "qual o contato", "qual contato"]):
            return f"Onde {topic} esta?", topic

        if lowered.startswith("qual a diferenca"):
            return f"Qual a diferenca em relacao a {topic}?", topic

        return f"Sobre {topic}: {question}", topic

    def _looks_contextual(self, lowered_question: str) -> bool:
        if lowered_question in CONTEXTUAL_REFERENCES:
            return True
        if any(lowered_question.startswith(prefix) for prefix in ["e ", "e o ", "e a ", "mas e", "mas o que"]):
            return True
        tokens = lowered_question.split()
        return len(tokens) <= 6 and any(token in CONTEXTUAL_REFERENCES for token in tokens)

    def _extract_recent_topic(self, history: list[dict[str, str]]) -> str | None:
        for item in reversed(history):
            if item.get("role") != "user":
                continue

            content = item.get("content", "").strip()
            if not content:
                continue

            normalized = self._normalize_text(content)
            match = re.search(r"(?:o que e|quem e|sobre)\s+(.+)", normalized, flags=re.IGNORECASE)
            if match:
                return match.group(1).strip(" ?.")

            title_like = re.findall(r"\b[A-ZÀ-Ý][\wÀ-ÿ-]+\b", content)
            if title_like:
                return " ".join(title_like)

            if len(content.split()) <= 8:
                return content.strip(" ?.")

        return None

    def _is_out_of_scope(self, question: str, docs: list[dict[str, Any]], best_doc_score: float) -> bool:
        if not docs:
            return True

        keywords = self._extract_keywords(question)
        if not keywords:
            return False

        overlap_hits = 0
        for doc in docs[:3]:
            blob = " ".join(
                [
                    str(doc.get("title", "")),
                    str(doc.get("faq_question", "")),
                    str(doc.get("faq_answer", "")),
                    str(doc.get("text", "")),
                    str(doc.get("category", "")),
                ]
            ).lower()
            overlap_hits += sum(1 for keyword in keywords if keyword in blob)

        if overlap_hits == 0:
            if len(keywords) == 1:
                return True
            if best_doc_score < 0.55:
                return True
        if best_doc_score < 0.33 and overlap_hits == 0:
            return True
        if best_doc_score < 0.28:
            return True
        return False

    def _choose_docs_for_answer(
        self,
        question: str,
        filtered_docs: list[dict[str, Any]],
        ranked_docs: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        docs = filtered_docs or ranked_docs[:5]
        if not docs:
            return []

        document_docs = [doc for doc in docs if doc.get("doc_type") == "document"]
        faq_docs = [doc for doc in docs if doc.get("doc_type") == "faq"]

        if self._should_prefer_documents(question, document_docs):
            return document_docs[:5] + faq_docs[:2]
        return docs

    def _should_prefer_documents(self, question: str, document_docs: list[dict[str, Any]]) -> bool:
        if not document_docs:
            return False

        lowered = self._normalize_text(question)
        best_document_score = max(float(doc.get("score", 0.0)) for doc in document_docs)

        if any(lowered.startswith(prefix) for prefix in DEFINITION_PREFIXES):
            return best_document_score >= 0.45
        if any(hint in lowered for hint in ACTION_HINTS):
            return best_document_score >= 0.42
        return best_document_score >= 0.4

    def _find_direct_faq_match(self, question: str, topic: str | None) -> dict[str, Any] | None:
        candidates = [doc for doc in self.vector_store.metadata if doc.get("doc_type") == "faq"]
        if not candidates:
            return None

        question_lower = self._normalize_text(question)
        keywords = set(self._extract_keywords(question_lower))
        topic_keywords = set(self._extract_keywords(topic or ""))
        question_subject = set(self._extract_subject_keywords(question_lower))
        best_doc = None
        best_score = 0.0

        for doc in candidates:
            faq_question = self._normalize_text(doc.get("faq_question", ""))
            title = self._normalize_text(str(doc.get("title", "")))
            blob = " ".join([faq_question, title])
            faq_subject = set(self._extract_subject_keywords(faq_question))

            score = 0.0
            if question_lower == faq_question:
                score += 10.0
            if topic_keywords and any(keyword in blob for keyword in topic_keywords):
                score += 4.0

            overlap = sum(1 for keyword in keywords if keyword in blob)
            score += overlap * 1.2

            if self._question_is_action_or_definition(question_lower):
                if not self._faq_matches_intent(faq_question, question_lower):
                    continue
                score += 2.0

            if question_subject:
                subject_overlap = len(question_subject & faq_subject)
                if subject_overlap == 0:
                    continue
                score += subject_overlap * 2.2

            if score > best_score:
                best_score = score
                best_doc = doc

        minimum_score = 6.0 if topic_keywords and self._question_is_action_or_definition(question_lower) else 7.0
        if best_doc is None or best_score < minimum_score:
            return None

        matched = dict(best_doc)
        matched["score"] = best_score / 10
        return matched

    def _find_topic_action_faq(self, question: str, topic: str | None) -> dict[str, Any] | None:
        if not topic:
            return None

        normalized_question = self._normalize_text(question.lower().strip())
        if not any(hint in normalized_question for hint in ACTION_HINTS):
            return None

        normalized_topic = self._normalize_text(topic.lower().strip())
        best_doc = None
        best_score = 0.0

        for doc in self.vector_store.metadata:
            if doc.get("doc_type") != "faq":
                continue

            faq_question = self._normalize_text(str(doc.get("faq_question", "")).lower())
            if normalized_topic not in faq_question:
                continue

            score = 2.0
            if any(term in faq_question for term in ["objetivo", "faz", "funcao", "papel", "promove", "contribui", "atua"]):
                score += 3.0
            if "objetivo" in faq_question:
                score += 1.0
            if "promove" in faq_question or "contribui" in faq_question:
                score += 0.8

            if score > best_score:
                best_score = score
                best_doc = doc

        if best_doc is None or best_score < 4.5:
            return None

        matched = dict(best_doc)
        matched["score"] = best_score / 10
        return matched

    def _find_direct_document_match(self, question: str) -> dict[str, Any] | None:
        normalized_question = self._normalize_text(question.lower().strip())
        if not any(normalized_question.startswith(prefix) for prefix in DEFINITION_PREFIXES):
            return None

        subject_keywords = self._extract_subject_keywords(normalized_question)
        if not subject_keywords:
            return None

        best_doc = None
        best_score = 0.0
        for doc in self.vector_store.metadata:
            if doc.get("doc_type") != "document":
                continue

            text = self._normalize_text(str(doc.get("text", "")).lower())
            title = self._normalize_text(str(doc.get("title", "")).lower())
            blob = f"{title} {text}"
            subject_hits = sum(1 for keyword in subject_keywords if keyword in blob)
            if subject_hits == 0:
                continue

            score = subject_hits * 2.5
            if any(f"({keyword})" in blob for keyword in subject_keywords):
                score += 2.5
            if any(marker in blob for marker in ["agencia de inovacao", "propriedade intelectual", "nucleo de inovacao", "nucleo de inovacao tecnologica"]):
                score += 2.0
            if any(marker in blob for marker in [" e a ", " e o ", " consiste em", " trata-se", " vinculada a", " vinculado a"]):
                score += 1.5
            if "agrade" in blob or "relatorio anual" in blob or "telefone" in blob:
                score -= 2.0

            if score > best_score:
                best_score = score
                best_doc = doc

        if best_doc is None or best_score < 4.5:
            return None

        matched = dict(best_doc)
        matched["score"] = best_score / 10
        return matched

    def _question_is_action_or_definition(self, question: str) -> bool:
        lowered = self._normalize_text(question)
        return any(hint in lowered for hint in ACTION_HINTS) or any(lowered.startswith(prefix) for prefix in DEFINITION_PREFIXES)

    def _faq_matches_intent(self, faq_question: str, user_question: str) -> bool:
        normalized_faq = self._normalize_text(faq_question)
        normalized_question = self._normalize_text(user_question)

        if any(normalized_question.startswith(prefix) for prefix in DEFINITION_PREFIXES):
            return any(normalized_faq.startswith(prefix) for prefix in DEFINITION_PREFIXES)
        if any(term in normalized_question for term in LOCATION_HINTS):
            return any(
                term in normalized_faq
                for term in ["onde", "localizada", "localizado", "endereco", "contato", "telefone", "email", "fica"]
            )
        if any(term in normalized_question for term in ACTION_HINTS):
            return any(
                term in normalized_faq
                for term in ["faz", "funcao", "objetivo", "objetivos", "papel", "competencia", "atribu", "promove", "contribui", "atua"]
            )
        return False

    def _extract_subject_keywords(self, text: str) -> list[str]:
        keywords = self._extract_keywords(text)
        return [
            keyword for keyword in keywords
            if keyword not in ACTION_HINTS
            and keyword not in {"objetivo", "objetivos", "papel", "funcao", "diferenca"}
            and keyword not in GENERIC_SUBJECTS
        ]

    def _pick_primary_subject(self, keywords: list[str]) -> str:
        for entity in PRIORITY_ENTITIES:
            if entity in keywords:
                return entity
        return keywords[0] if keywords else ""

    def _rerank_documents(self, question: str, docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        keywords = self._extract_keywords(question)
        ranked = []

        for doc in docs:
            text = " ".join(
                str(value)
                for value in [
                    doc.get("title", ""),
                    doc.get("faq_question", ""),
                    doc.get("faq_answer", ""),
                    doc.get("text", ""),
                    doc.get("category", ""),
                ]
            ).lower()
            keyword_hits = sum(1 for keyword in keywords if keyword in text)
            document_boost = 0.12 if doc.get("doc_type") == "document" else 0.0
            exact_question_boost = 0.45 if self._normalize_text(doc.get("faq_question", "")) == self._normalize_text(question) else 0.0
            doc["score"] = float(doc.get("score", 0.0)) + keyword_hits * 0.08 + document_boost + exact_question_boost
            ranked.append(doc)

        ranked.sort(key=lambda item: item.get("score", 0.0), reverse=True)
        return ranked

    def _select_faq_match(self, question: str, docs: list[dict[str, Any]]) -> dict[str, Any] | None:
        if not docs:
            return None

        normalized_question = self._normalize_text(question)
        keywords = set(self._extract_keywords(normalized_question))

        for doc in docs:
            faq_question = self._normalize_text(doc.get("faq_question", ""))
            overlap = sum(1 for keyword in keywords if keyword in faq_question)

            if normalized_question == faq_question:
                return doc
            if overlap >= 3 and doc.get("score", 0.0) >= 0.85 and self._faq_matches_intent(faq_question, normalized_question):
                return doc
        return None

    def _format_faq_answer(self, answer: str) -> str:
        cleaned = answer.strip()
        if not cleaned:
            return "Nao encontrei uma resposta clara para isso na base atual."
        return self._humanize_answer(cleaned)

    def _build_llm_answer(self, question: str, docs: list[dict[str, Any]], fallback_answer: str) -> str:
        snippets = "\n\n".join(
            f"Fonte: {doc['source']}\nTrecho: {self._excerpt(doc.get('faq_answer') or doc.get('text', ''), 500)}"
            for doc in docs[:4]
        )
        prompt = f"""Voce esta ajudando a redigir uma resposta curta, natural e conversacional em portugues.
Fale como uma pessoa explicando para outra, sem mencionar anexos, trechos, base ou contexto.
Use apenas as informacoes dos trechos abaixo.
Se os trechos nao forem suficientes, preserve a resposta de fallback.

Pergunta:
{question}

Resposta de fallback:
{fallback_answer}

Trechos:
{snippets}

Resposta final:"""
        return self.llm.generate_response(prompt).strip()

    def _build_extractive_answer(self, question: str, docs: list[dict[str, Any]]) -> str:
        if not docs:
            return "Nao encontrei informacoes suficientes na base atual para responder com seguranca."

        keywords = self._extract_keywords(question)
        subject_keywords = self._extract_subject_keywords(question)
        is_definition_question = any(
            self._normalize_text(question).startswith(prefix) for prefix in DEFINITION_PREFIXES
        )
        candidate_sentences: list[tuple[float, str]] = []

        for doc in docs:
            doc_score = float(doc.get("score", 0.0))
            for sentence in self._split_sentences(doc.get("text", "")):
                if self._looks_like_noise(sentence):
                    continue
                score = self._score_sentence(
                    sentence,
                    keywords,
                    subject_keywords,
                    doc_score,
                    is_definition_question,
                )
                if score > 0:
                    candidate_sentences.append((score, sentence.strip()))

        candidate_sentences.sort(key=lambda item: item[0], reverse=True)

        selected: list[str] = []
        selected_normalized = set()
        for _, sentence in candidate_sentences:
            normalized = sentence.lower()
            if normalized in selected_normalized:
                continue
            cleaned_sentence = self._clean_sentence(sentence)
            if not cleaned_sentence or self._looks_like_noise(cleaned_sentence):
                continue
            selected.append(cleaned_sentence)
            selected_normalized.add(normalized)
            if len(selected) == 3:
                break

        if not selected:
            return "Nao encontrei uma resposta confiavel na base atual para essa pergunta. Se quiser, voce pode reformular ou perguntar de forma mais especifica."

        first = selected[0] if selected else "Nao encontrei uma resposta clara."
        others = [item for item in selected[1:] if item]

        response_parts = [first]
        if others:
            response_parts.append(f"Além disso, {others[0][0].lower() + others[0][1:]}" if len(others[0]) > 1 else others[0])
        if len(others) > 1:
            response_parts.append(f"Tambem vale destacar que {others[1][0].lower() + others[1][1:]}" if len(others[1]) > 1 else others[1])

        return " ".join(part.strip() for part in response_parts if part.strip()).strip()

    def _looks_like_noise(self, text: str) -> bool:
        compact = re.sub(r"\s+", " ", text.strip())
        if not compact:
            return True

        if any(marker in compact for marker in ["|", "+----", "====", "picture", "start of picture text", "end of picture text"]):
            return True

        letters = sum(1 for char in compact if char.isalpha())
        digits = sum(1 for char in compact if char.isdigit())
        punctuation = sum(1 for char in compact if char in "|+-_=:/\\[]{}")

        if letters < 20:
            return True
        if punctuation > letters * 0.35:
            return True
        if digits > letters and letters < 60:
            return True

        lowered = compact.lower()
        noise_fragments = [
            "relatorio anual",
            "agradece em especial",
            "pagina ",
            "gps :",
            "quadro 1",
            "procedimentos de",
            "plano orcamentario",
            "definicao por referencia",
        ]
        if any(fragment in lowered for fragment in noise_fragments) and "agipi" not in lowered and "ageuni" not in lowered:
            return True

        return False

    def _clean_sentence(self, sentence: str) -> str:
        cleaned = re.sub(r"\s+", " ", sentence.strip())
        cleaned = re.sub(
            r"^(?:e|mas|alem disso|tambem|no entanto|por outro lado)\s+",
            "",
            self._display_text(cleaned),
            flags=re.IGNORECASE,
        )
        return self._humanize_answer(cleaned)

    def _humanize_answer(self, text: str) -> str:
        cleaned = re.sub(r"\s+", " ", text.strip())
        cleaned = re.sub(
            r"^(?:nos documentos(?: da uepg)?(?: analisados)?[,:\s]+|os documentos(?: da uepg)?(?: mostram| indicam| informam)?[,:\s]+|de acordo com (?:os )?documentos[,:\s]+)",
            "",
            self._display_text(cleaned),
            flags=re.IGNORECASE,
        )
        cleaned = re.sub(r"^(?:sim\.\s*)", "", cleaned, flags=re.IGNORECASE)
        cleaned = cleaned.strip(" .")
        if not cleaned:
            return text.strip()
        return cleaned[0].upper() + cleaned[1:] + ("." if cleaned[-1] not in ".!?" else "")

    def _extract_keywords(self, text: str) -> list[str]:
        normalized = self._normalize_text(text.lower())
        tokens = re.findall(r"\b[\w-]{3,}\b", normalized)
        return [token for token in tokens if token not in STOPWORDS]

    def _split_sentences(self, text: str) -> list[str]:
        compact_text = re.sub(r"\s+", " ", text.strip())
        compact_text = self._display_text(compact_text)
        sentences = re.split(r"(?<=[.!?])\s+|(?<=:)\s+|;\s+", compact_text)
        return [sentence for sentence in sentences if len(sentence.strip()) >= 30]

    def _score_sentence(
        self,
        sentence: str,
        keywords: list[str],
        subject_keywords: list[str],
        doc_score: float,
        is_definition_question: bool,
    ) -> float:
        sentence_lower = sentence.lower()
        keyword_hits = sum(1 for keyword in keywords if keyword in sentence_lower)
        if keyword_hits == 0 and keywords:
            return 0.0

        subject_hits = sum(1 for keyword in subject_keywords if keyword in sentence_lower)
        if subject_keywords and subject_hits == 0:
            return 0.0

        definition_bonus = 0.0
        if is_definition_question:
            if "(" in sentence and ")" in sentence:
                definition_bonus += 0.8
            if any(marker in sentence_lower for marker in [" e a ", " e o ", " consiste em", " trata-se", " corresponde a"]):
                definition_bonus += 0.8
            if subject_hits:
                definition_bonus += subject_hits * 0.9

        length_bonus = min(len(sentence) / 220, 1.0)
        return keyword_hits * 1.5 + subject_hits * 1.8 + doc_score * 2 + length_bonus + definition_bonus

    def _excerpt(self, text: str, limit: int = 280) -> str:
        compact_text = re.sub(r"\s+", " ", text.strip())
        if len(compact_text) <= limit:
            return compact_text
        return compact_text[: limit - 3].rstrip() + "..."

    def _display_text(self, text: str) -> str:
        fixed = text
        replacements = {
            "??": "?", "??": "?", "??": "?", "??": "?",
            "??": "?", "??": "?",
            "??": "?",
            "??": "?", "??": "?", "??": "?",
            "??": "?",
            "??": "?",
            "??": "?", "??": "?", "??": "?", "??": "?",
            "??": "?", "??": "?",
            "??": "?",
            "??": "?", "??": "?", "??": "?",
            "??": "?",
            "??": "?",
            "???": "?", "???": "?", "???": """, "???": """, "???": "'", "???": "'",
            "??": "?", "??": "?",
        }
        for broken, repaired in replacements.items():
            fixed = fixed.replace(broken, repaired)
        return fixed

    def _normalize_text(self, text: str) -> str:
        fixed = self._display_text(text)
        decomposed = unicodedata.normalize("NFKD", fixed)
        return "".join(char for char in decomposed if not unicodedata.combining(char))
