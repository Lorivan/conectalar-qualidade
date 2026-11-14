# Relatório Incremental de Qualidade — Sprints 1, 2 e 3

**Projeto:** ConectaLar — Sistema de Gestão Condominial
**Data de atualização:** 14/11/2026
**Versão do relatório:** 4.0
**Escopo:** execução das Sprints 1 a 3, correções implementadas no código e evidências disponíveis para a avaliação de qualidade.

> **Resumo para o grupo:** na Sprint 3, a suíte automatizada ganhou verificações explícitas para criação e consulta de ocorrência e para e-mail duplicado. As evidências locais registram as proteções de CSRF, autorização e D-03. A validação integrada no navegador e no PostgreSQL de teste, a conferência de HTTPS/credenciais e a conversão final usando o template do AVA ainda dependem de evidências/arquivos que não estão disponíveis nesta cópia do projeto. A tabela da Seção 11.3 separa o que foi feito do que falta.
>
> Este relatório distingue evidência observada, implementação presente no repositório e atividade que ainda depende de execução/validação. Nenhuma senha, token ou conteúdo de `.env` é reproduzido.

### Leitura rápida para quem vai finalizar a entrega

| Situação | O que isso significa | Próximo responsável sugerido |
| --- | --- | --- |
| **Feito localmente** | Testes de criação/consulta de ocorrência, autenticação obrigatória e e-mail duplicado foram incluídos; a suíte completa passou com 30 testes. Os logs estão em `docs/evidencias/sprint-03/`. | Você revisa o código e mantém os testes no commit da Sprint 3. |
| **Falta validar em integração** | Ainda não há execução comprovada pelo navegador nem gravação/consulta no PostgreSQL de teste. | Você e o colega executam os fluxos juntos com dados fictícios e guardam telas/consultas. |
| **Falta reconciliar** | Há históricos de 31 e 27 testes; a execução atual teve 30. A revisão local contém 27 funções de teste antes das três novas, mas isso não comprova os nomes/condições das execuções antigas. | Colega procura as saídas antigas; vocês comparam nomes, revisão, ambiente e comando. |
| **Falta conferir no ambiente real** | HTTPS, cookies no deployment e storage compartilhado do rate limit não foram testados nesta execução. Credenciais exigem revisão segura separada. | Vocês verificam o ambiente implantado; nenhum segredo deve ir para o relatório. |
| **Falta fechar o arquivo de envio** | A entrega da Sprint 3 vence em **15/11/2026**. O texto Markdown está atualizado, mas o template DOCX do AVA não está disponível localmente e o link não abriu neste ambiente. O sumário/paginação do PDF não foi conferido. | Colega insere no template oficial e exporta/revisa o PDF quando o DOCX estiver disponível. |

**Ordem prática:** 1) anexar/obter o template do AVA e as datas oficiais; 2) fazer os fluxos integrados e salvar evidências; 3) comparar as execuções antigas; 4) confirmar responsáveis e cards no Kanban; 5) fechar o relatório, revisar o sumário e enviar o PDF.

## 1. Controle de versões

| Versão | Data | Alteração | Evidência |
| --- | --- | --- | --- |
| 0.1 | 11/09/2026 | Planejamento inicial da avaliação, requisitos, riscos e quatro sprints. | Histórico Git; `docs/fase_01_qualidade_software.md`. |
| 2.0 | 27/10/2026 | Entrega 02 (Sprint 1), conforme nomenclatura formalizada nesta revisão; data e evidências correspondem ao registro local disponível. | Commit `b185c67` e arquivos em `sprint1_evidencias_e_patch/ev/`. |
| 3.0 | 27/10/2026 | Relatório incremental da Sprint 2, com integração, cenários e pendências registrados. | Commit local `4b407c7` e este relatório. |
| 4.0 | 14/11/2026 | Execução documental e técnica da Sprint 3: novos testes, análise dos resultados, backlog e planejamento de conclusão. | Este relatório e `docs/evidencias/sprint-03/`. |

**Revisão de nomenclatura:** a versão 2.0 identifica formalmente a Entrega 02 (Sprint 1), a versão 3.0 o relatório da Sprint 2 e a versão 4.0 esta atualização da Sprint 3. A identificação e as datas foram regularizadas a partir do histórico local; a equipe deve confirmar a data efetiva em que cada versão foi enviada. Não há evidência de aceite institucional nesta cópia.

## 2. Objetivo detalhado da Sprint 1

Estabelecer a linha de base de qualidade do ConectaLar, reproduzir defeitos prioritários, corrigir falhas de segurança e configuração justificadas por evidência, acrescentar regressões automatizadas e preservar rastreabilidade sem expor credenciais. O objetivo foi parcialmente alcançado: correções relevantes estão integradas e testadas; PostgreSQL foi consultado em modo somente de leitura, mas migração/fluxos no banco e validação no navegador seguem pendentes.

### Cronograma de qualidade em quatro períodos

O plano de qualidade divide o trabalho em quatro ciclos de duas semanas. O Git comprova atividade da Sprint 1 em 10–11/10/2026 e esta atualização encontra a Sprint 2 em andamento em 27/10/2026. As datas exatas de início/fim não foram registradas, portanto não são inferidas para os períodos seguintes.

| Sprint | Período oficial do plano | Foco | Estado e datas comprováveis |
| --- | --- | --- | --- |
| Sprint 1 | Semanas 1–2 | Diagnóstico, linha de base e correções prioritárias. | Atividade no Git em 10–11/10/2026. |
| Sprint 2 | Semanas 3–4 | Integração, validação e continuidade das correções. | Em andamento no registro de 27/10/2026. |
| Sprint 3 | Semanas 5–6 | Regressão, usabilidade e desempenho. | Orientações do professor detalhadas na seção 13; datas de calendário não constam nos arquivos consultados. |
| Sprint 4 | Semanas 7–8 | Avaliação final, consolidação de evidências e entrega. | Planejada; datas de calendário não constam nos arquivos consultados. |

As semanas 1–2, 3–4, 5–6 e 7–8 são os quatro períodos do plano inicial (`docs/primeira_entrega.md`). O prazo de entrega da Sprint 3 é **15/11/2026**, informado pelo grupo. A Sprint 4 está prevista para **29/11/2026**, ainda a confirmar. As datas oficiais de início/fim dos períodos não aparecem nos arquivos disponíveis e não foram estimadas. A prorrogação da entrega da Sprint 2 para **01/11/2026** fica registrada separadamente, sem alterar o plano inicial.

