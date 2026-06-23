** **
## **MINISTÉRIO DO DESENVOLVIMENTO, INDÚSTRIA, COMÉRCIO E SERVIÇOS INSTITUTO NACIONAL DA PROPRIEDADE INDUSTRIAL** 
## PORTARIA /INPI /DIRAD/CGTI Nº 3, DE 01 DE ABRIL DE 2024 
Publica o procedimento des�nado a guiar a implementação do processo de testes periódicos de restauração (restore) de dados digitais do INPI. 
## **O COORDENADOR-GERAL DE TECNOLOGIA DA INFORMAÇÃO DO INSTITUTO NACIONAL** 
**DA PROPRIEDADE INDUSTRIAL** , no uso das atribuições que lhe foram conferidas pelo Decreto nº 8.854, de 22 de setembro de 2016, e pela Portaria INPI PR nº 09, publicada em 13 de março de 2024, e tendo em vista no processo SEI nº 52402.014203/2023-59, 
## **RESOLVE:** 
**Art. 1º** Publicar na forma do anexo a esta Portaria o documento GETI–GSI–PP–0001, que versa sobre o procedimento des�nado a guiar a implementação do processo de testes periódicos de restauração (restore) de dados digitais do INPI, acompanhado do respec�vo formulário GETI–GSI–FR– 0002, que foram elaborados e revisados em conformidade com o Sistema de Padronização de Documentos, para alinhamento ao Manual do Sistema de Padronização de Documentos do INPI (GEQUGDS-MN-0001). 
**Art. 2º** Revogar a PORTARIA/INPI/CGTI Nº 02, DE 20 DE DEZEMBRO DE 2023 
**Art 3º** Esta Portaria entra em vigor na data de sua publicação. 
## **MARCUS VINICIUS DA MOTTA VIEIRA** 
Coordenador-Geral de Tecnologia da Informação 
** **
Documento assinado eletronicamente por **MARCUS VINICIUS DA MOTTA VIEIRA** , **Coordenador(a) Geral** , em 02/04/2024, às 11:32, conforme horário oficial de Brasília, com fundamento no art. 6º, § 1º, do Decreto nº 8.539, de 8 de outubro de 2015. 
** **
A auten�cidade deste documento pode ser conferida no site h�p://sei.inpi.gov.br/sei/controlador_externo.php? acao=documento_conferir&id_orgao_acesso_externo=0, informando o código verificador **0988948** e o código CRC **005973F4** . 
** **
** **
**Referência:** Processo nº 52402.014203/2023-59 
SEI nº 0988948 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|20/03/2024|
||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**|**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
**Sumário 1. Responsável ................................................................................................................................... 1 2. Objetivo .......................................................................................................................................... 1 3. Abrangência ................................................................................................................................... 1 4. Documentos complementares ...................................................................................................... 1 5. Glossário ........................................................................................................................................ 1 6. Descrição dos processos ou atividades ...................................................................................... 5 7. Entradas do processo ................................................................................................................... 6 8. Saídas do processo ....................................................................................................................... 6 9. Fluxo do processo ......................................................................................................................... 6 10. Indicadores do processo ............................................................................................................. 6 11. Dono do documento .................................................................................................................... 7 12. Outro(s) elaborador(es) do documento ...................................................................................... 7 13. Aprovador(es) do documento ..................................................................................................... 7 14. Bibliografia ................................................................................................................................... 7 15. Histórico das alterações .............................................................................................................. 7 16. Anexos .......................................................................................................................................... 8** 
## **1. Responsável** 
Corpo funcional lotado na Coordenação de Infraestrutura, Suporte e Segurança da Informação (COINF) com acesso permitido à solução de backup do INPI. 
## **2. Objetivo** 
O objetivo deste documento é descrever e guiar a implementação do Processo de backup e testes periódicos de restauração (restore) de dados digitais do INPI, de modo a garantir a disponibilidade contínua da informação em tempo hábil, especialmente, em caso de perda de dados e/ou interrupção das operações normais da organização. 
## **3. Abrangência** 
Este procedimento aplica-se ao processo Gestão de Segurança da Informação, tendo impacto nos operadores e gestores responsáveis pela gestão da segurança da informação no INPI. 
## **4. Documentos complementares** 
Plano de Restore – Formulário GETI-GSI-FR-0001 
Plano Específico de Backup – Formulário GETI-GSI-FR-0002 
## **5. Glossário** 
Administrador de Backup: servidor ou colaborador do INPI responsável pelos procedimentos de configuração, execução, monitoramento e testes dos procedimentos de Backup e Restore; 
**Página 1 de 8** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|20/03/2024|
||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**|**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
Administrador do recurso: servidor ou colaborador do INPI responsável pela operação de determinados serviços ou equipamentos da Secretaria de Tecnologia da Informação e Comunicação; 
Ativo: qualquer dado, dispositivo, ou outro componente, tangível ou intangível, de um ambiente que dá suporte a atividades relacionadas à TI. 
Backup: cópia de segurança gerada para possibilitar o acesso ou recuperação futura dos dados pertinentes ao INPI, tem por finalidade garantir a recuperação contra desastres, falhas ou comprometimento da integridade, além de permitir o controle histórico, rastreabilidade, auditoria, retorno ao estado anterior, entre outros. O termo também pode ser associado ao processo de geração da cópia de segurança (ver Processo de Backup); 
Confidencialidade: garantia de que o acesso à informação seja obtido apenas por pessoas autorizadas; 
Disponibilidade: garantia de que os usuários autorizados obtenham acesso à informação e aos recursos correspondentes sempre que necessários; 
Dado: informação em formato digital que pode ser transmitida ou processada. Pode corresponder a documentos, imagens, softwares, dados propriamente ditos (arquivos, bancos de dados), conteúdo multimídia ou qualquer outro registro de conteúdo passível de armazenamento em algum tipo de mídia. 
Desfazimento de Mídia: processo de segurança para remoção de informação e sanitização de mídia quando do seu descarte; 
Disco: dispositivo para armazenamento não volátil de dados, podendo ser magnético (ex. discos rígidos), ótico (ex. CD/DVD), estado sólido (ex. Pen drive); 
Dispositivo de Backup/Restore: storage, disco ótico ou biblioteca de fitas nos quais os Backups são gravados e dos quais podem ser restaurados. 
Escopo do Backup: define que tipo de informação ou dado precisa de cópia de segurança (ex.: banco de dados, configurações de rede, sistema de arquivos etc.); 
Ferramenta de Administração de Backup e Restore: Conjunto de programas especializados no planejamento, identificação, processamento e controle de Backup e Restore; 
OTRS: software destinado a apoiar os processos e as necessidades de GSTI do INPI; 
**Página 2 de 8** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|20/03/2024|
||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**|**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
Frequência de Backup: define com que frequência um backup irá ocorrer (ex.: diária, mensal, anual), levando em consideração fatores de criticidade e disponibilidade; 
Gestão de Serviços de TI (GSTI/ITSM): corresponde ao acompanhamento e gerenciamento do ciclo de vida dos serviços de TI por meio de um conjunto de estratégias, metodologias, controles e ferramentas; 
GSTI - Gestão de Serviços de Tecnologia da Informação 
IEC - Comissão Eletrotécnica Internacional (em inglês: International Electrotechnical Commission) 
Integridade: salvaguarda da exatidão e completeza da informação e dos métodos de processamento; 
Informação: é o dado organizado ou processado de forma a possuir algum sentido; 
ISO - Organização Internacional para Padronização (em inglês: International Organization for Standardization) 
ITIL - Biblioteca de Infraestrutura de Tecnologia da Informação (em inglês: Information Technology Infrastructure Library) 
ITSM – Gestão de Serviços de Tecnologia da Informação (em inglês: Information Technology Service Management) 
Janela de Backup: Período de tempo requerido para a geração de um backup; 
Localização do Backup: local onde a mídia de backup deverá ser armazenada e conservada, geralmente em ambiente seguro, local (on-site) ou remoto (off-site), dependendo dos fatores de criticidade e disponibilidade; 
Mecanismo de Backup: indica se o processo de cópia será feito manualmente ou de forma automática através de um software de backup; 
Mídia: dispositivo físico, geralmente unidade de disco ou fita magnética, no qual efetivamente armazenam-se os dados; 
Mídia de Backup: mídia na qual um ou mais Backups estão armazenados. 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. **Página 3 de 8** 
**Uso Interno** 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|20/03/2024|
||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**|**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
Período de Retenção do Backup: período de tempo em que o conteúdo da mídia de backup deve ser preservado; 
Plano de Restore: documento que formaliza o planejamento e as características de um Restore; 
Política de Segurança da Informação: é um documento formal que representa o conjunto de ações, técnicas e boas práticas relacionadas ao uso seguro de dados no âmbito do INPI ; 
Processo de Backup: ato de copiar dados para dispositivos de Backup/Restore, buscando a preservação destes para eventuais consultas ou recuperações; 
Processo de Restore: ver Restore; 
PSI – Política de Segurança da Informação 
Rastreabilidade: capacidade de detalhar o histórico, a aplicabilidade ou a localidade de um item de dado através de informações previamente registradas; 
Requisição de Backup/Restore: solicitação formal de serviço de Backup ou Restore feita pelos usuários de TI do INPI ; 
Requisição de Serviço: solicitação formal de serviço feita pelos usuários de TI do INPI ; 
Requisito de Negócio: requisito de alto nível que explica alguma necessidade do negócio e justifica a execução de um ou mais procedimentos; 
Requisito de Segurança: requisito de alto nível que busca garantir a confidencialidade, integridade e/ou disponibilidade dos dados do INPI , conforme a Política de Segurança da Informação; 
Requisito Técnico: requisito que determina o que deve ser feito (requisito funcional) ou como deve ser feito (requisito não-funcional); 
Restauração: ver Restore; 
Restore: processo de restauração de dados armazenados em uma cópia de segurança (Backup) para um disco ou outra mídia através da qual possam ser acessados pelos usuários ou aplicações; 
**Página 4 de 8** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|20/03/2024|
||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**|**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
Servidor: Computador responsável por gerenciar e oferecer serviços para uma rede de computadores clientes. 
Servidor de Backup: Computador responsável por gerenciar e oferecer/gerenciar os serviços de Backup e Restore. 
Software de Backup: ver Ferramenta de Administração de Backup e Restore; 
Storage: Equipamento composto de unidades de discos magnéticos e/ou de estado sólido, especializado no armazenamento e disponibilização de grandes volumes de dados. 
TI - Tecnologia da Informação 
Tipo de Backup: define como os dados serão copiados da origem para o destino, sendo os 3 tipos principais - completo (full), incremental e diferencial. 
## **6. Descrição dos processos ou atividades** 
## **6.1 Definir Plano de Restore** 
- a) Identificar Requisitante 
- b) Definir escopo 
- c) Definir detalhamento técnico 
- d) Registrar informações sobre a mídia 
- e) Elaborar Plano de Restauração 
- f) Atualizar Requisição de Serviço 
- g) Armazenar no OTRS 
## **6.2 Analisar Características do Plano** 
- a) Ler Plano de Restore 
- b) Verificar escopo 
- c) Verificar detalhes técnicos 
- d) Elaborar DRI para alocar os recursos necessários 
- e) Alocar recursos necessários à execução do Plano de Restore. 
## **6.3 Executar Restauração** 
- a) Implementar o plano de restore 
- b) Executar restauração de arquivos/diretórios 
- c) Atualizar Requisição de Serviço d) Em caso de sucesso: gerado um extrato automatizado pela própria ferramenta de restore, confirmando a execução correta. 
- e) Em caso de falha: criar um relatório de acompanhamento de restore, no qual deverá constar a data, os horários de início e término, os objetos e os clientes de restore, a causa da falha, a ação corretiva adotada e qual parte da restauração ficou comprometida. 
**Página 5 de 8** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|
|||**Revisão**|1.0|
|||**Aprovação**|20/03/2024|
||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**|**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
## **6.4 Monitorar Restauração** 
Verificar os logs e os registros de atividades relacionadas ao sistema de restore a procura de falhas, erros, configurações incorretas e escassez de recursos de armazenamento. 
## **6.5 Executar ações corretivas** 
- a) Solicitar envio dos arquivos originais 
- b) Analisar registros de monitoramento 
- c) Verificar a possibilidade de arquivos corrompidos 
- d) Mudanças no subprocesso de execução de restore 
- e) Verificar as ferramentas utilizadas no subprocesso de execução de backup/restore 
## **6.6 Registrar resultados** 
- a) Agrupar as informações dos processos de backup/restore executados pelo plano b) Construir Relatório de registro de resultados, conforme Plano de Restore 
- c) Atualizar Requisição de Serviço 
- d) Comunicar resultados para o gestor de segurança da informação 
- e) Preencher o Plano Específico de Backup 
## **6.7 Periodicidade** 
Este procedimento deve ser executado no trimestralmente, ou com frequência superior por solicitação do Gestor de Segurança da Informação. 
## **7. Entradas do processo** 
Plano de Restore. 
## **8. Saídas do processo** 
Plano de Restore 
Plano Específico de Backup 
## **9. Fluxo do processo** 
Não disponível 
## **10. Indicadores do processo** 
|**Descrição**|Número de solicitações de backup atendidas pelo Processo de<br>gestão de restore de arquivos digitais.|
|---|---|
|**Processo**|Processo de cópias de segurança (backup) e de restauração<br>(restore)|
**Uso Interno** Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. **Página 6 de 8** 
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|---|
||||**Revisão**|1.0|
||||**Aprovação**|20/03/2024|
||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**||**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
||||||
|||de dados|||
|**Responsável pela medição**||Administrador de backup|||
|**Local da medição**||Núcleo de Infraestrutura|||
|**Instrumento de captação**||Por meio do sistema de gerenciamento de solicitações referenciado<br>neste processo|||
|**Periodicidade da medição**||Anual|||
|**Fórmula**||Número de solicitações de_Backup/Restore_atendidas no período<br>de<br>medição, nas quais:<br>Solicitações atendidas = Solicitações registradas, iniciadas e<br>finalizadas dentro do período de medição<br>Período de medição = ano civil (01 de janeiro a 31 de dezembro)|||
|**Meta**||Cinco (5)<br>OBS: metas para anos seguintes serão definidas na revisão deste<br>documento, após a obtenção dos resultados da primeira execução<br>do<br>processo.|||
## **11. Dono do documento** 
Walace de Aguiar Ferreira, chefe de divisão, PR/DIRAD/CGTI/COINF/DISEG 
## **12. Outro(s) elaborador(es) do documento** 
Não se aplica. 
## **13. Aprovador(es) do documento** 
Marcus Vinícius da Motta Vieira, Coordenador-Geral, PR/DIRAD/CGTI 
## **14. Bibliografia** 
Não aplicável. 
## **15. Histórico das alterações** 
**Página 7 de 8** 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. 
**Uso Interno** 
||||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>PROCEDIMENTO|**Código **|GETI–GSI–PP–0001|
|---|---|---|---|---|---|---|
||||||**Revisão**|1.0|
||||||**Aprovação**|20/03/2024|
||||**PROCEDIMENTO DE BACKUP E TESTES**<br>**PERIÓDICOS DE RESTORE**||**Processo**|Gestão de Segurança<br>da Informação<br>Nivel 2|
||||||||
||**Nº da**<br>**Revisão**||**Data**|**Item e/ou Descrição**|||
||1.0|20/03/2024||Inclusão do Plano específico de Backup|||
||0.0|31/08/2023||Emissão inicial|||
## **16. Anexos** 
Não se aplica. 
Não é indicada a impressão deste documento. Certifique-se da versão vigente no INPI Drive do SGQ. **Página 8 de 8** 
**Uso Interno** 
GETI–GSI–FR–0001 PLANOS DE RESTORE REVISÃO 0.0 
** **
|||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**Código**|**Código**|GETI–GSI–FR–0001|GETI–GSI–FR–0001|GETI–GSI–FR–0001|
|---|---|---|---|---|---|---|---|---|---|---|
|||||||**Revisão**||0.0|||
|||||||**Aprovação**||08/12/2023|||
|||**PLANOS DE RESTORE**||||**Processo**||Gestão da Segurança da<br>Informação<br>Nível 2|||
||||||||||||
|||**Identificação**|||||||||
|Identificação do Ativo ou Sistema:|||||||Núm. Plano:|||Data|
|Propósito da Requisição:|||||||||||
|Nome do Requisitante|||||||Número do Chamado o||u RDM||
|Telefone:|||Email:||||Lotação:||||
|||||**Descrição do Escopo**|||||||
||||||||||||
|||||**Lliã d Dd**|**Abi ilid**||||||
|**Tipo**||**Prioridade**||**ocazaço o ao a**|**mente utzao**||||**Requisitos Adicionais**||
|||||**ser Restaurado**|**para restauração**||||||
||||||||||||
|`☐`Teste Periódico<br>`☐`Emergencial<br>`☐`Requisição de<br>Mudança<br><br><br><br><br>`☐`OUtro<br>Descrição:||~~`☐`~~Crítica<br>`☐`Alta<br>`☐`Média<br>`☐`Baixa||~~`☐`~~Disco<br>`☐`Fita<br>Tamanho Verificado:<br>Em<br>MB:___________________<br>Por extenso:<br>_______________________<br>_______________________<br>________|~~`☐`~~Testes<br>`☐`Homologação<br>Justificativa:<br>:______________________<br>_______________________<br>_______________________<br>_______________________<br>~~_~~______________________<br>___________________||||**Necessita DRI**<br>`☐`SIM`☐`NÃO<br>**Necessita Plano de**<br>**Testes**<br>~~`☐`~~SIM`☐`NÃO||
Página 1 de 3 
GETI–GSI–FR–0001 PLANOS DE RESTORE REVISÃO 0.0 
** **
**Observações ou detalhes adicionais da preparação do Restore** 
** **
** **<br>
AVALIAÇÃO DO TESTE DE RESTORE<br>Plano de Testes Realizado Resultado do Teste de Restore Falhas Identificadas<br>☐ SIM ☐ APROVADO<br>☐ NÃO ☐ REPROVADO<br>☐ Não se Aplica<br>Análise Técnica<br>Conclusões e Recomendações<br>Nome Cargo/Função Assinatura<br>** **<br>
Página 2 de 3 
GETI–GSI–FR–0001 PLANOS DE RESTORE REVISÃO 0.0 
** **
||**APROVAÇÃO DO PLANO**|**APROVAÇÃO DO PLANO**||
|---|---|---|---|
|**Nome**|**Cargo/Função**|**Aprovação**|**Assinatura**|
|Walace de Aguiar Ferreira|Gestor de Segurança da Informação|`☐`SIM`☐`NÃO||
|||☐SIM☐NÃO||
|||☐SIM☐NÃO||
|||☐SIM☐NÃO||
Página 3 de 3 
GETI–GSI–FR–0002 PLANO DE BACKUP REVISÃO 0.0 
** **
** **
||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**Código**|GETI–GSI–FR–0002|
|---|---|---|---|
|||**Revisão**|0.0|
|||**Aprovação**|20/03/2024|
||**PLANOS DE BACKUP**|**Processo**|Gestão de Segurança<br>da Informação<br>Nível 2|
## **CONTROLE E REGISTRO DO SGQ** 
||**HISTÓRICO DAS ALTERAÇÕES**|**HISTÓRICO DAS ALTERAÇÕES**|**HISTÓRICO DAS ALTERAÇÕES**|
|---|---|---|---|
|**No da revisão**|**Data**||**Itens revisados**|
|0.0|20/03/2024||Emissão inicial|
|||||
|||**QUADRO DE RESPONSÁVEIS**||
|**Dono do documento**||**Nome:**Walace de Aguiar Ferreira<br>**Função ou cargo:**Gestor de Segurança da Informação<br>**Divisão, Coordenação e/ou Diretoria: DISEG/CGTI**||
|**Outro(s) elaborador (es)1**||**Nome:**Rafael Bandeira Boabaid Rego<br>**Função ou cargo:**Técnico em PI<br>**Divisão, Coordenação e/ou Diretoria: DISEG/CGTI**||
|**Aprovador(es)2**||**Nome:**Marcus Vinícius da Motta Vieira<br>**Função ou cargo:**Coordenador Geral de Tecnologia da<br>Informação<br>**Divisão, Coordenação e/ou Diretoria: CGTI/DIRAD**||
Página 1 de 4 
GETI–GSI–FR–0002 PLANO DE BACKUP REVISÃO 0.0 
** **
||||**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**SISTEMA DE PADRONIZAÇÃO DO INPI**<br>FORMULÁRIO|**Código**|**Código**|GETI–GSI–FR–0002|GETI–GSI–FR–0002|GETI–GSI–FR–0002|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||**Revisão**||0.0|||
|||||||||**Aprovação**||20/03/2024|||
||||**PLANOS DE BACKUP**|||||**Processo**||Gestão de Segurança<br>da Informação<br>Nível 2|||
||||||||||||||
||||**Identificação**||||||||||
|Identificação do Ativo ou Sistema:|||||||||Núm. Plano de Backup:|||Data|
|Propósito da Requisição:|||||||||||||
|Nome do Requisitante|||||||||Número do Chamado ou DRI:||||
|Telefone:||||||Email:|||Lotação:||||
|**Descrição do Escopo**|||||||||||||
||||||||||||||
||||||**Frequência**||||**Período de**||||
|**Classe**||**Prioridade**|||||**Tipo**||**Retenção**||**Requisitos Adicionais**||
|`☐`Periódico<br>`☐`Emergencial<br>`☐`Condicional<br>Motivação:||~~`☐`~~Crítica<br>~~`☐`~~Alta<br>`☐`Média<br>`☐`Baixa||~~`☐`~~Diário<br>~~`☐`~~Semanal<br>`☐`Mensal<br>`☐`Anual|||~~`☐`~~Diário<br>~~`☐`~~Semanal<br>`☐`Mensal<br>`☐`Anual|Valor:<br>_______________<br>Por extenso:<br>___________________<br>___<br>`☐`Dias<br>`☐`Meses<br>`☐`Anos|||~~**C**~~**riptografia**<br>~~`☐`~~SIM`☐`NÃO<br>**Compactação**<br>~~`☐`~~SIM`☐`NÃO||
|||||||||**Período de**||
|---|---|---|---|---|---|---|---|---|---|
|**Classe**||**Prioridade**||**Frequência**||**Tipo**||**Retenção**|**Requisitos Adicionais**|
|`☐`Periódico|~~`☐`~~Crítica||~~`☐`~~Diário|||~~`☐`~~Diário||Valor:||
|||||||||_______________|~~**C**~~**riptografia**|
|`☐`Emergencial|~~`☐`~~Alta||~~`☐`~~Semanal|||~~`☐`~~Semanal|||~~`☐`~~SIM`☐`NÃO|
|||||||||Por extenso:||
|`☐`Condicional|`☐`Média||`☐`Mensal|||`☐`Mensal||___________________||
|Motivação:||||||||___|**Compactação**|
||`☐`Baixa||`☐`Anual|||`☐`Anual|||~~`☐`~~SIM`☐`NÃO|
|||||||||`☐`Dias||
|||||||||`☐`Meses||
|||||||||`☐`Anos||
Página 2 de 4 
GETI–GSI–FR–0002 PLANO DE BACKUP REVISÃO 0.0 
** **
** **
** **<br>
Observações<br>Forma de armazenamento Local de armazenamento Cadastramento na solução de Backup<br>☐ Disco<br>Valor: _______________<br>☐ Fita<br>Justificativas / Observações<br>Nome Cargo/Função Aprovação Assinatura<br>☐ SIM ☐ NÃO<br>** **<br>
Página 3 de 4 
GETI–GSI–FR–0002 PLANO DE BACKUP REVISÃO 0.0 
** **
||**APROVAÇÃO DOS PLANOS**|**APROVAÇÃO DOS PLANOS**||
|---|---|---|---|
|**Nome**|**Cargo/Função**|**Aprovação**|**Assinatura**|
|||`☐`SIM`☐`NÃO||
|||☐SIM☐NÃO||
|||☐SIM☐NÃO||
|||☐SIM☐NÃO||
Página 4 de 4