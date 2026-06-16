** **
## **MINISTÉRIO DO DESENVOLVIMENTO, INDÚSTRIA, COMÉRCIO E SERVIÇOS INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** 
PORTARIA /INPI / DIRAD/ CGTI Nº 04, DE 25 DE ABRIL DE 2024 
Publica os procedimentos e formulários sobre a implantação e requisição de mudanças na infraestrutura de produção. 
**O COORDENADOR-GERAL DE TECNOLOGIA DA INFORMAÇÃO DO INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** , no uso das atribuições que lhe foram conferidas pelo Decreto nº 8.854, de 22 de setembro de 2016, e pela Portaria INPI PR nº 09, publicada em 13 de março de 2024, e tendo em vista no processo SEI nº 52402.004240/2024-30, 
## **R E S O LV E :** 
Art. 1º Publicar na forma do anexo a esta Portaria os documentos elencados nos incisos I e II, que foram elaborados e revisados em conformidade com o Sistema de Padronização de Documentos, para alinhamento ao Manual do Sistema de Padronização de Documentos do INPI (GEQU-GDS-MN-0001). 
I - Procedimento GETI – STI – PP– 0001, que versa sobre a implantação de mudanças na infraestrutura em produção; 
II - Formulário GETI-STI-FR-0001, que se refere ao formulário para a requisição de mudança na infraestrutura de produção; 
Art. 3 º Revogar a PORTARIA/INPI/CGTI Nº 02, de 03 de novembro de 2021, e a PORTARIA/INPI/CGTI Nº 03, de 03 de novembro de 2021. 
Art 4º Esta Portaria entra em vigor na data de sua publicação. 
## **Marcus Vinicius da Mo�a Vieira** 
Coordenador-Geral de Tecnologia da Informação 
** **
Documento assinado eletronicamente por **MARCUS VINICIUS DA MOTTA VIEIRA** , **Coordenador(a) Geral** , em 14/05/2024, às 20:18, conforme horário oficial de Brasília, com fundamento no art. 6º, § 1º, do Decreto nº 8.539, de 8 de outubro de 2015. 
** **
A auten�cidade deste documento pode ser conferida no site 
h�p://sei.inpi.gov.br/sei/controlador_externo.php?acao=documento_conferir&id_orgao_acesso_externo=0, informando o código verificador **1010807** e o código CRC **AE9845F6** . 
** **
** **
**Referência:** Processo nº 52402.004240/2024-30 
SEI nº 1010807 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
**Sumário 1. Responsável ................................................................................................................................... 1 2. Objetivo .......................................................................................................................................... 1 3. Abrangência ................................................................................................................................... 1 4. Documentos complementares ...................................................................................................... 1 5. Glossário ........................................................................................................................................ 1 6. Descrição dos processos ou atividades ...................................................................................... 2 7. Entradas do processo ................................................................................................................... 5 8. Saídas do processo ....................................................................................................................... 5 9. Fluxo do processo ......................................................................................................................... 5 10. Indicadores do processo ........................................................................................................... 10 11. Dono do documento .................................................................................................................. 10 12. Outro(s) elaborador(es) do documento .................................................................................... 10 13. Aprovador(es) do documento ................................................................................................... 10 14. Bibliografia ................................................................................................................................. 10 15. Histórico das alterações ............................................................................................................ 10 16. Anexos ........................................................................................................................................ 11** 
## **1. Responsável** 
DIINF/COINF/CGTI 
## **2. Objetivo** 
Acelerar as alterações de infraestrutura, facilitando a comunicação de todos os interessados, e contribuindo para o tratamento dos riscos. 
## **3. Abrangência** 
Obrigatório para as alterações de infraestrutura em ambiente de produção. Adotado caso a caso para os demais ambientes. Consultar o Anexo 2 para obter detalhes sobre os ambientes operacionais do INPI. 
## **4. Documentos complementares** 
RDM – Requisição de Mudança em formato Microsoft Word (.docx), Anexo 1. 
## **5. Glossário** 
## **5.1. Siglas** 
- CCME – Comitê Consultivo de Mudanças e Emergências 
- COINF – Coordenação de Infraestrutura, Suporte e Segurança da Informação 
- DIINF – Divisão de Infraestrutura e Suporte 
- DISEG – Divisão de Segurança da Informação 
- IC – Item de Configuração 
- INPI – Instituto Nacional da Propriedade Industrial 
- ITIL – IT Infrastructure Library (Boas Práticas de Gerenciamento de TI) 
- ITSM – IT Service Management (Serviço de Gerenciamento de TI) 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 1 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
- POP – Procedimento Operacional Padrão 
- RDM – Requisição de Mudança 
- RPI – Revisão Pós-implementação 
- SERED – Serviço de Atendimento ao Usuário e Administração de Rede 
## **5.2. Definições** 
- **Comitê Consultivo de Mudanças e Emergências** - grupo formado pelo Gerente de Mudanças e pelos servidores públicos lotados na COINF, COSIS, ou qualquer das áreas abaixo dessas que estejam reunidos para analisar e aprovar, ou reprovar, as RDM em pauta; 
- **Item de Configuração** – qualquer componente ou serviço que precise ser gerenciado de forma a entregar um serviço de TIC. Por exemplo: servidor, roteador, software, web servisse, licença de software, etc.; 
- **Serviço** – conjunto de itens de configuração; 
- **Janela de Manutenção** – período de tempo semanal durante o qual poderão ser executadas RDM; 
- **Janela de Manutenção Emergencial** – período de tempo diário durante o qual poderão ser executadas RDM; 
- **Mudança** - qualquer alteração em item de configuração que demande planejamento e aprovação de áreas técnicas ou de negócio; 
- **Plano de Comunicação** – conjunto de mensagens, com seus respectivos conteúdos, destinatários e eventos disparadores; 
- **Plano de Retorno** – é o conjunto de atividades que deverá ser executado caso a RDM falhe. Seu objetivo é restaurar os itens de configuração ao seu estado anterior ou a um estado funcional; 
- **Procedimento Operacional Padrão** – é um documento (instrução de trabalho) que registra o passo a passo, garantindo que qualquer pessoa, minimamente qualificada, consiga realizá-lo sem grandes problemas. Trata-se de um roteiro padronizado com o objetivo de garantir a qualidade da entrega, diminuindo os desvios de execução; 
- **Processo de Gerenciamento de Mudanças** – é responsável por garantir que métodos e procedimentos padronizados sejam utilizados para registrar, analisar, planejar, agendar, implantar, documentar e revisar todas as mudanças na infraestrutura de produção; 
- **Requisição de Mudança (RDM)** – pedido formal, devidamente registrado, para realizar uma mudança; 
- **Revisão Pós-Implementação** – avaliação da execução e dos resultados da mudança para verificar se o objetivo foi atingido, e identificar as lições aprendidas; 
- **Serviço de Gerenciamento de TI** – software que automatiza os processos ITIL de Gerenciamento de chamados, Gerenciamento de Problemas, Gerenciamento de Requisições, Gerenciamento de Mudanças e Banco de Dados de Gerenciamento de Configuração. 
## **6. Descrição dos processos ou atividades** 
## **6.1. Calendário** 
**6.1.1.** O Gerente de Mudanças faz a RPI e envia o relatório para os participantes do CCME toda segunda-feira até as 12h00; 
**6.1.2.** O prazo para submissão de RDM se encerra às 12h00 toda terça-feira; 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 2 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
- **6.1.3.** O Gerente de Mudanças analisa e pauta as RDM para a próxima reunião do CCME até as 16h00 toda terça-feira; 
- **6.1.4.** O CCME se reúne ordinariamente toda quarta-feira de 11h00 às 12h00; 
- **6.1.5.** O Gerente de Mudanças efetua os ajustes definidos pelo CCME e envia relatório com as RDM agendadas até as 16h00 toda quarta-feira; 
**6.1.6.** As janelas padrão de manutenção começam na sexta-feira às 20h00 e terminam no domingo às 20h00; 
**6.1.7.** As janelas de manutenção emergencial começam às 20h00 e terminam às 06h00 todos os dias; 
**6.1.8.** O CCME se reunirá extraordinariamente sempre que solicitado pelo Gerente de Mudanças; 
** **
## **6.2. Tipo** 
**6.2.1. Padrão** – RDM submetida para aprovação sem data de execução definida, ou com data e hora dentro de janela padrão de manutenção, e que atende aos critérios necessários para seguir o fluxo de Autorização Expressa. Neste fluxo o agendamento pode ser aprovado pelos donos dos serviços afetados pelos itens de configuração citados na seção “Inventário” da RDM. Os critérios para ser considerada uma RDM padrão estão definidos no item 9.2.4 abaixo. 
**6.2.2. Programada** – RDM submetida para aprovação sem data de execução definida, ou com data e hora dentro de uma janela padrão de manutenção. Toda mudança programada passa obrigatoriamente pela análise e aprovação do CCME antes de ser executada, e se aprovada, será, preferencialmente, agendada para a janela padrão de manutenção seguinte a reunião do CCME que a aprovou; 
**6.2.3. Emergencial** – RDM submetida para aprovação com data e hora de execução fora de uma janela padrão de manutenção. Será agendada pelo integrante do CCME disponível no momento da submissão, executada conforme a necessidade e revisada na reunião do CCME subsequente; 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 3 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
## **6.3. Categoria** 
**6.3.1. Corretiva** – busca a resolução de incidente ou problema, devendo ser associada a pelo menos um número de chamado (incidente ou problema) dentre aqueles registrados na ferramenta de ITSM; 
**6.3.2. Adaptativa** – busca a adaptação a uma regra de negócio, sem adição de serviço ou funcionalidade, devendo ser associada a pelo menos um número de chamado (requisição) dentre aqueles registrados na ferramenta de ITSM; 
**6.3.3. Evolutiva** – busca a adição de novos serviços e/ou funcionalidades, devendo ser associada a pelo menos um projeto dentre aqueles registrados na ferramenta de gerenciamento de projetos. 
## **6.4. Ciclo de vida da mudança** 
**6.4.1. Nova** – a RDM recebeu uma identificação única e está disponível para ser planejada; 
**6.4.2. Planejada** – o Líder da Mudança concluiu o planejamento da mudança; 
**6.4.3. Pautada** – o Gerente de Mudanças concluiu que a RDM preenche os requisitos e que é o momento para sua implantação, podendo ser avaliada pelo CCME. Será verificado o preenchimento da RDM, se ela é repetição de outra RDM, e se já foi recusada anteriormente, podendo ser “Pautada”, ou seja, inserida na pauta da próxima reunião do CCME, ou “Cancelada” tendo os motivos registrados na nota de cancelamento; 
**6.4.4. Agendada** – significa que a RDM foi aceita e sua execução foi programada; 
**6.4.5. Executada** – indica que as atividades da RDM foram realizadas e a revisão pósimplementação pode ser feita; 
**6.4.6. Concluída** – as atividades foram concluídas e o efeito desejado foi produzido; 
**6.4.7. Revertida** – foi necessário executar o Plano de Retorno; 
**6.4.8. Cancelada** – a qualquer momento a RDM pode ser cancelada, mas o motivo do cancelamento deve ser registrado na RDM. 
## **6.5. Papéis e Responsabilidades** 
## **6.5.1.** Coordenador-Geral e Coordenadores 
 - Promover o uso correto do processo dentro da organização; 
 - Representar o processo no relacionamento da TIC com a organização e fornecedores; 
 - Acordar as metas de atendimento de mudanças para a organização; 
