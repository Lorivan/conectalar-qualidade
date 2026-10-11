from tests.conftest import csrf_token, login


def test_login_valido_redireciona_para_dashboard(client, sindico):
    response = login(client)

    assert response.status_code == 302
    assert '/dashboard' in response.headers['Location']


def test_login_normaliza_email(client, sindico):
    response = login(client, email='  SINDICO@CONECTALAR.COM  ')

    assert response.status_code == 302
    assert '/dashboard' in response.headers['Location']


def test_login_invalido_mostra_mensagem(client, sindico):
    response = login(client, senha='senha-errada')

    assert response.status_code == 200
    assert 'Email ou senha inválidos'.encode() in response.data


def test_dashboard_sem_sessao_redireciona_para_login(client):
    response = client.get('/dashboard')

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/')


def test_login_limita_tentativas_por_ip(app, client):
    app.config['RATELIMIT_ENABLED'] = True
    token = csrf_token(client)
    responses = [
        client.post(
            '/',
            data={'email': 'nao-existe@example.com', 'senha': 'incorreta', '_csrf_token': token},
            environ_overrides={'REMOTE_ADDR': '198.51.100.42'},
        )
        for _ in range(6)
    ]

    assert [response.status_code for response in responses[:-1]] == [200] * 5
    assert responses[-1].status_code == 429


def test_logout_requer_post_com_csrf(client, sindico):
    login(client)

    get_response = client.get('/logout')
    post_response = client.post('/logout', data={'_csrf_token': csrf_token(client)})

    assert get_response.status_code == 405
    assert post_response.status_code == 302
    assert post_response.headers['Location'].endswith('/')
