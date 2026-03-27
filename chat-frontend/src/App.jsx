import { useState, useRef, useEffect } from "react";
import { MOCK_MESSAGES } from "./mock/mockMessages";

function ScoreBar({ score }) {
    return (
        <div className="flex items-center gap-2 mt-2 w-full">
            <div className="flex-1 h-1.5 bg-gray-200 rounded overflow-hidden">
                <div
                    className="h-full bg-blue-500 rounded transition-all duration-500"
                    style={{ width: `${score * 100}%` }}
                />
            </div>
        </div>
    );
}

function DocCard({ doc }) {
    const scoreClass = doc.score >= 0.9 ? "text-green-600 bg-green-50" : doc.score >= 0.8 ? "text-yellow-600 bg-yellow-50" : "text-gray-600 bg-gray-100";

    return (
        <div className="border border-gray-300 rounded-lg p-3 bg-white hover:bg-gray-50 transition-colors">
            <div className="flex justify-between items-start gap-3 mb-2">
                <div className="font-semibold text-sm text-gray-800 break-all">{doc.source}</div>
            </div>
            <div className="w-25 bg-gray-100 border border-gray-200 px-1.5 rounded text-[10px]">
                {doc.id}
            </div>
        </div>
        // <div className="border border-gray-300 rounded-lg p-3 bg-white hover:bg-gray-50 transition-colors">
        //     <div className="flex justify-between items-start gap-3 mb-2">
        //         <div className="font-semibold text-sm text-gray-800">{doc.title}</div>
        //         <div className={`text-xs font-medium px-2 py-1 rounded border border-transparent ${scoreClass}`}>
        //             {(doc.score * 100).toFixed(0)}%
        //         </div>
        //     </div>

        //     <div className="text-xs text-gray-600 border-l-2 border-gray-300 pl-2 mb-3">
        //         "{doc.excerpt}"
        //     </div>

        //     <ScoreBar score={doc.score} />

        //     <div className="flex flex-wrap gap-3 mt-3 text-xs text-gray-500">
        //         <div className="flex items-center gap-1">
        //             <svg className="w-3 h-3" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
        //                 <rect x="2" y="1" width="12" height="14" rx="1.5" />
        //                 <line x1="5" y1="5" x2="11" y2="5" />
        //                 <line x1="5" y1="8" x2="11" y2="8" />
        //                 <line x1="5" y1="11" x2="8" y2="11" />
        //             </svg>
        //             {doc.source}
        //         </div>
        //         <div className="flex items-center gap-1">
        //             <svg className="w-3 h-3" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
        //                 <path d="M8 2L10 6H14L11 9L12 13L8 11L4 13L5 9L2 6H6L8 2Z" />
        //             </svg>
        //             Pág. {doc.page}
        //         </div>
        //         <div className="flex items-center gap-1">
        //             <svg className="w-3 h-3" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5">
        //                 <rect x="2" y="3" width="12" height="10" rx="1.5" />
        //                 <line x1="5" y1="6.5" x2="11" y2="6.5" />
        //                 <line x1="5" y1="9.5" x2="9" y2="9.5" />
        //             </svg>
        //             {doc.tokens} tokens
        //         </div>
        //         <div className="bg-gray-100 border border-gray-200 px-1.5 rounded text-[10px]">
        //             {doc.id}
        //         </div>
        //     </div>
        // </div>
    );
}