## 3. Tarefas e cartões de qualidade

Os identificadores T01/T02 e M01–M06 abaixo representam o plano rastreável deste relatório; não há captura/exportação do quadro externo para comprovar estados ou responsáveis atribuídos nele.

| Card | Escopo/critério | Resultado documentado | Situação |
| --- | --- | --- | --- |
| T01 | Usabilidade: login, abertura e localização de ocorrência no navegador; observar conclusão e obstáculos. | Não há protocolo de participante, observação, captura ou execução manual anexada. | Pendente de validação manual; os testes Flask não substituem observação de usabilidade. |
| T02 | Fluxo integrado de autenticação/cadastro e persistência. | Testes automatizados cobrem login, cadastro válido/inválido, persistência SQLite em memória e autorização. Consulta somente de leitura confirmou PostgreSQL 12.14, banco `conecta` e tabelas `usuarios`/`ocorrencias`; tabela `alembic_version` ausente. | Parcial; servidor e tabelas confirmados, migração versionada e fluxo PostgreSQL não comprovados. |
| M01 | D-01: atualização de status não deve ocorrer por GET; mutação requer POST e CSRF. | GET retorna 405; POST sem CSRF retorna 400 sem alterar status; POST autorizado altera. | Corrigido e coberto por regressão. |
| M02 | D-02: aceitar e-mail com espaços/caixa diferente sem expor credenciais. | Evidência de reprodução: login com e-mail normalizado redireciona para dashboard. | Corrigido e coberto por regressão. |
| M03 | D-03: informar status inválido/ocorrência inexistente, sem modificar dado. | Teste e script corrigido confirmam flash “status inválido” e estado permanece `Pendente`. | Correção presente, teste e reprodução pós atualizados. |
| M04 | D-04: atributos de cookie coerentes com ambiente. | Inspeção reproduzida: `HttpOnly=True`, `SameSite=Lax`; `Secure=False` em desenvolvimento e habilitado em produção pelo código. | Implementado; comportamento de produção depende de configuração HTTPS real. |
| M05 | D-05: limitar tentativas de login e comprovar bloqueio. | Teste e script atual fazem seis tentativas inválidas: cinco HTTP 200 e a sexta HTTP 429, com IP reservado para documentação. Configuração de produção exige armazenamento compartilhado. | Correção presente e automatizada; validar Redis/infra de produção permanece pendente. |
| M06 | D-06 a D-10: higiene de repositório, dependências, script de usuário, regressões e estilo. | `.env` removido do índice e `.env.example` criado; requirements em UTF-8 e versões fixadas; script pede segredo interativamente; suíte e lint sem achados após. | Implementado conforme commits e evidências; revisão de rotação de credenciais ainda requerida. |

## 4. Cenários executados: login e cadastro

Resultados de código HTTP e conteúdo correspondem aos testes Flask atuais. “Observado” aqui significa execução automatizada, não teste no navegador.

| Fluxo | Entradas usadas (fictícias) | Comportamento esperado | Resultado observado | Situação |
| --- | --- | --- | --- | --- |
| Login válido | E-mail/senha de fixture de síndico, obtidos do fixture de teste; valor de senha não reproduzido. | Redirecionar para `/dashboard` e iniciar sessão. | HTTP 302; destino `/dashboard`. | Aprovado no teste automatizado. |
| Login com espaços/caixa | `  SINDICO@CONECTALAR.COM  ` e senha da fixture. | Normalizar o e-mail e autenticar. | HTTP 302 para `/dashboard`. | Aprovado no teste automatizado. |
| Login inválido | E-mail fictício existente na fixture e senha incorreta. | Permanecer no login e apresentar mensagem genérica. | HTTP 200 e mensagem “Email ou senha inválidos”. | Aprovado no teste automatizado. |
| Tentativas repetidas | Seis POST inválidos com IP reservado `198.51.100.42`, token CSRF de teste. | Permitir cinco no intervalo e limitar a seguinte. | Primeiras cinco HTTP 200; sexta HTTP 429. | Aprovado no teste automatizado; limite distribuído em produção não verificado. |
| Cadastro válido | `Maria Moradora`, `maria@example.com`, unidade fictícia `Casa 22`, tipo `morador`, senha fornecida à fixture/formulário sem registro no relatório. | Síndico cadastra e usuário persiste com perfil/unidade corretos. | HTTP 302; usuário encontrado no banco de teste com nome e tipo esperados. | Aprovado no teste automatizado. |
| Cadastro inválido | Nome de 1 caractere, e-mail malformado, senha curta, unidade vazia e tipo não permitido. | Rejeitar sem persistir e informar validação. | HTTP 400; mensagem de e-mail inválido; registro ausente. | Aprovado no teste automatizado. |
| Login sem usuário/sessão em rota protegida | GET `/dashboard` sem sessão. | Redirecionar para login. | HTTP 302 para `/`. | Aprovado no teste automatizado. |

Não foram encontrados registros de execução manual de cadastro/login por usuário final, então não são atribuídos resultados de usabilidade a esses casos.

## 5. Análises estáticas, dependências e verificações antes/depois

Os valores de linha de base e pós-correção abaixo foram transcritos dos arquivos de evidência. Ferramentas/versões não aparecem em todos os logs; por isso não se infere comparação de ambiente perfeitamente idêntico.

