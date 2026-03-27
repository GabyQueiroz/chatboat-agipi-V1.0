export const MOCK_MESSAGES = [
    {
        id: 1,
        role: "user",
        content: "O que é aprendizado por reforço?",
        timestamp: "14:22",
    },
    {
        id: 2,
        role: "assistant",
        timestamp: "14:22",
        text: "Aprendizado por reforço é um paradigma de machine learning onde um agente aprende a tomar decisões interagindo com um ambiente. O agente recebe recompensas ou penalidades com base nas ações que executa, e seu objetivo é maximizar a recompensa acumulada ao longo do tempo. Diferente do aprendizado supervisionado, não há exemplos rotulados — o agente descobre por si mesmo quais estratégias levam a melhores resultados.",
        documents: [
            {
                id: "doc_0042",
                title: "Introdução ao Aprendizado por Reforço",
                source: "reinforcement_learning_intro.pdf",
                score: 0.97,
                excerpt:
                    "Aprendizado por reforço (RL) é uma área de machine learning onde um agente aprende a tomar decisões sequenciais para maximizar uma recompensa cumulativa...",
                page: 3,
                tokens: 512,
            },
            {
                id: "doc_0117",
                title: "Fundamentos de ML — Capítulo 7",
                source: "ml_fundamentals_ch7.pdf",
                score: 0.91,
                excerpt:
                    "O framework de RL é formalmente descrito por um Processo de Decisão de Markov (MDP), composto por estados, ações, transições e recompensas...",
                page: 142,
                tokens: 384,
            },
            {
                id: "doc_0203",
                title: "Q-Learning e Métodos de Diferença Temporal",
                source: "q_learning_survey.pdf",
                score: 0.84,
                excerpt:
                    "Métodos de diferença temporal combinam ideias do Monte Carlo e da programação dinâmica, permitindo o aprendizado a partir de experiências sem um modelo do ambiente...",
                page: 8,
                tokens: 296,
            },
        ],
    },
];