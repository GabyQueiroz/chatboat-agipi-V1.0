import { useEffect, useRef, useState } from "react";
import UserCard from "./components/UserCard"
import FeedbackBar from "./components/FeedbackBar"

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";
const REQUEST_TIMEOUT_MS = 25000;
const SUGGESTION_POOL = [
    {
        title: "AGEUNI",
        description: "Entenda o programa e seus objetivos.",
        prompt: "O que e o programa AGEUNI?",
    },
    {
        title: "AGIPI",
        description: "Veja o papel da agencia dentro da UEPG.",
        prompt: "O que e AGIPI?",
    },
    {
        title: "Registro de software",
        description: "Saiba como funciona o fluxo institucional.",
        prompt: "Como registrar um software?",
    },
    {
        title: "Incubadora",
        description: "Descubra como a incubacao funciona.",
        prompt: "Qual o papel da incubadora da AGIPI?",
    },
    {
        title: "NITs",
        description: "Entenda o papel dos nucleos de inovacao.",
        prompt: "O que sao NITs nas universidades?",
    },
    {
        title: "Lei de Inovacao",
        description: "Veja como ela se aplica nas universidades.",
        prompt: "O que diz a Lei de Inovacao sobre NITs?",
    },
    {
        title: "Universidade e empresa",
        description: "Explore a cooperacao com o setor produtivo.",
        prompt: "Como universidades interagem com empresas?",
    },
    {
        title: "INPROTEC",
        description: "Conheca a incubadora vinculada a AGIPI.",
        prompt: "O que e o INPROTEC?",
    },
    {
        title: "Startups",
        description: "Veja como a universidade apoia novos negocios.",
        prompt: "Como funciona o processo de incubacao?",
    },
    {
        title: "Servicos da AGIPI",
        description: "Confira os principais apoios oferecidos.",
        prompt: "Quais sao os principais servicos oferecidos pela AGIPI?",
    },
];

function formatScore(score) {
    return `${Math.round(score * 100)}%`;
}

function SourceCard({ source }) {
    return (
        <article className="rounded-2xl border border-slate-200 bg-white/90 p-4 shadow-sm">
            <div className="mb-2 flex items-start justify-between gap-3">
                <div>
                    <p className="text-xs uppercase tracking-[0.18em] text-slate-400">Fonte</p>
                    <h3 className="mt-1 text-sm font-semibold text-slate-900">{source.title || source.source}</h3>
                </div>
                <span className="rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-semibold text-emerald-700">
                    {formatScore(source.score || 0)}
                </span>
            </div>
            <p className="text-sm leading-6 text-slate-600">{source.excerpt || "Trecho nao disponivel."}</p>
            <p className="mt-3 break-all text-xs text-slate-400">{source.source}</p>
        </article>
    );
}

function AssistantMessage({ message, view, sessionData }) {
    const isError = message.role === "error";
    const statusClass = isError
        ? "border-rose-200 bg-rose-50 text-rose-700"
        : "border-slate-200 bg-white text-slate-800";

    return (
        <div className="flex max-w-3xl gap-3">
            <div className={`mt-1 flex h-9 w-9 shrink-0 items-center justify-center rounded-2xl text-xs font-bold ${isError ? "bg-rose-600 text-white" : "bg-slate-900 text-white"}`}>
                {isError ? "!" : "AI"}
            </div>
            <div className="flex-1 space-y-3">
                <div className="flex items-center gap-3 text-xs uppercase tracking-[0.18em] text-slate-400">
                    <span>{isError ? "Falha" : "Assistente"}</span>
                    <span>{message.timestamp}</span>
                </div>
                {view === "sources" && message.sources?.length > 0 && !isError ? (
                    <div className="grid gap-3 md:grid-cols-2">
                        {message.sources.map((source) => (
                            <SourceCard key={source.id} source={source} />
                        ))}
                    </div>
                ) : (
                    <div className={`rounded-[1.75rem] rounded-tl-sm border p-5 shadow-sm ${statusClass}`}>
                        <p className="whitespace-pre-wrap text-sm leading-7">{message.text}</p>
                        {message.warnings?.length ? (
                            <div className="mt-4 space-y-1 text-xs text-amber-700">
                                {message.warnings.map((warning) => (
                                    <p key={warning}>Aviso: {warning}</p>
                                ))}
                            </div>
                        ) : null}
                    </div>
                )}
                {!isError && sessionData && (
                    <FeedbackBar
                        interactionId={message.interactionId}
                        sessionId={sessionData.sessionId}
                        onFeedbackUpdate={() => {
                            // Handle feedback update if needed
                        }}
                    />
                )}
            </div>
        </div>
    );
}

function UserMessage({ message }) {
    return (
        <div className="flex justify-end">
            <div className="max-w-2xl rounded-[1.75rem] rounded-tr-sm border border-sky-100 bg-sky-50 px-5 py-4 shadow-sm">
                <p className="text-sm leading-7 text-slate-800">{message.content}</p>
                <p className="mt-2 text-right text-xs uppercase tracking-[0.18em] text-slate-400">{message.timestamp}</p>
            </div>
        </div>
    );
}

