# 🏢 ConectaLar - Sistema de Gestão Condominial

Bem-vindo ao **ConectaLar**!

Este projeto é um **MVP (Produto Mínimo Viável)** desenvolvido como atividade de extensão para a disciplina de Programação Web Aplicada da UniEvangélica.

O sistema tem como objetivo **digitalizar e centralizar o registro de ocorrências** dos moradores do **Condomínio Casas Flamboyant**, trazendo mais organização, transparência e eficiência na comunicação com a administração.

---

## 📌 MVP documentado

A documentação completa do Produto Mínimo Viável está disponível em:

- [`docs/mvp.md`](docs/mvp.md)
- [`docs/primeira_entrega.md`](docs/primeira_entrega.md) — documento-base da primeira entrega, com diagnóstico, requisitos, backlog, arquitetura e planejamento das sprints.

O documento descreve:

- funcionalidades entregues;
- tecnologias utilizadas;
- páginas e rotas disponíveis;
- limitações do MVP;
- escopo recomendado para próximas evoluções.

Para o semestre de **Qualidade de Software**, o planejamento inicial de avaliação do MVP — requisitos de qualidade, métricas, problemas, riscos, testes e sprints — está em:

- [`docs/fase_01_qualidade_software.md`](docs/fase_01_qualidade_software.md)

---

## 🚀 Funcionalidades

### 🔐 Autenticação

- Login de usuários.
- Senhas armazenadas com hash PBKDF2 do Werkzeug; validação bcrypt é mantida para hashes legados.
- Controle de sessão.
- Logout.
- Redirecionamento de usuários não autenticados para a tela de login.

### 👥 Gestão de usuários

- Cadastro de moradores e usuários pelo síndico.
- Listagem de usuários cadastrados.
- Controle de acesso por perfil (**síndico** e **morador**).
- Validação de nome, e-mail, senha, unidade e tipo de usuário.
- Prevenção de cadastro duplicado por e-mail.

### 📋 Ocorrências

- Registro de ocorrências por usuários autenticados.
- Associação da ocorrência ao usuário autor.
- Visualização das ocorrências no painel principal.
- Controle de status pelo síndico:
  - Pendente;
  - Em Andamento;
  - Resolvido.

### 📊 Dashboard

- Ordenação por prioridade de status.
- Filtro por status.
- Busca por título ou descrição.
- Paginação de ocorrências.
- Cards com contadores por status e total geral.
- Datas formatadas para o fuso de Brasília.
- Interface responsiva com Bootstrap.

### 🔒 Segurança e operação

- Proteção CSRF para requisições mutáveis.
- Atualização de status e logout somente por POST com token CSRF.
- Limite de cinco tentativas de login por minuto; produção exige armazenamento Redis compartilhado.
- Endpoint de saúde: `GET /healthz`.
- Páginas de erro padronizadas para `400`, `403`, `404` e `500`.
- Configuração por variáveis de ambiente.
- Exigência de `SECRET_KEY` em produção.

---

## 🛠 Tecnologias utilizadas

- **Back-end:** Python 3.x, Flask, Flask Blueprints.
- **Banco de dados:** PostgreSQL, SQLAlchemy, Flask-SQLAlchemy, psycopg2.
- **Front-end:** HTML5, CSS3, Jinja2, Bootstrap 5, Bootstrap Icons.
- **Segurança:** bcrypt, CSRF customizado, controle de sessão Flask.
- **Configuração:** python-dotenv e variáveis de ambiente.
- **Produção:** Gunicorn.
- **Testes:** pytest.

---

## 🗺 Páginas disponíveis

| Página / recurso | Rota | Acesso |
| --- | --- | --- |
| Login | `/` | Público |
| Logout | `/logout` | Usuário autenticado |
| Dashboard | `/dashboard` | Usuário autenticado |
| Nova ocorrência | `/nova-ocorrencia` | Usuário autenticado |
| Atualizar status (POST) | `/atualizar-status/<id>/<novo_status>` | Síndico |
| Cadastro de usuário | `/cadastro` | Síndico |
| Lista de usuários | `/usuarios` | Síndico |
| Saúde da aplicação | `/healthz` | Técnico/monitoramento |