| Verificação | Antes | Depois | Contexto e interpretação |
| --- | --- | --- | --- |
| Testes pytest (histórico Sprint 1) | 18 passaram; cobertura total 85% (346 statements, 52 não cobertos). | A evidência pós Sprint 1 registra 31 aprovados/88%; a revisão Sprint 2 registrou 27; a reexecução Sprint 3 registrou 30 aprovados. | São execuções em revisões/configurações diferentes. A composição precisa ser comparada antes de inferir regressão ou cobertura. A execução detalhada Sprint 3 consta em `docs/evidencias/sprint-03/pytest_2026-11-14.txt`. |
| Flake8 | 14 ocorrências: espaçamento, imports não usados, EOF e imports fora de ordem. | 0 ocorrências registradas. | Correções de estilo reduzem ruído, mas não validam comportamento. |
| pip-audit | 1 vulnerabilidade conhecida: Werkzeug 3.1.8, CVE-2026-102598, correção 3.1.9. | “No known vulnerabilities found”. | Dependência atualizada/fixada no conjunto auditado; auditoria não cobre segredos, código próprio ou dependências fora do arquivo. |
| Bandit | `bandit-exit=0`. | `depois_bandit.txt` registra também `bandit-exit=0`. | Sem achados detectados pela configuração executada; não é certificação de segurança. |
| Radon | Média de complexidade B (6,75); maior bloco listado B (8) em validação de usuário. | Não há saída posterior no pacote de evidências. | Linha de base apenas; não afirmar melhoria de complexidade. |
| Reprodução D-01 a D-05 | D-01 GET alterava estado sem CSRF; D-02 e-mail em caixa diferente falhava; D-03 sem feedback; D-04 `SameSite=None`; D-05 30 tentativas sem bloqueio. | Reexecução atual: D-01 GET 405/estado Pendente; D-02 HTTP 302; D-03 POST HTTP 200, feedback verdadeiro e estado preservado; D-04 `SameSite=Lax`; D-05 `[200, 200, 200, 200, 200, 429]`. | Script e saída atuais coerentes com os testes. |
| Repositório/dependências | `antes_repo.txt` registra 68 itens indexados, incluindo `.env`; `requirements.txt` em UTF-16 e dependência Werkzeug vulnerável. | `depois_repo.txt` registra 0 itens sensíveis identificados pelo verificador; arquivo de requisitos ASCII/UTF-8; pip-audit sem vulnerabilidade conhecida. | Saídas do verificador não são prova de rotação de segredos. O `.env` removido pode ter sido exposto historicamente no Git. |

## 6. Problemas, defeitos e não conformidades

| ID | Achado | Evidência/impacto | Estado e ação |
| --- | --- | --- | --- |
| D-01 | Alteração de estado por GET e sem CSRF. | Reprodução antes: GET sem CSRF alterava status. | Corrigido com POST e CSRF; teste de regressão preserva estado em GET/POST inválido. |
| D-02 | Login sensível à caixa/espaços do e-mail. | Reprodução antes retornava HTTP 200 em vez de 302. | Corrigido com normalização; teste automatizado aprovado. |
| D-03 | Feedback para status inválido/inexistente. | Reprodução antes não encontrou mensagem; teste atual confirma mensagem e preservação do estado. | Código/teste corrigidos; `sprint1_evidencias_e_patch/ev/depois_reproducao_atualizada.txt` registra a execução posterior. A validação integrada continua pendente. |
| D-04 | Configuração de cookie sem `SameSite=Lax`. | Reprodução antes registrou `None`. | Corrigido; `Secure` é ativado em produção. Revisar apenas após configuração do ambiente alvo. |
| D-05 | Sem limite de tentativas de login. | Reprodução inicial encontrou respostas 200 em 30 tentativas. | Corrigido em código e teste (sexta tentativa 429); ainda falta comprovar storage compartilhado/Redis em implantação. |
| D-06 | `.env` e artefatos locais no índice Git. | Verificador antes contou 68 itens e detectou `.env`. | Arquivo removido do índice e regras de ignore adicionadas; verificar e rotacionar qualquer credencial real que tenha sido versionada. |
| D-07/D-08 | Codificação de requirements e vulnerabilidade de Werkzeug. | UTF-16; pip-audit apontou CVE em 3.1.8. | Requisitos regravados em UTF-8, versões fixadas e Werkzeug atualizado; auditoria pós sem vulnerabilidades conhecidas. |
| D-09 | Script de criação de usuário com risco de segredo fixo/ação destrutiva. | Commit dedicado altera o fluxo e protege operação. | Senha interativa e confirmação/controle implementados; segredo não registrado em evidências. |
| D-10 | Lint e cobertura insuficientes para regressões recentes. | 14 achados de flake8 e 18 testes na linha de base. | Evidência histórica pós registra Flake8 zerado e 31 testes; revisões posteriores registraram 27 e 30. A composição das execuções ainda precisa ser comparada. |

## 7. Gestão do Backlog do Projeto

O quadro externo não está disponível neste repositório; a tabela registra o estado verificável pelos commits/testes e explicita o que não foi confirmado no quadro.

| Item | Prioridade | Sprint | Estado verificável | Critério/pendência |
| --- | --- | --- | --- | --- |
| T01 — Usabilidade no navegador | Alta | 1–3 | Continua sem execução manual documentada; esta atualização não atribui resultado de usabilidade aos testes Flask. | Executar roteiro com participante autorizado, registrar tarefas/conclusões e anonimizar observações. |
| T02 — Login/cadastro e persistência | Alta | 1–3 | Testes automatizados em SQLite; novos casos e resultado da Sprint 3 na Seção 11.3. PostgreSQL 12.14/tabelas foram consultados anteriormente sem escrita. | Executar fluxo de cadastro/login no navegador e confirmar persistência no schema PostgreSQL de teste. |
| M01 — D-01 método e CSRF | Alta | 1 | Corrigido/testado. | Fechado tecnicamente; sem aprovação global antecipada. |
| M02 — D-02 normalização de login | Alta | 1 | Corrigido/testado. | Fechado tecnicamente. |
| M03 — D-03 feedback/status | Alta | 1–3 | Teste automatizado confirma mensagem para status inválido e estado preservado. | Revalidar pelo navegador e no banco PostgreSQL de teste. |
| M04 — D-04 cookies | Alta | 1 | Código e reprodução local coerentes. | Verificação em implantação TLS fica para ambiente-alvo. |
| M05 — D-05 rate limit | Alta | 1–2 | Teste automatizado comprova HTTP 429 na sexta tentativa. | Confirmar `RATELIMIT_STORAGE_URI` compartilhado no ambiente real e registrar teste sem expor endpoint/segredo. |
| M06 — D-06…D-10 higiene, dependências e regressão | Alta | 1 | Correções e evidências em commits/arquivos. | Revisar rotação de segredo potencialmente exposto no histórico e manter auditoria recorrente. |
| Sprint 2 — integração/validação | Alta | 2 | Relatório e execução técnica localizados; ainda sem evidência de aceite institucional. | Manter pendências de PostgreSQL, navegador e credenciais até comprovação. |
| S3-01 — rastreabilidade T03/RQ03 | Alta | 3 | Criação/consulta, atualização e autorização separados na Seção 11.3; novos testes registrados por ID. | Ligar os IDs a requisitos/cards reais no Kanban. |
| S3-02 — comparar suítes | Alta | 3 | Execução com 30 testes documentada; listas históricas de 31/27 casos não estão disponíveis para comparação completa. | Recuperar saídas antigas e comparar casos, revisão, ambiente e parâmetros antes de concluir regressão/cobertura. |
| S3-03 — execução integrada | Alta | 3 | Fluxos automatizados locais aprovados em SQLite; execução integrada em navegador/PostgreSQL não comprovada. | Realizar com dados fictícios e registrar tela, resultado e consulta ao mesmo banco. |
| S3-04 — implantação e credenciais | Alta | 3 | HTTPS e revisão de rotação de credenciais não comprovados nesta atualização. | Verificar ambiente publicado e histórico Git; não inserir segredos em logs ou relatório. |
| S3-05 — relatório e entrega | Alta | 3 | Seções 1, 7, 9 e 11.3 atualizadas no Markdown; prazo de entrega em 15/11/2026; template e PDF institucional indisponíveis nesta cópia. | Obter DOCX do AVA, completar estrutura/paginação e conferir o PDF final até o prazo. Sprint 4 prevista em 29/11/2026, a confirmar. |

