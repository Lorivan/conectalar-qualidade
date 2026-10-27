# Relatório Incremental de Qualidade — Sprints 1 e 2

**Projeto:** ConectaLar — Sistema de Gestão Condominial
**Data de atualização:** 27/10/2026
**Versão do relatório:** 1.0
**Escopo:** execução da Sprint 1, tratamento documental da Sprint 2 e registro do estado verificável do código.

> Este relatório distingue evidência observada, implementação presente no repositório e atividade que ainda depende de execução/validação. Não declara aprovação institucional nem aprovação final da Sprint 2. Nenhuma senha, token ou conteúdo de `.env` é reproduzido.

## 1. Controle de versões

| Versão | Data | Alteração | Evidência |
| --- | --- | --- | --- |
| 0.1 | 11/09/2026 | Planejamento inicial da avaliação, requisitos, riscos e quatro sprints. | Histórico Git; `docs/fase_01_qualidade_software.md`. |
| 1.0 | 27/10/2026 | Consolidação incremental das correções e evidências da Sprint 1; plano, distribuição proposta e estado inicial da Sprint 2. | Commit `b185c67` e arquivos em `sprint1_evidencias_e_patch/ev/`; este relatório. |

As datas e os commits acima são os observados no histórico local. Não há evidência de revisão/aceite por todos os integrantes ou pela instituição parceira.

## 2. Objetivo detalhado da Sprint 1

Estabelecer a linha de base de qualidade do ConectaLar, reproduzir defeitos prioritários, corrigir falhas de segurança e configuração justificadas por evidência, acrescentar regressões automatizadas e preservar rastreabilidade sem expor credenciais. O objetivo foi parcialmente alcançado: correções relevantes estão integradas e testadas; PostgreSQL foi consultado em modo somente de leitura, mas migração/fluxos no banco e validação no navegador seguem pendentes.

### Cronograma de qualidade em quatro períodos

O plano de qualidade divide o trabalho em quatro ciclos de duas semanas. O Git comprova atividade da Sprint 1 em 10–11/10/2026 e esta atualização encontra a Sprint 2 em andamento em 27/10/2026. As datas exatas de início/fim não foram registradas, portanto não são inferidas para os períodos seguintes.

| Período | Janela planejada | Foco | Estado e datas comprováveis |
| --- | --- | --- | --- |
| Sprint 1 | Semanas 1–2 | Diagnóstico, linha de base e correções prioritárias. | Atividade no Git em 10–11/10/2026; datas formais de início/fim não registradas. |
| Sprint 2 | Semanas 3–4 | Integração, validação e continuidade das correções. | Em andamento na atualização de 27/10/2026; datas formais não registradas. |
| Sprint 3 | Semanas 5–6 | Regressão, usabilidade e desempenho. | Planejada; datas reais a registrar pelo grupo. |
| Sprint 4 | Semanas 7–8 | Avaliação final, consolidação de evidências e entrega. | Planejada; datas reais a registrar pelo grupo. |

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
| Testes pytest | 18 passaram; cobertura total 85% (346 statements, 52 não cobertos). | 31 passaram; cobertura total 88% (347 statements, 41 não cobertos). | A suíte ganhou 13 casos; cobertura cresceu 3 pontos percentuais. Cobertura não equivale a ausência de defeitos. |
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
| D-03 | Feedback para status inválido/inexistente. | Reprodução antes não encontrou mensagem; teste atual confirma mensagem e não mutação. | Código/teste corrigidos; script/arquivo de reprodução pós precisa ser regenerado. |
| D-04 | Configuração de cookie sem `SameSite=Lax`. | Reprodução antes registrou `None`. | Corrigido; `Secure` é ativado em produção. Revisar apenas após configuração do ambiente alvo. |
| D-05 | Sem limite de tentativas de login. | Reprodução inicial encontrou respostas 200 em 30 tentativas. | Corrigido em código e teste (sexta tentativa 429); ainda falta comprovar storage compartilhado/Redis em implantação. |
| D-06 | `.env` e artefatos locais no índice Git. | Verificador antes contou 68 itens e detectou `.env`. | Arquivo removido do índice e regras de ignore adicionadas; verificar e rotacionar qualquer credencial real que tenha sido versionada. |
| D-07/D-08 | Codificação de requirements e vulnerabilidade de Werkzeug. | UTF-16; pip-audit apontou CVE em 3.1.8. | Requisitos regravados em UTF-8, versões fixadas e Werkzeug atualizado; auditoria pós sem vulnerabilidades conhecidas. |
| D-09 | Script de criação de usuário com risco de segredo fixo/ação destrutiva. | Commit dedicado altera o fluxo e protege operação. | Senha interativa e confirmação/controle implementados; segredo não registrado em evidências. |
| D-10 | Lint e cobertura insuficientes para regressões recentes. | 14 achados de flake8 e 18 testes na linha de base. | A evidência histórica pós registra Flake8 zerado e 31 testes; a execução atual coletou 27, diferença pendente de reconciliação. |