- **6.5.2.** Gerente de Mudanças 
 - Zelar pelo uso correto do processo dentro da organização; 
 - Acompanhar a qualidade do atendimento das RDM; 
 - Reportar as métricas alcançadas pelo processo; 
 - Promover ações de melhoria no processo; 
 - Avaliar a viabilidade e agendar a execução das RDM planejadas; 
 - Analisar os riscos e a priorização das RDM; 
 - Seguir o calendário de janelas das mudanças; 
 - Gerenciar as filas de atendimento de mudanças; 
 - Convocar e presidir o CCME; 
 - Comunicar as ações e impactos esperados das mudanças programadas. 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 4 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
## **6.5.3.** Comitê Consultivo de Mudanças e Emergências 
- Analisar os riscos e impactos das mudanças pautadas e emergenciais; 
- Definir o agendamento das mudanças pautadas e emergenciais; 
- Aprovar a execução das RDMs pautadas e emergenciais. 
## **6.5.4.** Líder da Mudança 
- Validar o planejamento das atividades técnicas da RDM; 
- Coordenar a execução das atividades técnicas da RDM; 
- Decidir quanto à necessidade da execução do Plano de Retorno; 
- Explicitar os riscos e benefícios da RDM; 
- Realizar a revisão pós-implementação das RDM; 
- Atender aos chamados designados para criação de RDM; 
- Registrar no OTRS o sucesso ou a falha da RDM, bem como os detalhes relevantes de sua execução; 
## **6.5.5.** Analista Executor 
- Auxiliar o Líder da Mudança no planejamento e registro das atividades técnicas da RDM; 
- Definir as atividades técnicas da RDM; 
- Realizar as atividades técnicas programadas; 
- Comunicar com o Líder da Mudança sobre a execução das atividades; 
- Fornecer feedback técnico a respeito das atividades, riscos e viabilidade da RDM. 
## **6.5.6.** Requisitante da Mudança 
- Informar as necessidades de forma clara; 
- Cooperar com o Líder da Mudança durante o planejamento da RDM; 
- Fornecer resposta necessária para validação dos efeitos da mudança. 
## **7. Entradas do processo** 
- RDM – Requisição de Mudança 
## **8. Saídas do processo** 
- Requisição de Mudança concluída, revertida ou cancelada 
- Relatório da Revisão Pós-Implementação 
- Relatório Mensal de Gerenciamento de Mudança 
## **9. Fluxo do processo** 
O fluxo aqui apresentado pode ser implementado de várias formas diferentes em seus detalhes operacionais. Esses detalhes são definidos no Anexo 3 – Detalhes Operacionais de Implementação, e podem ser alterados ao longo do tempo sem que o fluxo definido aqui se altere, bastando publicar nova versão do Anexo 3. 
## **9.1. Abrir a RDM – Requisitante** 
O processo se inicia com a criação de uma RDM. É responsabilidade do Requisitante, depois de criá-la, preencher todos os campos da seção DETALHAMENTO da RDM, sendo eles: alinhamento estratégico, data de início e fim da execução, tempo de indisponibilidade esperado, nome da 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 5 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
mudança, identificação e dados de contato do requisitante, justificativa, benefícios esperados, riscos tratados, motivação, escopo, riscos da execução e classificação. Todos os campos são obrigatórios. Podendo ser usado o recurso da expressão “N/A – Não se Aplica” como resposta. 
Estado da RDM ao final da atividade: **Nova** 
## **9.2. Planejar a RDM – Líder da Mudança** 
A condição para executar essa atividade é a RDM estar no estado: **Nova** 
O planejamento da RDM envolve a definição de suas atividades técnicas, identificação dos seus riscos, determinação dos resultados desejados, e outras avaliações e decisões que serão importantes para garantir a entrega do benefício esperado pelo requisitante. 
Há muita interação entre o Líder da Mudança, o Gerente de Mudanças e o Requisitante durante o planejamento. O correto entendimento das necessidades, premissas e restrições, as quais a RDM está submetida é crítico para o tratamento dos riscos. 
É durante esta atividade que será decidido o tipo de RDM, qual o dia e horário mais adequados para sua execução, os prazos a serem cumpridos, as evidências que serão coletadas, o plano de testes e o plano de comunicação. 
## **9.2.1.** Definir atividades técnicas da RDM 
Um dos principais pontos do planejamento da RDM é a definição das atividades técnicas que serão desempenhadas. Devem ser determinadas as ações a serem realizadas para entregar o benefício esperado pelo Requisitante, e as ações em caso de falha ou erro durante a execução da RDM, de maneira a garantir a disponibilidade do serviço, e ações para verificar os resultados alcançados: o plano de testes. 
Como se trata do desenvolvimento de procedimentos técnicos, é importante que sejam 
definidas por analistas especialistas, preferencialmente os mesmos que os executarão. 
Caso o Líder da Mudança pretenda que a mudança seja categorizada como padrão, ele deve garantir que as atividades técnicas sejam todas baseadas exclusivamente em Procedimento Operacional Padrão (Instrução de Trabalho) vigentes. 
## **9.2.2.** Registrar o planejamento na RDM 
O Líder da Mudança deve garantir que todos os campos das seções DETALHAMENTO e PLANEJAMENTO da Requisição de Mudança estejam corretamente preenchidos. 
## **9.2.3.** Validar o planejamento 
Com todos os detalhes incluídos na RDM, o Líder da Mudança deve validar se o planejamento está de acordo com a justificativa e escopo. É importante observar se o prazo das atividades está dentro do acordado com o Requisitante. 
## **9.2.4.** Classificar a RDM 
Quando se tratar de uma RDM integralmente implementada através de ferramenta auditável de gerenciamento de configuração (exemplo, Rundeck) o Líder da Mudança deve marcar a opção correspondente. 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 6 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
O critério a ser seguido para a indicação do tipo de RDM segue abaixo: 
- Emergencial: execução fora de uma janela padrão de manutenção; 
- Programada: execução dentro de uma janela padrão de manutenção; 
- Padrão: 
 - Execução dentro de uma janela padrão de manutenção; e 
 - Todos os ativos envolvidos na mudança contam com backup regular testado e disponível para restauração imediata; e 
 - Atividades integralmente implementadas através de ferramenta auditável de gerenciamento de configuração; e 
 - Indisponibilidade prevista menor ou igual a 60 minutos, incluindo a execução do plano de rollback. 