## 8. Melhorias realizadas ou propostas

**Realizadas e presentes no repositório:** atualização de status por POST protegido por CSRF, feedback para status inválido/inexistente, normalização de e-mail de login, rate limiting, política de cookies de sessão, higiene do Git, modelo `.env.example`, atualização de dependências, script de usuário sem senha fixa, testes de regressão, lint e workflow de qualidade.

**Propostas/continuidade:** validar o rate limiter com storage compartilhado; revisar a necessidade de rotação de credenciais que possam ter estado no histórico; executar a integração com PostgreSQL e o roteiro no navegador; atualizar README/documentação com as mesmas versões verificadas.

## 9. Repositório do Projeto

**Repositório configurado:** `https://github.com/Lorivan/conectalar-qualidade` (remote local `origin`).
**Branch/revisão-base desta atualização:** branch `codex/security-quality-sprint1`, `HEAD` de referência `4b407c7e1a3c30a0143a1914318d072d3c67d1fd` (`style: clean report whitespace`). Os três testes acrescentados nesta Sprint 3 ainda estão como alterações locais e, portanto, não possuem commit próprio.
**Arquivos afetados:** `tests/test_ocorrencias.py`, `tests/test_usuarios.py` e este relatório. Evidências históricas estão em `sprint1_evidencias_e_patch/ev/`; a evidência de execução Sprint 3 ficará em `docs/evidencias/sprint-03/`.

O commit `b185c67` continua sendo a referência histórica para as correções da Sprint 1. A verificação de push/remoto e o commit de integração `577ae793` mencionado no feedback não puderam ser confirmados no histórico local disponível. Antes do envio, atualizem esta seção com o hash final após criar o commit e confirmem que ele está no remoto. Não incluam `.env`; usem `.env.example` como modelo e não reproduzam valores secretos.

## 10. Atividades de qualidade realizadas

- Reprodução documentada de D-01 a D-05 antes/depois.
- Análise de dependências com `pip-audit` e verificação estática com Flake8, Bandit e Radon.
- Adição de regressões de autenticação, autorização, CSRF, persistência e validação.
- Verificação de cobertura antes/depois e histórico de commits.
- Revisão de arquivos sensíveis, encoding de dependências e configuração de ambiente.
- Atualização de proteções de sessão, rate limiting, CSRF, gestão de senha e workflow de qualidade.

## 11. Relatório de execução das sprints

### 11.1 Sprint 1 — Diagnóstico e correções

As tarefas M01–M06 registram as correções e validações tecnicamente sustentadas neste relatório. A retrospectiva da Sprint 1 está na Seção 12; as evidências de antes/depois e commits estão em `sprint1_evidencias_e_patch/ev/`.

### 11.2 Sprint 2 — Integração, validação e continuidade

#### Objetivo detalhado

Integrar e validar as correções da Sprint 1 no ambiente de persistência alvo e em navegador real, fechar as evidências inconsistentes de D-03/D-05, revisar o gerenciamento de credenciais e avaliar login/cadastro, autorização e persistência sem antecipar aprovação do produto.

#### Planejamento e distribuição das atividades

O histórico disponível atribui os commits de Sprint 1 a Lorivan Lino Abreu, mas não comprova distribuição pactuada da Sprint 2. Para evitar atribuição fictícia, a distribuição abaixo é **proposta de trabalho**, pendente de confirmação pelo grupo:

| Atividade | Responsável sugerido | Entrega/critério |
| --- | --- | --- |
| Preparar PostgreSQL de teste, aplicar migrações e verificar persistência | Lorivan Lino Abreu | Versão do PostgreSQL, revisão da migração, fluxo de cadastro/ocorrência e consulta de persistência; nenhuma credencial no log. |
| Executar roteiro de login/cadastro e fluxo de ocorrência no navegador | Integrante a definir no grupo | Entradas fictícias, comportamento esperado/observado, HTTP/feedback e evidência anonimizada; sem declarar teste com usuário externo se não realizado. |
| Atualizar reprodução e evidências D-03/D-05; validar configuração de rate limit | Integrante a definir no grupo | Mensagem capturada no dashboard, limite após 5 tentativas e status do storage configurado; segredos omitidos. |
| Regressão, análise estática/dependências e consolidação do relatório | Lorivan Lino Abreu + revisão do grupo | Saídas datadas, backlog coerente e revisão coletiva registrada antes do aceite. |

#### Atividades de qualidade previstas e realizadas nesta atualização

**Realizadas nesta atualização:** revisão de código/commits, suíte atual (27 aprovados), reprodução D-01 a D-05 atualizada e consulta PostgreSQL somente de leitura, além da consolidação do backlog/cenários sem revelar senhas.
**A executar para concluir a Sprint 2:** aplicar/verificar migração e fluxos PostgreSQL em ambiente isolado, roteiro em navegador e confirmação da distribuição com o grupo. O controle de interface do navegador encerrou a tentativa por não conseguir determinar a URL atual com confiança.

#### Testes, análises e resultados

