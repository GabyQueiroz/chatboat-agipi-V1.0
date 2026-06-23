** **
## **MINISTÉRIO DO DESENVOLVIMENTO, INDÚSTRIA, COMÉRCIO E SERVIÇOS INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** 
## PORTARIA /INPI /DIRAD/ CGTI Nº 07, DE 07 DE AGOSTO DE 2024 
Publica os Procedimentos e o Fluxo de Processo sobre Detalhamento do Backlog do Produto (ou Histórias do Usuário) 
**O COORDENADOR-GERAL DE TECNOLOGIA DA INFORMAÇÃO DO INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** , no uso das atribuições que lhe foram conferidas pelo Decreto nº 8.854, de 22 de setembro de 2016, e pela Portaria INPI PR nº 09, publicada em 13 de março de 2024, e tendo em vista no processo SEI nº 52402.009002/2024-11, 
## **RESOLVE:** 
Art. 1º Publicar, na forma do anexo a esta Portaria, conforme definido no item 7.4 do Manual do Sistema de Padronização de Documentos GEQU-GDS-MN-0001, rev. 2.0, o Procedimento de Trabalho GETI–GST–PP-0001 e seu anexo GETI–GST–PP-0001, que versa sobre Detalhamento do Backlog do Produto (ou Histórias do Usuário); 
Art 2º Esta Portaria entra em vigor na data de sua publicação 
## **Marcus Vinicius da Mo�a Vieira** 
Coordenador-Geral de Tecnologia da Informação 
** **
Documento assinado eletronicamente por **MARCUS VINICIUS DA MOTTA VIEIRA** , **Coordenador(a) Geral** , em 07/08/2024, às 12:19, conforme horário oficial de Brasília, com fundamento no art. 6º, § 1º, do Decreto nº 8.539, de 8 de outubro de 2015. 
** **
A auten�cidade deste documento pode ser conferida no site h�p://sei.inpi.gov.br/sei/controlador_externo.php? acao=documento_conferir&id_orgao_acesso_externo=0, informando o código verificador **1057686** e o código CRC **282A01CB** . 
**Referência:** Processo nº 52402.009002/2024-11 
SEI nº 1057686 
Boletim Pessoal V do mês de Agosto de 2024 Expedido em 07/08/2024 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
## **Sumário** 
**1. Responsável ................................................................................................................................... 1 2. Objetivo .......................................................................................................................................... 2 3. Abrangência ................................................................................................................................... 2 4. Documentos Complementares ..................................................................................................... 2 5. Glossário ........................................................................................................................................ 2 6. Descrição dos processos ou atividades ...................................................................................... 3** 6.1. Detalhamento do produto ou projeto (compreensão do contexto e identificação das personas) ............................................................................................................................................. 4 6.2. Escrita da História do Usuário .................................................................................................. 4 6.3. Validar História do Usuário ....................................................................................................... 5 6.4. Status “História do Usuário Definida” ...................................................................................... 6 6.5. Fragmentar as Histórias em itens de backlog do produto ................................................... 6 6.6. Estimar o tamanho e esforço dos itens do backlog do produto .......................................... 6 6.7. Itens de backlog definidos ......................................................................................................... 6 6.8. Refinamento Contínuo ............................................................................................................... 7 **7. Entradas do processo ................................................................................................................... 7 8. Saídas do processo ....................................................................................................................... 8 9. Fluxo do processo ......................................................................................................................... 8 10. Indicadores do processo ............................................................................................................. 8 11. Dono do documento .................................................................................................................... 9 12. Outro(s) elaborador(es) do documento ...................................................................................... 9 13. Aprovador(es) do documento ..................................................................................................... 9 14. Bibliografia ................................................................................................................................... 9 15. Histórico das alterações .............................................................................................................. 9 16. Anexos .......................................................................................................................................... 9** 
## **1. Responsável** 
O Dono do Produto (P.O.) da área requisitante do projeto / produto, em parceria com a equipe de desenvolvimento de soluções de TIC. 
**Página 1 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
## **2. Objetivo** 
Este procedimento visa definir as atividades concernentes ao detalhamento do backlog do produto, ou seja, os entregáveis, também chamados de História dos Usuários, garantindo que essas Histórias sejam elaboradas de forma clara, compreensível e detalhada o suficiente para orientar o desenvolvimento de software de maneira eficaz, de modo que atenda às necessidades dos usuários finais. 
Este procedimento também visa estabelecer, para cada ator do processo, suas prerrogativas com o objetivo de buscar transparência e alinhamento às suas atribuições. Trata-se de um detalhamento de subprocesso mencionado no documento GETI-GTI-PP-0001 – Levantamento de Necessidades para o PDTIC (Fluxo Upstream). 
## **3. Abrangência** 
Este procedimento aplica-se aos Coordenadores, Diretores e demais integrantes do INPI que possam ocupar a posição de Dono de Produto da área requisitante do projeto. 
## **4. Documentos Complementares** 
- GETI-GTI-PP-0001- Levantamento de Necessidades para o PDTIC (Fluxo Upstream); 
- Plano Diretor de Tecnologia da Informação e Comunicação (PDTIC) vigente. 
## **5. Glossário** 
- Ambiente – Conjunto de recursos tecnológicos configurados para um propósito específico, como desenvolvimento, teste ou produção. Cada ambiente é isolado e possui suas próprias configurações, dados e políticas de segurança, garantindo que as atividades realizadas em um não afetem os demais. 
- Ambiente de produção – Ambiente real onde o software ou sistema é disponibilizado para os usuários finais, e onde as aplicações são executadas e acessadas pelos usuários no seu uso cotidiano. 
- Backlog do Produto – Lista de todas as funcionalidades, melhorias, correções e outros itens que devem ser desenvolvidos para um produto. O backlog é um conjunto de Histórias do Usuário e é gerenciado pelo Dono do Produto. 
- CGD – Comitê de Governança Digital; 
- CGTI – Coordenação-Geral de Tecnologia da Informação; 
- DIAPE – Divisão de Acompanhamento de Projetos Especiais; 
- DIINF – Divisão de Infraestrutura e Suporte; 
- DIPRO – Divisão de Padronização e Processos de Software; 
- Dono do Protudo (P.O.) – Pessoa responsável por gerenciar o backlog do produto e garantir que a equipe esteja focada nas prioridades certas. Também pode ser denominado demandante. 
- Funcionalidades – Conjunto de ações e serviços que um sistema ou produto de software pode executar, destinadas a atender às necessidades dos usuários do referido sistema. 
**Página 2 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
- História do Usuário – Descrição curta e simples de uma funcionalidade ou necessidade do usuário final do produto, geralmente formuladas como "Como [tipo de usuário], eu quero [ação] para [benefício]". As histórias do usuário são itens que compõem o backlog do produto. 
- Itens de Backlog do Produto – Cada componente individual listado no backlog do produto, que pode representar uma funcionalidade, melhoria, correção de bugs ou qualquer outro trabalho a ser realizado pela equipe de desenvolvimento. 
- Metodologias ágeis – Conjunto de práticas de gestão de projetos e desenvolvimento de software que promovem a colaboração, flexibilidade e entrega contínua de valor à área requisitante do projeto. 
- PDTIC – Plano Diretor de Tecnologia da Informação e Comunicação; 
- PO – _Product Owner_ ou Dono do Produto; 
- TIC – Tecnologia da Informação e Comunicações; 
- Release – Entregável de Software apto para ser disponibilizado no ambiente de produção; 
- Scrum – Estrutura de trabalho ágil que ajuda equipes a trabalhar juntas. Trata-se de uma metodologia que incentiva as equipes a aprenderem com experiências, se auto-organizarem enquanto trabalham em um problema e refletirem sobre seus resultados para melhorar continuamente. 
- Sistema de Demandas Redmine – Ferramenta utilizada pela CGTI para gerenciamento de projetos de desenvolvimento, demandas, acompanhamento do progresso das tarefas e colaboração com equipes de desenvolvimento. 
- Software – Conjunto de dados ou programas usados para operar computadores e executar tarefas específicas. 
- Sprint – período de tempo fixo e repetitivo, no qual uma equipe ágil trabalha para completar um conjunto específico de atividades; 
- Stakeholders – Pessoas ou grupos que têm interesse ou são afetados/ influenciados pelo andamento e resultado de um projeto. Pode incluir clientes, usuários finais, equipe de desenvolvimento, patrocinadores e qualquer outra parte interessada no projeto. 
- Wiki – Sistema de gerenciamento de conteúdo, dentro do Redmine, que permite a criação, edição e organização do conhecimento de um projeto. É utilizado para documentação e compartilhamento de conhecimento dentro da CGTI. 
## **6. Descrição dos processos ou atividades** 
A busca por inovação, melhoria contínua e o desenvolvimento dos serviços oferecidos pelo INPI para a sociedade é um compromisso de qualquer servidor dentro de suas atribuições. Portanto, a identificação de uma demanda tecnológica no INPI pode partir de quaisquer setores e funções da Autarquia. 
Para atingir esses objetivos, o detalhamento do Backlog do Produto (ou Histórias do Usuário), que buscamos descrever neste documento, se mostra como uma parte essencial do desenvolvimento de software, especialmente se tratando da utilização de metodologias ágeis para desenvolvimento de software, como Scrum. 
O Dono do Produto, da área requisitante, aqui denominado demandante, ficará responsável pelas principais atividades a seguir. 
**Página 3 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
## **6.1. Detalhamento do produto ou projeto (compreensão do contexto e identificação das personas)** 
Antes de começar a detalhar a história do usuário, é necessário entender de forma abrangente o contexto geral do projeto. Isso inclui os objetivos para o produto, as necessidades dos usuários, o planejamento das releases e o ambiente em que o software será utilizado: 
• Identificação dos stakeholders: O primeiro passo para compreender o contexto é identificar todos os stakeholders relevantes para o produto / projeto, incluindo não apenas os usuários finais do produto, mas também o proprietário do produto, a equipe de desenvolvimento, os gerentes de projeto e todas as outras partes interessadas que possam ter impacto no andamento do projeto. Tal tarefa será detalhada em Instrução de Trabalho específica. 
• Análise do ambiente: Trata-se do entendimento a respeito do ambiente no qual o produto será utilizado. Pode incluir, inclusive, restrições ou obrigações regulatórias ou legais que possam afetar o produto a ser desenvolvido, entre outros. 
• Definição dos objetivos do produto: Para começar o detalhamento do backlog do produto, é necessário ter uma compreensão clara dos objetivos do produto a ser desenvolvido. Isso inclui a compreensão do problema que o produto buscará resolver, as necessidades dos usuários que ele pretende atender e os resultados esperados do projeto. 
• Análise das necessidades dos usuários: Para realizar o detalhamento, é fundamental entender as necessidades e expectativas dos usuários finais do produto. Isso pode envolver a realização de entrevistas com usuários, análise de feedback dos usuários do sistema e outras técnicas de pesquisa. 
• Lista de Histórias do Usuário: É importante compreender o fluxo de trabalho dos usuários e como eles interagem com o produto. **Essa etapa é essencial para identificar as funcionalidadeschave que devem ser incluídas no detalhamento das histórias do usuário** , e pode envolver a criação de fluxos, mapas de jornada do usuário e outros artefatos que ajudem a visualizar o processo. 
• Planejar as Releases: Consiste em compilar e listar o conjunto de histórias de usuários que possibilitam disponibilizar parte do produto ou projeto em produção. Um produto ou projeto pode ter uma ou mais releases em seu planejamento. Essas releases representam versões do software que são entregáveis. 
• Estabelecimento de métricas: Por fim, é importante definir métricas que ajudem a avaliar o desempenho do produto após sua implementação. 
Ao compreender completamente o contexto do projeto, a equipe responsável pode criar Histórias do Usuário mais significativas e eficazes, que atendam às necessidades dos usuários finais do produto e contribuam para o sucesso de sua implementação e utilização. 
Além disso, é necessário realizar a identificação das personas, que são as representações fictícias dos usuários finais do produto. Elas ajudam a equipe a entender melhor para quem estão desenvolvendo e quais são as necessidades e expectativas desses usuários dos produtos finais. Cada história do usuário deve ser associada a uma ou mais personas relevantes e, uma vez que as personas foram definidas e validadas, cada história do usuário é associada a uma ou mais personas. Isso ajuda a equipe a manter o foco nas necessidades dos usuários durante o processo de desenvolvimento. 
## **6.2. Escrita da História do Usuário** 
**Página 4 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
Uma História do Usuário é uma descrição concisa de uma funcionalidade do produto, do ponto de vista do usuário. Ela segue uma estrutura simples, geralmente composta por três elementos: “quem”, “o que” e “por que”. Por exemplo: "Como um usuário, eu quero poder fazer login com minha conta do PAG para acessar o sistema de forma rápida e segura". 
Essa etapa é realizada pelo P.O. do produto, na Wiki do Sistema de Demandas – Redmine – e inclui: 
• Identificação do papel do usuário: O primeiro passo na escrita da História do Usuário é identificar o papel do usuário que está buscando uma determinada funcionalidade. Isso ajuda a equipe de desenvolvimento a entender melhor para quem estão desenvolvendo a funcionalidade e quais são suas necessidades específicas. 
• Definição da ação desejada: A história do usuário deve descrever uma ação específica que o usuário deseja realizar ou um problema que ele quer resolver. Essa ação pode ser algo como "fazer login", "criar um novo perfil", "pesquisar por processos", etc. A ação deve ser descrita de forma clara e concisa. 
• Inclusão do motivo ou benefício da ação: Além da ação desejada, o detalhamento da história deve incluir o motivo ou benefício existente por trás dessa ação/funcionalidade. Buscar responder perguntas como: “Por que o usuário quer realizar essa ação?”; “Qual é o objetivo final ou o valor que ele espera obter?”. Isso ajuda a equipe de desenvolvimento a entender o contexto por trás da funcionalidade e a priorizar adequadamente o desenvolvimento. 
• Utilização de uma linguagem simples e direta: As histórias do usuário devem ser escritas em linguagem simples e direta, de forma que sejam facilmente compreensíveis por todos os membros da equipe, independentemente de conhecimento profundo a respeito da parte técnica ou não. Por isso, deve-se evitar jargões técnicos ou termos ambíguos que possam levar a interpretações diferentes. Caso contrário, poderá haver falha na comunicação entre os Donos do Produto e a equipe de desenvolvimento, levando a falhas no desenvolvimento e quebra de expectativas. 
• Formato padrão: Embora não exista um formato único para escrever Histórias do Usuário, é comum seguir uma estrutura simples, como a seguinte: "Como um [usuário], eu quero [ação/funcionalidade desejada] para que [motivo ou benefício]". 
• Critério de aceitação: É essencial definir de forma clara e objetiva as condições necessárias para avaliar quando a história do usuário foi implementada de forma adequada pela equipe técnica. 
• Associação com a Release: É importante associar cada história do usuário a uma Release específica, indicando em qual entrega ou versão do software ela será incluída. 
Ao escrever as Histórias do Usuário de forma clara e detalhada, o demandante pode garantir que todos tenham uma compreensão correta das funcionalidades a serem desenvolvidas e que o produto final atenda às necessidades e expectativas dos usuários finais. É importante ressaltar que a História de Usuário escrita poderá ser alterada a qualquer tempo. No entanto, é crucial ter em mente que a compreensão de muitas mudanças na história do usuário após a implementação trará ônus para o INPI, exigirá retrabalho para a CGTI e resultará em valor não entregue para o usuário do INPI. 
Ao término da escrita da História do Usuário, o projeto deve ser enviado à DIPRO, para validação. 
## **6.3. Validar História do Usuário** 
Uma vez que a história do usuário está detalhada, a equipe da DIPRO dá início à análise formal da especificação do projeto, avaliando se a especificação inicial está aderente à forma definida pelo Template de documentação. 
Em seguida, a análise técnica da especificação do projeto é conduzida pelas equipes técnicas especializadas (DIAPE, DIINF ou DISIS, conforme a natureza específica de cada projeto). Essa 
**Página 5 de 9** 
**Uso Interno** Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
análise técnica se concentra em avaliar a viabilidade técnica das soluções propostas, identificar potenciais desafios e determinar os recursos necessários para uma implementação bem-sucedida, além da validar se o entendimento do setor técnico está de acordo com a expectativa que a área demandante possui para o resultado do projeto. 
Também é fundamental avaliar e validar se os Critérios de Aceitação das Histórias do Usuário foram estabelecidos de forma clara. Essa avaliação é essencial para garantir que o desenvolvimento do produto comece em uma base sólida e bem fundamentada, reduzindo riscos e otimizando a eficiência e eficácia do processo de desenvolvimento. 
## **6.4. Status “História do Usuário Definida”** 
Esta etapa marca um ponto crucial no ciclo de vida do projeto, e indica que a funcionalidade está preparada para avançar para a fase de desenvolvimento do produto, porém o início efetivo do desenvolvimento é realizado quando determinados critérios são atingidos. Por exemplo, quando há disponibilidade de equipe para realizar o desenvolvimento. **É importante notar que a equipe de desenvolvimento aguardará até que pelo menos um entregável de software apto para ser disponibilizado no ambiente de produção alcance o status de "História do Usuário Definida" para iniciar, de fato, o desenvolvimento do produto** . Este requisito garante que uma base substancial mínima de requisitos e especificações tenha sido estabelecida e validada antes de prosseguir. 
## **6.5. Fragmentar as Histórias em itens de backlog do produto** 
Nesta etapa, o objetivo é dividir as Histórias do Usuário em itens menores e mais gerenciáveis, que possam ser priorizados, estimados e desenvolvidos de maneira mais eficiente. Para isso, a equipe da área técnica revisa cada história do usuário para garantir que todos compreendam os requisitos e o objetivo da história, buscando analisar a História do Usuário para identificar componentes ou funcionalidades menores que compõem a história principal e determinar as subtarefas necessárias para implementar cada componente ou funcionalidade. 
## **6.6. Estimar o tamanho e esforço dos itens do backlog do produto** 
Após a fragmentação das Histórias em Itens de Backlog do Produto, é preciso determinar o tamanho e o esforço necessário para completar cada item do backlog do produto, facilitando a priorização e o planejamento das sprints. Para isso, a equipe técnica discute cada item de backlog para entender os requisitos, a complexidade e as possíveis dificuldades, utilizando técnicas de estimativas. 
É necessário identificar possíveis dependências entre itens de backlog que podem impactar o esforço estimado e avaliar riscos técnicos ou de negócio que possam aumentar o esforço necessário para completar os itens. 
Em seguida, a equipe técnica documenta as estimativas de tamanho e esforço para cada item de backlog, mantendo um registro histórico das estimativas para referência futura e melhoria contínua do processo de estimativa. 
É desejável envolver toda a equipe de desenvolvimento na estimativa para obter uma visão mais precisa e diversificada, realizando sessões de estimativa em um ambiente colaborativo e sem pressa para garantir a qualidade das estimativas. 
## **6.7. Itens de backlog definidos** 
**Página 6 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
O processo é considerado concluído quando todos os itens de backlog do produto foram fragmentados, detalhados, estimados e priorizados, e estão prontos para serem incluídos nas sprints. Este marco é essencial para garantir que a equipe de desenvolvimento tenha um backlog bem definido e preparado, permitindo uma execução eficiente e alinhada com os objetivos do projeto. 
Este marco representa a conclusão do processo de detalhamento das histórias do usuário. Significa que todos os itens de backlog do produto foram devidamente fragmentados, detalhados, estimados e priorizados, estando prontos para serem selecionados e trabalhados nas próximas sprints. A partir deste ponto, o backlog do produto está completo e preparado, proporcionando uma base sólida para a execução das sprints e garantindo que a equipe de desenvolvimento possa trabalhar de forma eficiente e alinhada com os objetivos do projeto. 
## **6.8. Refinamento Contínuo** 
O detalhamento da História do Usuário é um processo contínuo que ocorre ao longo do ciclo de vida do projeto. À medida que a equipe aprende mais sobre o produto e seus usuários, as Histórias do Usuário podem ser revisadas, refinadas e ajustadas para melhor atender às necessidades em evolução: 
• Feedback e aprendizado: Durante o desenvolvimento do projeto, a equipe responsável pelo desenvolvimento recebe feedback de várias fontes, incluindo usuários do produto, stakeholders do projeto, testes de homologação e métricas de desempenho. Esse feedback é usado para aprender com as experiências passadas e identificar áreas de melhoria nas histórias do usuário. 
• Revisão das histórias do usuário: Regularmente, a equipe demandante precisa revisar as histórias do usuário existentes para garantir que ainda estejam alinhadas com os objetivos do projeto e as necessidades dos usuários do produto. Isso pode envolver o aprimoramento da descrição das Histórias, o ajuste das prioridades ou até mesmo o descarte de histórias obsoletas ou redundantes. 
• Adaptação às mudanças: À medida que o projeto avança, é esperado que requisitos mudem, a depender do cenário dentro e fora do INPI. A equipe de desenvolvimento está ciente que poderá precisar se adaptar a essas mudanças, atualizando as Histórias do Usuário conforme necessário para refletir as novas direções necessárias para o projeto. 
• Colaboração e comunicação: O refinamento contínuo é um esforço colaborativo que envolve toda a equipe, incluindo o dono do produto, desenvolvedores, testadores e outros membros relevantes. A comunicação eficaz é fundamental para garantir que todos estejam alinhados e contribuam para o processo de refinamento. 
• Documentação e rastreabilidade: Todas as mudanças e atualizações nas Histórias do Usuário devem ser devidamente documentadas na Wiki do Sistema de Demandas Redmine, para garantir rastreabilidade e transparência. Isso ajuda a equipe a acompanhar o progresso do projeto e entender como as histórias foram refinadas ao longo do tempo. 
A etapa de refinamento contínuo é uma parte integrante do processo de desenvolvimento, onde as histórias do usuário são revisadas, aprimoradas e adaptadas às mudanças ao longo do ciclo de vida do projeto. Isso busca com que o produto final atenda às necessidades dos usuários e permaneça relevante. 
## **7. Entradas do processo** 
- Necessidades identificadas pelos demandantes; 
- Informações coletadas pelo P.O. para preenchimento do detalhamento do backlog do produto 
- (ou História do Usuário); 
**Página 7 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
- PDTIC vigente. 
## **8. Saídas do processo** 
- Histórias dos Usuários descritas de forma detalhada e clara; 
- Documentação do projeto pronta para desenvolvimento pela equipe responsável. 
## **9. Fluxo do processo** 
Vide GETI–GST–FP–0001 – Detalhamento do Backlog do Produto (ou Histórias do Usuário) Ver. 0.0, disponível em: 
<Link do Drive onde for armazenado o Fluxo> 
## **10. Indicadores do processo** 
**10.1 Taxa de Conclusão de Histórias do Usuário** : mede a proporção de histórias do usuário que foram completamente detalhadas em relação ao total de histórias do usuário identificadas. É uma métrica para avaliar o progresso do desenvolvimento de software. Ela é calculada como a proporção de histórias do usuário que foram totalmente detalhadas em relação ao número total de histórias do usuário concluídas em um determinado período de tempo ou projeto, conforme a seguir: 
(Número de Histórias do Usuário totalmente detalhadas) / (Número de Histórias do Usuário concluídas) x 100% 
**10.2 Tempo Médio de Detalhamento por História do Usuário** : mede o tempo médio necessário para detalhar uma história do usuário, desde a identificação da necessidade até a sua finalização. É uma métrica que permite avaliar a eficiência do processo de elaboração de requisitos ao longo do ciclo de desenvolvimento de software. É calculada somando o tempo total gasto para detalhar todas as Histórias do Usuário e dividindo esse valor pelo número total de Histórias do Usuário detalhadas, conforme a seguir: 
(Tempo total gasto para detalhar todas as Histórias do Usuário) / (Número total de Histórias do Usuário detalhadas) 
**10.3 Número Médio de Revisões ou Refinamentos Necessários** : acompanha o número médio de vezes que uma história do usuário é revisada ou refinada pelo P.O. antes de ser considerada completa e pronta para ser desenvolvida. Durante o processo de elaboração de requisitos, é comum que as histórias do usuário passem por diversas iterações de revisão e refinamento para garantir que atendam adequadamente às necessidades e expectativas dos usuários finais. Essas revisões e refinamentos são realizados pelo Product Owner, que é responsável por garantir que as histórias do usuário estejam claras, precisas e alinhadas com os objetivos do projeto. É calculada somando todos os números de revisões ou refinamentos necessários registrados e dividindo a soma pelo número total de histórias do usuário., conforme a seguir: 
(Soma dos números de revisões ou refinamentos necessários registrados) / (Número total de Histórias do Usuário). 
**Página 8 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GST–PP-0001|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|07/08/2024|
||**Detalhamento do Backlog do Produto (ou**<br>**Histórias do Usuário)**|**Processo**|Levantamento de<br>Necessidades e<br>Requisitos (Nivel 3)|
## **11. Dono do documento** 
Pedro Calisto Luppi Monteiro Junior, Coordenador, COSIS/CGTI/DIRAD. 
## **12. Outro(s) elaborador(es) do documento** 
Natália Pacheco Ribeiro Machado, Técnico em Planejamento, Gestão e Infraestrutura, DISTI/CGTI/DIRAD; 
Vinícius de Souza Machado, Técnico em Planejamento, Gestão e Infraestrutura, SERED/DIINF/COINF/CGTI/DIRAD. 
## **13. Aprovador(es) do documento** 
Marcus Vinícius da Motta Vieira, Coordenador-Geral, CGTI/DIRAD. 
## **14. Bibliografia** 
Não aplicável. 
## **15. Histórico das alterações** 
|**Nº da**<br>**Revisão**|**Data**|**Item e/ou Descrição**|
|---|---|---|
|0.0|22/07/2024|Emissão inicial|
||||
## **16. Anexos** 
- ANEXO 1 - GETI–GST–FP– 0001 - Detalhamento do Backlog do Produto (ou Histórias do Usuário). 
**Página 9 de 9** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
** **