## 7. Gestão do Backlog do Projeto

O quadro externo não está disponível neste repositório; a tabela registra o estado verificável pelos commits/testes e explicita o que não foi confirmado no quadro.

| Item | Prioridade | Sprint | Estado verificável | Critério/pendência |
| --- | --- | --- | --- | --- |
| T01 — Usabilidade no navegador | Alta | 1–2 | Não executado/documentado. | Aplicar roteiro com participante autorizado, anonimizar observações e guardar evidência. |
| T02 — Login/cadastro e persistência | Alta | 1–2 | Cobertura automatizada em SQLite; PostgreSQL 12.14 e tabelas consultados sem escrita; `alembic_version` ausente. | Preparar banco/schema de teste, aplicar migração e executar fluxo em PostgreSQL sem dados reais. |
| M01 — D-01 método e CSRF | Alta | 1 | Corrigido/testado. | Fechado tecnicamente; sem aprovação global antecipada. |
| M02 — D-02 normalização de login | Alta | 1 | Corrigido/testado. | Fechado tecnicamente. |
| M03 — D-03 feedback/status | Alta | 1 | Teste e reprodução pós confirmam feedback e estado preservado. | Revalidar integração com PostgreSQL. |
| M04 — D-04 cookies | Alta | 1 | Código e reprodução local coerentes. | Verificação em implantação TLS fica para ambiente-alvo. |
| M05 — D-05 rate limit | Alta | 1–2 | Teste automatizado comprova HTTP 429 na sexta tentativa. | Confirmar `RATELIMIT_STORAGE_URI` compartilhado no ambiente real e registrar teste sem expor endpoint/segredo. |
| M06 — D-06…D-10 higiene, dependências e regressão | Alta | 1 | Correções e evidências em commits/arquivos. | Revisar rotação de segredo potencialmente exposto no histórico e manter auditoria recorrente. |
| Sprint 2 — integração/validação | Alta | 2 | Em andamento, sem aprovação. | Completar migração/fluxos PostgreSQL, navegador, regressão e revisão final; registrar decisão de aceite pela equipe. |

## 8. Melhorias realizadas ou propostas

**Realizadas e presentes no repositório:** atualização de status por POST protegido por CSRF, feedback para status inválido/inexistente, normalização de e-mail de login, rate limiting, política de cookies de sessão, higiene do Git, modelo `.env.example`, atualização de dependências, script de usuário sem senha fixa, testes de regressão, lint e workflow de qualidade.

**Propostas/continuidade:** validar o rate limiter com storage compartilhado; revisar a necessidade de rotação de credenciais que possam ter estado no histórico; executar a integração com PostgreSQL e o roteiro no navegador; atualizar README/documentação com as mesmas versões verificadas.

## 9. Repositório do Projeto

