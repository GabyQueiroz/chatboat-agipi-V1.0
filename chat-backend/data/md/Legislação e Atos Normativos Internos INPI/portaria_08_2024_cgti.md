** **
## **MINISTÉRIO DO DESENVOLVIMENTO, INDÚSTRIA, COMÉRCIO E SERVIÇOS INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** 
## PORTARIA /INPI/DIRAD/CGTI Nº 8, DE 10 DE SETEMBRO DE 2024 
Publica a Metodologia de Desenvolvimento de So�ware 
**O COORDENADOR-GERAL DE TECNOLOGIA DA INFORMAÇÃO DO INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** , no uso das atribuições que lhe foram conferidas pelo Decreto nº 8.854, de 22 de setembro de 2016, e pela Portaria INPI PR nº 09, publicada em 13 de março de 2024, e tendo em vista o conteúdo do processo SEI nº 52402.009888/2024-01, 
## **RESOLVE:** 
Art. 1º Publicar, na forma do anexo a esta Portaria, conforme definido no item 7.4 do Manual do Sistema de Padronização de Documentos GEQU-GDS-MN-0001, rev. 2.0, a Metodologia de Desenvolvimento de So�ware (1084389) e seus anexos GETI-GST-FP-0008 (1084395); GETI-GST-FP-0009 (1084399); GETI-GST-FP-0010 (1084401); e GETI-GST-FP-0011 (1084404). 
Art. 2º Revogar a PORTARIA/INPI/CGTI nº 01, de 10 de novembro de 2023. 
Art 3º Esta Portaria entra em vigor na data de sua publicação. 
## **Marcus Vinicius da Mo�a Vieira** 
Coordenador-Geral de Tecnologia da Informação 
** **
Documento assinado eletronicamente por **MARCUS VINICIUS DA MOTTA VIEIRA** , **Coordenador(a) Geral** , em 20/09/2024, às 10:10, conforme horário oficial de Brasília, com fundamento no art. 6º, § 1º, do Decreto nº 8.539, de 8 de outubro de 2015. 
** **
A auten�cidade deste documento pode ser conferida no site h�p://sei.inpi.gov.br/sei/controlador_externo.php? acao=documento_conferir&id_orgao_acesso_externo=0, informando o código verificador **1086024** e o código CRC **AEB61014** . 
Boletim Pessoal XV do mês de Setembro RETIFICA.docx ~~de 2024 I~~ Expedido em SEI nº 1086024 20/09/2024 Republicada por erro material 
**Referência:** Processo nº 52402.009888/2024-01 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>MANUAL|**Código **|GETI – GST – MN – 0002|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|09/09/2024|
||**METODOLOGIA DE DESENVOLVIMENTO DE**<br>**SOFTWARE**|**Processo**|Gestão de Soluções<br>de TIC (Nível 2)|
## **Sumário** 
|**1. Introdução ...................................................................................................................................... 2**|**1. Introdução ...................................................................................................................................... 2**|
|---|---|
|**2. Objetivo .......................................................................................................................................... 2**||
|**3. Abrangência ................................................................................................................................... 2**||
|**4. Documentos complementares ...................................................................................................... 2**||
|**5. Glossário ........................................................................................................................................ 2**||
|**6. Fundamentos Gerais ..................................................................................................................... 4**||
||**6.1. Projeto de Software...............................................................................................................4**|
||**6.1.1. Serviços de desenvolvimento, manutenção e qualidade de software ....................... 4**|
||**6.2. Resultados esperados ........................................................................................................ 5**|
||**6.3. Princípios Gerais ................................................................................................................. 5**|
||**6.4. Práticas do método Scrum ................................................................................................. 6**|
||**6.5. Padrões e Requisitos .......................................................................................................... 7**|
||**6.6. Papéis e Responsabilidades .............................................................................................. 8**|
|**7. Descrição dos processos ou atividades .................................................................................... 10**||
||**7.1. Processo de desenvolvimento e manutenção de software ............................................ 10**|
||**7.1.1. Planejar a sprint .......................................................................................................... 10**|
||**7.1.2. Executar a sprint ......................................................................................................... 12**|
||**7.1.3. Revisar a sprint ........................................................................................................... 13**|
||**7.1.4. Entregar incremento ....................................................................................................15**|
|**8. Entradas do processo ................................................................................................................. 17**||
|**9. Saídas do processo ..................................................................................................................... 17**||
|**10.**|**Fluxo do processo ..................................................................................................................... 17**|
|**11.**|**Indicadores do processo ........................................................................................................... 17**|
||**11.1. Indicador de Aceitação da Sprint/Entrega .................................................................. 18**<br> **11.2. Indicador de Produtividade Ágil .................................................................................. 18**|
||**11.3. Indicador de Qualidade de código .............................................................................. 19**|
||**11.4. Indicador de Conformidades em Homologação ......................................................... 20**|
||**11.5. Leadtime ....................................................................................................................... 20**|
|**12.**|**Governança ........................................................................................................................... 21**|
|**13.**|**Dono do documento ............................................................................................................. 21**|
|**14.**|**Outros** **elaborador(es) do documento ................................................................................. 21**|
|**15.**|**Aprovador(es) do documento .............................................................................................. 21**|
|**16.**|**Bibliografia ............................................................................................................................ 21**|
|**17.**|**Histórico das alterações ...................................................................................................... 22**|
|**18.**|**Anexos .................................................................................................................................. 22**|
Página **1** de **22** 
## **1. Introdução** 
As metodologias de desenvolvimento de software consistem, basicamente, no conjunto de abordagens que podem ser utilizadas para a criação de sistemas de processamento de dados. 
Os serviços de desenvolvimento e manutenção de software integram, no ramo da engenharia de software, o processo de ciclo de vida do desenvolvimento de software ( _Software Development Life Cycle - SLDC_ ), ou seja, um processo contínuo e sistemático de construção que garante a qualidade e a correção precisa de falhas do software construído. Neste sentido, a continuidade dos serviços é uma característica inerente ao ciclo de vida do software assegurando a evolução dos requisitos, a disponibilidade e o desempenho das funcionalidades à medida que as necessidades de negócio e os recursos tecnológicos (físicos e lógicos) evoluem. 
Neste manual é descrita a metodologia aplicável aos projetos de desenvolvimento e manutenção de software no INPI, contemplando atividades, fluxos, responsáveis e artefatos necessários ao ciclo de vida do projeto. 
## **2. Objetivo** 
Definir um padrão para a gestão e o desenvolvimento de software no INPI, por meio de uma abordagem iterativa e incremental, adotando práticas ágeis, com o intuito de focar na qualidade da entrega do software e valor agregado para os clientes. 
## **3. Abrangência** 
Este documento abrange todas as áreas que atuam diretamente no processo de desenvolvimento e manutenção de software no âmbito do INPI, devendo ser amplamente divulgado a todos os servidores, colaboradores e empresas prestadoras de serviços dessas áreas. 
Igualmente, todas as áreas demandantes de soluções de tecnologia de informação precisam ter acesso ao documento e conhecimento de sua amplitude, a fim de que estejam cientes das etapas fundamentais para a implementação de um produto de software que atenda às necessidades pretendidas. 
## **4. Documentos complementares** 
GETI – GST – IT – 0001_Abertura de demandas no Sistema Redmine. GETI–GST–PP– 0001 – Detalhamento do Backlog do Produto (ou Histórias do Usuário) Ver. 0.0. 
## **5. Glossário** 
Artefatos – Subprodutos produzidos durante o desenvolvimento de software. Ajudam a descrever a função, arquitetura e o design do software ou estão relacionados com o próprio processo de desenvolvimento. 
Backlog da Sprint – conjunto de itens do Backlog do Produto selecionados para a Sprint 
Backlog do Produto – representa tudo que é necessário para desenvolver e lançar um produto de valor agregado ao negócio. É uma lista priorizada de todos os requisitos (funcionais e não funcionais), funções, tecnologias, melhorias e correções de defeitos que constituem as mudanças que serão efetuadas no produto para versões futuras. 
Página **2** de **22** 
Bugs – Erros em sistemas. 
CGTI – Coordenação Geral de Tecnologia da Informação. 
COSIS – Coordenação de Sistemas. 
DELPHI – Linguagem de programação para o desenvolvimento de sistemas. 
DIPRO – Divisão de Padronização de Software. 
DIREX – Diretoria Executiva. 
GETI – Gestão de Tecnologia da Informação e Comunicações. 
História de usuário - é uma explicação informal e geral sobre um recurso de software escrita a partir da perspectiva do usuário final ou cliente 
Incremento de produto – versão de um produto que pode ser liberada no final de um período(timebox). 
INPI – Instituto Nacional da Propriedade Industrial. 
Metodologias ágeis – são um conjunto de práticas que visam a entrega rápida e de alta qualidade do produto ou serviço e que promovem um processo de gerenciamento de projetos que incentiva a inspeção e adaptação frequente, beneficiando a eficiência e efetividade dos gestores públicos no controle da prestação dos serviços de TI, haja vista que o foco passa a ser realmente nas atividades que entregam valor para as áreas de negócios. 
PDTIC – Plano Diretor de Tecnologia da Informação e Comunicação. 
Refatoração ( _Refactoring_ ) – Processo de modificar um sistema de software para melhorar a estrutura interna do código sem alterar seu comportamento externo. 
Release – distribuição/liberação de um incremento de produto para um cliente ou usuários. A quantidade de sprints por release deve ser definida previamente à execução dos serviços. 
Timebox - Determina um limite de tempo para a conclusão de uma Sprint 
Tipo de Tarefa: Sprint – Nesta categoria são classificadas as tarefas que representam as sprints definidas para implementar as histórias de usuário. 
Tipo de Tarefa: Item da sprint – Nesta categoria são classificadas as tarefas que representam os itens de backlog da sprint. 
Sprint – Corresponde a um grupo de atividades para transformar os itens de backlog em um incremento de software. 
Página **3** de **22** 
## **6. Fundamentos Gerais** 
A metodologia está alicerçada em 4 pilares: 
1. Priorização balanceada: considera o valor agregado, visando promover práticas que permitam aos participantes do projeto desenvolver uma solução que maximize os benefícios e seja compatível com as restrições existentes. 
2. Colaboração: alinhamento de interesses e compartilhamento do entendimento, visando promover um ambiente de equipe saudável que promova a colaboração e a compreensão do projeto. 
3. Focar na arquitetura: concentração na arquitetura desde o início para minimizar riscos e organizar o desenvolvimento, além de promover práticas que minimizem os riscos na fase de desenvolvimento. 
4. Evolução contínua e obtenção de feedback: promove práticas que permitem a equipe obter feedback de maneira contínua e o mais cedo possível, permitindo agregar valor a cada desenvolvimento e diminuir o risco do projeto conforme a execução. 
## **6.1. Projeto de Software** 
Projeto de software é um serviço disponibilizado pela área de Tecnologia da Informação para atender às necessidades do Instituto. Como principais serviços nos projetos de desenvolvimento de software temos: desenvolvimento, manutenção de software e serviço de qualidade e teste avançado de software. 
## **6.1.1. Serviços de desenvolvimento, manutenção e qualidade de software** 
Compreendem o conjunto de atividades executadas com a finalidade de atender às necessidades do órgão ou entidade por meio da implementação de um novo software, de uma nova funcionalidade ou manutenção de funcionalidades já existentes. Suas atividades incluem: 
- a) aplicação de técnicas de engenharia de requisitos com vistas a identificar e especificar requisitos funcionais e não funcionais dos produtos a serem entregues; 
- b) execução de procedimentos de design / arquitetura de software com vistas a estabelecer os padrões, tecnologias, formas de organização e de componentização dos recursos a serem utilizados na construção e manutenção dos sistemas; 
- c) implementação dos códigos, componentes e recursos necessários à materialização do produto de software; 
- d) planejamento da execução de testes de software para modelar e elaborar estratégias de testes; 
- e) realização de testes de unidade, de integração, funcionais e testes de “fumaça”, com vistas a assegurar a qualidade do software; 
- f) criação/manutenção do versionamento dos artefatos no repositório do INPI; g) realização da homologação dos produtos junto aos clientes, com vistas a certificar-se que o software atende aos requisitos esperados; 
- h) realização da implantação dos produtos junto às áreas de operação e suporte de rede, ou áreas equivalentes, com o objetivo de assegurar a efetiva entrega do software em ambiente de produção; 
- i) adoção das medidas necessárias para assegurar a disponibilidade, integridade, confidencialidade e autenticidade das informações a serem tratadas no âmbito da prestação dos serviços de desenvolvimento, manutenção, testes e controle de qualidade de software; 
Página **4** de **22** 
- j) adoção das medidas para garantir a proteção dos dados, antecipando ameaças à privacidade, à segurança e à integridade, prevenindo acesso não autorizado às informações disponibilizadas para prestação dos serviços de desenvolvimento, manutenção, testes e controle de qualidade de software; 
- k) adoção de práticas de codificação segura; l) criação/atualização da documentação dos sistemas; 
- m) mapeamento de problemas, cenários e soluções dos sistemas em produção; n) apoio técnico na busca contínua pela melhoria de processos das áreas; o) apoio ao desenvolvimento e manutenção de software, atuando para garantir que os softwares entregues tenham sido testados de acordo com as melhores práticas de mercado e os padrões previstos neste MDS, apontando as falhas e/ou oportunidades de melhoria nos processos de desenvolvimento e testes, bem como nos produtos resultantes destes processos; 
- p) verificação da atualidade da documentação técnica dos sistemas; q) realização de diagnóstico de situações de gargalos e problemas de desempenho nos sistemas; 
- r) proposição de melhoria da arquitetura dos sistemas visando garantir a arquitetura mais robusta possível; 
## **6.2. Resultados esperados** 
Com a implementação desta Metodologia de Desenvolvimento de Software são esperados os seguintes benefícios: 
- fornecer novos serviços digitais, relacionados ao escopo de atuação do Instituto; 
- • manter e aprimorar a disponibilidade, segurança, acessibilidade e usabilidade dos serviços digitais ofertados; 
- aprimorar e evoluir os sistemas de informação que apoiam as políticas públicas de governo; 
- assegurar a troca eficiente de informações entre os diferentes processos de negócio; 
- • assegurar a segurança e privacidade das informações mantidas e processadas pelos sistemas; 
- manter a resiliência e eficiência dos sistemas de informação do Instituto; 
- • demonstrar agilidade no atendimento das demandas, mesmo que haja flutuações sazonais na quantidade de ordens de serviço; 
## **6.3. Princípios Gerais** 
Os princípios elencados na enumeração abaixo devem ser utilizados: 
- **I. PD1 - Primeiro Princípio Geral do Processo de Desenvolvimento de Software do INPI** Haverá apenas um processo de desenvolvimento de software para todo o Órgão, sob a responsabilidade da Divisão de Padronização de Software. 
- **II. PD2 - Segundo Princípio Geral do Processo de Desenvolvimento de Software do INPI** O desenvolvimento de software é atividade exclusiva da CGTI. 
## **III. PD3 - Princípio de Ferramentas e Instrumentos** 
- A Divisão de Padronização de Software definirá as ferramentas e instrumentos padrões da metodologia de desenvolvimento de software, que deverão ser utilizados por todos os agentes. 
## **IV. PD4 - Princípio de Viabilidade Técnica da Demanda** 
Página **5** de **22** 
O atendimento da demanda somente poderá ser executado após a análise da viabilidade técnica da solicitação, sendo esta onerosa para o INPI ou não. 
## **V. PD5 - Princípio de Prioridades** 
 - As demandas deverão seguir a determinação de prioridades estabelecida pelo Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC vigente). 
