# Evidências da Sprint 3

Esta pasta contém as saídas verificáveis dos testes automatizados executados em 14/11/2026.

| Arquivo | Conteúdo | Ambiente e limite |
| --- | --- | --- |
| `pytest_2026-11-14.txt` | Saída detalhada da suíte completa: 30 testes aprovados, comando, horário e revisão-base. | Flask test client com SQLite em memória. Não comprova execução no navegador nem no PostgreSQL. |
| `pytest_cenarios_rastreaveis_2026-11-14.txt` | Saída identificável de oito cenários de ocorrência, cadastro, CSRF, autorização e rate limit. | Mesmo ambiente local com SQLite em memória. |

Os três testes acrescentados na Sprint 3 estão em `tests/test_ocorrencias.py` e `tests/test_usuarios.py`. A revisão-base registrada é `4b407c7e1a3c30a0143a1914318d072d3c67d1fd`; os testes ainda precisam ser incluídos em um commit. Não há capturas do navegador ou evidência de persistência em PostgreSQL nesta pasta.