**Repositório configurado:** `https://github.com/Lorivan/conectalar-qualidade` (remote `origin`, observado no Git local em 27/10/2026).
**Branch observada:** `codex/security-quality-sprint1`; `HEAD` em `b185c67` (`Hardening and quality improvements for Sprint 1`).
**Evidências versionadas:** `sprint1_evidencias_e_patch/ev/`, incluindo `depois_reproducao_atualizada.txt`; código em `app/`, `tests/`, `migrations/`; este relatório em `docs/`.

O commit `b185c67` reúne a implementação observada da Sprint 1. Os commits anteriores incluem correções de regressão, higiene do repositório e dependências, conforme `commits.txt`. Não se assume que o remoto está atualizado com este `HEAD`; a verificação de envio/push não foi feita. `.env` não deve ser incluído, copiado ou exibido; usar `.env.example` apenas como modelo, com valores não secretos.

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

#### Problemas, defeitos e não conformidades identificados

- Script/saída pós de D-03 e D-05 foram atualizados; a configuração do storage compartilhado em produção continua pendente.
- PostgreSQL está acessível e possui as tabelas principais, mas não apresenta `alembic_version`; aplicação de migrações/fluxos não foi realizada nesta revisão.
- Não há resultado de navegação manual, revisão de participantes ou aceite coletivo; o helper encerrou a tentativa por incerteza sobre a URL atual.
- O segredo `.env` apareceu no índice antes da correção; remover o arquivo do estado corrente não revoga eventual credencial. Verificar e rotacionar, quando aplicável, sem copiar o valor para evidências.
- Distribuição real da Sprint 2 não consta em evidência; responsáveis deste plano são sugestões explícitas, não registro de execução.

#### Validação dos resultados e decisão

As correções automatizadas disponíveis sustentam a validação técnica individual dos cenários marcados como aprovados nas tabelas. O relatório não antecipa aprovação da Sprint 2: integração de migração e fluxos com PostgreSQL, execução em navegador, checagem de credenciais e revisão coletiva são condições ainda abertas. O aceite deve ser registrado após essas atividades por quem efetivamente as executar.

#### Retrospectiva da Sprint 2

**Estado nesta revisão:** Sprint 2 em andamento; ainda não há base factual para uma retrospectiva de sprint concluída. O que já se observa é que testes de regressão ajudam a distinguir defeito de falha do script de reprodução, e que rastreabilidade exige atualizar a evidência junto com a implementação. Ao encerrar a sprint, registrar fatos do trabalho executado, impedimentos encontrados, decisões tomadas e ações com responsáveis acordados — sem preencher retrospectiva como se essas atividades já tivessem ocorrido.

## 12. Retrospectiva da Sprint 1 e próximos passos

### Retrospectiva baseada no trabalho evidenciado

**Funcionou:** a reprodução dos defeitos priorizou correções objetivas; commits separados permitem rastrear parte das alterações; o pacote pós histórico registra 31 testes contra 18 na linha de base, com lint limpo e auditoria de dependências sem vulnerabilidade conhecida. A execução atual coletou 27 e requer conciliação.
**A melhorar:** manter script de reprodução sincronizado com mensagens e rate limiting; registrar responsável e evidência diretamente no quadro; preservar informação de credencial sem pressupor que removê-la do HEAD elimina exposição histórica.
**Aprendizado:** saídas automatizadas dependem de um critério de observação atualizado; quando houver conflito entre um script e um teste específico, é preciso investigar a asserção, não escolher silenciosamente um resultado.

### Próximos passos

1. Reconciliar a diferença entre 27 testes nesta execução e a evidência histórica de 31 testes.
2. Aplicar migração e fluxos em PostgreSQL isolado, com dados fictícios; primeiro definir banco/schema de teste.
3. Aplicar roteiro de navegador e registrar resultados sem dados pessoais.
4. Verificar configuração de storage compartilhado e avaliar rotação das credenciais potencialmente expostas no histórico, sem inserir segredos no relatório.
5. Confirmar com o grupo a distribuição real da Sprint 2 e completar retrospectiva/aceite após execução.
