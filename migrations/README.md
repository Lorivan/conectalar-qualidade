# Migrações (Flask-Migrate / Alembic)

A aplicação inicializa o Flask-Migrate em `app/__init__.py`. A revisão `20261011_0001` serve de baseline: cria as tabelas ausentes e não recria tabelas existentes. Para bancos já existentes, faça backup e valide o schema antes de registrar a revisão.

## Fluxo de desenvolvimento

```bash
flask --app run db migrate -m "describe schema change"
flask --app run db upgrade
```

Não use `db.create_all()` como substituto de migrações em produção.
