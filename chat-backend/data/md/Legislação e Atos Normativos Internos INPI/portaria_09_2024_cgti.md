** **
## **MINISTÉRIO DO DESENVOLVIMENTO, INDÚSTRIA, COMÉRCIO E SERVIÇOS INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** 
## PORTARIA /INPI / Nº 9, DE 07 DE OUTUBRO DE 2024 
Publica a Metodologia de Desenvolvimento de Produtos de Dados 
## **O COORDENADOR-GERAL DE TECNOLOGIA DA INFORMAÇÃO DO INSTITUTO NACIONAL** 
**DA PROPRIEDADE INDUSTRIAL** , no uso das atribuições que lhe foram conferidas pelo Decreto nº 8.854, de 22 de setembro de 2016, e pela Portaria INPI PR nº 09, publicada em 13 de março de 2024, e tendo em vista o conteúdo do processo SEI nº 52402.009888/2024-01, 
## **RESOLVE:** 
Art. 1º Publicar, na forma do anexo a esta Portaria, conforme definido no item 7.4 do Manual do Sistema de Padronização de Documentos GEQU-GGD-MN-0001, rev. 0.0, a Metodologia de Desenvolvimento de Produtos de Dados (1095224) e seus anexos GETI-GGD-FP-0001 (1092936); GETIGGD-FP-0002 (1092937); GETI-GGD-FP-0003 (1092939); e GETI-GGD-FP-0004 (1092941). 
Art. 2º Esta Portaria entra em vigor na data de sua publicação. 
**Arthur Henrique Goes Samary** Coordenador-Geral de Tecnologia da Informação Subs�tuto 
** **
Documento assinado eletronicamente por **ARTHUR HENRIQUE GOES SAMARY** , **Coordenador(a) Geral Subs�tuto(a)** , em 08/10/2024, às 17:19, conforme horário oficial de Brasília, com fundamento no art. 6º, § 1º, do Decreto nº 8.539, de 8 de outubro de 2015. 
** **
A auten�cidade deste documento pode ser conferida no site h�p://sei.inpi.gov.br/sei/controlador_externo.php? acao=documento_conferir&id_orgao_acesso_externo=0, informando o código verificador **1095226** e o código CRC **BB878541** . 
** **
**Referência:** Processo nº 52402.011527/2024-16 
SEI nº 1095226 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>MANUAL|**Código **|GETI – GGD – MN – 0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|02/10/2024|
||**METODOLOGIA DE DESENVOLVIMENTO DE**<br>**PRODUTOS DE DADOS**|**Processo**|Gestão e Governança de<br>Dados (Nível 2)|
## **Sumário** 
|**1. Introdução ...................................................................................................................................... 2**|
|---|
|**2. Objetivo .......................................................................................................................................... 2**|
|**3. Abrangência ................................................................................................................................... 3**|
|**4. Documentos complementares ...................................................................................................... 3**|
|**5. Glossário ........................................................................................................................................ 3**|
|**6. Fundamentos Gerais ..................................................................................................................... 4**|
|**6.1. Produtos de dados ...................................................................................................................... 4**|
|**6.1.1. Serviços de desenvolvimento de produtos de dados ........................................................... 4**|
|**6.2. Resultados esperados ................................................................................................................ 5**|
|**6.3. Princípios Gerais......................................................................................................................... 5**|
|**6.4. Práticas do método Scrum ......................................................................................................... 6**|
|**6.5. Padrões e Requisitos .................................................................................................................. 6**|
|**6.6. Papéis e Responsabilidades ...................................................................................................... 8**|
|**7. Descrição dos processos ou atividades .................................................................................... 10**|
|**7.1. Processo de desenvolvimento e manutenção de Produtos de Dados .................................. 10**|
|**7.1.1. Planejar a sprint (vide fluxo GETI-GGD-FP-0001_Planejar a sprint_rev0.0) ....................... 10**|
|**7.1.2. Executar a sprint (vide fluxo GETI- GGD -FP-0002_Executar a sprint_rev0.0) .................. 12**|
|**7.1.3. Revisar a sprint (vide fluxo GETI-GGD-FP-0003_Revisar_sprint_rev0.0) ........................... 13**|
|**7.1.4. Entregar incremento ou produto de dados (vide fluxo GETI-GGD-FP-0004_Entregar**|
|**incremento_ou_produto_de_dados_rev0.0) ....................................................................... 15**|
|**8. Entradas do processo ................................................................................................................. 17**|
|**9. Saídas do processo / resultados esperados .............................................................................. 17**|
|**10. Fluxo do processo ..................................................................................................................... 17**|
|**11. Indicadores do processo ........................................................................................................... 17**|
|**11.1. Indicador de Aceitação da Sprint/Entrega ............................................................................. 17**<br>**11.2. Indicador de Produtividade Ágil ............................................................................................ 18**|
|**11.3. Indicador de Qualidade de código ......................................................................................... 18**|
|**11.4. Indicador de Conformidades em Homologação ................................................................... 19**|
|**11.5. Leadtime .................................................................................................................................. 20**|
|**12.**<br>**Governança ........................................................................................................................... 20**|
|**13.**<br>**Dono do documento ............................................................................................................. 20**|
|**14.**<br>**Elaborador(es) do documento ............................................................................................. 20**|
|**15.**<br>**Aprovador(es) do documento .............................................................................................. 20**|
|**16.**<br>**Bibliografia ............................................................................................................................ 21**|
|**17.**<br>**Histórico das alterações ...................................................................................................... 21**<br>**18.**<br>**Anexo - CATÁLOGO DE SERVIÇOS DE PRODUTOS DE DADOS ..................................... 21**|
Página **1** de **23** 
## **1. Introdução** 
**Produtos de dados** são um tipo de produto de tecnologia que consome e analisa dados para organizar ou gerar novos dados em forma de informações, insights e decisões que ajudam alguém (o usuário) a atingir seu objetivo final, ou seja, **produtos de dados** são produtos gerados a partir da coleta, processamento e análise de dados. (https://www.linkedin.com/pulse/data-product-vs-tech-guimaferreira/) 
Os **produtos de dados** podem ser classificados de acordo com o tipo de resultado gerado pelo produto e sua e sua forma de interação com os usuários. Em relação ao tipo de resultado eles podem ser categorizados em fornecimento de dados brutos, dados derivados, algoritmos (por ex. modelo de aprendizado de máquina), suporte a decisão (ex. IA) ou decisões automatizadas. Em relação a forma de interação podem ser entregues APIs, dashboards, visualizações e relatórios assim como elementos web. 
A tabela a seguir mostra a relação desses tipos de resultado e sua forma de interação com os usuários: 
||**Dados**<br>**Brutos**|**Dados**<br>**Derivados**|**Algoritmos**|**Suporte à**<br>**Decisões**|**Decisões**<br>**Automatizadas**|
|---|---|---|---|---|---|
|**API**|X|X|X|X|X|
|**Dashboards,**<br>**Visualizações e Relatórios**|X|X|X|X|X|
|**Elementos Web**|X|X|X|X|X|
Mover-se diagonalmente da parte superior esquerda (Dados brutos-API) para a parte inferior direita (tomada de decisão automatizada - elementos web) é passar de produtos técnicos, orientados à engenharia de dados, para produtos mais típicos de software. 
Nesse sentido, as atividades de desenvolvimento de produtos de dados, incluindo data warehouse, big data, business intelligence e administração e governança de dados, entre outros, foram incluídas no modelo de contratação de serviços de desenvolvimento, manutenção e sustentação de software que foi instituído pela Portaria SGD/MGI nº 750, de 20 de março de 2023. O uso deste modelo é obrigatório para os órgãos e entidades integrantes do Sistema de Administração dos Recursos de Tecnologia da Informação - SISP do Poder Executivo Federal. 
Para ajustar a sua metodologia ao novo modelo, o INPI publicou a nova Metodologia de Desenvolvimento de Software – MDS (GETI – GST – MN – 0002), na qual o desenvolvimento de produtos de dados se enquadra. No entanto, apesar de estar incluído no MDS, o INPI apresenta esta metodologia específica para o desenvolvimento de produtos de dados, de forma a ajustar o MDS para que contemple as características relativas ao desenvolvimento de produtos de dados. 
Portanto, este manual é derivado da metodologia aplicável aos projetos de desenvolvimento e manutenção de software no INPI e contempla atividades, fluxos, responsáveis e artefatos necessários ao ciclo de vida do projeto, com modificações específicas para abarcar o desenvolvimento de produtos de dados. 
## **2. Objetivo** 
Definir um padrão para a gestão e o desenvolvimento de produtos de dados no INPI, por meio de uma abordagem iterativa e incremental, adotando práticas ágeis, com o intuito de focar na qualidade da entrega dos produtos de dados com valor agregado para os clientes. 
Página **2** de **23** 
## **3. Abrangência** 
Este documento abrange todas as áreas que atuam diretamente no processo de desenvolvimento e manutenção de produtos de dados no âmbito do INPI, devendo ser amplamente divulgado a todos os servidores, colaboradores e empresas prestadoras de serviços dessas áreas. 
Igualmente, todas as áreas demandantes de soluções de tecnologia de informação precisam ter acesso ao documento e conhecimento de sua amplitude, a fim de que estejam cientes das etapas fundamentais para a implementação de um produto de dados que atenda às necessidades pretendidas. 
## **4. Documentos complementares** 
GETI – GST – IT – 0001 – Abertura de demandas no Sistema Redmine. 
GETI – GST – PP – 0001 – Detalhamento do Backlog do Produto (ou Histórias do Usuário) Ver. 0.0. GETI – GST – MN – 0002 – Metodologia de Desenvolvimento de Software 
## **5. Glossário** 
Artefatos – Subprodutos produzidos durante o desenvolvimento de software ou do produto de dados. Ajudam a descrever a função, arquitetura e o design do produto de dados ou estão relacionados com o próprio processo de desenvolvimento. 
Backlog da Sprint – conjunto de itens do Backlog do Produto selecionados para a Sprint 
Backlog do Produto – representa tudo que é necessário para desenvolver e lançar um produto de valor agregado ao negócio. É uma lista priorizada de todos os requisitos (funcionais e não funcionais), funções, tecnologias, melhorias e correções de defeitos que constituem as mudanças que serão efetuadas no produto para versões futuras. 
CGTI – Coordenação Geral de Tecnologia da Informação. 
GETI – Gestão de Tecnologia da Informação e Comunicações. 
História de usuário - é uma explicação informal e geral sobre um recurso de software ou de um produto de dados, escrita a partir da perspectiva do usuário final ou cliente. 
Incremento de produto – versão de um produto que pode ser liberada no final de um período (timebox). 
INPI – Instituto Nacional da Propriedade Industrial. 
Metodologias ágeis – são um conjunto de práticas que visam a entrega rápida e de alta qualidade do produto ou serviço e que promovem um processo de gerenciamento de projetos que incentiva a inspeção e adaptação frequente, beneficiando a eficiência e efetividade dos gestores públicos no controle da prestação dos serviços de TI, haja vista que o foco passa a ser realmente nas atividades que entregam valor para as áreas de negócios. 
PDTIC – Plano Diretor de Tecnologia da Informação e Comunicação. 
Produto de dados - Produtos gerados a partir da coleta, processamento e análise de dados, podem incluir data warehouse, big data, relatórios, visualizações, dashboards, modelos preditivos, métricas ou insights entre outros produtos derivados de dados. 
Página **3** de **23** 
Release – distribuição/liberação de um incremento de produto para um cliente ou usuários. A quantidade de sprints por release deve ser definida previamente à execução dos serviços. 
Timebox - Determina um limite de tempo para a conclusão de uma Sprint. 
Tipo de Tarefa: Sprint – Nesta categoria são classificadas as tarefas que representam as sprints definidas para implementar as histórias de usuário. 
Tipo de Tarefa: Item da sprint – Nesta categoria são classificadas as tarefas que representam os itens de backlog da sprint. 
Sprint – Corresponde a um grupo de atividades para transformar os itens de backlog em um incremento de software ou de produto de dados. 
## **6. Fundamentos Gerais** 
A metodologia está alicerçada em 4 pilares: 
1. Priorização balanceada: considera o valor agregado, visando promover práticas que permitam aos participantes do projeto desenvolver uma solução que maximize os benefícios e seja compatível com as restrições existentes. 
2. Colaboração: alinhamento de interesses e compartilhamento do entendimento, visando promover um ambiente de equipe saudável que promova a colaboração e a compreensão do projeto. 
3. Focar na arquitetura: concentração na arquitetura desde o início para minimizar riscos e organizar o desenvolvimento, além de promover práticas que minimizem os riscos na fase de desenvolvimento. 
4. Evolução contínua e obtenção de feedback: promove práticas que permitem a equipe obter feedback de maneira contínua e o mais cedo possível, permitindo agregar valor a cada desenvolvimento e diminuir o risco do projeto conforme a execução. 
** **
## **Produtos de dados** 
O projeto de desenvolvimento de produtos de dados é um serviço disponibilizado pela área de Tecnologia da Informação para atender às necessidades do Instituto. Como principais serviços nos projetos de desenvolvimento de produtos de dados temos: elaboração de ETLs, analytics (Dashboards) e dados abertos. 
## **6.1.1. Serviços de desenvolvimento de produtos de dados** 
As atividades relacionadas a prestação de serviços de desenvolvimento de produtos de dados têm como objetivo oferecer suporte especializado, construção e aprimoramento de projetos de dados para assegurar o tratamento adequado ao longo de todo o ciclo de vida dos dados, desde sua criação até sua utilização avançada. Isso inclui foco na administração de dados, metadados, soluções de BI, Big Data e Ciência de Dados, bem como na governança e gestão de dados. Esses serviços abrangem desde a definição de requisitos e modelagem até o desenvolvimento de soluções analíticas, incluindo Inteligência Artificial, tanto em ambientes tradicionais quanto na nuvem, garantindo qualidade e segurança contínuas, incluindo no mínimo as seguintes atividades, além de outras: 
Página **4** de **23** 
1. definição de requisitos de dados. 
2. modelagem de dados. 
3. criação e manutenção de metadados. 
4. integrações de dados. 
5. apoio à operação de dados. 
6. gerenciamento de dados mestres e de referência. 
7. melhoria da qualidade de dados. 
8. implementação de medidas de segurança de dados. 
9. desenvolvimento de arquiteturas Big Data e Data Lake. 
10. implementação de Data Warehouse. 
11. desenvolvimento de soluções de Business Intelligence (BI). 
12. criação de modelos preditivos e prescritivos. 
13. aplicação de técnicas de Inteligência Artificial. 
14. sustentação contínua das soluções de dados. 
15. implementação de estruturas Big Data e Data Lake. 
16. desenvolvimento de soluções analíticas. 
17. sustentação e evolução das soluções implementadas 
** **
## **Resultados esperados** 
Com a implementação desta Metodologia de Desenvolvimento de Produtos de Dados são esperados os seguintes benefícios: 
- fornecer novos produtos de dados, relacionados ao escopo de atuação do Instituto; 
- • manter e aprimorar a disponibilidade, segurança, acessibilidade e usabilidade dos dados; 
- aprimorar e evoluir os sistemas de informação e dados que apoiam as políticas públicas de governo; 
- permitir que as decisões no INPI possam ser orientadas a dados; 
- assegurar a troca eficiente de informações entre os diferentes processos de negócio; 
- assegurar a segurança e privacidade das informações mantidas e processadas pelos sistemas e produtos de dados; 
- manter a resiliência e eficiência dos sistemas de informação e produtos de dados do Instituto; 
- • demonstrar agilidade no atendimento das demandas, mesmo que haja flutuações sazonais; 
## **Princípios Gerais** 
** **
Os princípios elencados na enumeração abaixo devem ser utilizados: 
## **I. PD1 - Princípio de Ferramentas e Instrumentos** 
- A área de gestão de dados definirá as ferramentas e instrumentos padrões da metodologia de desenvolvimento de produtos de dados, que deverão ser utilizados por todos os agentes. 
## **II. PD2 - Princípio de Viabilidade Técnica da Demanda** 
- O atendimento da demanda somente poderá ser executado após a análise da viabilidade técnica da solicitação, sendo esta onerosa para o INPI ou não. 
## **III. PD3 - Princípio de Prioridades** 
- As demandas deverão seguir a determinação de prioridades estabelecida pelo Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC vigente). 
## **IV. PD4 – Princípio da Simplicidade** 
Elimine tudo aquilo que for desnecessário, pois ele onera e sobrecarrega o processo, as pessoas e o produto. 
Página **5** de **23** 
- **V. PD5 – Princípio do Foco** 
Estabeleça um foco nos itens de solução, nas necessidades e nos problemas, para que a energia de trabalho se concentre apenas nos objetivos e acordos firmados. 
## **Práticas do método Scrum** 
** **
Para promover a entrega de projetos de software ou de produto de dados que cumpram as metas de qualidade, prazo e custos, os métodos ágeis preconizam uma série de valores e princípios distintos do desenvolvimento tradicional. O entendimento destes valores e princípios, bem como suas práticas, são fatores de sucesso. Todos os envolvidos no projeto devem conhecer princípios e práticas dos métodos ágeis. 
O processo de desenvolvimento Ágil adotado baseia-se no método Scrum, sendo esta uma metodologia que propõe que um projeto seja dividido em diversos (pequenos) ciclos de atividades, com reuniões frequentes para que a equipe possa alinhar o que vem fazendo e pensar formas de melhorar o processo com agilidade. 
Resumindo, o processo Scrum acontece em três etapas: 
- O dono do produto analisa as necessidades e faz o backlog do produto; 
- As equipes scrum trabalham em uma entrega de valor durante um período denominado sprint; 
- • As equipes scrum e as partes interessadas inspecionam e ajustam os resultados para o próximo sprint. 
E então o processo é repetido, conforme Figura1. 
## Figura 1 - Fluxo do Scrum para um Sprint 
** **
Institute Project Management (2022). 
** **
## **Padrões e Requisitos** 
Deve-se observar, no que couber, os seguintes padrões: 
- ABNT NBR 11515:2007 - Guia de práticas para segurança física relativas ao armazenamento de dados; 
- ABNT NBR 16167:2013 - Diretrizes para classificação, rotulação e tratamento da informação; 
- ABNT NBR ISO 22301:2013 - Sistemas de gestão de continuidade de negócios; 
- ABNT NBR ISO 22313:2015 - Sistemas de gestão de continuidade de negócios; 
- ABNT NBR ISO 23081-1:2019 - Metadados para documentos de arquivo; 
Página **6** de **23** 
- ABNT NBR ISO 27031:2015 - Diretrizes para a prontidão para a continuidade dos negócios da tecnologia da informação e comunicação; 
- ABNT NBR ISO/IEC 25030:2008 - Engenharia de software - Requisitos e Avaliação da Qualidade de Produto de Software (SQuaRE) - Requisitos de qualidade; 
- ABNT NBR ISO/IEC 27002:2013 - Código de prática para controles de segurança da informação; 
- ABNT NBR ISO/IEC 27014:2013 - Governança de segurança da informação; 
- ABNT NBR ISO/IEC 27017:2016 - Código de prática para controles de segurança da informação com base; 
- ABNT NBR ISO/IEC 27037:2012 - Diretrizes para identificação, coleta, aquisição e preservação de evidência digital; 
- ABNT NBR ISO/IEC/IEEE 12207:2021 - Engenharia de sistemas e software - Processos de ciclo de vida de software; 
- Abordagem TDD ( _Test Driven Development_ ); 
- Arquitetura Técnica Referencial para Abertura de Dados (https://www.gov.br/inpi/pt-br/acessoa-informacao/dados- 
 - abertos/arquivos/documentos/diversos/ArquiteturaTcnicaReferencialdeAberturadeDados.pdf). 
