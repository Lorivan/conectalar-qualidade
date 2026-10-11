from app.models import Ocorrencia
from tests.conftest import csrf_token, login


def test_nova_ocorrencia_valida_persiste_no_banco(client, app, sindico):
    login(client)

    response = client.post(
        '/nova-ocorrencia',
        data={
            'titulo': 'Portão com ruído',
            'descricao': 'O portão principal está fazendo ruído alto ao abrir.',
            '_csrf_token': csrf_token(client),
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    with app.app_context():
        ocorrencia = Ocorrencia.query.filter_by(titulo='Portão com ruído').first()
        assert ocorrencia is not None
        assert ocorrencia.status == 'Pendente'
        assert ocorrencia.autor.email == 'sindico@conectalar.com'


def test_morador_visualiza_atalho_para_nova_ocorrencia_no_dashboard(client, morador):
    login(client, email='morador@conectalar.com')

    response = client.get('/dashboard')

    assert response.status_code == 200
    assert b'+ Nova Ocorr' in response.data
    assert b'/nova-ocorrencia' in response.data
    assert b'+ Novo Morador' not in response.data


def test_morador_registra_ocorrencia(client, app, morador):
    login(client, email='morador@conectalar.com')

    response = client.post(
        '/nova-ocorrencia',
        data={
            'titulo': 'Vazamento na garagem',
            'descricao': 'Existe um vazamento constante no piso da garagem.',
            '_csrf_token': csrf_token(client),
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    with app.app_context():
        ocorrencia = Ocorrencia.query.filter_by(titulo='Vazamento na garagem').first()
        assert ocorrencia is not None
        assert ocorrencia.autor.email == 'morador@conectalar.com'


def test_nova_ocorrencia_invalida_nao_persiste(client, app, sindico):
    login(client)

    response = client.post(
        '/nova-ocorrencia',
        data={
            'titulo': 'A',
            'descricao': 'curta',
            '_csrf_token': csrf_token(client),
        },
    )

    assert response.status_code == 400
    assert 'Informe um título com pelo menos 3 caracteres.'.encode() in response.data
    with app.app_context():
        assert Ocorrencia.query.count() == 0


def test_atualizar_status_exige_sindico(client, app, morador):
    with client.session_transaction() as sess:
        sess['usuario_id'] = morador.id
        sess['usuario_nome'] = morador.nome
        sess['usuario_tipo'] = morador.tipo

    response = client.post(
        '/atualizar-status/1/Resolvido',
        data={'_csrf_token': csrf_token(client)},
    )

    assert response.status_code == 403


def test_atualizar_status_rejeita_get(client, app, sindico):
    login(client)

    response = client.get('/atualizar-status/1/Resolvido')

    assert response.status_code == 405


def test_atualizar_status_requer_csrf(client, app, sindico):
    login(client)
    ocorrencia = Ocorrencia(titulo='Portão', descricao='Descrição suficiente para registro.', usuario_id=sindico.id)
    from app import db
    db.session.add(ocorrencia)
    db.session.commit()

    response = client.post(f'/atualizar-status/{ocorrencia.id}/Resolvido')

    assert response.status_code == 400
    assert db.session.get(Ocorrencia, ocorrencia.id).status == 'Pendente'


def test_atualizar_status_por_sindico_persiste(client, app, sindico):
    login(client)
    ocorrencia = Ocorrencia(titulo='Portão', descricao='Descrição suficiente para registro.', usuario_id=sindico.id)
    from app import db
    db.session.add(ocorrencia)
    db.session.commit()

    response = client.post(
        f'/atualizar-status/{ocorrencia.id}/Resolvido',
        data={'_csrf_token': csrf_token(client)},
    )

    assert response.status_code == 302
    assert db.session.get(Ocorrencia, ocorrencia.id).status == 'Resolvido'


def test_atualizar_status_invalido_informa_usuario(client, app, sindico):
    login(client)
    ocorrencia = Ocorrencia(titulo='Portão', descricao='Descrição suficiente para registro.', usuario_id=sindico.id)
    from app import db
    db.session.add(ocorrencia)
    db.session.commit()

    response = client.post(
        f'/atualizar-status/{ocorrencia.id}/Cancelado',
        data={'_csrf_token': csrf_token(client)},
    )

    assert response.status_code == 302
    assert 'status inválido'.encode() in client.get('/dashboard').data
    assert db.session.get(Ocorrencia, ocorrencia.id).status == 'Pendente'