Se a RDM for classificada como emergencial a explicação dessa necessidade deve estar registrada no campo Motivação. 
A RDM só evoluirá para o estado Planejada depois que todos os campos da RDM forem preenchidos. Quando for o caso, deve ser registrada a expressão: N/A – Não se Aplica. 
Estado da RDM ao final da atividade: **Planejada** 
## **9.3. Pautar a RDM – Gerente de Mudanças** 
A condição para executar essa atividade é a RDM estar no estado: **Planejada** 
O Gerente de Mudanças deve conferir o preenchimento da RDM, sobretudo a consistência das informações registradas na seção detalhamento. Em especial os campos que serão utilizados pelas áreas de gestão (CGTI, COINF e COSIS) nas suas tomadas de decisão: benefícios esperados (tecnologia e negócio), riscos tratados (tecnologia), e classificação (tipo e categoria). 
Em especial verificar se os critérios do item 9.2.4 estão presentes nas RDM classificadas com 
tipo: Padrão pelo Líder da Mudança. 
Caso uma RDM tenha sido classificada como Padrão, ao ser pautada pelo Gerente de Mudanças o processo de Autorização Expressa será iniciado. 
O processo de Autorização Expressa envia pedido de autorização a todos os donos de serviços afetados pelos itens de configuração citados no inventário. Se todos os donos aprovarem a mudança, ela será agendada para a próxima janela padrão de manutenção disponível. 
Estado da RDM ao final da atividade: 
- **Nova** – caso seja identificada informação incorreta, imprecisa, inadequada ou imprópria; 
- **Planejada** – caso seja considerada válida, mas ainda não seja o momento de executá-la; 
- **Pautada** – caso seja considerada válida e no momento adequado para execução. 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 7 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
## **9.4. Autorizar a execução da RDM – Comitê Consultivo de Mudança e Emergências** 
A condição para executar essa atividade é a RDM estar no estado: **Pautada ou Agendada** 
Existem dois fluxos de agendamento possíveis para uma RDM: 
- RDM programada sempre terá seu agendamento autorizado pelo CCME, 
- RDM emergencial sempre terá seu agendamento autorizado pelo CCME, e 
- RDM padrão terá seu agendamento autorizado preferencialmente pelos donos de serviços afetados pelos itens de configuração citados no inventário, mas também pode ter seu agendamento, ou reagendamento, autorizado pelo CCME se ainda estiver no estado pautada ou agendada quando ocorrer a reunião do CCME. 
A decisão se dá por maioria simples dos votos dos participantes da reunião do CCME. E os votos podem ser registrados individualmente, sem a necessidade de uma reunião presencial, ou diretamente na RDM pelo Gerente de Mudanças, quando a decisão ocorrer de forma coletiva em reunião, seja ela virtual, presencial ou híbrida. 
Caso, durante as reuniões, ordinárias ou extraordinárias, não seja possível obter os votos dos membros do CCME, o Gerente de Mudanças pode decidir sozinho pela aprovação ou pela reprovação. 
Estado da RDM ao final da atividade: 
- **Agendada** – quando a RDM for aprovada pelo CCME; 
- **Planejada** – quando a RDM não for aprovada, mas puder ser pautada novamente; 
- **Nova** – quando a RDM não for aprovada, e precisar de ajustes no planejamento antes de ser pautada novamente; 
- **Cancelada** – quando a RDM não for aprovada, e não houver interesse em pauta-la novamente. 
## **9.5. Comunicar sobre a programação de mudanças – Gerente de Mudanças** 
O Gerente de Mudanças deve manter um calendário de mudanças acessível a todos os interessados autorizados a visualizar o calendário de mudanças da CGTI. 
O Gerente de Mudanças deve zelar pela atualização do calendário registrado, garantindo que 
esteja fidedigno. 
O Gerente de Mudanças também é responsável por executar o plano de comunicação de cada RDM, sendo assim, o Gerente de Mudanças deve comunicar os interessados (os envolvidos na execução da mudança e os donos de serviços afetados pelos itens de configuração citados no inventário), preferencialmente por e-mail, sobre a expectativa de indisponibilidade dos serviços afetados pelas mudanças. 
## **9.6. Coordenar a execução da RDM – Líder da Mudança** 
A condição para executar essa atividade é a RDM estar no estado: **Agendada** 
O Líder da Mudança realiza a coordenação da execução da RDM. Esse trabalho consiste em acompanhar as atividades técnicas, obter o feedback dos executores, acionar analistas e comunicar com o Gerente de Mudanças e os interessados sobre o andamento do trabalho. 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 8 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
A ferramenta oficial de comunicação entre os atores durante a execução da RDM é a sala Gerenciamento de Mudanças do Element. É nessa sala que o Líder da Mudança deve informar o início e o fim da execução da mudança, bem como qualquer fato relevante. 
Durante seu trabalho, os analistas devem comunicar ao líder se perceberem que o prazo de execução não será cumprido, além de qualquer evento não previstos relevante para o bom andamento da mudança. 
Em caso de imprevistos, cabe ao Líder da Mudança decidir pela execução ou não do Plano de Retorno, ou então pela extensão do prazo planejado para a RDM, limitado à janela de manutenção disponível. Ele pode consultar o Gerente de Mudanças para auxiliar na decisão, sempre utilizando o Element como meio de contato preferencial. 
## **9.6.1.** Executar atividades – Analista Executor 
Cabe ao analista executor executar as atividades determinadas no planejamento da mudança. O analista não deve alterar o escopo ou a finalidade da sua atividade. Caso haja algum imprevisto ou impedimento para a realização da atividade, o analista deve informar ao Líder da Mudança para que uma decisão seja tomada. 
É importante também indicar adequadamente informações e a conclusão da sua atividade para o bom andamento da RDM. Além da aplicação correta do conhecimento técnico, a comunicação entre os analistas e o Líder da Mudança é crucial para o seu sucesso. 
## **9.6.2.** Informar sobre a conclusão da RDM – Líder da Mudança 
Quando a última atividade técnica for executada ou seja impossível dar continuidade no plano de ação, o analista executor deve comunicar ao Líder da Mudança. Neste ponto, o Líder da Mudança deve então determinar se a RDM atingiu o seu objetivo executando o plano de teste. Se necessário, solicitar ajuda ao Requisitante. Caso a RDM tenha sido malsucedida, o Líder da Mudança também deve decidir se o Plano de retorno é necessário. 
## 9.6.2.1. Executar atividades de retorno 
Esta atividade só é executada se o Líder da Mudança tiver decidido que o Plano de retorno é necessário para o restabelecimento do ambiente operacional. A sua execução segue os mesmos princípios da execução das atividades do Plano de Implementação da RDM. 
A verificação do funcionamento do ambiente afetado na mudança deve ser realizada para garantir que o serviço foi disponibilizado adequadamente. 
Estado da RDM ao final da atividade: **Executada** 
## **9.7. Realizar a revisão pós-implementação – Gerente de Mudanças** 
A condição para executar essa atividade é a RDM estar no estado: **Executada** 
O Gerente de Mudanças tem um prazo de 2 dias para verificar os resultados alcançados pela RDM, e também se ocorreu algum impacto como incidentes ou alarmes não previstos. Nesse caso, os incidentes devem ser tratados e relacionados com a RDM. 
Estado da RDM ao final da atividade: 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 9 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
- **Concluída** – as atividades foram concluídas e o efeito desejado foi produzido; 
- **Revertida** – houve falha na execução de atividades ou o efeito desejado não foi alcançado, o plano de retorno foi executado. 
## **10. Indicadores do processo** 
- Quantidade de mudança por tipo; 
- Quantidade de mudança por categoria; 
- Quantidade de mudança por dia da semana; 
- Quantidade de mudança por etapa no ciclo de vida; 
 Taxa de sucesso, número de mudanças em estado concluída, dividido pelo somatório de mudanças nos estados: concluída, revertida e cancelada. 
