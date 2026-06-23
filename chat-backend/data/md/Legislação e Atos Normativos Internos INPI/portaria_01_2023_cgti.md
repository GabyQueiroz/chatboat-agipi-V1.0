** **
## **MINISTÉRIO DO DESENVOLVIMENTO, INDÚSTRIA, COMÉRCIO E SERVIÇOS INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** 
PORTARIA/INPI/CGTI Nº 01, DE 10 DE NOVEMBRO DE 2023 
**PORTARIA/INPI/CGTI Nº 01, DE 10 DE NOVEMBRO DE 2023** 
Publica Manual de Metodologia de Desenvolvimento de So�ware 
**O COORDENADOR-GERAL DE TECNOLOGIA DA INFORMAÇÃO,** no uso das atribuições que lhe foram conferidas pelo Decreto nº 11.207, de 26 de setembro de 2022, e pela Portaria MDIC nº 11, de 27 de janeiro de 2017, 
## RESOLVE: 
**Art. 1º** Publicar na forma do anexo a esta Portaria o documento GETI-GST-MN-0001, que versa sobre o Manual de Metodologia de Desenvolvimento de So�ware no âmbito do INPI, assim como seus respec�vos fluxos de processos GETI-GST-FP-0001, GETI-GST-FP-0002, GETI-GST-FP-0003, GETI-GST-FP-0004, GETI-GSTFP-0005 e GETI-GST-FP-0006, que foram elaborados e revisados em conformidade com o Sistema de Padronização de Documentos, para alinhamento ao Manual do Sistema de Padronização de Documentos do INPI (GEQU-GDS-MN-0001). 
**Art. 2º** Esta Portaria entra em vigor em 01 de dezembro de 2023, nos termos do art. 4º, caput e incisos I e II do Decreto nº 10.139, de 28 de novembro de 2019, revogando a PORTARIA/INPI/CGTI Nº 01, DE 27 de janeiro de 2022, publicada no Bole�m de Pessoal I, de 01 de fevereiro de 2022. 
MARCUS VINICIUS DA MOTTA VIEIRA Coordenador-Geral de Tecnologia da Informação 
** **
** **
Documento assinado eletronicamente por **MARCUS VINICIUS DA MOTTA VIEIRA** , **Coordenador(a) Geral** , em 13/11/2023, às 13:16, conforme horário oficial de Brasília, com fundamento no art. 6º, § 1º, do Decreto nº 8.539, de 8 de outubro de 2015. 
** **
A auten�cidade deste documento pode ser conferida no site h�p://sei.inpi.gov.br/sei/controlador_externo.php? acao=documento_conferir&id_orgao_acesso_externo=0, informando o código verificador **0917696** e o código CRC **1F5EF7F1** . 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>MANUAL|**Código **|GETI – GST – MN – 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Elaboração**|07/12/2021|
||**METODOLOGIA DE DESENVOLVIMENTO DE**<br>**SOFTWARE**|**Aprovação**|10/10/2022|
|||**Processo**|Gestão de Soluções<br>de TIC|
## **Sumário** 
**1. Introdução ...................................................................................................................................... 2 2. Objetivo .......................................................................................................................................... 2 3. Abrangência ................................................................................................................................... 2 4. Documentos complementares ...................................................................................................... 2 5. Glossário ........................................................................................................................................ 2 6. Fundamentos Gerais ..................................................................................................................... 4 6.1 Alicerce da Metodologia ....................................................................................................... 4 6.2. Princípios .............................................................................................................................. 4 6.3. Resultados esperados ......................................................................................................... 4 6.4. Prioridade das Demandas ................................................................................................... 5 6.5. Práticas Ágeis ...................................................................................................................... 5 6.6. Papeis e Responsabilidades ............................................................................................... 6 6.7. Política de Atualização ........................................................................................................ 6 7. Descrição dos processos ou atividades ...................................................................................... 7 7.1. Demandas realizadas pelo Ateliê de Software ................................................................... 7 7.1.1. Backlog de Projetos ................................................................................................... 7 7.1.2. Demanda de Funcionalidade ..................................................................................... 8 7.1.3. Demanda Evolutiva .................................................................................................. 10 7.1.4. Manutenção .............................................................................................................. 15 7.1.5. Fluxo de Rejeição ..................................................................................................... 19 7.2. Demandas realizadas Internamente .................................................................................. 20 8. Entradas do processo ................................................................................................................. 22 9. Saídas do processo / resultados esperados .............................................................................. 22 10. Fluxo do processo ..................................................................................................................... 22 11. Indicadores do processo ........................................................................................................... 22 11.1. Prazo de entrega .............................................................................................................. 22 11.2. Qualidade de código ........................................................................................................ 27 11.3. Rejeição ............................................................................................................................ 28 11.4. Leadtime ........................................................................................................................... 28 12. Governança ................................................................................................................................ 29 13. Dono do documento .................................................................................................................. 29 14. Elaborador(es) do documento .................................................................................................. 29 15. Aprovador(es) do documento ................................................................................................... 29 16. Bibliografia ................................................................................................................................. 29 17. Histórico das alterações ............................................................................................................ 30 18. Anexos ........................................................................................................................................ 30** 
Página **1** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **1. Introdução** 
As metodologias de desenvolvimento de software consistem, basicamente, no conjunto de abordagens que podem ser utilizadas para a criação de sistemas de processamento de dados. O sucesso de qualquer projeto voltado à elaboração de software depende diretamente da escolha da metodologia mais adequada. 
Neste manual é descrita a metodologia aplicável aos projetos de desenvolvimento e manutenção de software no INPI, contemplando atividades, fluxos, responsáveis e artefatos necessários ao ciclo de vida do projeto. 
## **2. Objetivo** 
Definir um padrão para a gestão e o desenvolvimento de software no INPI, através de uma abordagem iterativa e incremental, adotando práticas ágeis, com o intuito de focar na qualidade da entrega do software e valor agregado para os clientes. 
## **3. Abrangência** 
Este documento abrange todas as áreas que atuam diretamente no processo de desenvolvimento e manutenção de software no âmbito do INPI, devendo ser amplamente divulgado a todos os servidores, colaboradores e empresas prestadores de serviços dessas áreas. 
Igualmente, todas as áreas demandantes de soluções de tecnologia de informação precisam ter acesso ao documento e conhecimento de sua amplitude, a fim de que estejam cientes das etapas fundamentais para a implementação de um produto de software que atenda às necessidades pretendidas. 
## **4. Documentos complementares** 
GETI – GST – IT – 0001_Abertura de demandas no Sistema Redmine. 
## **5. Glossário** 
Artefatos – Subprodutos produzidos durante o desenvolvimento de software. Ajudam a descrever a função, arquitetura e o design do software ou estão relacionados com o próprio processo de desenvolvimento. 
ANAC – Agência Nacional de Aviação Civil. 
ANCINE – Agência Nacional do Cinema. 
Bugs – Erros em sistemas. 
CGTI – Coordenação Geral de Tecnologia da Informação. 
COSIS – Coordenação de Sistemas. 
DELPHI – Linguagem de programação para o desenvolvimento de sistemas. 
Página **2** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
DIPRO – Divisão de Padronização de Software. 
DIREX – Diretoria Executiva. 
GETI – Gestão de Tecnologia da Informação e Comunicações. 
INPI – Instituto Nacional da Propriedade Industrial. 
Lean Startup ( _Startup_ Enxuta) – Metodologia orientada para a criação de produtos com ciclos de aprendizado rápidos, onde as mudanças no direcionamento das estratégias acontecem visando um crescimento acelerado, envolvendo um trabalho de identificação e eliminação de desperdícios nos processos. 
Lean Kanban – Metodologia que tem o objetivo de evitar tanto a falta como o excesso de produção, evidenciar problemas e definir o que deve ser feito, sem que seja necessária a orientação de superiores ou do planejamento e controle da produção. Requer estabilidade, disciplina e padronização. 
MVP (“Minimum Viable Product”, ou “Produto Mínimo Viável”) – Pode ser descrito como sendo uma versão beta de um produto, desenvolvida de forma ágil e econômica para ser apresentada ao seu público-alvo e receber feedbacks. Trata-se de uma ferramenta para obter informações sobre o seu mercado e validar premissas. 
PDTIC – Plano Diretor de Tecnologia da Informação e Comunicação. 
PJERJ – Poder Judiciário do Estado do Rio de Janeiro. 
Refatoração (Refactoring) – Processo de modificar um sistema de software para melhorar a estrutura interna do código sem alterar seu comportamento externo. 
SUSEP – Superintendência de Seguros Privados. 
Tipo de Tarefa: DEMANDA – Nessa categoria são classificadas as tarefas de execução com o ateliê de software e demandas internas. 
Tipo de Tarefa: FUNCIONALIDADE – Nessa categoria são classificadas as tarefas relacionadas aos projetos e que incluem novas funções do sistema, sendo que uma Funcionalidade pode ter associada a ela uma ou várias demandas de execução. 
Tipo de Tarefa: REJEIÇÃO – Nessa categoria são classificadas as tarefas que registram uma falha, sendo sempre associadas à demanda que gerou o erro. Nesse caso as regras não cumpridas podem ser testes com falha ou especificação com falha. 
TRT – Tribunal Regional do Trabalho. 
UNIs – Unidades de Serviço Técnico do INPI, equivalente a uma hora de esforço especializado não individualizada. 
XP (eXtreme Programming) – Metodologia ágil que se ajusta bem a projetos de software com requisitos vagos e em constante mudança, adotando a estratégia de acompanhamento contínuo e realização pequenos ajustes durante o desenvolvimento. 
Página **3** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **6. Fundamentos Gerais** 
## **6.1 Alicerce da Metodologia** 
A metodologia é alicerçada em 4 pilares: 
1. Priorização balanceada: considera o valor agregado, visando promover práticas que permitam aos participantes do projeto desenvolver uma solução que maximize os benefícios e seja compatível com as restrições existentes. 
2. Colaboração: alinhamento de interesses e compartilhamento do entendimento, visando promover um ambiente de equipe saudável que promova a colaboração e a compreensão do projeto. 
3. Focar na arquitetura: concentração na arquitetura desde o início para minimizar riscos e organizar o desenvolvimento, além de promover práticas que minimizem os riscos na fase de desenvolvimento. 
4. Evolução contínua e obtenção de feedback: promove práticas que permitem a equipe obter feedback de maneira contínua e o mais cedo possível, permitindo agregar valor a cada desenvolvimento e diminuir o risco do projeto conforme a execução. 
## **6.2. Princípios** 
## **I. PD1 - Primeiro Princípio Geral do Processo de Desenvolvimento de Software do INPI** 
- Haverá apenas um processo de desenvolvimento de software para todo o Órgão, sob a responsabilidade da Divisão de Padronização e Processo de Software. 
## **II. PD2 - Segundo Princípio Geral do Processo de Desenvolvimento de Software do INPI** 
O desenvolvimento de software é atividade exclusiva da CGTI. 
## **III. PD3 - Princípio de Ferramentas e Instrumentos** 
- A Divisão de Padronização e Processo de Software definirá as ferramentas e instrumentos padrões de sustentação do processo e arquitetura de sistema, que deverão ser utilizados por todos os agentes. 
## **IV. PD4 - Princípio de Controle de Demanda** 
- O atendimento da demanda somente poderá ser executado após a aprovação da solicitação, sendo esta onerosa para o INPI ou não. 
## **V. PD5 - Princípio de Prioridades** 
- As demandas deverão seguir a determinação de prioridades estabelecida pelo Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC vigente) ou pela própria Administração do órgão, em casos excepcionais. 
## **6.3. Resultados esperados** 
Com a adoção dessa metodologia, é esperado um ambiente de desenvolvimento que se apresente de maneira mais transparente para o INPI na forma como é conduzido o 
Página **4** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
processo de avaliação e priorização de uma demanda de software, bem como os princípios que nortearão as decisões acerca do encaminhamento desta demanda. 
A padronização da arquitetura tem como objetivos, além da otimização dos recursos de TI, a flexibilização das ações, evolução do sistema de forma a agregar valor às atividades fim do INPI, focando na melhoria da qualidade, na maximização de performance nos códigos fonte e maior assertividade dos resultados. 
Tal como ocorreu em órgãos da administração pública após a implementação de processos normalizadores da atividade de desenvolvimento de software, particularmente SUSEP, ANAC, ANCINE, TRT e PJERJ, o INPI baseado neles espera alcançar com a implementação de sua Metodologia de Desenvolvimento de Software os seguintes benefícios: 
- Melhoria dos serviços oferecidos aos clientes; 
- Ampliação da qualidade da solução de TI a ser entregue; 
- Otimização da aplicação dos recursos humanos disponíveis; 
- Ampliação do nível de satisfação dos clientes finais; 
- • Padronização do processo de desenvolvimento de sistemas; 
- Aumento da produtividade nos processos de desenvolvimento, operação e 
- manutenção de software; 
- Assertividade na estimativa de custos e prazos pelos profissionais envolvidos; 
- • Rastreabilidade dos serviços prestados aos usuários. 
## **6.4. Prioridade das Demandas** 
As demandas seguirão a ordem de prioridades estabelecida pelo Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC) ou aquela definida pela Administração do INPI, visando o atingimento das metas estratégicas, o atendimento das demandas rotineiras e incidentes que venham a ocorrer, garantindo o pleno funcionamento dos sistemas de tratamento da informação existentes no INPI e a continuidade dos serviços. 
## **6.5. Práticas Ágeis** 
A Metodologia do INPI está baseada na gestão do fluxo entre a demanda de negócio e a entrega de valor ao cliente final, a partir da concepção de um Mínimo Produto Viável, o MVP, com um fluxo iterativo e incremental onde o trabalho em progresso é limitado em um sistema puxado adaptativo, mais conveniente à gestão do trabalho do conhecimento e com foco na eficácia. 
O INPI possui o modelo de desenvolvimento de software _,_ adequado às suas necessidades e às especificidades de sua atividade. A visão do INPI da técnica de produção de soluções em _software_ mantem-se apoiada em dois pilares: 
- a) _**Lean Kanban**_ e _**Lean Startup**_ - gestão visual do fluxo de entrega de valor aplicada a tarefas não repetitivas de “trabalho do conhecimento”, subordinação às capacidades, limites e Sistema Puxado de produção, com vistas à redução do Tempo de Espera em Fila, liquidez do sistema e consequente aumento de sua eficácia. 
- b) **Software Livre e eXtreme Programming** - o modelo de execução de desenvolvimento de software do INPI se baseia nas práticas ágeis da eXtreme Programming em uma cultura de Software Livre. Dentre as práticas destacam-se: 
Página **5** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
cliente presente; times multidisciplinares auto organizados; desenvolvimento orientado por testes; padrões de codificação; ciclos de feedback curtos (versões pequenas e projeto simples); refatoração; intensa comunicação visual; automatização e implantação contínuas. 
## **6.6. Papeis e Responsabilidades** 
**Tabela 1: Descrição de papéis e responsabilidades** 
|**Papel**|**Descrição**|**Responsabilidade**|
|---|---|---|
|**Cliente**<br>**(INPI)**|Servidor do INPI|Descrever o projeto; definir backlog com as<br>funcionalidades dos sistemas envolvidos no<br>projeto; escrever histórias das funcionalidades<br>detalhando-as de acordo com as necessidades<br>e<br>resultados<br>esperados;<br>abrir<br>demandas<br>relacionadas à manutenção dos sistemas já<br>existentes e homologar implementação.|
|**Analista**<br>**(INPI)**|Servidor da área<br>de TI|Analisar a solicitação de um novo projeto; criar<br>projeto no sistema de controle de demandas do<br>INPI (Redmine); validar a escrita das histórias<br>de usuário; priorizar demandas; analisar e<br>detalhar solicitações de novas funcionalidades;<br>validar especificações e orçamentos referentes<br>às demandas, testar implementação; registrar<br>defeitos relacionados às demandas e concluir<br>demandas.|
|**Ateliê de**<br>**Software**|Colaborador<br>da<br>empresa<br>contratada|Analisar e desenvolver novas funcionalidades<br>de<br>sistemas;<br>realizar<br>manutenção<br>em<br>funcionalidades de sistemas já existentes;<br>realizar<br>orçamento<br>de<br>demandas<br>e<br>especificação;<br>realizar<br>testes<br>e<br>entregar<br>artefatos.|
|**Analista**<br>**DIPRO**|Servidor da área<br>de TI alocado na<br>DIPRO|Analisar o fluxo de demandas e propor<br>melhorias; avaliar a qualidade das entregas de<br>software e registrar defeito nos casos em que a<br>entrega não atenda aos requisitos mínimos de<br>qualidade exigidos.|
## **6.7. Política de Atualização** 
Este documento poderá ser atualizado pelo INPI sempre que surgirem novas diretrizes ou haja alteração de diretriz já existente. Também poderá sofrer modificações a fim de atender a normas vigentes, situações não previstas, recomendações de órgãos de controle, bem como adequar texto para eliminar eventuais ambiguidades, omissões ou contradições. 
Além disso, atualizações nos normativos complementares a este guia podem implicar alterações no mesmo. Após a atualização deste manual, a versão mais recente deve ser usada em todos os novos projetos, a partir de sua data de publicação. 
Página **6** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **7. Descrição dos processos ou atividades** 
## **7.1. Demandas realizadas pelo Ateliê de Software** 
## 7.1.1. Backlog de Projetos (vide fluxo GETI-GST-FP-0001_Backlog de Projetos) 
## **Atividade:** Criar Projeto 
Criação do projeto no sistema de controle de demandas do INPI – Redmine, onde ficarão armazenadas todas as informações de demandas e atividades relacionadas 
|**Atividade:**Criar Projeto|**Atividade:**Criar Projeto|
|---|---|
|Criação do projeto no sistema de controle de demandas do INPI – Redmine, onde ficarão<br>armazenadas todas as informações de demandas e atividades relacionadas||
|**Responsável**|**Entrega**|
|Analista (INPI)|Projeto criado no Redmine|
|**Tarefas executadas**|**Descrição**|
|Criar projeto|Verificar se o projeto já existe, caso contrário o analista<br>deve criar o mesmo no sistema.|
|**Observação**||
|--||
## **Atividade:** Definir backlog do projeto 
Definição da lista com as descrições das funcionalidades necessárias para a entrega de um produto e priorização para a implementação. 
|**Atividade:**Definir backlog do projeto|**Atividade:**Definir backlog do projeto|
|---|---|
|Definição da lista com as descrições das funcionalidades necessárias para a entrega de um<br>produto epriorizaçãopara a implementação.||
|**Responsável**|**Entrega**|
|Cliente (INPI)|Backlog do projeto|
|**Tarefas executadas**|**Descrição**|
|Definir itens do backlog|Listar itens com as funcionalidades de um sistema.|
|**Observação**||
|A metodologia adota premissas ágeis, ou seja, é iterativa e incremental. Sendo assim, a<br>definição do que será executado é decidido em conjunto com o Analista (INPI).||
## **Atividade:** Avisar término da Atividade 
Enviar notificação de término da atividade para os responsáveis. 
|**Atividade:**Avisar término da Atividade|**Atividade:**Avisar término da Atividade|
|---|---|
|Enviar notificação de término da atividade para os responsáveis.||
|**Responsável**|**Entrega**|
|Cliente (INPI)|Notificação|
|**Tarefas executadas**|**Descrição**|
|Enviar e-mail|Comunicar à CGTI a finalização da definição do backlog<br>doprojeto|
|**Observação**||
|Notificação se dará via e-mail para o analista responsável ou chefe da DISIS em<br>disis@inpi.gov.br.||
Página **7** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## 7.1.2. Demanda de Funcionalidade (vide fluxo GETI-GST-FP-0002_Demanda de Funcionalidade) 
|**Atividade:**Criar Demanda|**Atividade:**Criar Demanda|
|---|---|
|Criação de demanda do tipo “Funcionalidade” no projeto disponibilizado no sistema de<br>controle de demandas do INPI – Redmine||
|**Responsável**|**Entrega**|
|Analista (INPI)|Registro de demanda|
|**Tarefas executadas**|**Descrição**|
|Abrir demanda|Criar demanda nos projetos disponibilizados no sistema<br>Redmine, conforme necessidade com exceção do projeto<br>“Manutenção”|
|Avançar atividade|Dar encaminhamento à demanda criada, alterando o<br>status da mesmapara “Escrever História”|
|**Observação**||
|Demanda do Tipo FUNCIONALIDADE||
## **Atividade:** Escrever História 
Detalhamento da funcionalidade através de uma explicação informal e geral sobre um recurso de software escrita a partir da perspectiva do usuário final. Seu objetivo é articular como um recurso de software pode gerar valor para o cliente. 
|**Atividade:**Escrever História|**Atividade:**Escrever História|
|---|---|
|Detalhamento da funcionalidade através de uma explicação informal e geral sobre um<br>recurso de software escrita a partir da perspectiva do usuário final. Seu objetivo é articular<br>como um recurso de software pode gerar valor para o cliente.||
|||
|**Responsável**|**Entrega**|
|Cliente (INPI)|História|
|**Tarefas executadas**|**Descrição**|
|Definição textual|Usando de linguagem não técnica, dar contexto ao que<br>se necessita,evidenciando oproblema a ser tratado|
|**Observação**||
|Demanda do Tipo FUNCIONALIDADE||
## **Atividade:** Validar História 
Analista (INPI) e Ateliê devem avaliar a viabilidade de atendimento, levando em consideração, o escopo, objetivos, tempo, duração e esforço. 
|**Atividade:**Validar História|**Atividade:**Validar História|
|---|---|
|Analista (INPI) e Ateliê devem avaliar a viabilidade de atendimento, levando em<br>consideração,o escopo,objetivos,tempo,duração e esforço.||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Analisar requisitos|Compreender<br>e<br>analisar<br>a<br>possibilidade<br>do<br>desenvolvimento de acordo com os recursos disponíveis|
|Propor solução|Propor<br>ao<br>Cliente<br>(INPI)<br>uma<br>solução<br>para<br>o<br>desenvolvimento|
|**Observação**||
|Atividade conjunta do Analista (INPI) e Ateliê||
Página **8** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **Atividade:** Priorizar demanda 
Analisar a criticidade e urgência da solicitação em relação às demandas já existentes na fila de priorização. 
|**Atividade:**Priorizar demanda|**Atividade:**Priorizar demanda|
|---|---|
|Analisar a criticidade e urgência da solicitação em relação às demandas já existentes na fila<br>depriorização.||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Verificar demandas|Verificar demandas existentes na fila de execução,<br>definindo as mais urgentes a serem atendidas|
|Definir demandas|Definir qual demanda é prioritária e enviar para<br>desenvolvimento|
|**Observação**||
|Na atividade de “Definir demandas” são abertas as demandas do Tipo DEMANDA, para a<br>execução dofluxo de desenvolvimento peloAteliê.||
## **Atividade:** Desenvolver demanda 
Equipe de desenvolvimento codifica os itens e funcionalidades detalhados 
|**Atividade:**Desenvolver demanda|**Atividade:**Desenvolver demanda|
|---|---|
|Equipe de desenvolvimento codifica os itens e funcionalidades detalhados||
|**Responsável**|**Entrega**|
|Ateliê de Software|Software|
|**Tarefas executadas**|**Descrição**|
|Execução da demanda|Execução das demandas evolutivas ou internas para<br>atendimento dos requisitos da funcionalidade.|
|**Observação**||
|A atividade de desenvolvimento é executada nas demandas do Tipo DEMANDA.||
## **Atividade:** Realizar homologação 
Cliente (INPI) verifica o produto desenvolvido para aprovação 
|**Atividade:**Realizar homologação|**Atividade:**Realizar homologação|
|---|---|
|Cliente (INPI) verifica o produto desenvolvido para aprovação||
|**Responsável**|**Entrega**|
|Cliente (INPI)|Aprovação ou correção|
|**Tarefas executadas**|**Descrição**|
|Testar funcionalidades|Executar a aplicação para verificar se atende as<br>necessidades conforme solicitado|
|Apontar defeitos e melhorias|Informar qualquer correção necessária ou proposta de<br>melhoria|
|**Observação**||
|Atividade realizada no ambiente de Testes||
Página **9** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Registrar defeito 
Abrir demanda para registrar algum erro de implementação ou requisito não implementado 
|**Atividade:**Registrar defeito|**Atividade:**Registrar defeito|
|---|---|
|Abrir demanda para registrar algum erro de implementação ou requisito não implementado||
|**Responsável**|**Entrega**|
|Analista (INPI)|Erro registrado|
|**Tarefas executadas**|**Descrição**|
|Criar defeito no sistema|Criar demanda do tipo “Rejeição” no sistema de controle<br>de demandas do INPI – Redmine, informando descrição<br>do erro|
|Associar a demanda|Usando recurso do sistema Redmine, associar “Rejeição”<br>criada a demanda que gerou esse defeito|
|**Observação**||
|Demanda do Tipo REJEIÇÃO||
## **Atividade:** Concluir demanda 
Atualizar status da demanda para concluído 
|**Atividade:**Concluir demanda|**Atividade:**Concluir demanda|
|---|---|
|Atualizar status da demanda para concluído||
|**Responsável**|**Entrega**|
|Analista(INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Informar status|Avançar demanda para “Demanda finalizada”|
|**Observação**||
|Em casos específicos, a demanda pode ser concluída mesmo sem a disponibilização da<br>funcionalidade no ambiente deprodução.||
## 7.1.3. Demanda Evolutiva (vide fluxo GETI-GST-FP-0003_Demanda Evolutiva) 
|**Atividade:**Criar Demanda|**Atividade:**Criar Demanda|
|---|---|
|Criação de demanda no projeto disponibilizado no sistema de controle de demandas do<br>INPI–Redmine||
|**Responsável**|**Entrega**|
|Analista(INPI)|Registro de demanda|
|**Tarefas executadas**|**Descrição**|
|Abrir demanda|Criar demanda nos projetos disponibilizados no sistema<br>Redmine conforme necessidade com exceção do projeto<br>“Manutenção”|
|Avançar atividade|Dar encaminhamento à demanda criada alterando o<br>statuspara “Detalhar solicitação da funcionalidade”|
|**Observação**||
|Demanda do Tipo DEMANDA||
Página **10** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Detalhar solicitação da funcionalidade 
|**Atividade:**Detalhar solicitação da funcionalidade|**Atividade:**Detalhar solicitação da funcionalidade|
|---|---|
|Descrever funcionalidades a um nível de detalhe suficiente para o entendimento dos<br>requisitos para quehaja consenso entreINPIe desenvolvedor||
|**Responsável**|**Entrega**|
|Analista(INPI)|Detalhes da funcionalidade|
|**Tarefas executadas**|**Descrição**|
|Descrever requisitos|Descrever tecnicamente o que se requer e como atingir o<br>resultado esperado|
|**Observação**||
|Atividade em conjunto com o Ateliê||
**Atividade:** Realizar especificação/orçamento 
Especificar e gerar orçamento 
|**Atividade:**Realizar especificação/orçamento|**Atividade:**Realizar especificação/orçamento|
|---|---|
|Especificar e gerar orçamento||
|**Responsável**|**Entrega**|
|Ateliê de Software|Especificação/Orçamento|
|**Tarefas executadas**|**Descrição**|
|Inserir orçamento|No sistema Redmine, definir quais itens de repertório<br>serão utilizados para a implementação da demanda e<br>UNIS necessárias para o desenvolvimento|
|Especificar artefatos|Especificar os artefatos necessários, de acordo com a<br>especificidade da demanda|
|**Observação**||
|O prazo para a entrega da especificação/orçamento é de 5 (cinco) dias úteis.<br>Os artefatos a serem entregues dependem do escopo, objetivos, tempo, risco e esforço e<br>serão demandados pelo Analista (INPI).||
## **Atividade:** Validar especificação/orçamento 
Avaliar para aprovação o orçamento 
|**Atividade:**Validar especificação/orçamento|**Atividade:**Validar especificação/orçamento|
|---|---|
|Avaliar para aprovação o orçamento||
|**Responsável**|**Entrega**|
|Analista (INPI)|Aprovação ou item para correção|
|**Tarefas executadas**|**Descrição**|
|Verificar orçamento|Com base nas definições das funcionalidades, certificar<br>que a especificação e orçamento entregues pelo Ateliê<br>correspondem ao que de fato precisa ser feito.|
|Informar ajuste|Caso observe algum erro, enviar para ajuste|
|**Observação**||
|--||
Página **11** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Ajustar especificação/orçamento 
Corrigir especificação/orçamento 
|**Atividade:**Ajustar especificação/orçamento|**Atividade:**Ajustar especificação/orçamento|
|---|---|
|Corrigir especificação/orçamento||
|**Responsável**|**Entrega**|
|Ateliê de Software|Orçamento ajustado|
|**Tarefas executadas**|**Descrição**|
|Adequar orçamento|Com base nas informações do Analista (INPI), corrigir no<br>sistema o orçamento|
|Adequar especificação|Com base nas informações do Analista (INPI), corrigir<br>especificações entregues com erro|
|**Observação**||
|--||
## **Atividade:** Realizar implementação 
Implementar software a partir dos requisitos definidos. 
|**Atividade:**Realizar implementação|**Atividade:**Realizar implementação|
|---|---|
|Implementar software a partir dos requisitos definidos.||
|**Responsável**|**Entrega**|
|Ateliê de Software|Versão para implementar|
|**Tarefas executadas**|**Descrição**|
|Implementar novo código|Implementar e realizar a revisão do código gerado de<br>acordo com os padrões de qualidade de código definidos<br>pelo INPI|
|Submeter solução a testes|Ajustar e executar os testes já escritos, verificando o<br>funcionamento do sistema, e fazer as devidas correções,<br>caso<br>necessário<br>(tanto<br>nos<br>testes<br>quanto<br>na<br>implementação da solução).|
|Gerar<br>versão<br>para<br>implementação|Configurar versão em ambiente de homologação para<br>testes|
|**Observação**||
|--||
## **Atividade:** Validação de qualidade de código 
Verificar se os artefatos estão de acordo com os padrões de qualidade esperados 
|**Atividade:**Validação de qualidade de código|**Atividade:**Validação de qualidade de código|
|---|---|
|Verificar se os artefatos estão de acordo com os padrões de qualidade esperados||
|**Responsável**|**Entrega**|
|DIPRO|Código validado|
|**Tarefas executadas**|**Descrição**|
|Avaliar código|Verificar a qualidade do código gerado, de acordo com<br>os parâmetros de qualidade definidos pelo INPI|
|Registrar defeito|Se necessário, encaminharpara registro de defeito|
|**Observação**||
|Antes da homologação, a validação ocorre no ambiente de testes e, após homologação, no<br>ambiente de produção. Em caso de erro, deve ser aberta uma demanda Tipo REJEIÇÃO||
Página **12** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
|**Atividade:**Testar Implementação|**Atividade:**Testar Implementação|
|---|---|
|Verificar implementação||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Executar teste|Executar testes para validar a implementação|
|Verificar funcionalidade|Validar se a solução atende as especificações descritas<br>na demanda.|
|Registrar defeito|Se necessário, encaminhar para registro de defeito|
|**Observação**||
|Em caso de erro, deve ser aberta uma demanda Tipo REJEIÇÃO||
## **Atividade:** Homologar Implementação 
Aprovar o desenvolvimento realizado 
|**Atividade:**Homologar Implementação|**Atividade:**Homologar Implementação|
|---|---|
|Aprovar o desenvolvimento realizado||
|**Responsável**|**Entrega**|
|Cliente (INPI)|Aprovação ou correção|
|**Tarefas executadas**|**Descrição**|
|Testar funcionalidades|Executar<br>aplicação<br>para<br>verificar<br>se<br>atende<br>às<br>necessidades conforme solicitado|
|Apontar defeitos e melhorias|Informar qualquer correção necessária ou proposta de<br>melhoria|
|**Observação**||
|O prazo para a homologação é de 5 (cinco) dias úteis. Após esse prazo, se não houver<br>manifestação da área de negócio, a implementação será considerada homologada<br>tacitamente.||
**Atividade:** Registrar defeito 
Abrir demanda para registrar algum erro de implementação ou requisito não implementado 
|**Atividade:**Registrar defeito|**Atividade:**Registrar defeito|
|---|---|
|Abrir demanda para registrar algum erro de implementação ou requisito não implementado||
|**Responsável**|**Entrega**|
|Analista (INPI)|Erro registrado|
|**Tarefas executadas**|**Descrição**|
|Criar defeito no sistema|Criar demanda do tipo “Rejeição” no sistema de controle<br>de demandas do INPI – Redmine, informando descrição<br>do erro|
|Associar a demanda|Usando recurso do sistema Redmine, associar “Rejeição”<br>criada a demandaquegerou esse defeito|
|**Observação**||
|Demanda do Tipo REJEIÇÃO||
Página **13** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Entregar artefatos 
Entregar artefatos gerados em conformidade com os padrões de qualidade 
|**Atividade:**Entregar artefatos|**Atividade:**Entregar artefatos|
|---|---|
|Entregar artefatos gerados em conformidade com os padrões de qualidade||
|**Responsável**|**Entrega**|
|Ateliê de Software|Artefatos|
|**Tarefas executadas**|**Descrição**|
|Disponibilizar entregáveis|Entregáveis a serem implantados em produção são<br>disponibilizados para os Analistas (INPI)|
|**Observação**||
|--||
## **Atividade:** Atualizar registro de demanda 
Analista formaliza entrega de demanda 
|**Atividade:**Atualizar registro de demanda|**Atividade:**Atualizar registro de demanda|
|---|---|
|Analista formaliza entrega de demanda||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Registrar<br>a<br>finalização<br>da<br>demanda e alterar status|Formalizar que a demanda foi entregue de acordo com<br>os requisitos solicitados e avançar demanda para o<br>status “Atualizar registro de demanda”|
|**Observação**||
|--||
|**Atividade:**Demanda concluída com ônus|**Atividade:**Demanda concluída com ônus|
|---|---|
|Alterar status da demanda para concluído||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Informar status|Avançar demanda para o status “Demanda concluída<br>com ônus”|
|**Observação**||
|--||
Página **14** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## 7.1.4. Manutenção (vide fluxo GETI-GST-FP-0004_Manutenção) 
## **Atividade:** Criar Demanda 
Criar demanda no sistema de controle de demandas do INPI – Redmine 
|**Atividade:**Criar Demanda|**Atividade:**Criar Demanda|
|---|---|
|Criar demanda no sistema de controle de demandas do INPI – Redmine||
|**Responsável**|**Entrega**|
|Cliente (INPI)|Registro de demanda|
|**Tarefas executadas**|**Descrição**|
|Abrir demanda|Criar demanda no projeto “Manutenção” disponibilizado<br>no sistema Redmine.|
|Avançar atividade|Dar encaminhamento à demanda criada alterando o<br>status para “: Analisar solicitação de Manutenção”|
|**Observação**||
|Essa atividade seguirá de acordo com a instrução de trabalho GETI – GST – IT –<br>0001_Abertura de demandas no Sistema Redmine.||
**Atividade:** Analisar solicitação de Manutenção 
Avaliar a viabilidade de atendimento e, se viável, encaminhar à próxima atividade. 
|**Atividade:**Analisar solicitação de Manutenção|**Atividade:**Analisar solicitação de Manutenção|
|---|---|
|Avaliar a viabilidade de atendimento e, se viável, encaminhar à próxima atividade.||
|**Responsável**|**Entrega**|
|Analista(INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Analisar requisitos|Analisar se os requisitos definidos pelo Cliente (INPI) são<br>suficientespara o entendimento doproblema relatado|
|Propor solução|Identificar a melhor solução para o problema reportado<br>de acordo com recursos disponíveis e metodologia|
|**Observação**||
|Atividade conjunta com Ateliê||
## **Atividade:** Realizar especificação/orçamento 
|**Atividade:**Realizar especificação/orçamento|**Atividade:**Realizar especificação/orçamento|
|---|---|
|||
|Especificar egerar orçamento||
|**Responsável**|**Entrega**|
|Ateliê de Software|Especificação/Orçamento|
|**Tarefas executadas**|**Descrição**|
|Inserir orçamento|No sistema Redmine, definir quais itens de repertório<br>serão utilizados para a implementação da demanda e<br>UNIS necessárias para o desenvolvimento|
|Especificar artefatos|Especificar os artefatos necessários, de acordo com a<br>especificidade da demanda|
|**Observação**||
|O prazo para a entrega da especificação/orçamento é de 5 (cinco) dias úteis<br>Os artefatos a serem entregues dependem do escopo, objetivos, tempo, risco e esforço e<br>serão demandados pelo Analista (INPI).||
Página **15** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Validar especificação/orçamento 
Avaliar para aprovação o orçamento 
|**Atividade:**Validar especificação/orçamento|**Atividade:**Validar especificação/orçamento|
|---|---|
|Avaliar para aprovação o orçamento||
|**Responsável**|**Entrega**|
|Analista (INPI)|Aprovação ou item para correção|
|**Tarefas executadas**|**Descrição**|
|Verificar orçamento|Com base nas definições das funcionalidades, certificar<br>que a especificação e orçamento entregues pelo Ateliê<br>correspondem ao que de fato precisa ser feito.|
|Informar ajuste|Caso observe algum erro, enviar para ajuste|
|**Observação**||
|--||
## **Atividade:** Ajustar especificação/orçamento 
Corrigir especificação/orçamento 
|**Atividade:**Ajustar especificação/orçamento|**Atividade:**Ajustar especificação/orçamento|
|---|---|
|Corrigir especificação/orçamento||
|**Responsável**|**Entrega**|
|Ateliê de Software|Orçamento ajustado|
|**Tarefas executadas**|**Descrição**|
|Adequar orçamento|Com base nas informações do Analista (INPI), corrigir no<br>sistema o orçamento|
|Adequar especificação|Com base nas informações do Analista (INPI), corrigir<br>especificações entregues com erro|
|**Observação**||
|--||
## **Atividade:** Realizar implementação 
Implementar software a partir dos requisitos definidos 
|**Atividade:**Realizar implementação|**Atividade:**Realizar implementação|
|---|---|
|Implementar software apartir dos requisitos definidos||
|**Responsável**|**Entrega**|
|Ateliê de Software|Versão para implementar|
|**Tarefas executadas**|**Descrição**|
|Implementar novo código|Implementar e realizar a revisão do código gerado de<br>acordo com os padrões de qualidade de código definidos<br>pelo INPI|
|Submeter solução a testes|Ajustar e executar os testes, verificando o funcionamento<br>do sistema, e fazer as devidas correções, caso<br>necessário (tanto nos testes quanto na implementação<br>da solução).|
|Gerar<br>versão<br>para<br>implementação|Configurar versão em ambiente de homologação para<br>testes|
|**Observação**||
|--||
Página **16** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Validação de qualidade de código 
Verificar se os artefatos estão de acordo com os padrões de qualidade esperados 
|**Atividade:**Validação de qualidade de código|**Atividade:**Validação de qualidade de código|
|---|---|
|Verificar se os artefatos estão de acordo com os padrões de qualidade esperados||
|**Responsável**|**Entrega**|
|DIPRO|Código validado|
|**Tarefas executadas**|**Descrição**|
|Avaliar código|Verificar a qualidade do código gerado, de acordo com<br>osparâmetros dequalidade definidospelo INPI|
|Registrar defeito|Se necessário, encaminhar para registro de defeito|
|**Observação**||
|Antes da homologação a validação ocorre no ambiente de testes, após homologação, no<br>ambiente deprodução. Em caso de erro,deve ser aberta uma demanda Tipo Rejeição||
|**Atividade:**Testar Implementação|**Atividade:**Testar Implementação|
|---|---|
|Verificar implementação||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Executar teste|Executar testes para validar a implementação|
|Verificar funcionalidade|Validar se a solução atende as especificações descritas<br>na demanda.|
|Registrar defeito|Se necessário, encaminhar para registro de defeito|
|**Observação**||
|Em caso de erro, deve ser aberta uma demanda Tipo REJEIÇÃO||
**Atividade:** Homologar Implementação 
Aprovar o desenvolvimento realizado 
|**Atividade:**Homologar Implementação|**Atividade:**Homologar Implementação|
|---|---|
|Aprovar o desenvolvimento realizado||
|**Responsável**|**Entrega**|
|Cliente (INPI)|Aprovação ou correção|
|**Tarefas executadas**|**Descrição**|
|Testar funcionalidades|Executar<br>aplicação<br>para<br>verificar<br>se<br>atende<br>às<br>necessidades conforme solicitado|
|Apontar defeitos e melhorias|Informar qualquer correção necessária ou proposta de<br>melhoria|
|**Observação**||
|O prazo para a homologação é de 5 (cinco) dias úteis, após esse prazo, se não houver<br>manifestação da área de negócio, a implementação será considerada homologada<br>tacitamente||
Página **17** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Registrar defeito 
Abrir demanda para registrar algum erro de implementação ou requisito não implementado 
|**Atividade:**Registrar defeito|**Atividade:**Registrar defeito|
|---|---|
|Abrir demanda para registrar algum erro de implementação ou requisito não implementado||
|**Responsável**|**Entrega**|
|Analista (INPI)|Erro registrado|
|**Tarefas executadas**|**Descrição**|
|Criar defeito no sistema|Criar demanda do tipo “Rejeição” no sistema de controle<br>de demandas do INPI – Redmine, informando descrição<br>do erro|
|Associar a demanda|Usando recurso do sistema Redmine, associar “Rejeição”<br>criada a demanda que gerou esse defeito|
|**Observação**||
|O prazo para a homologação é de 5 (cinco) dias úteis, após esse prazo, se não houver<br>manifestação da área de negócio, a implementação será considerada homologada<br>tacitamente||
**Atividade:** Entregar artefatos 
Entregar artefatos gerados em conformidade com os padrões de qualidade 
|**Atividade:**Entregar artefatos|**Atividade:**Entregar artefatos|
|---|---|
|Entregar artefatosgerados em conformidade com ospadrões dequalidade||
|**Responsável**|**Entrega**|
|Ateliê de Software|Artefatos|
|**Tarefas executadas**|**Descrição**|
|Disponibilizar entregáveis|Entregáveis a serem implantados em produção são<br>disponibilizados para os Analistas(INPI)|
|**Observação**||
|--||
|**Atividade:**Atualizar registro de demanda|**Atividade:**Atualizar registro de demanda|
|---|---|
|Analista formaliza entrega de demanda||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Registrar<br>a<br>finalização<br>da<br>demanda e alterar status|Formalizar que a demanda foi entregue de acordo com<br>os requisitos solicitados e avançar demanda para o<br>status“Atualizar registro de demanda”|
|**Observação**||
|--||
Página **18** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Atividade:** Concluir demanda 
Alterar status da demanda para concluído 
|**Atividade:**Concluir demanda|**Atividade:**Concluir demanda|
|---|---|
|Alterar status da demanda para concluído||
|**Responsável**|**Entrega**|
|Analista(INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Informar status|Avançar demanda para o status “Demanda concluída<br>com ônus”.|
|**Observação**||
|--||
## 7.1.5. Fluxo de Rejeição (vide fluxo GETI-GST-FP-0005_Demanda do Tipo Rejeição) 
|**Atividade:**Criar demanda|**Atividade:**Criar demanda|
|---|---|
|Criar demanda no sistema de controle de demandas do INPI – Redmine||
|**Responsável**|**Entrega**|
|Analista (INPI)|Registro de demanda|
|**Tarefas executadas**|**Descrição**|
|Abrir demanda|Criar demanda no sistema Redmine informando qual<br>regra não foi cumprida e qual tarefa gerou a rejeição|
|Alinhar internamente|Dar encaminhamento à demanda criada depois de<br>reunião de alinhamento interno com o Ateliê para<br>compreender a causa raíz do problema, alterando o<br>status para: “Realizar correção” se verificado que se trata<br>de um defeito a ser corrigido pelo Ateliê. Caso contrário<br>alterar status para:“Cancelar”|
|**Observação**||
|Demanda do Tipo REJEIÇÃO||
**Atividade:** Realizar correção 
Implementar correção no software a partir das informações descritas pelo Analista (INPI) 
|**Atividade:**Realizar correção|**Atividade:**Realizar correção|
|---|---|
|Implementar correção no software a partir das informações descritas pelo Analista (INPI)||
|**Responsável**|**Entrega**|
|Ateliê de Software|Versão corrigida|
|**Tarefas executadas**|**Descrição**|
|Realizar correção|Ajustar e executar os testes, verificando o funcionamento<br>do sistema, e fazer as devidas correções (tanto nos<br>testes quanto na implementação da solução).|
|Gerar<br>versão<br>para<br>implementação|Configurar versão em ambiente de homologação para<br>testes|
|**Observação**||
|--||
Página **19** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **Atividade:** Fechar 
Fechar demanda no sistema de controle de demandas do INPI – Redmine 
|**Atividade:**Fechar|**Atividade:**Fechar|
|---|---|
|Fechar demanda no sistema de controle de demandas do INPI – Redmine||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Verificar correção|Conferir itens corrigidos|
|Fechar demanda|Fechar demanda no sistema Redmine.|
|**Observação**||
|--||
## **Atividade:** Cancelar 
Cancelar demanda no sistema de controle de demandas do INPI – Redmine 
|**Atividade:**Cancelar|**Atividade:**Cancelar|
|---|---|
|Cancelar demanda no sistema de controle de demandas do INPI – Redmine||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Cancelar demanda|Cancela demanda no sistema Redmine, informando o<br>motivo.|
|**Observação**||
|--||
## **7.2. Demandas realizadas Internamente (vide fluxo GETI-GST-FP-0006_Demandas Internas)** 
|**Atividade:**Priorizar demanda|**Atividade:**Priorizar demanda|
|---|---|
|Analisar a criticidade e urgência da solicitação em relação às demandas já existentes na fila<br>depriorização||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Verificar demandas|Verificar demandas existentes na fila de execução,<br>definindo as mais urgentes a serem atendidas|
|Definir demandas|Definir qual demanda é prioritária e enviar para<br>desenvolvimento|
|**Observação**||
|--||
Página **20** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **Atividade:** Desenvolver internamente 
Atender demanda sem usar recursos do ateliê de software. 
|**Atividade:**Desenvolver internamente|**Atividade:**Desenvolver internamente|
|---|---|
|Atender demanda sem usar recursos do ateliê de software.||
|**Responsável**|**Entrega**|
|Analista (INPI)|Software|
|**Tarefas executadas**|**Descrição**|
|Realizar atendimento|Definir e executar solução|
|Solicitar validação|Notificar Cliente (INPI) para homologar demanda|
|**Observação**||
|--||
**Atividade:** Homologar demanda Verificação do Cliente (INPI) para assegurar que a execução da demanda está em conformidade com o solicitado. 
|**Atividade:**Homologar demanda|**Atividade:**Homologar demanda|
|---|---|
|Verificação do Cliente (INPI) para assegurar que a execução da demanda está em<br>conformidade com o solicitado.||
|**Responsável**|**Entrega**|
|Cliente (INPI)|Nota de aprovação ou correção|
|**Tarefas executadas**|**Descrição**|
|Verificar atendimento|Validar atendimento da demanda|
|Informar Analista|Informar aprovação ou item para correção|
|**Observação**||
|--||
## **Atividade:** Finalizar demanda 
Alteração do status para concluído e preenchimento de campos relacionados a conclusão. 
|**Atividade:**Finalizar demanda|**Atividade:**Finalizar demanda|
|---|---|
|Alteração do status para concluído e preenchimento de campos relacionados a conclusão.||
|**Responsável**|**Entrega**|
|Analista (INPI)|--|
|**Tarefas executadas**|**Descrição**|
|Fechar demanda|Alterar demanda para status “Demanda concluída sem<br>ônus” e especificar quantidade de UNIs e classificação|
|**Observação**||
|--||
Página **21** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **8. Entradas do processo** 
Projetos e demandas inseridos no sistema de controle de demandas do INPI (Redmine). 
## **9. Saídas do processo / resultados esperados** 
Artefatos produzidos durante o desenvolvimento e manutenção dos sistemas, conforme item 11 deste manual. 
## **10. Fluxo do processo** 
GETI-GST-FP-0001_Backlog de Projetos_rev1.0 
GETI-GST-FP-0002_Demanda de Funcionalidade_rev1.0 
GETI-GST-FP-0003_Demanda Evolutiva_rev1.0 
GETI-GST-FP-0004_Manutenção_rev1.0 
GETI-GST-FP-0005_Demanda do Tipo Rejeição_rev1.0 
GETI-GST-FP-0006_Demandas Internas_rev1.0 
## **11. Indicadores do processo** 
## **11.1. Prazo de entrega** 
O Prazo máximo para a entrega de uma demanda é calculado automaticamente em função das UNIs orçadas para a demanda, dividido pelo número de UNIs do “Dia Padrão” (6 UNIs), arredondado para o próximo dia útil, levando-se em conta apenas dias úteis. Através de formulário próprio implementado no sistema Redmine, as UNIS são computadas em cada um dos itens de repertório utilizado nas demandas e o prazo de entrega da implementação é calculado automaticamente, conforme tabela apresentada abaixo: 
## **Tabela 2: Repertório por item** 
|Área|Descrição da<br>atividade|UNIs|Estimativa<br>total de<br>UNIs|<br>Perfis|Artefatos<br>a<br>serem<br>entregues|
|---|---|---|---|---|---|
|Design|Criação de protótipo<br>de uma tela|3|30|Analista de<br>Usabilidade/<br>Design|Protótipo com<br>navegação entre as<br>telas em ferramenta<br>de Design.|
||Alteração de protótipo<br>de uma tela|<br>1|12|Analista de<br>Usabilidade/<br>Design|Protótipo com<br>navegação entre as<br>telas em ferramenta<br>de Design.|
|Análise|Criação de Desenho<br>da arquitetura da<br>solução (exemplos:<br>modelo de dados,<br>fluxo de integração<br>entre serviços etc.)|18|72|Analista /<br>Desenvolvedor<br>Arquiteto de<br>Software|Arquitetura da<br>solução entregue no<br>repositório de<br>documentações do<br>INPI|
Página **22** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
|Área|Descrição da<br>atividade|UNIs|Estimativa<br>total de<br>UNIs|<br>Perfis|Artefatos<br>a<br>serem<br>entregues|
|---|---|---|---|---|---|
||Alteração de<br>Desenho da<br>arquitetura da<br>solução (exemplos:<br>modelo de dados,<br>fluxo de integração<br>entre serviços etc.)|6|36|Analista /<br>Desenvolvedor<br>Arquiteto de<br>Software|Arquitetura da<br>solução entregue no<br>repositório de<br>documentações do<br>INPI|
||Verificação,<br>disparada pela<br>constatação de erros<br>em produção que<br>impactam a utilização<br>do sistema. Devem<br>ser atendidas<br>imediatamente,<br>independente de<br>prioridades|6 por<br>demanda|216|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Identificação do erro<br>entregue no<br>repositório de<br>documentações do<br>INPI|
|Desenvolvimento|Criação de template<br>(exemplos: jasper<br>report, formulário<br>Delphi etc) ou de<br>telas (exemplos: html,<br>jsf etc) de sistemas|6|1884|Analista de<br>Usabilidade/<br>Design<br>Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Alteração de template<br>(exemplos: jasper<br>report, formulário<br>Delphi etc) ou de<br>telas (exemplos: html,<br>jsf etc) de sistemas|1|740|Analista de<br>Usabilidade/<br>Design<br>Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Criação de teste<br>utilizando<br>ferramentas<br>automatizadas<br>(exemplos: Junit,<br>Postman, Selenium,<br>Spock etc), quando<br>não existentes no<br>sistema e solicitados<br>pelo INPI, ou seja,<br>dissociados do<br>processo de<br>desenvolvimento.|0,5 para<br>cada teste|14|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Criação teste de<br>integração com|3 para cada<br>teste|510|Analista/<br>Desenvolvedor|Código fonte<br>versionado no|
Página **23** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
|Área|Descrição da<br>atividade|UNIs|Estimativa<br>total de<br>UNIs|<br>Perfis|Artefatos<br>a<br>serem<br>entregues|
|---|---|---|---|---|---|
||validação e acesso a<br>base de dados em<br>memória ou chamada<br>a serviço interno ou<br>externo, incluindo<br>geração de massa de<br>dados.|||Arquiteto de<br>Software|repositório do INPI.|
|Desenvolvimento|Criação -<br>Desenvolvimento de<br>1 (uma) operação de<br>criação, leitura,<br>atualização ou<br>remoção.<br>Programação<br>completa, incluindo<br>teste utilizando<br>ferramentas<br>automatizadas (não<br>limitado a uma<br>ferramenta),<br>utilização de<br>biblioteca, validação<br>dos campos,<br>sanitização.<br>Criação -<br>Desenvolvimento de<br>funcionalidade de<br>bibliotecas<br>reutilizáveis<br>Este item só pode ser<br>utilizado em casos de<br>criação de<br>funcionalidades.|9|9702|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.<br>Testes automatizados<br>entregues no<br>repositório/ferramenta<br>de testes do INPI.<br>Documentação<br>funcional entregue no<br>repositório de<br>documentações do<br>INPI.|
||Alteração -<br>Desenvolvimento de<br>1 (uma) operação de<br>criação, leitura,<br>atualização ou<br>remoção.<br>Programação<br>completa, incluindo<br>teste utilizando<br>ferramentas<br>automatizadas (não<br>limitado a uma<br>ferramenta),<br>utilização de<br>biblioteca, validação<br>dos campos,<br>sanitização.|3|6693|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.<br>Testes automatizados<br>entregues no<br>repositório/ferramenta<br>de testes do INPI.<br>Documentação<br>funcional entregue no<br>repositório de<br>documentações do<br>INPI.|
Página **24** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
|Área|Descrição da<br>atividade|UNIs|Estimativa<br>total de<br>UNIs|<br>Perfis|Artefatos<br>a<br>serem<br>entregues|
|---|---|---|---|---|---|
||Alteração -<br>Desenvolvimento de<br>funcionalidade de<br>bibliotecas<br>reutilizáveis<br>Este item só pode ser<br>utilizado em casos de<br>alteração de<br>funcionalidades.|||||
||Reaproveitar uma<br>operação dentro de<br>um mesmo sistema.<br>Programação<br>completa, incluindo<br>teste utilizando<br>ferramentas<br>automatizadas|3 por<br>operação|111|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Criação –<br>Desenvolvimento de<br>função de front-end<br>de um sistema.|2 por função|1022|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Alteração de função<br>de front-end de um<br>sistema.|1 por função|372|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Alteração de<br>configuração de<br>dependência<br>(parâmetros de<br>configuração, versões<br>etc)|<br>1 por<br>dependência|37|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Extração de<br>Relatórios a partir de<br>base de dados<br>Este item só deve ser<br>utilizado em casos<br>que não envolvam<br>geração de código<br>fonte.|6 por<br>demanda|366|Analista/<br>Desenvolvedor|Relatório entregue no<br>repositório de<br>documentações do<br>INPI.<br>Script de banco<br>versionado no<br>repositório do INPI.|
||Alteração não<br>funcional em código-<br>fonte de sistema em<br>produção<br>(parâmetros não|1 por<br>demanda|37|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
Página **25** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
|Área|Descrição da<br>atividade|UNIs|Estimativa<br>total de<br>UNIs|<br>Perfis|Artefatos<br>a<br>serem<br>entregues|
|---|---|---|---|---|---|
||relacionados a<br>dependências que<br>estejam hard-coded)|||||
|Implantação|Criação de script para<br>automação de<br>atividade (script<br>ansible etc)|<br>6 por script|330|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Alteração de script<br>para automação de<br>atividade (script<br>ansible etc)|1 por de<br>script|11|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Criação de etapa no<br>jenkinsfile|2 por etapa|260|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Código fonte<br>versionado no<br>repositório do INPI.|
||Execução de<br>rotina/execução de<br>scripts<br>automatizados.|1 por<br>demanda|27|Analista/<br>Desenvolvedor|Evidências da<br>execução entregues<br>no repositório de<br>documentação.|
|Arquitetura|Criação de novos<br>ambientes de<br>sistemas<br>(contemplando toda a<br>infra-estrutura e<br>execução de scripts<br>necessários para o<br>funcionamento do<br>ambiente, criação de<br>scripts ansible)|60 UNIS por<br>ambiente|960|Arquiteto de<br>Software|Ambiente criado e<br>disponibilizado para<br>utilização;<br>Scripts ansible<br>versionados no<br>repositório de código<br>fonte;<br>Apresentação<br>disponibilizada no<br>repositório de<br>documentação, após<br>a apresentação.|
|Banco de Dados|Criação/alteração de<br>estrutura de BD;<br>Atualização de dado<br>em banco (criação,<br>atualização ou<br>remoção) quando<br>solicitada pelo INPI;<br>Script DDL para<br>criação de banco de<br>dados completo em<br>memória para testes<br>de integração.|2 por<br>demanda|230|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Script anexado no<br>repositório de<br>documentação.<br>Script de banco<br>versionado no<br>repositório do INPI.|
Página **26** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
|Área|Descrição da<br>atividade|UNIs|Estimativa<br>total de<br>UNIs|<br>Perfis|Artefatos<br>a<br>serem<br>entregues|
|---|---|---|---|---|---|
|Documentação|Estudo de código-<br>fonte Conforme<br>descrito no item 5.7|30 UNIS por<br>sistema|420|Analista/<br>Desenvolvedor<br>Arquiteto de<br>Software|Apresentação<br>disponibilizada no<br>repositório de<br>documentação|
O indicador para avaliação do atraso no prazo das demandas considera dias úteis de atraso não justificados para cada etapa da demanda solicitada, conforme equação abaixo: 
**IA** = 0,05 × [dias úteis de atraso] 
## **11.2. Qualidade de código** 
Através de ferramenta automatizada de verificação de qualidade de software, como por exemplo, SonarQube, é realizada uma análise estática do código para detectar bugs, duplicidade de código e vulnerabilidades de segurança, com exceção da linguagem DELPHI. 
Tendo a codificação que atingir a qualidade definida conforme parâmetros descritos abaixo: 
**Tabela 3: Parâmetros de qualidade para primeira versão do código fonte** 
|**Primeira versão do código fonte**|**Primeira versão do código fonte**||
|---|---|---|
|**Métrica**|**Unidade**|**Valor**|
|Reliability Rating|Nota|A|
|Security Rating|Nota|A|
|Duplicated Lines|Percentual|<= 5%|
|Complexity / Function|Média|<= 3|
|Complexity / File|Média|<= 12|
|Complexity / Class|Média|<= 12|
|Maintainnability Rating|Nota|A|
|Technical Debt Ratio|Percentual|<= 2,5%|
|Blocker Issues|Quantidade|= 0|
|Critical Issues|Quantidade|= 0|
|Unit Tests Coverage|Percentual|>= 80%|
|Unit Tests Success|Percentual|= 100%|
|Skipped Unit Test|Quantidade|= 0|
Página **27** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
**Tabela 4: Parâmetros de qualidade para código fonte que já possua análise no SonarQube** 
|**Versõespara código fonteque**|**já possuam análise no**|**SonarQube**|
|---|---|---|
|**Métrica**|**Unidade**|**Valor**|
|Reliability: New Bugs|Quantidade|= 0|
|Security: New Vulnerabilities|Quantidade|= 0|
|Duplicated Lines|Percentual|Deve diminuir na comparação<br>com a versão imediatamente<br>anterior|
|Maintainability:<br>New<br>Code<br>Smells|Quantidade|= 0|
|Technical Debt Ratio on New<br>Code|Percentual|<= 2,5%|
|New Blocker Issues|Quantidade|= 0|
|New Critical Issues|Quantidade|= 0|
|Unit Tests Coverage on New<br>Code|Percentual|>= 80%|
|Unit Tests Success|Percentual|= 100%|
|Skipped Unit Test|Quantidade|= 0|
## **11.3. Rejeição** 
A depender da qualidade da entrega dos artefatos, estes poderão ser rejeitados e esta ação registrada no sistema de controle de demandas do INPI (Redmine) como tarefa do tipo “Rejeição” associada à demanda que gerou o erro. 
O indicador para avaliação do número de rejeições causadas por falhas de documentação, metodologia, implementação ou qualidade, identificados em teste/homologação será dado pela seguinte equação: 
**IR** = 0,10 × [quantidade de rejeições da demanda] 
## **11.4. Leadtime** 
Como métrica para controlar quanto tempo uma tarefa leva para ser completada é adotado o Lead Time que é calculado com o número de dias entre o início e o fim de uma entrega. Esse intervalo é calculado conforme a demanda alcança diferentes status no processo de desenvolvimento: 
## • **Tarefas do tipo DEMANDA:** 
INICIO_LEADTIME – Quando a demanda atinge a situação “Analisar solicitação” ou a situação “Detalhar solicitação” 
FIM_LEADTIME – Quando a demanda atinge a situação “Entregar artefatos” 
Com o monitoramento do Lead Time é possível detectar pontos de lentidão, antecipando oportunidades de melhorias por meio de ações específicas e direcionadas. 
Página **28** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **12. Governança** 
Não aplicável. 
## **13. Dono do documento** 
Rhodrigo da Venda Santana, Chefe de Divisão, PR/DIREX/CGTI/COSIS/DIPRO 
## **14. Elaborador(es) do documento** 
Celso de Souza Tchao, PR/DIREX/CGTI/COSIS/DIPRO 
## **15. Aprovador(es) do documento** 
Marcus Vinicius da Motta Vieira, Coordenador Geral, PR/DIREX/CGTI Pedro Calisto Luppi Monteiro Junior, Coordenador de Sistemas, PR/DIREX/CGTI/COSIS 
## **16. Bibliografia** 
ANCINE – Agência Nacional de Cinema. **Metodologia de Desenvolvimento de Sistemas** . 2011. Disponível em: http://mds.ancine.gov.br/index.php. Acesso em 10 de set. 2021. 
EPL - Empresa de Planejamento e Logística. **Processo de Desenvolvimento de Software da Empresa de Planejamento e Logística PDS – EPL Versão 2.0** . Disponível em: https://www.epl.gov.br/pds. Acesso em 26 de jul. 2021. 
FINEP - Financiadora de Estudos e Projetos. **Metodologia de desenvolvimento de software da FINEP – MDS FINEP Versão 2.1** . 2017. Disponível em: http://www.finep.gov.br/images/licitacoes/2017/Consulta012017/I_MDS.pdf. Acesso em 26 de jul. 2021. 
PJERJ - Poder Judiciário do Estado do Rio de Janeiro. **Metodologia de desenvolvimento de sistemas - Versão 2.0** . Disponível em: http://www.tjrj.jus.br/documents/10136/6364473/anexo-a.pdf. Acesso em 26 de jul. 2021. 
SUSEP – Superintendência de Seguros Privados. **Metodologia de Gestão e Desenvolvimento de Software** . 2011. Disponível em: http://www.susep.gov.br/setoressusep/noticias/download/tisusep/MGDS_SUSEP_v1.0.pdf. Acesso em 26 de jul. 2021. 
TRT7 - Tribunal Regional do Trabalho da 7ª Região. PDS-TRT7 **Processo de Desenvolvimento de Software.** 2016. Disponível em: https://www.trt7.jus.br/files/institucional/governanca_ti/processos/PDS-TRT7-rev-1_0-semAto.pdf. Acesso em 26 de jul. 2021. 
Página **29** de **30** 
METODOLOGIA DE DESENVOLVIMENTO DE SOFTWARE 
GETI – GST – MN – 0001 
## **17. Histórico das alterações** 
|**Data**|**Nº revisão**|**Item**|**Descrição**|
|---|---|---|---|
|||||
|||Todo||
|07/12/2021|0.0||Emissão inicial|
|||documento||
|||||
|||||
|||||
||||Adequação dos fluxos, troca de elaborador e|
|10/10/2023|1.0|10, 14 e 15||
||||<br>aprovador do documento.|
|||||
|||||
## **18. Anexos** 
Não aplicável. 
Página **30** de **30** 
** **
** **
** **
** **
** **
** **
** **
** **
** **
** **
** **
** **
** **
** **
** **