| Verificação | Resultado disponível | Estado |
| --- | --- | --- |
| Pytest atual | `27 passed` em 44,31 s nesta revisão. Evidência histórica anterior: 31 passed. | Aprovado nessa execução; reconciliar a diferença entre conjuntos/execuções ao reproduzir a evidência histórica. |
| Flake8 / Bandit | Não executáveis nesta `.venv` (`No module named flake8/bandit`). Saídas pós históricas registram Flake8 0 e Bandit exit 0. | Repetição pendente. |
| pip-audit | Comando iniciado, não concluiu e foi interrompido; evidência histórica pós registra sem vulnerabilidade conhecida. | Repetição pendente. |
| PostgreSQL + migração | Consulta somente de leitura confirmou PostgreSQL 12.14, banco `conecta` e tabelas de aplicação; `alembic_version` ausente. Nenhuma alteração foi feita. | Servidor/schema básico confirmados; migração e fluxos pendentes. |
| Navegador | Helper encerrou a inspeção por não conseguir determinar a URL atual com confiança. | Sem resultado de navegador; pendente. |
| D-03/D-05 | Testes atuais e reprodução atualizada verificam feedback sem mutação e 429 na sexta tentativa. | Validado em teste automatizado/reprodução isolada SQLite. |

#### Rastreabilidade dos cenários e execuções

T01, T02 e T03 identificam testes planejados, não uma execução única. Os códigos `S2-EX-xx` abaixo distinguem cenários executados. A referência de revisão do código consultada nesta atualização é `4b407c7` (HEAD local); a execução é pelo cliente de teste Flask com SQLite isolado, salvo indicação em contrário. As saídas completas disponíveis devem ser arquivadas junto à evidência indicada. Data/hora individual de execução e comando não foram registrados nas evidências disponíveis; preencher esses campos ao reexecutar, sem atribuir retroativamente uma data.

| Teste planejado / requisito | Execução e cenário | Data/hora | Versão/revisão | Ambiente e entrada | Esperado | Observado / evidência |
| --- | --- | --- | --- | --- | --- | --- |
| T01 — usabilidade de login e localização de ocorrência | S2-EX-01 — tentativa de inspeção automatizada da interface | Não registrada | `4b407c7` (revisão consultada) | Navegador; URL não pôde ser determinada com confiança | Executar roteiro e registrar observação | Não executado; sem evidência de navegador. Não confundir com teste Flask. |
| T02 — cadastro e persistência | S2-EX-02 — cadastro inválido demonstrado | Não registrada | `4b407c7` (revisão consultada) | Cliente Flask/SQLite em memória; nome de 1 caractere, e-mail malformado, senha curta, unidade vazia e tipo não permitido | Rejeitar, não persistir e apresentar validação | HTTP 400, mensagem de e-mail inválido, registro ausente; evidência automatizada. |
| T02 — cadastro e persistência | S2-EX-03 — campos obrigatórios; S2-EX-04 — duplicidade; S2-EX-05 — persistência PostgreSQL; S2-EX-06 — mensagens de validação no navegador | Não registradas | A registrar na reexecução | Navegador/PostgreSQL de teste; entradas fictícias | Rejeitar obrigatórios/duplicidade com mensagem clara; persistir cadastro válido no PostgreSQL | Sem comprovação integrada específica nesta revisão. Não inferir aprovação pelo cenário S2-EX-02. |
| T03 / RQ03 — criação e consulta de ocorrência | S2-EX-07 — criação de ocorrência e consulta no banco | Não registrada | A registrar na reexecução | Navegador/PostgreSQL de teste; usuário e dados fictícios | Criar ocorrência e confirmar consulta/persistência | Testes isolados não comprovam fluxo integrado no PostgreSQL; pendente. |
| T03 / RQ03 — atualização de status | S2-EX-08 — método GET; S2-EX-09 — POST sem CSRF válido; S2-EX-10 — status inválido (D-03) | Não registrada | `4b407c7` (revisão consultada) | Cliente Flask/SQLite em memória; status e token controlados pelo teste | GET não muta; CSRF inválido rejeitado; status inválido informa erro e preserva estado | GET HTTP 405; POST sem CSRF HTTP 400; D-03 observado em teste isolado, resposta HTTP 200 e estado preservado. Revalidar integrado no navegador e banco. |
| T02 — autenticação / D-05 | S2-EX-11 — tentativas inválidas repetidas | Não registrada | `4b407c7` (revisão consultada) | Cliente Flask/SQLite em memória; seis tentativas inválidas | Limitar após cinco tentativas | Cinco respostas HTTP 200 e sexta HTTP 429; evidência automatizada. Storage compartilhado em produção segue pendente. |

**Identificadores de rastreio:** manter o ID planejado (T01/T02/T03 e RQ03) e usar também o ID de execução (S2-EX-xx). Em cada reexecução, preencher data/hora, hash completo, versão da aplicação, ambiente, comando, massa fictícia, resultado esperado/observado e caminho da saída. Associar cada linha ao defeito e ao card correspondente no quadro. Não declarar concluídos os cenários identificados como pendentes.

#### Problemas, defeitos e não conformidades identificados

- Script/saída pós de D-03 e D-05 foram atualizados; a configuração do storage compartilhado em produção continua pendente.
- PostgreSQL está acessível e possui as tabelas principais, mas não apresenta `alembic_version`; aplicação de migrações/fluxos não foi realizada nesta revisão.
- Não há resultado de navegação manual, revisão de participantes ou aceite coletivo; o helper encerrou a tentativa por incerteza sobre a URL atual.
- O segredo `.env` apareceu no índice antes da correção; remover o arquivo do estado corrente não revoga eventual credencial. Verificar e rotacionar, quando aplicável, sem copiar o valor para evidências.
- Distribuição real da Sprint 2 não consta em evidência; responsáveis deste plano são sugestões explícitas, não registro de execução.

#### Validação dos resultados e decisão

As correções automatizadas disponíveis sustentam a validação técnica individual dos cenários marcados como aprovados nas tabelas. O relatório não antecipa aprovação da Sprint 2: integração de migração e fluxos com PostgreSQL, execução em navegador, checagem de credenciais e revisão coletiva são condições ainda abertas. O aceite deve ser registrado após essas atividades por quem efetivamente as executar.

#### 11.2.9 Retrospectiva da Sprint 2

**Estado nesta revisão:** a Sprint 2 foi documentada como em andamento no registro de 27/10/2026. Abaixo, os quatro subtítulos seguem o template e separam os aprendizados observáveis dos itens que dependem de validação futura.

##### O que Funcionou Bem

- As verificações automatizadas registraram resultados objetivos para HTTP 429, HTTP 405 e rejeição de POST sem CSRF válido.
- A atualização da reprodução de D-03 permitiu observar feedback de erro e preservação do estado em cenário isolado.
- A execução atual de 27 testes e a evidência histórica de 31 foram preservadas como execuções distintas, sem afirmar equivalência entre elas.