- Decreto 8777/2016 instituidor da Política de Dados Abertos do Poder Executivo Federal 
- • Decreto nº 10.046, de 09 de outubro de 2019 que dispõe sobre a governança no compartilhamento de dados no âmbito da administração pública federal e institui o Cadastro Base do Cidadão e o Comitê Central de Governança de Dados; 
- Guia de Abertura de Dados (http://wiki.gtinda.ibge.gov.br/Produto-GT1-Guia-de-Abertura-deDados.ashx) 
- Guia de Gerenciamento de Vulnerabilidades e Modelo de Política de Gerenciamento de Vulnerabilidades - SGD/ME, disponível em https://www.gov.br/governodigital/pt-br/segurancae-protecao-de-dados/ppsi; 
- Guia de Requisitos Mínimos de Segurança e Privacidade para APIs - SGD/ME, disponível em https://www.gov.br/governodigital/pt-br/seguranca-e-protecao-de-dados/ppsi; 
- Guia de Requisitos Mínimos de Segurança e Privacidade para Aplicativos Móveis - SGD/ME, 
- disponível em https://www.gov.br/governodigital/pt-br/seguranca-e-protecaode-dados/ppsi; 
- Guia de Segurança em Aplicações Web - SGD/ME, disponível em https://www.gov.br/governodigital/pt-br/seguranca-e-protecao-de-dados/ppsi; 
- Instrução Normativa 04/2012 - Institui a Infraestrutura Nacional de Dados Abertos 
- Lei de acesso a informação - Lei 12.527/2011 - Regula o Acesso a Informações 
- Lei de Governo Digital - Lei nº 14.129, de 29 de março de 2021 , prevê A Estratégia Nacional de Governo Digital (ENGD) 
- Lei Geral de Proteção de Dados - LGPD - Lei 13.709, de 2018; 
- Padrão Digital de Governo ( _Design System_ ) e suas atualizações com relação ao padrão visual das aplicações, disponível no endereço: https://www.gov.br/ds/home ; 
- Padrões de projeto ( _Design Patterns_ ) ou padrões arquiteturais consolidados no mercado aderentes às necessidades da aplicação, além de métodos de codificação limpa (Clean Code); 
- PORTARIA/INPI/DIREX Nº 004, DE 23 DE JULHO DE 2024, Institui o Subcomitê de Infraestrutura de Dados do INPI e regulamenta o seu funcionamento. Princípios de _Security by Design, Privacy by Design e Shift-left testing_ , de forma a minimizar os riscos de privacidade e segurança em tempo de concepção dos projetos; 
Página **7** de **23** 
## **Papéis e Responsabilidades** 
** **
**Tabela 1: Descrição de papéis e responsabilidades** 
|<br>**Papel**|<br>**Descrição**|<br>**Responsabilidade**|
|---|---|---|
|**Cliente (INPI)**|Servidor do INPI|•<br>Descrever o projeto de acordo com<br>as<br>necessidades<br>e<br>resultados<br>esperados;<br>•<br>Abrir demandas de manutenção;<br>•<br>Homologar implementação;|
|**Analista TI (INPI)**|Servidor da área<br>de TI|•<br>Compreender<br>necessidades<br>de<br>usuários,<br>motivações<br>e<br>comportamentos,<br>transformando<br>informações em insights e_features_;<br>•<br>Analisar a solicitação de um novo<br>projeto; criar projeto no sistema de<br>controle de demandas do INPI<br>(Redmine);<br>•<br>Validar a escrita das histórias de<br>usuário;<br>priorizar<br>demandas;<br>analisar e detalhar solicitações de<br>novos produtos de dados;<br>•<br>Validar<br>especificações<br>e<br>testar<br>implementação;<br>•<br>Registrar defeitos relacionados às<br>demandas e concluir demandas.|
|**Scrum Master**|Profissional com<br>conhecimento<br>aprofundado<br>em técnicas<br>ágeis.|•<br>Garantir que o_Scrum_seja entendido<br>e aplicado;<br>•<br>Assegurar que todos os eventos do<br>Scrum têm lugar e são positivos,<br>produtivos e mantidos dentro tempo<br>previsto;<br>•<br>Apoiar o Dono do Produto e a<br>organização na adoção de práticas<br>ágeis;<br>•<br>Buscar melhoria contínua do time;<br>•<br>Facilitar<br>a<br>colaboração<br>dos<br>stakeholders conforme solicitado ou<br>necessário;<br>•<br>Acompanhar<br>e<br>apresentar<br>os<br>indicadores do processo;<br>•<br>Remover<br>impedimentos<br>para<br>a<br>equipe de desenvolvimento durante<br>a execução das Sprints.<br>•<br>Criar o Sprint Backlog;|
|**Dono do Produto (Product Owner**<br>**– PO)**|Servidor<br>representante da<br>área demandante<br>de soluções de<br>software,|•<br>Responsável por ordenar o trabalho<br>a ser realizado pelo time, criando,<br>mantendo<br>e<br>priorizando<br>o(s)<br>backlog(s) do(s) produto(s);|
Página **8** de **23** 
|**Papel**|**Descrição**|**Responsabilidade**|
|---|---|---|
||designado por<br>autoridade<br>competente|•<br>Criar e compartilhar a Visão do<br>Produto;<br>•<br>Planejar o Roadmap;<br>•<br>Construir o Backlog do Produto;<br>•<br>Expressar claramente os itens do<br>Backlog do Produto;<br>•<br>Ordenar e priorizar os itens do<br>Backlog do Produto;<br>•<br>Definir quais itens farão parte da<br>sprint;<br>•<br>Garantir<br>que<br>o<br>time<br>de<br>desenvolvimento entenda os itens<br>do Backlog do Produto no nível<br>necessário;<br>•<br>Apoiar no planejamento da Release;<br>•<br>Validar o produto de dados;<br>•<br>Validar a release ao final de cada<br>sprint;<br>•<br>Reportar a Avaliação de Satisfação<br>do Produto.|
|**Desenvolvedores de software**|Desenvolvedores<br>que fazem parte<br>do time ágil|•<br>Construir o(s) produto(s) de dados;|
|**Partes interessadas**<br>**(Stakeholders)**|Profissionais<br>impactados pela<br>solução ou que<br>possuam<br>interesse na<br>entrega da<br>solução|•<br>Opinar<br>e<br>contribuir<br>para<br>o<br>planejamento e tomadas de decisão<br>do negócio ou projeto;<br>•<br>Esclarecer dúvidas;<br>•<br>Se necessário, apoiar o PO na<br>validação da sprint ou release.|
|**Analista de Qualidade (INPI)**|Servidor da área<br>de TI|•<br>Garantir a qualidade dos sistemas<br>durante todo o ciclo do processo de<br>desenvolvimento do produto de<br>dados até a sua implantação,<br>minimizando a ocorrência de erros<br>no ambiente de produção;|
|**Analistas de Teste e Qualidade**|Analistas de<br>Teste e<br>Qualidade que<br>fazem parte do<br>time ágil|•<br>Realizar<br>a<br>revisão de<br>código,<br>realização de testes avançados e<br>revisão<br>da<br>qualidade<br>da<br>documentação produzida;<br>•<br>Aferir os critérios de aceitação da<br>qualidade dos produtos entregues.|
|**Analista de Negócio**|Analistas de<br>negócio que<br>fazem parte do<br>time ágil|•<br>Desenhar<br>solução<br>para<br>novos<br>produtos e serviços, para posterior<br>desdobramento em especificações<br>funcionaispara desenvolvimento de|
Página **9** de **23** 
|**Papel**|**Descrição**|**Responsabilidade**|
|---|---|---|
|||sistemas ou produtos de dados, com<br>base em metodologia ágil.<br>•<br>Compreender<br>necessidades<br>de<br>usuários,<br>motivações<br>e<br>comportamentos,<br>transformando<br>informações em insights e_features_.|
## **7. Descrição dos processos ou atividades** 
** **
## **Processo de desenvolvimento e manutenção de Produtos de Dados** 
## **7.1.1. Planejar a sprint (vide fluxo GETI-GGD-FP-0001_Planejar a sprint_rev0.0)** 
**Atividade:** Criar tarefa do tipo Sprint 
Criar no sistema de abertura de demandas uma tarefa do tipo Sprint. 
|**Atividade:**Criar tarefa do tipo Sprint|**Atividade:**Criar tarefa do tipo Sprint|
|---|---|
|Criar no sistema de abertura de demandas uma tarefa do tipo Sprint.||
|**Entrega:**Tarefa Sprint criada no sistema||
|**Responsável**|**Participante**|
|Analista TI|Analista TI|
|**Tarefas executadas**|**Descrição**|
|No sistema Redmine, criar a<br>demanda do tipo Sprint|Criar demanda do tipo Sprint no sistema Redmine<br>contendo informações básicas da sprint emquestão.|
|**Observação**||
|||
**Atividade:** Associar itens backlog do produto 
Realizar a associação da Sprint com os itens de backlog priorizados pelo dono do produto 
**Entrega:** Itens de backlog associados à Sprint 
|**Atividade:**Associar itens backlog do produto|**Atividade:**Associar itens backlog do produto|
|---|---|
|Realizar a associação da Sprint com os itens de backlog priorizados pelo dono do produto||
|**Entrega:**Itens de backlog associados à Sprint||
|**Responsável**|**Participante**|
|Analista TI|Analista TI, Dono do Produto|
|**Tarefas executadas**|**Descrição**|
|Associar os itens de backlog à<br>sprintque está sendoplanejada|No sistema Redmine, realizar a associação dos itens de<br>backlogà sprintplanejada|
|**Observação**||
|||
Página **10** de **23** 
**Atividade:** Fragmentar os itens do backlog do produto em itens backlog da Sprint 
Definição da lista de itens backlog da Sprint. 
|**Atividade:**Fragmentar os itens do backlog do produto em itens backlog da Sprint|**Atividade:**Fragmentar os itens do backlog do produto em itens backlog da Sprint|
|---|---|
|Definição da lista de itens backlog da Sprint.||
|**Entrega:**itens da Sprint||
|**Responsável**|**Participante**|
|Analista TI|Analista TI/Desenvolvedor/Analista de negócio|
|**Tarefas executadas**|**Descrição**|
|Detalhar os itens de backlog do<br>produto,dividindo-os em itens.|Detalhamento dos itens que compõem uma Sprint.|
|**Observação**||
|||
**Atividade:** Estimar os itens backlog da Sprint 
Estimar esforço dos itens da Sprint. 
|**Atividade:**Estimar os itens backlog da Sprint|**Atividade:**Estimar os itens backlog da Sprint|
|---|---|
|Estimar esforço dos itens da Sprint.||
|**Entrega:**esforço dos itens da Sprint||
|**Responsável**|**Participante**|
|Desenvolvedor|Analista TI/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
|Realizar estimativa do item da<br>Sprint|Estimativa do esforço do item da Sprint|
|**Observação**||
|||
**Atividade:** Definir itens da Sprint 
Definir itens da Sprint 
|**Atividade:**Definir itens da Sprint|**Atividade:**Definir itens da Sprint|
|---|---|
|Definir itens da Sprint||
|**Entrega:**Sprint definida||
|**Responsável**|**Participante**|
|Dono do Produto|Analista TI/Dono do Produto/Scrum Master|
|**Tarefas executadas**|**Descrição**|
|Definir itens da Sprint|Definição de qual itens farão parte da Sprint|
|**Observação**||
|||
Página **11** de **23** 
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
|No sistema Redmine, criar a<br>demanda do tipo Sprint|Criar demanda do tipo Sprint no sistema Redmine<br>contendo informações básicas da sprint emquestão.|
|**Observação**||
|||
## **7.1.2. Executar a sprint (vide fluxo GETI- GGD -FP-0002_Executar a sprint_rev0.0)** 
**Atividade:** Codificar item 
Realizar a codificação do item da Sprint 
|**Atividade:**Codificar item|**Atividade:**Codificar item|
|---|---|
|Realizar a codificação do item da Sprint||
|**Entrega:**Item da Sprint codificado||
|**Responsável**|**Participante**|
|Scrum Master|Scrum Master/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
|Codificar o item da Sprint|Codificar o item da Sprint de acordo com as<br>especificações definidaspelos clientes|
|**Observação**||
|A codificação de produtos de dados pode envolver tanto o código em si para extração e<br>transformação dos dados, como pode ser voltada para desenvolvimento de modelos de<br>aprendizado de máquina ou outras atividades relacionadas a analytics ou ciência de dados.||
**Atividade:** Testar item 
Realizar testes relacionados à codificação do item da Sprint 
|**Atividade:**Testar item|**Atividade:**Testar item|
|---|---|
|Realizar testes relacionados à codificação do item da Sprint||
|**Entrega:**||
|**Responsável**|**Participante**|
|Scrum Master|Scrum Master/Desenvolvedor|
|**Tarefas executadas**|**Descrição**|
|Testes de codificação|Testes associados à codificação do item da Sprint<br>desenvolvido|
|**Observação**||
|||
Página **12** de **23** 
**Atividade:** Entregar item 
Realizar a entrega do item da Sprint 
**Entrega:** Itens consolidados e entregues 
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
## **7.1.3. Revisar a sprint (vide fluxo GETI-GGD-FP-0003_Revisar_sprint_rev0.0)** 
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
|Validar<br>os<br>indicadores<br>de<br>qualidade do software gerado na<br>Sprint|Teste do software implementado.|
|**Observação**||
|Os testes de qualidade são executados quando pertinente. A validação é realizada na<br>release.||
**Atividade:** Testar itens 
Testar a entrega da Sprint. 
|**Atividade:**Testar itens|**Atividade:**Testar itens|
|---|---|
|Testar a entrega da Sprint.||
|**Entrega:**Sprint testada||
|**Responsável**|**Participante**|
|Analista de Testes e Qualidade|Analista de Testes e Qualidade/Analista TI/PO|
|**Tarefas executadas**|**Descrição**|
|Testar todos os itens da Sprint|Itens da Sprint testados|
|**Observação**||
|Os testes dequalidade são executadosquandopertinente.||
Página **13** de **23** 
**Atividade:** Homologar itens 
Validar os itens da Sprint entregues 
**Entrega:** incremento aprovado 
|**Atividade:**Homologar itens|**Atividade:**Homologar itens|
|---|---|
|Validar os itens da Sprint entregues||
|**Entrega:**incremento aprovado||
|**Responsável**|**Participante**|
|Dono do produto|Cliente/ Dono do produto|
|**Tarefas executadas**|**Descrição**|
|Validar o produto de dados como<br>um<br>todo<br>a<br>partir<br>da<br>implementação<br>de<br>cada<br>incremento ou item da sprint.|Validação do produto|
|**Observação**||
|||
**Atividade:** Entregar artefatos 
Entregar artefatos 
**Entrega:** artefatos **Responsável Participante** Scrum Master Scrum Master/Desenvolvedor **Tarefas executadas Descrição** Entregar os artefatos Entrega do produto 
**Observação** 
## **Atividade:** Verificar qualidade 
Verificar a qualidade do produto de dados gerado por meio da consolidação dos itens da sprint validando os indicadores definidos. 
**Entrega:** Qualidade da demanda validada 
|**Atividade:**Verificar qualidade|**Atividade:**Verificar qualidade|
|---|---|
|Verificar a qualidade do produto de dados gerado por meio da consolidação dos itens da<br>sprint validando os indicadores definidos.||
|**Entrega:**Qualidade da demanda validada||
|**Responsável**|**Participante**|
|Analista de Testes e Qualidade|Analista de Testes e Qualidade|
|**Tarefas executadas**|**Descrição**|
|Validar<br>os<br>indicadores<br>de<br>qualidade do software gerado na<br>sprint|Teste do produto de dados implementado.|
|**Observação**||
|A validação é realizada na máster.||
Página **14** de **23** 
**Atividade:** Encerrar Sprint 
Formalizar a finalização da Sprint. 
**Entrega:** Sprint encerrada 
|**Atividade:**Encerrar Sprint|**Atividade:**Encerrar Sprint|
|---|---|
|Formalizar a finalização da Sprint.||
|**Entrega:**Sprint encerrada||
|**Responsável**|**Participante**|
|Analista de TI|Analista de TI|
|**Tarefas executadas**|**Descrição**|
|Encerrar a Sprint informando se<br>a<br>mesma<br>foi<br>aprovada<br>totalmente ou parcialmente|Sprint finalizada|
|**Observação**||
|||
## **7.1.4. Entregar incremento ou produto de dados (vide fluxo GETI-GGD-FP-0004_Entregar incremento_ou_produto_de_dados_rev0.0)** 
**Atividade:** Planejar a implantação da Sprint 
Realizar o planejamento da implantação do incremento ou produto de dados 
**Entrega:** Plano para implantar incremento em produção 
|**Atividade:**Planejar a implantação da Sprint|**Atividade:**Planejar a implantação da Sprint|
|---|---|
|Realizar o planejamento da implantação do incremento ou produto de dados||
|**Entrega:**Plano para implantar incremento em produção||
|**Responsável**|**Participante**|
|Dono do produto|Dono do produto /Analista TI|
|**Tarefas executadas**|**Descrição**|
|Planejar a implantação do produto<br>de dados emprodução|Implantação do incremento ou produto de dados<br>realizado|
|**Observação**||
|||
**Atividade:** Implantar a Sprint 
Realizar a implantação do incremento ou produto de dados no ambiente de produção 
**Entrega:** incremento implantado 
|**Entrega:**incremento implantado||
|---|---|
|**Responsável**|**Participante**|
|Analista TI|Analista TI|
|**Tarefas executadas**|**Descrição**|
Página **15** de **23** 
Implantar o incremento ou produto Incremento ou produto de dados implantado no ambiente de dados de produção 
**Observação** 
**Atividade:** Atualizar o backlog do produto 
Realizar a atualização do backlog do produto após a entrega do incremento 
**Entrega:** backlog do produto atualizado 
|**Atividade:**Atualizar o backlog do produto|**Atividade:**Atualizar o backlog do produto|
|---|---|
|Realizar a atualização do backlog do produto após a entrega do incremento||
|**Entrega:**backlog do produto atualizado||
|**Responsável**|**Participante**|
|PO|Cliente/PO|
|**Tarefas executadas**|**Descrição**|
|Atualizar backlog do produto|Backlog do produto atualizado com o novo produto de<br>dados ou as novas funcionalidades implementadas no<br>produto de dados|
|**Observação**||
|||
**Atividade:** Realizar a retrospectiva da sprint 
Realizar a retrospectiva da sprint para avaliar os pontos positivos e negativos 
**Entrega:** Plano de melhoria contínua 
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
Página **16** de **23** 
## **8. Entradas do processo** 
Itens de Backlog do Produto definidos na saída do processo “GETI–GST–PP– 0001 – Detalhamento do Backlog do Produto (ou Histórias do Usuário) Ver. 0.0”. 
## **9. Saídas do processo / resultados esperados** 
Artefatos produzidos durante o desenvolvimento e manutenção dos produtos de dados. 
## **10. Fluxo do processo** 
## **GETI-GGD-FP-0001_Planejar a sprint** 
## **GETI-GGD-FP-0002_Executar a sprint** 
## **GETI-GGD-FP-0003_Revisar a sprint** 
## **GETI-GGD-FP-0004_Entregar incremento ou produto de dados** 
## **11. Indicadores do processo** 
Os seguintes indicadores são previstos neste documento: 
- a) Indicador de Aceitação da Sprint/Entrega (IAS); 
- b) Indicador de Produtividade Ágil (IPA); 
- c) Indicador de qualidade de código (IQC); 
- d) Indicador de Conformidades em Homologação (ICH); 
- e) Leadtime. 
** **
## **Indicador de Aceitação da Sprint/Entrega** 
Verificar se as demandas planejadas nas sprints foram executadas no timebox e com qualidade, conforme tabela a seguir: 
**Tabela 1: IAS** 
|Finalidade|Garantir a qualidade na entrega das**sprints**.|
|---|---|
|Meta a cumprir|IAS igual ou superior a 75%|
|Forma de<br>acompanhamento|São apuradas a quantidade total de**sprints**entregues no período, a<br>quantidade de**sprints**que foram aceitas integralmente e a<br>quantidade de**sprints**aceitas parcialmente.|
|Periodicidade|Mensal|
|Mecanismo de cálculo (%)|É feita uma relação de proporção entre a quantidade de**sprints**<br>aceitas<br>integralmente e parcialmente junto ao total, chegando a um valor<br>percentual:<br>**IAS = (Qi + Qp/3) x 100**<br>**______________**<br>**Qt**<br>Onde:<br>IAS = Indicador de Aceitação da**Sprint**/Entrega;<br>Qi = Quantidade de**sprints**aceitas integralmente;<br>Qp = Quantidade de**sprints**aceitas parcialmente;<br>Qt=Quantidade total de**sprints**enviadas para aceite.|
Página **17** de **23** 
|Observações|O peso das**sprints**aceitas integralmente deve ser maior que o das<br>aceitas parcialmente. Nessa fórmula específica, o peso das**sprints**<br>aceitas integralmente é três vezes maior que o das aceitas<br>parcialmente.<br>Para efeitos desse indicador, não são contabilizadas**sprints**<br>rejeitadas, pois não atendem aos critérios mínimos de aceitação<br>previamente estabelecidos.|
|---|---|
## **Indicador de Produtividade Ágil** 
** **
Monitorar o alcance das metas de produtividade. 
**Tabela 2: IPA** 
|Finalidade|Garantir a produtividade das equipes ágeis, em termos do alcance<br>de metas aferidas por meio de métricas de**software**, observando os<br>critérios de qualidade e de aceitação definidos, bem como<br>mensuração em termo de produto ou resultado entregue.|
|---|---|
|Meta a cumprir|IPA igual ou superior a 90%|
|Forma de<br>acompanhamento|A produtividade será aferida por meio de metas de produtividade em<br>quantidades de produtos de dados observando a produtividade<br>mínima prevista no Anexo.|
|Periodicidade|Mensal|
|Mecanismo de cálculo (%)|**IPA = 100 * ( Pr / Pp )**<br>Onde:<br>IPA = Indicador de Produtividade Ágil;<br>Pr = Produtividade realizada no período para os perfis profissionais<br>alocados, em função da métrica de**produtos de dados**previamente<br>estabelecida;<br>Pp = Produtividade prevista no período para os perfis profissionais<br>alocados, em função da métrica de**produtos de dados**previamente<br>estabelecida.<br>Para calcular a Produtividade realizada no período (Pr) é utilizado o<br>catálogo de produtos de dados no Anexo.|
|Observações||
## **Indicador de Qualidade de código** 
** **
Assegurar a qualidade técnica das entregas. Utilizando, como por exemplo, SonarQube, é realizada uma análise estática do código para detectar bugs, duplicidade de código e vulnerabilidades de segurança, com exceção da linguagem DELPHI, conforme parâmetros definidos na tabela 3. 
**Tabela 3: Parâmetros de qualidade para primeira versão do código fonte** 
|**Grupo**|**Indicador**|**Unidade**|**Meta**|
|---|---|---|---|
|Projeto|Complexity / file ou equivalente|média total|<=10|
||Complexity / class ou equivalente|média total|<=10|
||Complexity / function ou<br>equivalente|média total|<= 3|
||Duplications ou equivalente|%|<=4%|
||Security<br>Issue<br>Tags<br>ou<br>equivalente|unidades|=0|
Página **18** de **23** 
||Technical<br>Debt<br>ratio<br>ou<br>equivalente|%|<= 2,5%|
|---|---|---|---|
||SQALE RATING ou equivalente|Nota|=A|
|Violações de código (possíveis<br>bugs, estilo de codificação, más<br>práticas de codificação)|Critical Issues ou equivalente|unidades|=0|
||Blocker Issues ou equivalente|unidades|=0|
|Indicadores relacionados a<br>testes|Unit Tests Coverage - camada<br>negócio / Impl ou equivalente|%|>=70%|
||Unit Test Success ou equivalente|%|=100%|
||Skipped Tests ou equivalente|unidades|=0|
O Indicador de qualidade de código (IQC) será calculado dividindo a Quantidade de requisitos de qualidade de código atendidos (ΣQrc) pela Quantidade total de requisitos de qualidade de código avaliados (ΣQtr), conforme descrito na tabela 4: 
**Tabela 4: IQC** 
|**abela 4: IQC**||
|---|---|
|Finalidade|Assegurar a qualidade do código em projetos de desenvolvimento,<br>diminuir a ocorrência de defeitos e medir o nível de adequação<br>do código fonte a características de qualidade determinadas pela<br>contratante|
|Meta a cumprir|>=90%|
|Forma de<br>acompanhamento|A aferição será realizada por meio de ferramentas automatizadas|
|Periodicidade|Por período previamente definido, seja em termos de**sprints**<br>executadas ou releases homologadas.|
|Mecanismo de cálculo (%)|**IQC = 100 * (Qrc / Qtr)**<br>Onde:<br>IQC = Indicador de qualidade de código;<br>Qrc = Somatório da Quantidade de requisitos de qualidade de código<br>atendidos;<br>Qtr = Somatório da Quantidade total de requisitos de qualidade de<br>código avaliados.|
|Observações|A qualidade de código faz parte da visão dos desenvolvedores,<br>engenheiros, arquitetos e, em alguns casos, analistas e gerentes.<br>Indicadores da qualidade de código incluem: complexidade do<br>código, duplicações de código, tamanho do código, entre outros.<br>Vale ressaltar que a menor qualidade no código está relacionada a<br>uma ocorrência maior de defeitos nas aplicações, que afetarão<br>diretamente a produtividade da equipe de desenvolvimento. Esse<br>indicador será utilizado desde o início do projeto, fazendo com que o<br>código seja desenvolvido dentro de padrões aceitáveis de qualidade.<br>Problemas de qualidade no código-fonte do**software**pré-existentes<br>devem ser desconsiderados na aferição do IQC.|
** **
Indicador de Conformidades em Homologação 
Assegurar o cumprimento dos prazos estabelecidos. 
**Tabela 5: ICH** 
|**abela 5: ICH**||
|---|---|
|Finalidade|Apura a quantidade de conformidades registradas pelo usuário<br>durante a homologação do produto.|
|Meta a cumprir|ICH igual ou superior a 90%.|
Página **19** de **23** 
|Forma de<br>acompanhamento|É apurada a quantidade de itens da sprint entregues em<br>conformidade aos requisitos mínimos de qualidade de código e<br>atendimento aos requisitos funcionais no período de referência.|
|---|---|
|Periodicidade|Mensal|
|Mecanismo de cálculo (%)|**ICH = ((Qp - Qpe) / Qp) * 100**<br>Onde:<br>ICH = Indicador de Conformidades em Homologação.<br>Qpe = Quantidade de itens da sprint entregues com erros de<br>codificação e/ou não implementação adequada dos requisitos<br>funcionais que foram identificados no ambiente de homologação.<br>Qp=Quantidade itens da sprint previstos.|
|Observações:|Não serão considerados erros identificados e reportados<br>previamente pela equipe de testes e que não foram ajustados pela<br>equipe responsável pelo desenvolvimento.|
** **
## **Leadtime** 
Como métrica para controlar quanto tempo uma tarefa leva para ser completada é adotado o Leadtime que é calculado com o número de dias entre o início e o fim de uma entrega. Esse intervalo é calculado conforme a demanda alcança diferentes status no processo de desenvolvimento: 
## • **Tarefas do tipo Sprint:** 
INICIO_LEADTIME – Quando a demanda atinge a situação “Associar itens de backlog” 
FIM_LEADTIME – Quando a demanda atinge a situação “Entregar itens da Sprint” 
Com o monitoramento do Lead Time é possível detectar pontos de lentidão, antecipando oportunidades de melhorias por meio de ações específicas e direcionadas. 
## **12. Governança** 
Não aplicável. 
## **13. Dono do documento** 
Celso de Souza Tchao, Chefe de Divisão, PR/DIRAD/CGTI/DIAPE 
## **14. Elaborador(es) do documento** 
Cristina d’Urso de Souza Mendes Santos, Pesquisadora em PI, PR/DIRAD/CGTI/DIAPE Rhodrigo da Venda Santana, Chefe de Divisão, PR/DIRAD/CGTI/COSIS/DIPRO Vladimir Guimarães de Carvalho, colaborador, PR/DIRAD/CGTI 
## **15. Aprovador(es) do documento** 
Marcus Vinicius da Motta Vieira, Coordenador Geral, PR/DIRAD/CGTI Celso de Souza Tchao, Chefe de Divisão, PR/DIRAD/CGTI/DIAPE 
Página **20** de **23** 
## **16. Bibliografia** 
Governo Federal. **Infraestrutura Nacional de Dados. Disponível em:** https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados. Acesso em 09 de Setembro de 2024 
Portaria SGD/MGI nº 750, de 20 de março de 2023 
Instrução Normativa SGD/ME nº 94, de 23 de dezembro de 2022 
EZAKI, CARLA. O que são produtos de dados? Aug 18, 2023. Disponível em: https://medium.com/luizalabs/o-que-s%C3%A3o-produtos-de-dados-57b6e6fa7e39. Acesso em:2024 
FERREIRA, Guido. Data Product vs Tech Product , Belo Horizonte, 2020 Disponível em: https://pt.linkedin.com/pulse/data-product-vs-tech-guima-ferreira. Acesso em: 2024 
## **17. Histórico das alterações** 
|**Data**|**Nº revisão**|**Item**|**Descrição**|
|---|---|---|---|
|||||
|||Todo||
|01/10/2024|0.0||Emissão inicial|
|||documento||
|||||
|||||
## **18. Anexo - CATÁLOGO DE SERVIÇOS DE PRODUTOS DE DADOS** 
1. Este anexo apresenta catálogo de serviços técnicos de produtos de DADOS. 
2. O catálogo de serviços de produtos de dados é composto pelos seguintes campos: 
 - Tipo: apresenta os tipos (categorias) das atividades que integram o catálogo de dados (ex: big data, inteligência artificial, machine learning, etc); 
 - Descrição da Atividade: apresenta a descrição do serviço a ser realizada pelo profissional; 
 - Unidade de Medida: corresponde a um item mensurável para aferição e recebimento do produto de dados; 
 - Esforço de referência (horas): corresponde a estimativa de horas necessárias para a realização da atividade técnica. 