function Message({ msg, viewMode }) {
    if (msg.role === "user") {
        return (
            <div className="flex justify-end">
                <div className="bg-blue-50 border border-blue-100 rounded-2xl rounded-tr-sm p-3 max-w-[75%]">
                    <div className="text-sm text-gray-800">{msg.content}</div>
                    <div className="text-[10px] text-gray-400 mt-1 text-right">{msg.timestamp}</div>
                </div>
            </div>
        );
    }

    return (
        <div className="flex flex-col gap-2">
            <div className="flex items-center gap-2">
                <div className="w-6 h-6 rounded bg-gray-800 text-white flex items-center justify-center text-[10px] font-bold shrink-0">
                    AI
                </div>
                <div className="text-[10px] text-gray-500 uppercase tracking-wider">
                    IA · {msg.timestamp}
                </div>
            </div>

            {viewMode === "text" ? (
                <div className="bg-white border border-gray-200 rounded-2xl rounded-tl-sm p-4 max-w-[85%]">
                    <div className="text-sm text-gray-800 leading-relaxed">{msg.text}</div>
                </div>
            ) : (
                <div className="flex flex-col gap-3 max-w-[85%]">
                    <div className="flex items-center gap-2 text-[10px] text-gray-500 uppercase tracking-wide">
                        <span className="whitespace-nowrap">{msg.documents.length} documentos recuperados</span>
                        <div className="flex-1 h-px bg-gray-200" />
                    </div>
                    {msg.documents.map((doc) => (
                        <DocCard key={doc.id} doc={doc} />
                    ))}
                </div>
            )}
        </div>
    );
}

