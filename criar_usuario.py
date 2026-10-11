"""Provisiona um usuário síndico sem senha padrão nem exclusão de dados."""

from getpass import getpass

from sqlalchemy.exc import SQLAlchemyError

from app import app, db
from app.models import Usuario
from app.services.auth_service import gerar_hash_senha


def main() -> int:
    if app.config.get('IS_PRODUCTION'):
        raise RuntimeError('Não execute este provisionador em produção.')

    nome = input('Nome do síndico: ').strip()
    email = input('E-mail do síndico: ').strip().lower()
    senha = getpass('Senha (mínimo 12 caracteres): ')
    confirmacao = getpass('Confirme a senha: ')

    if len(nome) < 3 or '@' not in email:
        raise ValueError('Nome ou e-mail inválido.')
    if len(senha) < 12 or senha != confirmacao:
        raise ValueError('A senha deve ter ao menos 12 caracteres e coincidir com a confirmação.')

    with app.app_context():
        if Usuario.query.filter_by(email=email).first():
            raise ValueError('Já existe usuário cadastrado com este e-mail.')
        db.session.add(Usuario(
            nome=nome,
            email=email,
            senha=gerar_hash_senha(senha),
            unidade='Administração',
            tipo='sindico',
        ))
        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            raise

    print('Usuário síndico criado com sucesso.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
