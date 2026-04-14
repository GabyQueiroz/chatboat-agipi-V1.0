import React, { useState } from 'react'

export default function UserCard({ onLogin }) {
    const [tempName, setTempName] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        if (!tempName.trim()) return;

        onLogin(tempName.trim());
    };

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
            <div className="bg-white rounded-2xl p-6 w-full max-w-sm shadow-xl">
                <h2 className="text-xl font-bold text-gray-800 mb-2">Bem-vindo(a)!</h2>
                <p className="text-sm text-gray-500 mb-4">
                    Por favor, informe seu nome para iniciarmos a conversa.
                </p>
                <form onSubmit={handleSubmit} className="flex flex-col gap-3">
                    <input
                        type="text"
                        placeholder="Seu nome"
                        value={tempName}
                        onChange={(e) => setTempName(e.target.value)}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        autoFocus
                    />
                    <button
                        type="submit"
                        disabled={!tempName.trim()}
                        className="w-full bg-blue-600 text-white font-medium py-2 rounded-lg hover:bg-blue-700 cursor-pointer disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
                    >
                        Entrar no Chat
                    </button>
                </form>
            </div>
        </div>
    );
}