## **11. Dono do documento** 
Rafael de Sant’Anna Corrêa Nunes, Analista de PGI em PI, DIINF/COINF/CGTI. 
## **12. Outro(s) elaborador(es) do documento** 
Renato Soares, colaborador, Digisystem (Coordenador de Infra) 
## **13. Aprovador(es) do documento** 
Gilberto Lima, chefe da DIINF/COINF/CGTI 
Arthur Samary, coordenador da COINF/CGTI 
## **14. Bibliografia** 
ITIL – Information Technology Infrastructure Library 
## **15. Histórico das alterações** 
** **
** **<br>
Nº da<br>Data Item e/ou Descrição<br>Revisão<br>0.0 01/10/2021 Emissão Inicial<br>Inclusão do critério relativo ao backup e ajuste do tempo de<br>** **<br>
|**Nº da**<br>**Revisão**<br>**Data**<br>**Item e/ou Descrição**|**Nº da**<br>**Revisão**<br>**Data**<br>**Item e/ou Descrição**|**Nº da**<br>**Revisão**<br>**Data**<br>**Item e/ou Descrição**|
|---|---|---|
|0.0<br>01/10/2021<br>Emissão Inicial|||
|||Inclusão do critério relativo ao backup e ajuste do tempo de|
|1.0|18/04/2024|indisponibilidade considerando o rollback para considerar uma mudança<br>como padrão. Inclusão do anexo 2 – Ambientes Operacionais.<br>Alterações com o intuito de deixar o procedimento independente da<br>existência de um sistema ITSM. As atividades automáticas de<br>comunicação foram transformadas em atividades manuais sob a<br>responsabilidade do Gerente de Mudanças.<br>Inclusão da Requisição de Mudança v3.0 como Anexo 1.<br>Inclusão do Anexo 3 – Detalhes Operacionais de Implementação; revisão<br>do item 9 – fluxo de processo; inclusão do campo líder da mudança na<br>RDM – Anexo2.|
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 10 de 11** 
**Uso Interno** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI – STI – PP– 0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|18/04/2024|
||**GERENCIAMENTO DE MUDANÇAS**|**Processo**|Sustentação de TIC|
## **16. Anexos** 
Anexo 1 – RDM – Requisição de Mudança 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Página 11 de 11** 
**Uso Interno** 
REQUISIÇÃO DE MUDANÇA NA INFRAESTRUTURA EM PRODUÇÃO GETI – STI – FR – 0001 
** **
** **<br>
Código GETI – STI – FR – 0001<br>SISTEMA DE PADRONIZAÇÃO DO INPI<br>Revisão 1.0<br>FORMULÁRIO<br>Elaboração 04/03/2024<br>REQUISIÇÃO DE MUDANÇA NA Aprovação 18/04/2024<br>INFRAESTRUTURA EM PRODUÇÃO Processo Sustentação de TIC<br>** **<br>
** **
** **<br>
HISTÓRICO DAS ALTERAÇÕES<br>N [o] da revisão Data Itens revisados<br>1.0 04/03/2024 Revisão total do documento<br>QUADRO DE RESPONSÁVEIS<br>Nome: Rafael de Sant’Anna Corrêa Nunes<br>Dono do documento Função ou cargo: Analista de PGI em PI<br>Divisão, Coordenação e/ou Diretoria: DIINF/COINF/CGTI/DIRAD<br>Nome: Renato Soares<br>Outro(s) elaborador(es) [1]<br>Função ou cargo: Colaborador<br>Divisão, Coordenação e/ou Diretoria:<br>Nome: Arthur Samary<br>Aprovador(es) [2] Função ou cargo: Coordenador da COINF<br>Divisão, Coordenação e/ou Diretoria: COINF/CGTI/DIRAD<br>Nome: Gilberto Lima<br>Aprovador(es) Função ou cargo: Chefe da DIINF<br>Divisão, Coordenação e/ou Diretoria: DIINF/COINF/CGTI/DIRAD<br>** **<br>
|DATA DE<br>APROVAÇÃO||||Assinatura do<br>Gestor de Mudança||
|---|---|---|---|---|---|
|||||||
|||||**DETALHAMENTO**||
|**ALINHAMENTO**<br>**ESTRATÉGICO**||PDTIC||INCIDENTE, PROBLEMA OU<br>REQUISIÇÃO NOITSM||
|**EXECUÇÃO**||Início<br>(data e hora)||Fim<br>(data e hora)<br>Tempo de<br>Indisponibilidade||
|**NOME**<br>Descrição resumida da mudança;<br>Tende a resumir seu propósito, ou<br>descreve sua atividade principal;||||||
|**REQUISITANTE**||NOME||UNIDADE||
|||E-MAIL||RAMAL||
|||MATRÍCULA||ASSINATURA<br>DIGITAL||
|**JUSTIFICATIVA**<br>Por que a mudança é necessária?<br>O que acontece se não mudarmos?||||||
|**BENEFÍCIOS**<br>**ESPERADOS**||TECNOLOGIA|| Atualização<br> Correção<br>Implantação||
1 Replicar este campo conforme o no de elaboradores. 
No caso de terceirizados, identificar como “colaborador(a)” no campo de “função ou cargo da pessoa”. 2 Replicar este campo conforme o no de aprovadores. 
1 de 4 
REQUISIÇÃO DE MUDANÇA NA INFRAESTRUTURA EM PRODUÇÃO GETI – STI – FR – 0001 
** **
** **<br>
 Melhorar a experiência do usuário<br> Aumentar a produtividade do INPI<br>NEGÓCIO<br> Economizar recursos<br> Habilitar novo serviço<br> Indisponibilidade<br>RISCOS<br>TECNOLOGIA  Atraso em projeto do PDTIC<br>TRATADOS<br> Desperdício de recursos<br>MOTIVAÇÃO<br>Por que precisa ser agora?<br>ESCOPO<br>O que vai ser mudado?<br>Onde será feita a mudança? Que ativos?<br>Que serviços?<br>RISCOS DA<br>EXECUÇÃO<br>É esperada alguma indisponibilidade<br>durante a execução?<br>Por quanto tempo?<br>Em que serviços?<br>Pode haver redução de performance?<br>Tipo  Padrão  Corretiva<br>Padrão - apenas quando estiver<br>CLASSIFICAÇÃO conforme item 9.2.4 do Procedimento  Programada Categoria  Adaptativa<br>de Gestão de Mudança. Nesse caso,<br>teremos 2 opções de tipo marcadas,  Emergencial  Evolutiva<br>prevalecendo o tipo: Padrão<br>** **<br>