const App = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [viewMode, setViewMode] = useState("text");
    const [isTyping, setIsTyping] = useState(false);

    const textareaRef = useRef(null);
    const bottomRef = useRef(null);

    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }, [messages, isTyping, viewMode]);

    const autoResize = () => {
        const ta = textareaRef.current;
        if (!ta) return;
        ta.style.height = "auto";
        ta.style.height = Math.min(ta.scrollHeight, 120) + "px";
    };

    const handleSend = async () => {
        const trimmed = input.trim();
        if (!trimmed) return;

        const userMsg = {
            id: Date.now(),
            role: "user",
            content: trimmed,
            timestamp: new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" }),
        };

        setMessages((prev) => [...prev, userMsg]);
        setInput("");

        if (textareaRef.current) textareaRef.current.style.height = "auto";
        setIsTyping(true);

        try {
            const response = await fetch("http://localhost:8000/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ "question": userMsg.content })
            });

            if (!response.ok) {
                const errorData = await response.json();
                console.error("Erro da API:", errorData);
                throw new Error(`Erro na API: ${response.status}`);
            }

            const data = await response.json();

            let sources = [];
            if (data && data.sources.length > 0) {
                data.sources.map((source) => {
                    sources.push({
                        id: "[TESTE] doc_" + Math.floor(Math.random() * 999).toString().padStart(4, "0"),
                        title: "[TESTE] Documento de exemplo — " + trimmed.slice(0, 30),
                        source: source,
                        score: 0.88 + Math.random() * 0.1,
                        excerpt: "[TESTE] Trecho relevante do documento recuperado pelo índice FAISS para responder à consulta do usuário...",
                        page: Math.floor(Math.random() * 200) + 1,
                        tokens: Math.floor(Math.random() * 400) + 128,
                    });
                });
            }
            const aiMsg = {
                id: Date.now() + 1,
                role: "assistant",
                timestamp: new Date().toLocaleTimeString("pt-BR", { hour: "2-digit", minute: "2-digit" }),
                text: data?.answer || "Resposta indisponível",
                documents: sources,
            };
            setMessages((prev) => [...prev, aiMsg]);
        } catch (error) {
            console.log(error);
        } finally {
            setIsTyping(false);
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };

    const suggestions = ["O que é RAG?", "Como funciona FAISS?", "Explique embeddings"];

    return (
        <div className="flex flex-col h-screen max-w-4xl mx-auto bg-gray-50 font-sans text-gray-900">
            {/* Header */}
            <header className="flex items-center justify-between p-4 bg-white border-b border-gray-200 shrink-0">
                <div className="flex items-center gap-3">
                    <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
                    <div>
                        <div className="font-bold text-sm uppercase tracking-wider text-gray-800">[TESTE] ASSISTENTE AGIPI</div>
                        {/* <div className="text-[10px] text-gray-500 font-mono">FAISS INDEX · ACTIVE</div> */}
                    </div>
                </div>

                <div className="flex bg-gray-100 border border-gray-200 rounded-lg p-1 gap-1">
                    <button
                        className={`flex items-center gap-2 px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${viewMode === "text" ? "bg-white text-blue-600 shadow-sm border border-gray-200" : "text-gray-500 hover:text-gray-800"}`}
                        onClick={() => setViewMode("text")}
                    >
                        Resposta
                    </button>
                    <button
                        className={`flex items-center gap-2 px-3 py-1.5 rounded-md text-xs font-medium transition-colors ${viewMode === "docs" ? "bg-white text-blue-600 shadow-sm border border-gray-200" : "text-gray-500 hover:text-gray-800"}`}
                        onClick={() => setViewMode("docs")}
                    >
                        Documentos
                    </button>
                </div>
            </header>

            {/* Area de Mensagens */}
            <div className="flex-1 overflow-y-auto p-4 md:p-6 flex flex-col gap-6">
                {messages.length === 0 ? (
                    <div className="flex-1 flex flex-col items-center justify-center gap-4 text-center opacity-70">
                        <div className="text-gray-400 mb-2">
                            <svg className="w-12 h-12" viewBox="0 0 48 48" fill="none" stroke="currentColor" strokeWidth="1.5">
                                <circle cx="24" cy="24" r="20" />
                                <path d="M16 24 Q24 16 32 24 Q24 32 16 24Z" />
                                <circle cx="24" cy="24" r="3" fill="currentColor" />
                            </svg>
                        </div>
                        <div className="font-bold text-sm uppercase tracking-wide text-gray-600">Início da Sessão</div>
                        <div className="text-xs text-gray-500 max-w-xs">Faça uma pergunta para testar a IA com recuperação por índice FAISS</div>
                        <div className="flex flex-wrap justify-center gap-2 mt-4">
                            {suggestions.map((s) => (
                                <button key={s} className="px-3 py-1.5 rounded-full border border-gray-300 text-xs text-gray-600 hover:border-blue-500 hover:text-blue-600 hover:bg-blue-50 transition-colors" onClick={() => setInput(s)}>
                                    {s}
                                </button>
                            ))}
                        </div>
                    </div>
                ) : (
                    <>
                        {messages.map((msg) => (
                            <Message key={msg.id} msg={msg} viewMode={viewMode} />
                        ))}
                        {isTyping && (
                            <div className="flex items-center gap-2">
                                <div className="w-6 h-6 rounded bg-gray-800 text-white flex items-center justify-center text-[10px] font-bold shrink-0">AI</div>
                                <div className="flex gap-1 bg-white border border-gray-200 rounded-full px-3 py-2">
                                    <div className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                                    <div className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                                    <div className="w-1.5 h-1.5 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                                </div>
                            </div>
                        )}
                    </>
                )}
                <div ref={bottomRef} />
            </div>

            {/* Input */}
            <div className="p-4 bg-white border-t border-gray-200 shrink-0">
                <div className="flex items-end gap-2 bg-gray-50 border border-gray-300 rounded-xl p-2 focus-within:border-blue-400 focus-within:ring-1 focus-within:ring-blue-400 transition-all">
                    <textarea
                        ref={textareaRef}
                        className="flex-1 bg-transparent border-none outline-none text-sm text-gray-800 resize-none max-h-32 overflow-y-auto px-2 py-1 placeholder-gray-400"
                        placeholder="Faça uma pergunta para a IA…"
                        value={input}
                        onChange={(e) => { setInput(e.target.value); autoResize(); }}
                        onKeyDown={handleKeyDown}
                        rows={1}
                    />
                    <button
                        className="w-8 h-8 flex items-center justify-center rounded-lg bg-blue-600 text-white hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed shrink-0 transition-colors cursor-pointer"
                        onClick={handleSend}
                        disabled={!input.trim() || isTyping}
                    >
                        <svg className="w-4 h-4" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <line x1="2" y1="8" x2="13" y2="8" />
                            <polyline points="9,4 13,8 9,12" />
                        </svg>
                    </button>
                </div>
                <div className="text-[10px] text-gray-400 mt-2 px-1 text-center">
                    Enter para enviar · Shift+Enter para nova linha
                </div>
            </div>
        </div>
    );
}

export default App
