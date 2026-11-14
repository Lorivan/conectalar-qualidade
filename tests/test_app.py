from app import db
from sqlalchemy import text
from tests.conftest import csrf_token


def test_app_factory_responde_healthcheck(client):
    response = client.get('/healthz')

    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}


def test_banco_em_teste_executa_consulta(app):
    with app.app_context():
        resultado = db.session.execute(text('SELECT 1')).scalar()

    assert resultado == 1


def test_cookie_de_sessao_tem_atributos_seguros(app, client, sindico):
    app.config['SESSION_COOKIE_SECURE'] = True
    response = client.post(
        '/',
        data={
            'email': sindico.email,
            'senha': '123456',
            '_csrf_token': csrf_token(client),
        },
    )

    cookie = next(value for value in response.headers.getlist('Set-Cookie') if value.startswith('session='))
    assert 'HttpOnly' in cookie
    assert 'Secure' in cookie
    assert 'SameSite=Lax' in cookie