2 de 4 
REQUISIÇÃO DE MUDANÇA NA INFRAESTRUTURA EM PRODUÇÃO GETI – STI – FR – 0001 
** **
** **<br>
PLANEJAMENTO<br>LÍDER DA MUDANÇA<br>Responsável pelo planejamento;<br>Responsável por coordenar a execução;<br>INVENTÁRIO<br>Lista os itens de configuração modificados;<br>Lista os serviços afetados;<br>ENVOLVIDOS<br>Lista das equipes executoras;<br>Lista nominal dos profissionais externos;<br>Incluir dados de contato.<br>PLANO DE AÇÃO<br>Agrupado por etapa, com duração prevista;<br>Separado por equipe e item de configuração;<br>Formato de passo a passo;<br>Receitas executáveis;<br>Incluindo link para os POPs;<br>PLANO DE TESTE<br>Zabbix, Dynatrace, etc não são suficientes?<br>Testes automatizados;<br>Receitas executáveis;<br>Critérios para o sucesso;<br>Gatilho para o Rollback.<br>PLANO DE RETORNO<br>(ROLLBACK)<br>Separado por equipe e item de configuração;<br>Formato de passo a passo;<br>Receitas executáveis;<br>Incluindo link para os POPs;<br> Não<br>AUDITÁVEL<br> Sim, integralmente implementada através de ferramenta auditável de gerenciamento de configuração (exemplo, Rundeck)<br>Caso a RDM seja classificada como auditável, e atenda aos demais requisitos (item 9.2.4)<br>Pedido de Autorização Expressa para seguir o fluxo de autorização expressa, enviar pedido de autorização a todos os donos<br>de serviços afetados pelos itens de configuração citados no inventário.<br>Uma vez agendada a execução, enviar comunicado para todos os donos de serviços afetados<br>Aviso de Agendamento pelos itens de configuração citados no inventário e para a DISTI solicitando a comunicação<br>geral nos casos onde a interrupção dos serviços externos ultrapassar 60 minutos.<br>Aviso de Execução Enviar comunicado para os envolvidos 15 min antes do início agendado.<br>Enviar comunicado para os envolvidos e os donos de serviços afetados pelos itens de<br>PLANO DE COMUNICAÇÃO Aviso de Encerramento configuração citados no inventário logo após a mudança ser considerada encerrada,<br>informando o estado final: concluída, revertida ou cancelada.<br>** **<br>
3 de 4 
REQUISIÇÃO DE MUDANÇA NA INFRAESTRUTURA EM PRODUÇÃO GETI – STI – FR – 0001 
## **RPI – REVISÃO PÓS-IMPLANTAÇÃO** 
**LIÇÕES APRENDIDAS** 
4 de 4