- **VI. PD6 – Princípio da Simplicidade** Elimine tudo aquilo que for desnecessário, pois ele onera e sobrecarrega o processo, as pessoas e o produto. 
**VII. PD7 – Princípio do Foco** Estabeleça um foco nos itens de solução, nas necessidades e nos problemas, para que a energia de trabalho se concentre apenas nos objetivos e acordos firmados. 
## **6.4. Práticas do método Scrum** 
Para promover a entrega de projetos de software que cumpram as metas de qualidade, prazo e custos, os métodos ágeis preconizam uma série de valores e princípios distintos do desenvolvimento tradicional de software. O entendimento destes valores e princípios, bem como suas práticas, são fatores de sucesso. Todos os envolvidos no projeto devem conhecer princípios e práticas dos métodos ágeis. 
O processo de desenvolvimento ágil de software adotado baseia-se no método Scrum, sendo esta uma metodologia que propõe que um projeto seja dividido em diversos (pequenos) ciclos de atividades, com reuniões frequentes para que a equipe possa alinhar o que vem fazendo e pensar formas de melhorar o processo com agilidade. 
Resumindo, o processo Scrum acontece em três etapas: 
- O dono do produto analisa as necessidades e faz o backlog do produto; 
- As equipes scrum trabalham em uma entrega de valor durante um período denominado sprint; 
- As equipes scrum e as partes interessadas inspecionam e ajustam os resultados para o próximo sprint. 
E então o processo é repetido, conforme Figura1. 
Figura 1 - Fluxo do Scrum para um Sprint 
** **
Institute Project Management (2022). 
Página **6** de **22** 
## **6.5. Padrões e Requisitos** 
Deve-se observar, no que couber, os seguintes padrões: 
- Lei Geral de Proteção de Dados - LGPD - Lei 13.709, de 2018; 
- Princípios de _Security by Design, Privacy by Design e Shift-left testing_ , de forma a minimizar os riscos de privacidade e segurança em tempo de concepção dos projetos; 
- Padrão Digital de Governo ( _Design System_ ) e suas atualizações com relação ao padrão visual das aplicações, disponível no endereço: **https://www.gov.br/ds/home** ; 
- Padrões de projeto ( _Design Patterns_ ) ou padrões arquiteturais consolidados no mercado aderentes às necessidades da aplicação, além de métodos de codificação limpa (Clean Code); 
- Abordagem TDD ( _Test Driven Development_ ); 
- ABNT NBR ISO/IEC/IEEE 12207:2021 - Engenharia de sistemas e software - Processos de ciclo de vida de software; 
- ABNT NBR ISO/IEC 25030:2008 - Engenharia de software - Requisitos e Avaliação da Qualidade de Produto de Software (SQuaRE) - Requisitos de qualidade; 
- ABNT NBR ISO 22301:2013 - Sistemas de gestão de continuidade de negócios; 
- ABNT NBR ISO 22313:2015 - Sistemas de gestão de continuidade de negócios; 
- ABNT NBR ISO 27031:2015 - Diretrizes para a prontidão para a continuidade dos negócios da tecnologia da informação e comunicação; 
- ABNT NBR ISO 23081-1:2019 - Metadados para documentos de arquivo; 
- ABNT NBR 11515:2007 - Guia de práticas para segurança física relativas ao armazenamento de dados; 
- ABNT NBR ISO/IEC 27037:2012 - Diretrizes para identificação, coleta, aquisição e preservação de evidência digital; 
- ABNT NBR ISO/IEC 27002:2013 - Código de prática para controles de segurança da informação; 
- ABNT NBR ISO/IEC 27014:2013 - Governança de segurança da informação; 
- ABNT NBR 16167:2013 - Diretrizes para classificação, rotulação e tratamento da informação; 
- ABNT NBR ISO/IEC 27017:2016 - Código de prática para controles de segurança da informação com base; 
- Guia de Gerenciamento de Vulnerabilidades e Modelo de Política de Gerenciamento de Vulnerabilidades - SGD/ME, disponível em https://www.gov.br/governodigital/pt-br/segurancae-protecao-de-dados/ppsi; 
- Guia de Segurança em Aplicações Web - SGD/ME, disponível em https://www.gov.br/governodigital/pt-br/seguranca-e-protecao-de-dados/ppsi; 
- Guia de Requisitos Mínimos de Segurança e Privacidade para APIs - SGD/ME, disponível em https://www.gov.br/governodigital/pt-br/seguranca-e-protecao-de-dados/ppsi; 
- Guia de Requisitos Mínimos de Segurança e Privacidade para Aplicativos Móveis - SGD/ME, 
- disponível em https://www.gov.br/governodigital/pt-br/seguranca-e-protecaode-dados/ppsi; 
Página **7** de **22** 
## **6.6. Papéis e Responsabilidades** 
**Tabela 1: Descrição de papéis e responsabilidades** 
|**Papel**|**Descrição**|**Responsabilidade**|
|---|---|---|
|**Cliente (INPI)**|Servidor do INPI|•Descrever o projeto de acordo<br>com<br>as<br>necessidades<br>e<br>resultados esperados;<br>•Abrir demandas de manutenção;<br>•<br>Homologar implementação;|
|**Analista TI**<br>**(INPI)**|Servidor da área<br>de TI|•<br>Analisar a solicitação de um novo<br>projeto; criar projeto no sistema de<br>controle de demandas do INPI<br>(Redmine);<br>•<br>Validar a escrita das histórias de<br>usuário;<br>priorizar<br>demandas;<br>analisar e detalhar solicitações de<br>novas funcionalidades;<br>•<br>Validar<br>especificações<br>e<br>testar<br>implementação;<br>•<br>Registrar defeitos relacionados às<br>demandas e concluir demandas.|
|**Scrum Master**|Profissional com<br>conhecimento<br>aprofundado<br>em<br>técnicas<br>ágeis.|•<br>Garantir<br>que<br>o<br>_Scrum_<br>seja<br>entendido e aplicado;<br>•<br>Assegurar que todos os eventos do<br>Scrum têm lugar e são positivos,<br>produtivos e mantidos dentro tempo<br>previsto;<br>•<br>Apoiar o Dono do Produto e a<br>organização na adoção de práticas<br>ágeis;<br>•<br>Buscar melhoria contínua do time;<br>•<br>Facilitar<br>a<br>colaboração<br>dos<br>stakeholders conforme solicitado ou<br>necessário;<br>•<br>Acompanhar<br>e<br>apresentar<br>os<br>indicadores do processo;<br>•<br>Remover<br>impedimentos<br>para<br>a<br>equipe de desenvolvimento durante<br>a execução das Sprints.<br>•<br>Criar o Sprint Backlog;|
|**Dono do Produto (Product Owner**<br>`–`**PO)**|Servidor<br>representante da<br>área demandante<br>de soluções de<br>software,<br>designado<br>por<br>autoridade<br>competente|•<br>Responsável por ordenar o trabalho<br>a ser realizado pelo time, criando,<br>mantendo<br>e<br>priorizando<br>o(s)<br>backlog(s) do(s) produto(s);<br>•<br>Criar e compartilhar a Visão do<br>Produto;<br>•<br>Planejar o Roadmap;<br>•<br>Construir o Backlog do Produto;<br>•<br>Expressar claramente os itens do<br>Backlog do Produto;<br>•<br>Ordenar e priorizar os itens do|
Página **8** de **22** 
|||Backlog do Produto;<br>•<br>Definir quais itens farão parte da<br>sprint;<br>•<br>Garantir<br>que<br>o<br>time<br>de<br>desenvolvimento entenda os itens<br>do Backlog do Produto no nível<br>necessário;<br>•<br>Apoiar<br>no<br>planejamento<br>da<br>Release;<br>•<br>Validar incremento de Software;<br>•<br>Validar a release ao final de cada<br>sprint;<br>•<br>Reportar a Avaliação de Satisfação<br>do Produto.|
|---|---|---|
|**Desenvolvedores de software**|Desenvolvedores<br>que fazem parte<br>do time ágil|•<br>Construir<br>o(s)<br>produto(s)<br>de<br>software;|
|**Partes interessadas**<br>**(Stakeholders)**|Profissionais<br>impactados<br>pela solução ou<br>que<br>possuam<br>interesse na<br>entrega<br>da<br>solução|•<br>Opinar<br>e<br>contribuir<br>para<br>o<br>planejamento e tomadas de decisão<br>do negócio ou projeto;<br>•<br>Esclarecer dúvidas;<br>•<br>Se necessário, apoiar o PO na<br>validação da sprint ou release.|
|**Analista de Qualidade (INPI)**|Servidor da área<br>de TI|•<br>Garantir a qualidade dos sistemas<br>durante todo o ciclo do processo de<br>software até a sua implantação,<br>minimizando a ocorrência de erros<br>no ambiente de produção;|
|**Analistas de Teste e Qualidade**|Analistas<br>de<br>Teste e<br>Qualidade<br>que<br>fazem parte do<br>time ágil|•<br>Realizar<br>a<br>revisão de<br>código,<br>realização de testes avançados e<br>revisão<br>da<br>qualidade<br>da<br>documentação produzida;<br>•<br>Aferir os critérios de aceitação da<br>qualidade dos produtos entregues.|
|**Analista de Negócio**|Analistas<br>de<br>negócio<br>que<br>fazem parte do<br>time ágil|•<br>Desenhar<br>solução<br>para<br>novos<br>produtos e serviços, para posterior<br>desdobramento em especificações<br>funcionais para desenvolvimento de<br>sistemas,<br>com<br>base<br>em<br>metodologia ágil.<br>•<br>Compreender<br>necessidades<br>de<br>usuários,<br>motivações<br>e<br>comportamentos, transformando<br>informações em insights e features.|
Página **9** de **22** 
## **7. Descrição dos processos ou atividades** 
## **7.1. Processo de desenvolvimento e manutenção de software** 
## **7.1.1. Planejar a sprint (vide fluxo GETI-GST-FP-0008_Planejar a sprint_rev0.0)** 
**Atividade:** Criar tarefa do tipo Sprint 
Criar no sistema de abertura de demandas uma tarefa do tipo Sprint. 
|**Atividade:**Criar tarefa do tipo Sprint|**Atividade:**Criar tarefa do tipo Sprint|
|---|---|
|Criar no sistema de abertura de demandas uma tarefa do tipo Sprint.||
|**Entrega:**Tarefa Sprint criada no sistema||
|**Responsável**|**Participante**|
|Analista TI|Analista TI|
|**Tarefas executadas**|**Descrição**|
|No sistema Redmine, criar a<br>demanda do tipo Sprint|Criar demanda do tipo Sprint no sistema Redmine<br>contendo informações básicas do sprint emquestão.|
|**Observação**||
|||
|**Atividade:**Associar itens backlog do produto|**Atividade:**Associar itens backlog do produto|
|---|---|
|Realizar a associação da Sprint com os itens de backlog priorizados pelo Dono do produto||
|**Entrega:**Itens de backlog associados à Sprint||
|**Responsável**|**Participante**|
|Analista TI|Analista TI, Dono do Produto|
|**Tarefas executadas**|**Descrição**|
|Associar os itens de backlog à<br>sprintque está sendoplanejada|No sistema Redmine, realizar a associação dos itens de<br>backlogà sprintplanejada|
|**Observação**||
|||
|**Atividade:**Associar itens backlog do produto|**Atividade:**Associar itens backlog do produto|
|---|---|
|Realizar a associação da Sprint com os itens de backlog priorizados pelo Dono do produto||
|**Entrega:**Itens de backlog associados à Sprint||
|**Responsável**|**Participante**|
|Analista TI|Analista TI, Dono do Produto|
|**Tarefas executadas**|**Descrição**|
|Associar os itens de backlog à<br>sprintque está sendoplanejada|No sistema Redmine, realizar a associação dos itens de<br>backlogà sprintplanejada|
|**Observação**||
|||
**Atividade:** Fragmentar em itens backlog de Sprint 
Definição da lista de itens backlog de sprint. 
|**Entrega:**itens da sprint||
|---|---|
|**Responsável**|**Participante**|
Página **10** de **22** 
|Analista TI|Analista TI/Desenvolvedor/Analista de negócio|
|---|---|
|**Tarefas executadas**|**Descrição**|
|Detalhar os itens de backlog do<br>produto,dividindo-os em itens.|Detalhamento dos itens que compõem uma sprint.|
|**Observação**||
|||
**Atividade:** Estimar os itens backlog de sprint 
Estimar esforço dos itens de sprint. 
|**Atividade:**Estimar os itens backlog de sprint|**Atividade:**Estimar os itens backlog de sprint|
|---|---|
|Estimar esforço dos itens de sprint.||
|**Entrega:**esforço dos itens da sprint||
|**Responsável**|**Participante**|
|Desenvolvedor|Analista TI/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
|Realizar estimativa do item da<br>sprint|Estimativa do esforço do item da sprint|
|**Observação**||
|||
**Atividade:** Definir itens da sprint 
Definir itens da sprint 
|**Atividade:**Definir itens da sprint|**Atividade:**Definir itens da sprint|
|---|---|
|Definir itens da sprint||
|**Entrega:**sprint definida||
|**Responsável**|**Participante**|
|Dono do Produto|Analista TI/Dono do Produto/Scrum Master|
|**Tarefas executadas**|**Descrição**|
|Definir itens da sprint|Definição de qual itens farão parte da sprint|
|**Observação**||
|||
Página **11** de **22** 
**Atividade:** Criar tarefa do tipo item da Sprint 
Criar no sistema de abertura de demandas uma tarefa do tipo item da Sprint. 
**Entrega:** Tarefa item da Sprint criada no sistema 
|**Atividade:**Criar tarefa do tipo item da Sprint|**Atividade:**Criar tarefa do tipo item da Sprint|
|---|---|
|Criar no sistema de abertura de demandas uma tarefa do tipo item da Sprint.||
|**Entrega:**Tarefa item da Sprint criada no sistema||
|**Responsável**|**Participante**|
|Analista TI|Analista TI|
|**Tarefas executadas**|**Descrição**|
|No sistema Redmine, criar a<br>demanda do tipo Sprint|Criar demanda do tipo Sprint no sistema Redmine<br>contendo informações básicas do sprint emquestão.|
|**Observação**||
|||
## **7.1.2. Executar a sprint (vide fluxo GETI-GST-FP-0009_Executar a sprint_rev0.0)** 
**Atividade:** Codificar item 
Realizar a codificação do item da Sprint 
**Entrega:** Item da Sprint codificado 
|**Atividade:**Codificar item|**Atividade:**Codificar item|
|---|---|
|Realizar a codificação do item da Sprint||
|**Entrega:**Item da Sprint codificado||
|**Responsável**|**Participante**|
|Scrum Master|Scrum Master/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
|Codificar o item da Sprint|Codificar o item da Sprint de acordo com as<br>especificações definidaspelos clientes|
|**Observação**||
|||
**Atividade:** Testar item 
Realizar testes relacionados à codificação do item da Sprint 
|**Atividade:**Testar item|**Atividade:**Testar item|
|---|---|
|Realizar testes relacionados à codificação do item da Sprint||
|**Entrega:**||
|**Responsável**|**Participante**|
|Scrum Master|Scrum Master/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
Página **12** de **22** 
Testes de codificação 
Testes associados à codificação do item da Sprint desenvolvido 
**Observação** 
**Atividade:** Entregar item 
Realizar a entrega do item da Sprint 
|**Atividade:**Entregar item|**Atividade:**Entregar item|
|---|---|
|Realizar a entrega do item da Sprint||
|**Entrega:**Itens consolidados e entregues||
|**Responsável**|**Participante**|
|Scrum Master/Desenvolvedor|Scrum Master/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
|Entregar o item da Sprint|Entrega do item da Sprint|
|**Observação**||
|||
## **7.1.3. Revisar a sprint (vide fluxo GETI-GST-FP-0010_Revisar_sprint_rev0.0)** 
**Atividade:** Verificar qualidade 
Verificar a qualidade de software gerado por meio da consolidação dos itens da sprint validando os indicadores definidos. 
**Entrega:** Qualidade da demanda validada 
|**Atividade:**Verificar qualidade|**Atividade:**Verificar qualidade|
|---|---|
|Verificar a qualidade de software gerado por meio da consolidação dos itens da sprint<br>validando os indicadores definidos.||
|**Entrega:**Qualidade da demanda validada||
|**Responsável**|**Participante**|
|Analista de Testes e Qualidade|Analista de Testes e Qualidade|
|**Tarefas executadas**|**Descrição**|
|Validar<br>os<br>indicadores<br>de<br>qualidade do software gerado<br>na sprint|Teste do software implementado.|
|**Observação**||
|A validação é realizada na release||
**Atividade:** Testar itens 
Testar a entrega da Sprint. 
**Entrega:** Sprint testada 
Página **13** de **22** 
|**Responsável**|**Participante**|
|---|---|
|Analista de Testes e Qualidade|Analista de Testes e Qualidade/Analista TI/PO|
|**Tarefas executadas**|**Descrição**|
|Testar todos os itens da Sprint|Itens da Sprint testados|
|**Observação**||
|||
**Atividade:** Homologar itens 
Validar os itens da Sprint entregues 
**Entrega:** incremento aprovado **Responsável Participante** Dono do produto Cliente/ Dono do produto **Tarefas executadas Descrição** Validar o software como um todo a partir da implementação Validação do produto de cada incremento de software **Observação** 
## **Atividade:** Entregar artefatos 
Entregar artefatos 
|**Atividade:**Entregar artefatos|**Atividade:**Entregar artefatos|
|---|---|
|Entregar artefatos||
|**Entrega:**artefatos||
|**Responsável**|**Participante**|
|Scrum Master|Scrum Master/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
|Entregar os artefatos na branch<br>Master|Entrega do produto|
|**Observação**||
|||
Página **14** de **22** 
**Atividade:** Verificar qualidade Master 
Verificar a qualidade de software gerado por meio da consolidação dos itens da sprint validando os indicadores definidos. 
**Entrega:** Qualidade da demanda validada 
**Responsável Participante** Analista de Testes e Qualidade Analista de Testes e Qualidade **Tarefas executadas Descrição** Validar os indicadores de qualidade do software gerado Teste do software implementado. na sprint **Observação** 
A validação é realizada na master 
## **Atividade:** Encerrar Sprint 
Formalizar a finalização da Sprint. 
**Entrega:** Sprint encerrada 
**Responsável Participante** Analista de TI Analista de TI **Tarefas executadas Descrição** Encerrar a sprint informando se a mesma foi aprovada Sprint finalizada totalmente ou parcialmente **Observação** 
## **7.1.4. Entregar incremento (vide fluxo GETI-GST-FP-0011_Entregar incremento_rev0.0)** 
## **Atividade:** Planejar a implantação da Sprint 
Realizar o planejamento da implantação do incremento de software 
**Entrega:** Plano para implantar incremento em produção **Responsável Participante** 
Página **15** de **22** 
|Dono do produto|Dono do produto /Analista TI|
|---|---|
|**Tarefas executadas**|**Descrição**|
|Planejar<br>a<br>implantação<br>do<br>incremento<br>de<br>software<br>em<br>produção|Implantação do incremento de software realizada|
|**Observação**||
|||
**Atividade:** Implantar a Sprint 
Realizar a implantação do incremento de software no ambiente de produção 
|**Atividade:**Implantar a Sprint|**Atividade:**Implantar a Sprint|
|---|---|
|Realizar a implantação do incremento de software no ambiente de produção||
|**Entrega:**incremento implantado||
|**Responsável**|**Participante**|
|Analista TI|Analista TI|
|**Tarefas executadas**|**Descrição**|
|Implantar incremento de software|Incremento de software implantado no ambiente de<br>produção|
|**Observação**||
|||
**Atividade:** Atualizar o backlog do produto 
Realizar a atualização do backlog do produto após a entrega do incremento de software 
|**Atividade:**Atualizar o backlog do produto|**Atividade:**Atualizar o backlog do produto|
|---|---|
|Realizar a atualização do backlog do produto após a entrega do incremento de software||
|**Entrega:**backlog do produto atualizado||
|**Responsável**|**Participante**|
|PO|Cliente/PO|
|**Tarefas executadas**|**Descrição**|
|Atualizar backlog do produto|Backlog<br>do<br>produto<br>atualizado<br>com<br>as<br>novas<br>funcionalidades implementadas no incremento de<br>software|
|**Observação**||
|||
Página **16** de **22** 
**Atividade:** Realizar a retrospectiva da sprint 
Realizar a retrospectiva da sprint para avaliar os pontos positivos e negativos 
|**Atividade:**Realizar a retrospectiva da sprint|**Atividade:**Realizar a retrospectiva da sprint|
|---|---|
|Realizar a retrospectiva da sprint para avaliar os pontos positivos e negativos||
|**Entrega:**Plano de melhoria contínua||
|**Responsável**|**Participante**|
|Scrum Master|Cliente/Desenvolvedor/ Analista TI/PO/Scrum Master|
|**Tarefas executadas**|**Descrição**|
|Avaliar a última Sprint e criar um<br>plano de açãopara apróxima.|Evento que fecha a Sprint|
|**Observação**||
|||
## **8. Entradas do processo** 
Itens de Backlog do Produto definidos na saída do processo “GETI–GST–PP– 0001 – Detalhamento do Backlog do Produto (ou Histórias do Usuário) Ver. 0.0”. 
## **9. Saídas do processo** 
Artefatos produzidos durante o desenvolvimento e manutenção dos sistemas, conforme item 11 deste manual. 
## **10. Fluxo do processo** 
GETI-GST-FP-0008_Planejar a sprint 
GETI-GST-FP-0009_Executar a sprint 
GETI-GST-FP-0010_ Revisar a sprint 
GETI-GST-FP-0011_Entregar incremento 
## **11. Indicadores do processo** 
Os seguintes indicadores são previstos neste documento: 
- a) Indicador de Aceitação da Sprint/Entrega (IAS); 
- b) Indicador de Produtividade Ágil (IPA); 
- c) Indicador de qualidade de código (IQC); 
- d) Indicador de Conformidades em Homologação (ICH); 
- e) Leadtime. 
Página **17** de **22** 
## **11.1. Indicador de Aceitação da Sprint/Entrega** 
Verificar se as demandas planejadas nas sprints foram executadas no timebox e com qualidade, conforme tabela a seguir: 
**Tabela 1: IAS** 
|**Tabela 1: IAS**||
|---|---|
|Finalidade|Garantir a qualidade na entrega das**sprints**.|
|Meta a cumprir|IAS igual ou superior a 75%|
|Forma de<br>acompanhamento|São apuradas a quantidade total de**sprints**entregues no período, a<br>quantidade de**sprints**que foram aceitas integralmente e a<br>quantidade de**sprints**aceitas parcialmente.|
|Periodicidade|Mensal|
|Mecanismo de cálculo (%)|É feita uma relação de proporção entre a quantidade de**sprints**<br>aceitas<br>integralmente e parcialmente junto ao total, chegando a um valor<br>percentual:<br>**IAS = (Qi + Qp/3) x 100**<br>**______________**<br>**Qt**<br>Onde:<br>IAS = Indicador de Aceitação da**Sprint**/Entrega;<br>Qi = Quantidade de**sprints**aceitas integralmente;<br>Qp = Quantidade de**sprints**aceitas parcialmente;<br>Qt=Quantidade total de**sprints**enviadas para aceite.|
|Observações|O peso das**sprints**aceitas integralmente deve ser maior que o das<br>aceitas parcialmente. Nessa fórmula específica, o peso das**sprints**<br>aceitas integralmente é três vezes maior que o das aceitas<br>parcialmente.<br>Para efeitos desse indicador, não são contabilizadas**sprints**<br>rejeitadas, pois não atendem aos critérios mínimos de aceitação<br>previamente estabelecidos.|
## **11.2. Indicador de Produtividade Ágil** 
Monitorar o alcance das metas de produtividade. 
**Tabela 2: IPA** 
|Finalidade|Garantir a produtividade das equipes ágeis, em termos do alcance de<br>metas aferidas por meio de métricas de**software**, observando os<br>critérios de qualidade e de aceitação definidos, bem como<br>mensuração em termo de produto ou resultado entregue.|
|---|---|
|Meta a cumprir|IPA igual ou superior a 90%|
|Forma de<br>acompanhamento|Afere-se a produtividade realizada no período, considerando as metas<br>de produtividade em linhas de código|
|Periodicidade|Mensal|
|Mecanismo de cálculo (%)|**IPA = 100 * ( Pr / Pp)**<br>Onde:<br>IPA = Indicador de Produtividade Ágil;<br>Pr = Produtividade realizada no período para os perfis profissionais<br>alocados, em função da métrica de**software**previamente<br>estabelecida;<br>Pp = Produtividade prevista no período para os perfis profissionais<br>alocados, em função da métrica de**software**previamente|
Página **18** de **22** 
estabelecida. 
Para calcular a Produtividade realizada no período (Pr) em linhas de código deve-se considerar a quantidade de linhas de código alteradas no software no período de aferição, com apoio de ferramenta. É considerada linha de código alterada uma nova linha inserida ou uma linha existente que foi modificada. Não serão contabilizadas linhas removidas, linhas em branco, linhas de comentários e alterações com intuito de somente aumentar artificialmente o número de linhas. Observações 
## **11.3. Indicador de Qualidade de código** 
Assegurar a qualidade técnica das entregas. Utilizando, como por exemplo, SonarQube, é realizada uma análise estática do código para detectar bugs, duplicidade de código e vulnerabilidades de segurança, com exceção da linguagem DELPHI, conforme parâmetros definidos na tabela 3. 
**Tabela 3: Parâmetros de qualidade para primeira versão do código fonte** 
|<br>**Grupo**|<br>**Indicador**|<br>**Unidade**|**Meta**|
|---|---|---|---|
|Projeto|Complexity / file ou equivalente|média total|<=10|
||Complexity / class ou equivalente|média total|<=10|
||Complexity /function ou<br>quivalente|média total|<= 3|
||Duplications ou equivalente|%|<=4%|
||Security<br>Issue<br>Tags<br>ou<br>equivalente|unidades|=0|
||Technical<br>Debt<br>ratio<br>ou<br>equivalente|%|<=<br>2,5%|
||SQALE RATING ou equivalente|Nota|=A|
|Violações de código (possíveis<br>bugs, estilo de codificação, más<br>práticas de codificação)|Critical Issues ou equivalente|unidades|=0|
||Blocker Issues ou equivalente|unidades|=0|
|Indicadores relacionados a<br>testes|Unit Tests Coverage - camada<br>negócio / Impl ou equivalente|%|>=70%|
||Unit Test Success ou equivalente|%|=100%|
||Skipped Tests ou equivalente|unidades|=0|
O Indicador de qualidade de código (IQC) será calculado dividindo a Quantidade de requisitos de qualidade de código atendidos (ΣQrc) pela Quantidade total de requisitos de qualidade de código avaliados (ΣQtr), conforme descrito na tabela 4: 
**Tabela 4: IQC** 
|**Tabela 4: IQC**||
|---|---|
|Finalidade|Assegurar a qualidade do código em projetos de desenvolvimento,<br>diminuir a ocorrência de defeitos e medir o nível de adequação<br>do código fonte a características de qualidade determinadas pela<br>contratante|
|Meta a cumprir|>=90%|
|Forma de<br>acompanhamento|A aferição será realizada por meio de ferramentas automatizadas|
|Periodicidade|Por período previamente definido, seja em termos de**sprints**|
Página **19** de **22** 
||executadas ou releases homologadas.|
|---|---|
|Mecanismo de cálculo (%)|**IQC = 100 * (Qrc / Qtr)**<br>Onde:<br>IQC = Indicador de qualidade de código;<br>Qrc = Somatório da Quantidade de requisitos de qualidade de código<br>atendidos;<br>Qtr = Somatório da Quantidade total de requisitos de qualidade de<br>código avaliados.|
|Observações|A qualidade de código faz parte da visão dos desenvolvedores,<br>engenheiros, arquitetos e, em alguns casos, analistas e gerentes.<br>Indicadores da qualidade de código incluem: complexidade do código,<br>duplicações de código, tamanho do código, entre outros.<br>Vale ressaltar que a menor qualidade no código está relacionada a<br>uma ocorrência maior de defeitos nas aplicações, que afetarão<br>diretamente a produtividade da equipe de desenvolvimento. Esse<br>indicador será utilizado desde o início do projeto, fazendo com que o<br>código seja desenvolvido dentro de padrões aceitáveis de qualidade.<br>Problemas de qualidade no código-fonte do**software**pré-existentes<br>devem ser desconsiderados na aferição do IQC.|
## **11.4.** Indicador de Conformidades em Homologação 
Assegurar o cumprimento dos prazos estabelecidos. 
**Tabela 5: ICH** 
|Finalidade|Apura a quantidade de conformidades registradas pelo usuário<br>durante a homologação do produto.|
|---|---|
|Meta a cumprir|ICH igual ou superior a 90%.|
|Forma de<br>acompanhamento|É apurada a quantidade de itens da sprint entregues em conformidade<br>aos requisitos mínimos de qualidade de código e atendimento aos<br>requisitos funcionais no período de referência.|
|Periodicidade|Mensal|
|Mecanismo de cálculo (%)|**ICH = ((Qp - Qpe) / Qp) * 100**<br>Onde:<br>ICH = Indicador de Conformidades em Homologação.<br>Qpe = Quantidade de itens da sprint entregues com erros de<br>codificação e/ou não implementação adequada dos requisitos<br>funcionais que foram identificados<br>no ambiente de homologação.<br>Qp=Quantidade itens da sprint previstos.|
|Observações:|Não serão considerados erros identificados e reportados previamente<br>pela equipe de testes e que não foram ajustados pela equipe<br>responsável pelo desenvolvimento.|
## **11.5. Leadtime** 
Como métrica para controlar quanto tempo uma tarefa leva para ser completada é adotado o Lead Time que é calculado com o número de dias entre o início e o fim de uma entrega. Esse intervalo é calculado conforme a demanda alcança diferentes status no processo de desenvolvimento: 
Página **20** de **22** 
## • **Tarefas do tipo Sprint:** 
INICIO_LEADTIME – Quando a demanda atinge a situação “Associar itens de backlog” 
FIM_LEADTIME – Quando a demanda atinge a situação “Entregar itens da Sprint” 
Com o monitoramento do Lead Time é possível detectar pontos de lentidão, antecipando oportunidades de melhorias por meio de ações específicas e direcionadas. 
## **12. Governança** 
Não aplicável. 
## **13. Dono do documento** 
Rhodrigo da Venda Santana, Chefe de Divisão, PR/DIRAD/CGTI/DIPRO 
## **14. Outro(s) elaborador(es) do documento** 
Vladimir Guimarães de Carvalho, colaborador, PR/DIRAD/CGTI 
## **15. Aprovador(es) do documento** 
Marcus Vinicius da Motta Vieira, Coordenador Geral, PR/DIRAD/CGTI Pedro Calisto Luppi Monteiro Junior, Coordenador de Sistemas, PR/DIRAD/CGTI/COSIS 
## **16. Bibliografia** 
IN SGD/ME nº 94, de 2022. 
EPL - Empresa de Planejamento e Logística. **Processo de Desenvolvimento de Software da Empresa de Planejamento e Logística PDS – EPL Versão 2.0** . Disponível em: https://www.epl.gov.br/pds. Acesso em 26 de jul. 2021. 
FINEP - Financiadora de Estudos e Projetos. **Metodologia de desenvolvimento de software da FINEP – MDS FINEP Versão 2.1** . 2017. Disponível em: http://www.finep.gov.br/images/licitacoes/2017/Consulta012017/I_MDS.pdf. Acesso em 26 de jul. 2021. 
PJERJ - Poder Judiciário do Estado do Rio de Janeiro. **Metodologia de desenvolvimento de sistemas - Versão 2.0** . Disponível em: http://www.tjrj.jus.br/documents/10136/6364473/anexo-a.pdf. Acesso em 26 de jul. 2021. 
SCRUM – Conhecimento de Scrum (Guia SBOK) – 3rd Edição. Disponível em: https://portaldaobmep.impa.br/uploads/material_teorico/d9gycv8klfcwc.pdf. 2017. 
SUSEP – Superintendência de Seguros Privados. **Metodologia de Gestão e Desenvolvimento de Software** . 2011. Disponível em: http://www.susep.gov.br/setoressusep/noticias/download/tisusep/MGDS_SUSEP_v1.0.pdf. Acesso em 26 de jul. 2021. 
TRT7 - Tribunal Regional do Trabalho da 7ª Região. PDS-TRT7 **Processo de Desenvolvimento de Software.** 2016. Disponível em: 
Página **21** de **22** 
https://www.trt7.jus.br/files/institucional/governanca_ti/processos/PDS-TRT7-rev-1_0-semAto.pdf. Acesso em 26 de jul. 2021. 
## **17. Histórico das alterações** 
|**Data**|**Nº revisão**|**Item**|**Descrição**|
|---|---|---|---|
|||||
|||Todo||
|01/08/2024|0.0||Emissão inicial|
|||documento||
|||||
|||||
## **18. Anexos** 
Não aplicável. 
Página **22** de **22** 
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