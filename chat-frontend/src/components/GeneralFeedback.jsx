import { useState } from "react";
import { createPortal } from "react-dom";

import { FiMessageSquare } from "react-icons/fi";

export default function GeneralFeedback({ sessionId, isSidebarOpen, API_BASE_URL }) {
    const [isOpen, setIsOpen] = useState(false);
    const [submitted, setSubmitted] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    const [formData, setFormData] = useState({
        precision_rating: "",
        interface_suggestions: "",
        missing_features: ""
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        console.log(formData)
        try {
            const res = await fetch(`${API_BASE_URL}/chat/${sessionId}/feedback`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData)
            });
            if (res.ok) {
                setSubmitted(true);
                setTimeout(() => setIsOpen(false), 2000);
            }
        } catch (err) {
            alert("Erro ao enviar feedback.");
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <>
            <a
                href="#"
                className="inline-flex items-center hover:bg-slate-100 w-full gap-3 px-3 py-2 whitespace-nowrap"
                onClick={(e) => {
                    e.preventDefault();
                    setIsOpen(true);
                }}
            >
                <FiMessageSquare className="shrink-0" size={24} />
                {isSidebarOpen && "Feedback"}
            </a>

            {isOpen && createPortal(
                <div className="fixed inset-0 bg-black/60 z-[60] flex items-center justify-center p-4 backdrop-blur-sm">
                    <div className="bg-white rounded-2xl shadow-2xl max-w-lg w-full p-8 relative">
                        <h2 className="text-2xl font-bold text-slate-900 mb-2">Sua opinião é importante</h2>
                        <p className="text-slate-500 mb-6 text-sm">Ajude-nos a melhorar o Assistente AGIPI.</p>

                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-1">
                                    Como avalia a precisão das respostas? *
                                </label>
                                <select
                                    required
                                    className="w-full border border-slate-200 rounded-lg p-2 text-sm focus:ring-2 focus:ring-sky-500"
                                    value={formData.question1}
                                    onChange={e => setFormData({ ...formData, question1: e.target.value })}
                                >
                                    <option value="">Selecione...</option>
                                    <option value="excelente">Excelente</option>
                                    <option value="boa">Boa</option>
                                    <option value="regular">Regular</option>
                                    <option value="ruim">Ruim</option>
                                </select>
                            </div>

                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-1">
                                    Sugestões para a interface (Opcional)
                                </label>
                                <textarea
                                    className="w-full border border-slate-200 rounded-lg p-2 text-sm h-20 resize-none"
                                    placeholder="O que mudaria no visual?"
                                    value={formData.question2}
                                    onChange={e => setFormData({ ...formData, question2: e.target.value })}
                                />
                            </div>

                            <div>
                                <label className="block text-sm font-semibold text-slate-700 mb-1">
                                    Funcionalidades que sentiu falta (Opcional)
                                </label>
                                <textarea
                                    className="w-full border border-slate-200 rounded-lg p-2 text-sm h-20 resize-none"
                                    placeholder="O que o robô deveria fazer e não faz?"
                                    value={formData.question3}
                                    onChange={e => setFormData({ ...formData, question3: e.target.value })}
                                />
                            </div>

                            <div className="flex gap-3 mt-6">
                                <button
                                    type="button"
                                    onClick={() => setIsOpen(false)}
                                    className="flex-1 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 rounded-lg transition cursor-pointer"
                                >
                                    Cancelar
                                </button>
                                <button
                                    type="submit"
                                    disabled={isLoading}
                                    className="flex-1 py-2 bg-sky-600 text-white text-sm font-medium rounded-lg hover:bg-sky-700 disabled:opacity-50 transition cursor-pointer"
                                >
                                    {isLoading ? "Enviando..." : "Enviar Feedback"}
                                </button>
                            </div>
                        </form>
                    </div>
                </div>,
                document.body
            )}
        </>
    );
}