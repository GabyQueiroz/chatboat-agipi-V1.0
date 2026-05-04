import { useState } from "react";
import { createPortal } from "react-dom";
import { MessageSquarePlus } from "lucide-react";

export default function GeneralFeedback({ sessionId, API_BASE_URL }) {
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
            {!submitted && (
                <button 
                    onClick={() => setIsOpen(true)}
                    className="fixed bottom-6 right-6 bg-slate-900 text-white p-4 rounded-full shadow-2xl hover:scale-110 transition-transform z-40 flex items-center gap-2 cursor-pointer"
                    title="Dar feedback geral"
                >
                    <MessageSquarePlus size={24} />
                    <span className="hidden md:inline font-medium text-sm">Feedback</span>
                </button>
            )}

            {isOpen && createPortal(
                <div className="fixed inset-0 bg-black/60 z-[60] flex items-center justify-center p-4 backdrop-blur-sm">
                    <div className="bg-white rounded-2xl shadow-2xl max-w-lg w-full p-8 relative">
                        <h2 className="text-2xl font-bold text-slate-900 mb-2">Sua opinião é importante</h2>
                        <p className="text-slate-500 mb-6 text-sm">Ajude-nos a melhorar o Assistente AGIPI.</p>

                        {submitted ? (
                            <div className="py-10 text-center">
                                <div className="text-emerald-500 text-5xl mb-4">✓</div>
                                <h3 className="font-semibold">Obrigado! Seu feedback foi salvo.</h3>
                            </div>
                        ) : (
                            <form onSubmit={handleSubmit} className="space-y-4">
                                <div>
                                    <label className="block text-sm font-semibold text-slate-700 mb-1">
                                        Como avalia a precisão das respostas? *
                                    </label>
                                    <select 
                                        required
                                        className="w-full border border-slate-200 rounded-lg p-2 text-sm focus:ring-2 focus:ring-sky-500"
                                        value={formData.question1}
                                        onChange={e => setFormData({...formData, question1: e.target.value})}
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
                                        onChange={e => setFormData({...formData, question2: e.target.value})}
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
                                        onChange={e => setFormData({...formData, question3: e.target.value})}
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
                        )}
                    </div>
                </div>,
                document.body
            )}
        </>
    );
}