##### O que Pode Melhorar

- Vincular cada execução a ID próprio, data, revisão completa, ambiente, entrada, esperado/observado e saída identificável.
- Completar os fluxos integrados em navegador e PostgreSQL; consulta inicial de conexão/tabelas não comprova gravação, consulta nem persistência dos fluxos.
- Comparar a composição e as condições das execuções de 31 e 27 testes antes de concluir sobre regressão ou cobertura.

##### Aprendizados da Sprint

- Um teste isolado valida a regra no contexto coberto, mas não substitui a comprovação integrada no navegador e no banco alvo. D-03 passou a apresentar feedback e preservar o estado no teste isolado; o fluxo integrado continua pendente.
- As execuções de 31 e 27 testes não podem ser comparadas apenas pelo total. É necessário comparar casos coletados, revisão, configuração e ambiente antes de atribuir diferença a regressão ou cobertura.
- Confirmar conexão e existência de tabelas no PostgreSQL documenta disponibilidade inicial do ambiente; comprovar o fluxo requer registro de execução e persistência nesse banco.

##### Ações para a Próxima Sprint

1. Revisar T03/RQ03 e registrar separadamente criação, consulta, atualização de status e controle de acesso.
2. Reexecutar cenários prioritários em revisão identificada, comparar composição das suítes de 31 e 27 testes e anexar saídas.
3. Validar cadastro, autenticação e ocorrências no navegador e PostgreSQL; registrar HTTPS e situação das credenciais em itens separados, sem expor segredos.
4. Atualizar versão formal, calendário, sumário e retrospectiva no arquivo institucional de entrega.

### 11.3 Sprint 3 — Regressão e avaliação dos efeitos das correções

#### Objetivo detalhado da sprint

Verificar se as correções e melhorias relatadas nas Sprints 1 e 2 continuam funcionando e se os fluxos de cadastro e ocorrências têm cobertura rastreável. A Sprint 3 acrescentou testes automatizados para criação seguida de consulta de ocorrência, bloqueio de criação sem autenticação e rejeição de e-mail duplicado. A execução completa local aprovou 30 testes. Esta validação usa o cliente de teste Flask e SQLite em memória; não representa teste de usabilidade no navegador ou execução integrada no PostgreSQL.

#### Planejamento e distribuição das atividades

Como o quadro Kanban e a divisão real da equipe não estão disponíveis no repositório, a tabela a seguir é uma proposta de execução. Confirmem responsável e prazo no quadro antes do envio.

| Atividade | Responsável sugerido | Entrega e critério de aceite |
| --- | --- | --- |
| Corrigir cobertura de cadastro/ocorrência e rodar a regressão local | Você / responsável pelo código | Testes nomeados por cenário; saída completa e revisão registradas. Concluído localmente nesta atualização. |
| Executar os fluxos no navegador e PostgreSQL de teste | Você + colega, em conjunto | Cadastro, autenticação, criação/consulta/atualização de ocorrência com massa fictícia; evidência de tela e consulta/persistência no mesmo banco. Pendente. |
| Atualizar as seções formais do relatório e conferir o PDF institucional até 15/11/2026 | Colega responsável pelo documento, com sua revisão | Seções 1, 7, 9 e 11.3 completas; sumário/paginação conferidos no template do AVA. O Markdown foi atualizado; template e PDF institucional dependem do arquivo DOCX do AVA. |
| Conferir HTTPS, credenciais e comparação das suítes | Revisão em dupla | HTTPS avaliado no ambiente de implantação; credenciais verificadas sem expor valores; listas de 31/27/30 testes comparadas por composição, revisão e ambiente. Pendente. |

#### Atividades de qualidade realizadas

- Revisados os casos existentes de autenticação, autorização, CSRF, rate limit, cadastro, criação de ocorrência e atualização de status.
- Acrescentado teste para confirmar que uma ocorrência criada pode ser consultada no dashboard e está associada ao autor no banco de teste.
- Acrescentado teste para confirmar que usuário sem sessão não cria ocorrência.
- Acrescentado teste para rejeitar e-mail duplicado sem criar segundo usuário.
- Executada a suíte completa com SQLite em memória. A saída textual e o hash-base estão em `docs/evidencias/sprint-03/pytest_2026-11-14.txt`.
- Atualizadas as Seções 1, 7 e 9 deste relatório e incluída a Seção 11.3 com resultados, limitações e próximos passos.

#### Testes e análises executados

**Correspondência entre plano e execução:** conforme a descrição do professor sobre a seção 6.3, `T03` foi planejado para registrar e consultar uma ocorrência. Os cenários de atualização de status, CSRF e status inválido são desdobramentos adicionais e devem ter IDs de execução próprios; eles não substituem a criação/consulta planejada. O feedback associa `RQ03` à revisão dos cenários de atualização, então esta atualização liga RQ03 a esses casos. A redação integral de RQ03 e a matriz original de requisitos não foram encontradas no workspace; o grupo deve conferir a descrição literal no documento institucional antes do envio.

| Referência do plano | Escopo planejado/associado | IDs de execução nesta atualização | Situação |
| --- | --- | --- | --- |
| T03 | Criar e consultar ocorrência | S3-EX-01; `test_nova_ocorrencia_valida_persiste_no_banco`; `test_nova_ocorrencia_criada_fica_disponivel_na_consulta_dashboard` | Criação e consulta verificadas em SQLite; integrado PostgreSQL/navegador pendente. |
| RQ03 | Atualização de status, conforme orientação do professor | S3-EX-04 a S3-EX-07 | Método, CSRF, estado inválido e autorização cobertos por testes locais; confirmar a redação integral de RQ03 e validar integrado. |
| Cenários adicionais ao T03 | Autenticação de acesso e proteção contra duplicidade no cadastro | S3-EX-02 e S3-EX-03 | IDs próprios e testes dedicados; SQLite em memória. |

