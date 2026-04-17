import { useState } from "react";
import { createPortal } from "react-dom";
import { ThumbsUp, ThumbsDown, MessageSquareText } from "lucide-react";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

function FeedbackModal({ isOpen, comment, onCommentChange, onSubmit, onClose, isLoading }) {
    if (!isOpen) return null;

    return createPortal(
        <div className="fixed inset-0 bg-black/50 z-50 flex items-center justify-center p-4">
            <div className="bg-white rounded-2xl shadow-xl max-w-md w-full p-6">
                <h3 className="text-lg font-semibold text-slate-900 mb-4">Adicionar comentário</h3>
                <textarea
                    className="w-full border border-slate-200 rounded-lg p-3 text-sm resize-none focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent"
                    placeholder="Seu comentário..."
                    rows={5}
                    value={comment}
                    onChange={(e) => onCommentChange(e.target.value.slice(0, 5000))}
                    disabled={isLoading}
                />
                <p className="text-xs text-slate-400 mt-2">{comment.length}/5000</p>
                <div className="flex gap-2 mt-6">
                    <button
                        className="flex-1 rounded-lg border border-slate-200 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-50 transition disabled:opacity-50"
                        onClick={onClose}
                        disabled={isLoading}
                    >
                        Cancelar
                    </button>
                    <button
                        className="flex-1 rounded-lg bg-sky-600 text-white px-4 py-2 text-sm font-medium hover:bg-sky-700 transition disabled:opacity-50"
                        onClick={onSubmit}
                        disabled={isLoading}
                    >
                        {isLoading ? "Enviando..." : "Enviar"}
                    </button>
                </div>
            </div>
        </div>,
        document.body
    );
}

export default function FeedbackBar({ interactionId, sessionId, onFeedbackUpdate }) {
    const [relevance, setRelevance] = useState(0);
    const [comment, setComment] = useState("");
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [hasError, setHasError] = useState(false);

    const handleFeedbackSubmit = async (newRelevance) => {
        setIsLoading(true);
        setError(null);
        setHasError(false);

        try {
            const response = await fetch(
                `${API_BASE_URL}/chat/${sessionId}/${interactionId}/feedback`,
                {
                    method: "PATCH",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        relevance: newRelevance,
                        comment: comment,
                    }),
                }
            );

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData?.detail || `Erro ao atualizar feedback: ${response.status}`);
            }

            const data = await response.json();
            setRelevance(newRelevance);

            if (onFeedbackUpdate) {
                onFeedbackUpdate(data.feedback);
            }
        } catch (err) {
            setError(err.message || "Não foi possível atualizar o feedback");
            setHasError(true);
            console.error("Feedback error:", err);
        } finally {
            setIsLoading(false);
        }
    };

    const handleLike = () => handleFeedbackSubmit(1);
    const handleDislike = () => handleFeedbackSubmit(-1);
    const handleNeutral = () => handleFeedbackSubmit(0);

    const handleCommentSubmit = async () => {
        await handleFeedbackSubmit(relevance);
        setIsModalOpen(false);
    };

    return (
        <>
            <div className="flex items-center gap-2 mt-3 pt-3 border-t border-slate-200">
                <div className="ml-auto">
                    {!error && relevance !== 0 && (
                        <span className="text-xs text-slate-400 me-2">
                            Esta resposta foi útil?
                        </span>
                    )}
                    <button
                        className={`inline-flex h-8 w-8 items-center justify-center rounded-lg transition cursor-pointer ${relevance === 1
                            ? "bg-emerald-100 text-emerald-700"
                            : "text-slate-400 hover:bg-slate-100"
                            } disabled:opacity-50`}
                        onClick={handleLike}
                        disabled={isLoading}
                        title="Útil"
                    >
                        <ThumbsUp className="h-4 w-4" />
                    </button>

                    <button
                        className={`inline-flex h-8 w-8 items-center justify-center rounded-lg transition cursor-pointer ${relevance === -1
                            ? "bg-rose-100 text-rose-700"
                            : "text-slate-400 hover:bg-slate-100"
                            } disabled:opacity-50`}
                        onClick={handleDislike}
                        disabled={isLoading}
                        title="Não útil"
                    >
                        <ThumbsDown className="h-4 w-4" />
                    </button>

                    <button
                        className="inline-flex h-8 px-2 items-center justify-center rounded-lg text-slate-400 hover:bg-slate-100 transition text-xs font-medium disabled:opacity-50 cursor-pointer"
                        onClick={() => setIsModalOpen(true)}
                        disabled={isLoading}
                        title="Adicionar comentário"
                    >
                        <MessageSquareText className="h-4 w-4" />
                    </button>

                    {error && (
                        <span className="text-xs text-rose-600 ml-auto">{error}</span>
                    )}
                </div>
            </div>

            <FeedbackModal
                isOpen={isModalOpen}
                comment={comment}
                onCommentChange={setComment}
                onSubmit={handleCommentSubmit}
                onClose={() => setIsModalOpen(false)}
                isLoading={isLoading}
            />
        </>
    );
}