3.Os profissionais que executarão as atividades definidas em ordem de serviço, devem ter perfil compatível com o serviço técnico a ser realizado. 
4. A aferição das metas de produtividades dos perfis profissionais de Administração de Dados e Analistas de BI deve observar as atividades, os produtos esperados, a unidade de medida e o esforço previstos no catálogo a seguir: 
Página **21** de **23** 
|**Tipo**|**Descrição da Atividade**|**Unidade de**<br>**medida**|**Esforço de**<br>**Referência(horas)**|
|---|---|---|---|
|DW e<br>Analytics|Construção do job ETL|Por Job|10|
|DW e<br>Analytics|Construção de job para<br>geração de bases de dados<br>para treinamento, validação<br>etestes|Por Job|1|
|Big Data|Realizar suporte técnico em<br>Analytics|Por<br>atendimento|8|
|Big Data|Instalar<br>serviços/componentes|Por serviço ou<br>componente|<br>16|
|Big Data|Configurar<br>serviços/componentes|Por serviço ou<br>componente|<br>8|
|Big Data|Realizar pesquisa técnica de<br>componentes|Por relatório|24|
|Big Data|Executar testes|Por Teste|24|
|Big Data|Elaborar roteiro de<br>instalação/configuração|Por serviço ou<br>componente|<br>24|
|Big Data|Elaborar script de automação|Por tarefa|24|
|Análise e<br>exploração<br>de dados|Construir/alterar relatório<br>utilizando ferramentas de<br>visualização de dados|Por relatório|2|
|Análise e<br>exploração<br>de dados|Construir/alterar gráfico<br>utilizando ferramentas de<br>visualização de dados|Por gráfico|2|
|Análise e<br>exploração<br>de dados|Construir/alterar Indicador<br>utilizando ferramentas de<br>visualização de dados|Por indicador|1|
|Análise e<br>exploração<br>de dados|Construir/alterar Dashboard<br>utilizando ferramentas de<br>visualização de dados|Por<br>dashboard|8|
|Análise e<br>exploração<br>de dados|Mapear Objeto de Dados|Por<br>objeto/tabela|1|
|Análise e<br>exploração<br>de dados|Construir/alterar funções,<br>scripts ou métricas<br>calculadas utilizadas em<br>ferramentas de visualização<br>de dados|Por função,<br>script ou<br>métrica|2|
|Web<br>Analytics|Construir ou alterar script<br>para a criação de imagens<br>de containers|Por arquivo<br>de script|16|
|Web<br>Analytics|Realizar pesquisa técnica de<br>componentes|Por relatório|24|
|Inteligência<br>Artificial|<br>Elaborar query para<br>Inteligência Artificial|Objeto/Tabela|<br>3|
Página **22** de **23** 
|**Tipo**|**Descrição da Atividade**|**Unidade de**<br>**medida**|**Esforço de**<br>**Referência(horas)**|
|---|---|---|---|
|Machine<br>Learning|Planejamento da solução|Por relatório|40|
|Machine<br>Learning|Treinamento/Retreinamento<br>de Modelo e Análise de<br>Resultados|Por Iteração<br>de<br>Treinamento|52|
|Machine<br>Learning|Parametrização/Configuração<br>de Modelo|<br>Por modelo|20|
|Machine<br>Learning|Pesquisa técnica de Modelos<br>e Métodos|Por Modelo<br>Avaliado|20|
|Machine<br>Learning|Pré-processamento de dados|Por script|30|
|Machine<br>Learning|Realizar exploração ou<br>modelagem de dados|Por relatório|20|
Página **23** de **23** 
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