function getRandomSuggestions(count = 5) {
    const pool = [...SUGGESTION_POOL];
    const selected = [];

    while (pool.length > 0 && selected.length < count) {
        const index = Math.floor(Math.random() * pool.length);
        selected.push(pool.splice(index, 1)[0]);
    }

    return selected;
}

export default function App() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [view, setView] = useState("answer");
    const [isSending, setIsSending] = useState(false);
    const [suggestions] = useState(() => getRandomSuggestions());
    const [sessionData, setSessionData] = useState(null);

    const textareaRef = useRef(null);
    const bottomRef = useRef(null);

    useEffect(() => {
        const savedSession = sessionStorage.getItem("app_session")
        if (savedSession) {
            setSessionData(JSON.parse(savedSession));
        }
    }, []);

    const handleLogin = (userName) => {
        const newSession = {
            userName: userName.trim(),
            sessionId: window.crypto && crypto.randomUUID ? crypto.randomUUID() : Date.now().toString(36) + Math.random().toString(36).substring(2),
        };

        setSessionData(newSession);
        sessionStorage.setItem("app_session", JSON.stringify(newSession));
    };

    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages, isSending, view]);

    function resizeTextarea() {
        const element = textareaRef.current;
        if (!element) return;
        element.style.height = "auto";
        element.style.height = `${Math.min(element.scrollHeight, 180)}px`;
    }

    function buildErrorMessage(error) {
        if (error.name === "AbortError") {
            return "A resposta demorou mais do que o esperado. Verifique se o backend esta ativo e se o indice ja terminou de carregar.";
        }
        return error.message || "Nao foi possivel completar a consulta.";
    }

    function buildHistoryPayload(currentMessages) {
        return currentMessages
            .filter((message) => message.role === "user" || message.role === "assistant")
            .slice(-6)
            .map((message) => ({
                role: message.role,
                content: message.role === "user" ? message.content : message.text,
            }));
    }

    async function handleSend() {
        const trimmed = input.trim();
        if (!trimmed || isSending) return;

        const interactionId = window.crypto && crypto.randomUUID ? crypto.randomUUID() : Date.now().toString(36) + Math.random().toString(36).substring(2);

        const userMessage = {
            id: `user-${Date.now()}`,
            role: "user",
            content: trimmed,
            interactionId: interactionId,
            timestamp: new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" }),
        };

        const nextMessages = [...messages, userMessage];
        setMessages(nextMessages);
        setInput("");
        if (textareaRef.current) {
            textareaRef.current.style.height = "auto";
        }
        setIsSending(true);

        const controller = new AbortController();
        const timeoutId = window.setTimeout(() => controller.abort(), REQUEST_TIMEOUT_MS);

        try {
            const response = await fetch(`${API_BASE_URL}/chat`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    question: trimmed,
                    history: buildHistoryPayload(nextMessages),
                    user_name: sessionData.userName,
                    session_id: sessionData.sessionId,
                    interaction_id: interactionId,
                }),
                signal: controller.signal,
            });

            const data = await response.json();
            if (!response.ok) {
                throw new Error(data?.detail || `Erro na API: ${response.status}`);
            }

            const assistantMessage = {
                id: `assistant-${Date.now()}`,
                role: "assistant",
                text: data.answer,
                interactionId: interactionId,
                timestamp: new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" }),
                warnings: data.warnings || [],
                sources: data.sources || [],
            };

            setMessages((current) => [...current, assistantMessage]);
        } catch (error) {
            setMessages((current) => [
                ...current,
                {
                    id: `error-${Date.now()}`,
                    role: "error",
                    text: buildErrorMessage(error),
                    interactionId: interactionId,
                    timestamp: new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" }),
                    warnings: [],
                    sources: [],
                },
            ]);
        } finally {
            window.clearTimeout(timeoutId);
            setIsSending(false);
        }
    }

    function handleKeyDown(event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            handleSend();
        }
    }

    return (
        <div className="min-h-screen bg-[radial-gradient(circle_at_top_left,_rgba(14,165,233,0.14),_transparent_28%),linear-gradient(180deg,_#f8fafc_0%,_#eef2ff_100%)] text-slate-900">
            <div className="mx-auto min-h-screen max-w-6xl px-4 py-6 lg:px-8">
                {!sessionData && (
                    <UserCard onLogin={handleLogin} />
                )}

                <main className="flex min-h-[88vh] flex-col overflow-hidden rounded-[2rem] border border-white/60 bg-white/70 shadow-[0_24px_80px_rgba(15,23,42,0.08)] backdrop-blur">
                    <header className="border-b border-slate-200/80 px-6 py-5">
                        <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
                            <div>
                                <p className="text-xs uppercase tracking-[0.26em] text-sky-600">AGIPI knowledge assistant</p>
                                <h1 className="mt-2 text-2xl font-semibold tracking-tight text-slate-950">Assistente documental rapido e pronto para publicacao</h1>
                            </div>
                            <div className="flex rounded-full border border-slate-200 bg-slate-100 p-1 text-sm">
                                <button
                                    className={`rounded-full px-4 py-2 transition ${view === "answer" ? "bg-white text-slate-900 shadow-sm" : "text-slate-500"}`}
                                    onClick={() => setView("answer")}
                                >
                                    Resposta
                                </button>
                                <button
                                    className={`rounded-full px-4 py-2 transition ${view === "sources" ? "bg-white text-slate-900 shadow-sm" : "text-slate-500"}`}
                                    onClick={() => setView("sources")}
                                >
                                    Fontes
                                </button>
                            </div>
                        </div>
                    </header>

                    <section className="flex-1 space-y-6 overflow-y-auto px-6 py-6">
                        {messages.length === 0 ? (
                            <div className="flex h-full flex-col items-center justify-center text-center">
                                <div className="inline-flex rounded-full bg-sky-100 px-3 py-1 text-xs font-semibold uppercase tracking-[0.24em] text-sky-700">
                                    consulta guiada
                                </div>
                                <h2 className="mt-6 text-3xl font-semibold tracking-tight text-slate-950">Pergunte com base na sua base documental</h2>
                                <p className="mt-4 max-w-xl text-sm leading-7 text-slate-500">
                                    Pergunte sobre AGEUNI, AGIPI, EPITEC, inovacao universitaria, incubacao, NITs e documentos institucionais da UEPG.
                                </p>
                                <div className="mt-8 grid w-full max-w-4xl gap-3 md:grid-cols-2">
                                    {suggestions.map((suggestion) => (
                                        <button
                                            key={suggestion.prompt}
                                            className="rounded-[1.5rem] border border-slate-200 bg-white p-4 text-left shadow-sm transition hover:border-sky-300 hover:shadow-md"
                                            onClick={() => setInput(suggestion.prompt)}
                                        >
                                            <p className="text-sm font-semibold text-slate-900">{suggestion.title}</p>
                                            <p className="mt-1 text-sm leading-6 text-slate-500">{suggestion.description}</p>
                                            <p className="mt-3 text-sm text-sky-700">{suggestion.prompt}</p>
                                        </button>
                                    ))}
                                </div>
                            </div>
                        ) : (
                            messages.map((message) => (
                                message.role === "user"
                                    ? <UserMessage key={message.id} message={message} />
                                    : <AssistantMessage key={message.id} message={message} view={view} sessionData={sessionData} />
                            ))
                        )}

                        {isSending ? (
                            <div className="flex max-w-3xl gap-3">
                                <div className="mt-1 flex h-9 w-9 shrink-0 items-center justify-center rounded-2xl bg-slate-900 text-xs font-bold text-white">AI</div>
                                <div className="rounded-[1.75rem] rounded-tl-sm border border-slate-200 bg-white px-5 py-4 shadow-sm">
                                    <div className="flex gap-2">
                                        <span className="h-2.5 w-2.5 animate-bounce rounded-full bg-sky-500 [animation-delay:-0.2s]" />
                                        <span className="h-2.5 w-2.5 animate-bounce rounded-full bg-sky-500 [animation-delay:-0.1s]" />
                                        <span className="h-2.5 w-2.5 animate-bounce rounded-full bg-sky-500" />
                                    </div>
                                </div>
                            </div>
                        ) : null}

                        <div ref={bottomRef} />
                    </section>

                    <section className="border-t border-slate-200/80 px-6 py-5">
                        <div className="rounded-[1.75rem] border border-slate-200 bg-white p-3 shadow-sm">
                            <div className="flex items-end gap-3">
                                <textarea
                                    ref={textareaRef}
                                    className="min-h-[52px] flex-1 resize-none border-0 bg-transparent px-2 py-2 text-sm leading-6 text-slate-800 outline-none placeholder:text-slate-400"
                                    placeholder="Digite sua pergunta sobre os documentos..."
                                    rows={1}
                                    value={input}
                                    onChange={(event) => {
                                        setInput(event.target.value);
                                        resizeTextarea();
                                    }}
                                    onKeyDown={handleKeyDown}
                                    disabled={!sessionData || isSending}
                                />
                                <button
                                    className="inline-flex h-11 w-11 items-center justify-center rounded-2xl bg-slate-900 text-white transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:bg-slate-300"
                                    disabled={!sessionData || !input.trim() || isSending}
                                    onClick={handleSend}
                                >
                                    <svg className="h-4 w-4" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                        <line x1="2" y1="8" x2="13" y2="8" />
                                        <polyline points="9,4 13,8 9,12" />
                                    </svg>
                                </button>
                            </div>
                            <p className="mt-2 px-2 text-xs uppercase tracking-[0.18em] text-slate-400">Enter envia. Shift + Enter cria nova linha.</p>
                        </div>
                    </section>
                </main>

            </div>
        </div>
    );
}
