import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ['APP_ENV'] = 'testing'
os.environ['SECRET_KEY'] = 'test-secret-key'
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'
os.environ['AUTO_CREATE_DB'] = 'true'
os.environ['DEBUG'] = 'false'

import pytest

from app import create_app, db
from app.models import Usuario
from app.services.auth_service import gerar_hash_senha


@pytest.fixture()
def app():
    test_app = create_app()
    test_app.config.update(TESTING=True, RATELIMIT_ENABLED=False)

    with test_app.app_context():
        db.drop_all()
        db.create_all()
        yield test_app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def sindico(app):
    usuario = Usuario(
        nome='Síndico Teste',
        email='sindico@conectalar.com',
        senha=gerar_hash_senha('123456'),
        unidade='Admin',
        tipo='sindico',
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario


@pytest.fixture()
def morador(app):
    usuario = Usuario(
        nome='Morador Teste',
        email='morador@conectalar.com',
        senha=gerar_hash_senha('123456'),
        unidade='Casa 10',
        tipo='morador',
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario


def csrf_token(client):
    token = 'csrf-token-test'
    with client.session_transaction() as sess:
        sess['_csrf_token'] = token
    return token


def login(client, email='sindico@conectalar.com', senha='123456'):
    return client.post(
        '/',
        data={
            'email': email,
            'senha': senha,
            '_csrf_token': csrf_token(client),
        },
        follow_redirects=False,
    )