| ID de execução | Cenário | Resultado esperado | Resultado observado | Ambiente/evidência |
| --- | --- | --- | --- | --- |
| S3-EX-01 | Criar ocorrência válida e consultá-la no dashboard, verificando o autor no banco | Criação redireciona; ocorrência aparece na consulta e persiste associada ao usuário autenticado | Aprovado na suíte; inclui gravação e consulta pelo cliente de teste | Flask test client + SQLite em memória; `tests/test_ocorrencias.py`; saída completa na evidência de pytest. |
| S3-EX-02 | Tentar criar ocorrência sem autenticação | Rejeitar/encaminhar ao login e não executar fluxo autenticado | Redirecionamento HTTP 302 para login; aprovado | Flask test client + SQLite em memória; `tests/test_ocorrencias.py`. |
| S3-EX-03 | Cadastrar e-mail já existente | Rejeitar com mensagem e manter apenas um registro | HTTP 400; uma ocorrência de usuário com o e-mail; aprovado | Flask test client + SQLite em memória; `tests/test_usuarios.py`. |
| S3-EX-04 | Atualização de status por GET | Não permitir mutação via GET | HTTP 405; caso já existente aprovado | Flask test client; `tests/test_ocorrencias.py`. |
| S3-EX-05 | POST de status sem CSRF válido | Rejeitar sem alterar o status | HTTP 400; estado permanece `Pendente`; caso já existente aprovado | Flask test client + SQLite em memória; `tests/test_ocorrencias.py`. |
| S3-EX-06 | Status inválido (D-03) | Informar erro e preservar o estado | Feedback de status inválido; estado permanece `Pendente`; caso já existente aprovado | Flask test client + SQLite em memória; `tests/test_ocorrencias.py`. |
| S3-EX-07 | Morador tenta atualizar status reservado a síndico | Negar acesso | HTTP 403; caso já existente aprovado | Flask test client; `tests/test_ocorrencias.py`. |
| S3-EX-08 | Seis logins inválidos | Bloquear a sexta tentativa | Cinco HTTP 200 e sexto HTTP 429; caso já existente aprovado | Flask test client; `tests/test_auth.py`; storage compartilhado de produção não exercitado. |
| S3-EX-09 | Suíte completa | Não haver falhas na regressão local | **30 passed em 90,31 s**, exit code 0 | Python do `.venv`, pytest, SQLite em memória; início 14/11/2026 19:01 -03:00; saída detalhada em `docs/evidencias/sprint-03/pytest_2026-11-14.txt`. |

**Comparação com execuções anteriores:** a evidência histórica informa 31 testes na Sprint 1 e o registro da Sprint 2 informa 27; a reexecução da Sprint 3 teve 30. A inspeção dos commits locais `b185c67` e `4b407c7` encontrou 27 definições de teste, mas não localizou a saída/lista da execução histórica de 31. Assim, o total 31 não pode ser reconciliado com a revisão disponível; não se conclui que houve regressão ou ganho/perda de cobertura. A nova execução adicionou três testes à base local de 27. O hash `4b407c7` é a revisão-base; as alterações de teste desta execução estão no working tree e ainda não têm commit.

#### Problemas, defeitos ou não conformidades identificados

- Não foi identificado novo defeito de implementação nos fluxos cobertos pelos testes existentes; as alterações desta Sprint 3 ampliam a verificação automatizada.
- A suite de 30 testes não exercita PostgreSQL, navegador real, deployment HTTPS ou armazenamento compartilhado do rate limiter.
- Não há evidência local das listas de testes coletados nas execuções históricas de 31 e 27 casos; a comparação permanece inconclusiva.
- O relatório institucional em DOCX e o template do AVA não estão no workspace. O acesso ao link falhou neste ambiente, então sumário, paginação e fidelidade do template não foram verificados.
- O prazo de entrega da Sprint 3 informado é 15/11/2026; a Sprint 4 está prevista para 29/11/2026, a confirmar. O calendário disponível especifica semanas 1–2, 3–4, 5–6 e 7–8, mas não contém datas oficiais de início/fim.
- A existência de um commit de integração `577ae793` foi relatada no feedback, mas esse hash não foi encontrado na cópia local do Git.

#### Melhorias e correções realizadas ou propostas

**Realizadas nesta Sprint 3:** três novos testes automatizados cobrem leitura após criação, autenticação no registro de ocorrência e unicidade de e-mail. Os testes são aditivos e não alteraram o comportamento da aplicação.

**Implementadas em ciclos anteriores e revalidadas pela suíte:** alteração de status somente por POST/CSRF, controle de acesso a síndico, retorno de erro para status inválido com preservação do registro, proteção de tentativas de login, validação de cadastro e persistência local em SQLite.

**Recomendações técnicas pendentes:** executar os mesmos cenários em banco PostgreSQL isolado e no navegador; comprovar consulta e persistência após reinício; testar HTTPS e cookies no ambiente publicado; confirmar storage compartilhado do rate limit; comparar as três execuções por nomes de testes e parâmetros. Essas verificações dependem do ambiente da equipe e não podem ser inferidas pela suíte SQLite.

#### Evidências contextualizadas

| Evidência | O que demonstra | Limite |
| --- | --- | --- |
| `docs/evidencias/sprint-03/pytest_2026-11-14.txt` | Comando, horário, revisão-base, ambiente e resultado da suíte completa (30 aprovados). | Não contém vídeo/capturas de navegador nem execução PostgreSQL. |
| `tests/test_ocorrencias.py` | Casos de criação, consulta no dashboard, autenticação, CSRF, método HTTP, status inválido e autorização. | Persistência é apenas SQLite em memória no fixture. |
| `tests/test_usuarios.py` | Cadastro válido/inválido, unicidade do e-mail e listagem paginada. | Não valida cadastro integrado no PostgreSQL ou interação humana no navegador. |
| `docs/evidencias/sprint-03/` | Pasta de evidências criada para logs e materiais da Sprint 3. | Capturas e saídas integradas devem ser incluídas pela equipe após execução. |

#### Validação dos resultados

O comando completo terminou com exit code 0 e 30 testes aprovados; a evidência registra revisão-base `4b407c7e1a3c30a0143a1914318d072d3c67d1fd`, horário e ambiente. Os novos testes verificam condições observáveis de criação/consulta e duplicidade. Os casos para HTTP 405, CSRF inválido, D-03, autorização e HTTP 429 também passaram dentro da mesma suíte. Isso sustenta a regressão automatizada em SQLite, mas não autoriza declarar a validação integrada de Sprint 3 concluída: faltam navegador, PostgreSQL, comparação das execuções históricas, HTTPS e revisão de credenciais.

#### Retrospectiva da Sprint 3

##### O que Funcionou Bem

- Os cenários adicionados verificam não só o status HTTP, mas também consulta e estado persistido em SQLite.
- A saída da regressão foi registrada com horário, comando, ambiente e revisão-base.
- As proteções de acesso, método, CSRF e rate limit existentes foram reexecutadas junto às novas verificações.

##### O que Pode Melhorar