---

## ⚙️ Como rodar o projeto

### 1. Pré-requisitos

- Python 3.10+
- PostgreSQL instalado

### 2. Configuração do ambiente

No terminal, dentro da pasta do projeto:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Ativar ambiente (Linux/macOS)
source venv/bin/activate

# Instalar dependências de execução e qualidade
pip install -r requirements-dev.txt
```

### 3. Configuração do banco de dados

Crie um banco no PostgreSQL com o nome:

```text
conecta
```

Copie `.env.example` para `.env` e configure os valores locais. Gere uma chave aleatória para `SECRET_KEY`; não compartilhe nem versione o arquivo `.env`.

```env
cp .env.example .env
```

### 4. Execução

```bash
# Aplicar as migrações do banco
flask --app run db upgrade

# Criar usuário síndico interativamente, se necessário (somente ambiente local)
python criar_usuario.py

# Rodar o sistema
python run.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000/
```

## 🧪 Testes

Dependências de desenvolvimento/testes:

```bash
pip install -r requirements-dev.txt
```

Executar a suíte automatizada:

```bash
pytest
ruff check .
pip-audit -r requirements.txt
```

Em produção, defina `APP_ENV=production`, `SECRET_KEY`, os parâmetros do banco e `RATELIMIT_STORAGE_URI` apontando para armazenamento compartilhado, como Redis. A aplicação exige esse armazenamento para que a limitação de login funcione entre workers.

---

## 📚 Documentação das Sprints 3 e 4

Para responder aos pontos de melhoria da avaliação da Sprint 3 e preparar a Sprint 4, foram criados documentos de apoio com:

- documentação de envio da Sprint 3;
- visão da estrutura modular do projeto;
- roteiro para comprovar persistência no banco;
- matriz de rastreabilidade entre funcionalidade, commit e evidência;
- plano operacional para evoluir o sistema na Sprint 4.

Documentos:

- [`docs/sprint_03_documentacao_entrega.md`](docs/sprint_03_documentacao_entrega.md)
- [`docs/sprint_04_finalizacao_evidencias.md`](docs/sprint_04_finalizacao_evidencias.md)
- [`docs/sprint_04_plano_execucao.md`](docs/sprint_04_plano_execucao.md)
- [`docs/sprint_04_execucao_realizada.md`](docs/sprint_04_execucao_realizada.md)

## 📋 Relatório Incremental — Sprints 1 e 2

O relatório incremental da avaliação de qualidade reúne o controle de versões,
backlog, cenários de login/cadastro, evidências da Sprint 1 e o estado de
planejamento/validação da Sprint 2:

- [`docs/relatorio_incremental_sprint1_sprint2.md`](docs/relatorio_incremental_sprint1_sprint2.md)

---

## 🔒 Variáveis de ambiente para produção

Para executar em produção com segurança:

- `APP_ENV=production`
- `SECRET_KEY=<chave forte obrigatória>`
- `DEBUG=false`
- `AUTO_CREATE_DB=false`

> Em `APP_ENV=production`, a aplicação não inicia sem `SECRET_KEY` definida.

---

## 📈 Próximas melhorias

- Filtro por data.
- Upload de anexos nas ocorrências.
- Comentários e histórico de movimentações.
- Dashboard com gráficos.
- Notificações.
- API REST.
- Gestão administrativa avançada de usuários.
- Suporte a múltiplos condomínios.

---

## 👥 Equipe

- Lorivan Lino de Abreu
- Rafael Fortunato Rodrigues De Aquino
- Stephanie Wolff Silva
- Vinicius Maciel Azevedo

---

## 📌 Observações

Este projeto foi desenvolvido com foco em aprendizado prático e aplicação real de conceitos de desenvolvimento web, evoluindo de um MVP para uma base sólida de sistema.
# conectalar-qualidade