- Associar cada cenário a card/critério de aceite real do Kanban e salvar as saídas como evidências individuais.
- Reexecutar em PostgreSQL de teste e navegador; automatização local em SQLite não comprova a integração do ambiente-alvo.
- Recuperar as listas originais das execuções com 31 e 27 testes para compará-las com a execução de 30.
- Obter o DOCX institucional e as datas oficiais para concluir sumário, paginação e calendário.

##### Aprendizados da Sprint

- Criar uma ocorrência e vê-la no dashboard testa uma relação diferente de apenas validar o POST; os dois passos precisam estar no cenário rastreável.
- Uma suíte maior/menor em quantidade não prova, isoladamente, regressão ou mudança de cobertura.
- O ambiente precisa ser parte da evidência: SQLite em memória valida regras locais e não demonstra gravação no PostgreSQL nem implantação HTTPS.

##### Ações para a Próxima Sprint

1. Executar cadastro, login e criação/consulta/atualização de ocorrência em navegador e PostgreSQL isolado; anexar capturas e consultas SQL anonimizadas.
2. Comparar casos e parâmetros das execuções de 31, 27 e 30 testes e documentar diferenças.
3. Validar cookies/HTTPS e rate limit com storage compartilhado no ambiente implantado; revisar credenciais do histórico sem expor valores.
4. Atualizar responsável, datas acordadas, hash final e estado real no Kanban e no relatório.
5. Inserir este conteúdo no DOCX institucional, atualizar sumário/paginação, exportar e revisar o PDF antes do envio.

## 12. Retrospectiva da Sprint 1 e próximos passos

### Retrospectiva baseada no trabalho evidenciado

**O que Funcionou Bem:** a reprodução dos defeitos priorizou correções objetivas; commits separados permitem rastrear parte das alterações; a evidência histórica registra 31 testes contra 18 na linha de base.
**O que Pode Melhorar:** manter script de reprodução sincronizado com mensagens e rate limiting; registrar responsável e evidência diretamente no quadro; preservar informação de credencial sem pressupor que removê-la do HEAD elimina exposição histórica.
**Aprendizados da Sprint:** saídas automatizadas dependem de um critério de observação atualizado; quando houver conflito entre um script e um teste específico, é preciso investigar a asserção, não escolher silenciosamente um resultado. A revisão Sprint 2 registrou 27 testes e a Sprint 3 registrou 30; não há comparação de composição completa com a evidência histórica de 31 para concluir regressão ou mudança de cobertura.
**Ações para a Próxima Sprint:** reconciliar as execuções; concluir validações integradas e manter rastreabilidade por cenário e versão.

### Próximos passos

1. Comparar a composição das evidências históricas de 31 e 27 testes com a execução Sprint 3 de 30 testes.
2. Aplicar migração e fluxos em PostgreSQL isolado, com dados fictícios; primeiro definir banco/schema de teste.
3. Aplicar roteiro de navegador e registrar resultados sem dados pessoais.
4. Verificar configuração de storage compartilhado e avaliar rotação das credenciais potencialmente expostas no histórico, sem inserir segredos no relatório.
5. Confirmar com o grupo a distribuição real da Sprint 2 e completar retrospectiva/aceite após execução.

## 13. Orientações do professor para a Sprint 3

Esta seção converte os comentários recebidos em tarefas verificáveis. Os itens abaixo são orientação do professor; responsável e prazo devem ser acordados no grupo e registrados no quadro, sem atribuir nomes ou datas não fornecidos.

| ID | Ação obrigatória | Evidência/critério de conclusão |
| --- | --- | --- |
| S3-01 | Revisar a relação entre T03, RQ03 e os cenários de atualização de status. Separar criação, consulta e atualização de ocorrências; registrar também o cenário de controle de acesso. | Matriz plano→cenário→execução→resultado, com pendências explicitadas. |
| S3-02 | Reexecutar cenários prioritários em uma versão identificada. Comparar a composição e as condições das execuções de 31 e 27 testes antes de falar em regressão ou cobertura. | Hash/revisão, data, ambiente, comando, lista/nome dos testes coletados e saída completa de cada execução. |
| S3-03 | Vincular cada saída ao defeito, card e critério de aceite; incluir evidências identificáveis de HTTP 429, proteção CSRF e D-03. | Saídas datadas, IDs de execução únicos e referências cruzadas no quadro/documento. |
| S3-04 | Completar testes integrados de cadastro, autenticação e ocorrências no navegador e PostgreSQL, usando dados fictícios e ambiente de teste. | Registro de execução da interface e evidência de gravação/consulta no PostgreSQL. A verificação de conexão/tabelas é apenas disponibilidade inicial. |
| S3-05 | Registrar separadamente verificação de implantação em HTTPS e situação das credenciais no histórico Git. | Resultado de HTTPS no ambiente implantado; revisão segura de credenciais/rotação, sem publicar valores secretos. |
| S3-06 | Corrigir relatório incremental: versões formais 2.0 e 3.0; sumário e paginação do PDF; retrospectiva nos quatro subtítulos; quatro períodos do cronograma e prorrogação da Sprint 2 em 01/11/2026 registrada à parte. | Relatório institucional atualizado, índice revisado após exportação para PDF e datas copiadas do calendário oficial da disciplina. |

**Divisão de trabalho sugerida para o grupo (confirmar no Kanban):** você pode conduzir S3-01 a S3-05, que dependem de código, reexecução e evidências técnicas; o outro integrante pode conduzir S3-06, atualizar o documento institucional e conferir sumário/paginação após exportar o PDF. Façam revisão cruzada dos resultados e combinem prazo/responsável antes de iniciar. Essa é uma proposta operacional, não uma atribuição já acordada.

### Checklist de saída da Sprint 3

- [ ] T03/RQ03 e criação, consulta, atualização e controle de acesso discriminados.
- [ ] Cada cenário executado tem referência única, versão, data, ambiente, entrada, resultado esperado/observado e evidência.
- [ ] Execuções de 31 e 27 testes comparadas por composição e condições.
- [ ] Fluxos de cadastro, autenticação e ocorrências executados no navegador e no PostgreSQL de teste.
- [ ] HTTPS e credenciais tratados em registros separados, sem valores secretos.
- [ ] Documento atualizado, sumário/paginação conferidos no PDF e prorrogação para 01/11/2026 indicada separadamente.
- [ ] Responsáveis e prazos acordados pelo grupo e atualizados no Kanban.
