"""Reproduz defeitos do ConectaLar (rodar na raiz do repositorio)."""
import os, sys
sys.path.insert(0, os.getcwd())
os.environ.update(APP_ENV='testing', SECRET_KEY='k', DATABASE_URL='sqlite:///:memory:',
                  AUTO_CREATE_DB='true', DEBUG='false')
from app import create_app, db
from app.models import Usuario, Ocorrencia
from app.services.auth_service import gerar_hash_senha

app = create_app(); app.config.update(TESTING=True)
with app.app_context():
    db.create_all()
    s = Usuario(nome='Sindico', email='sindico@x.com', senha=gerar_hash_senha('123456'), unidade='A', tipo='sindico')
    m = Usuario(nome='Morador', email='morador@x.com', senha=gerar_hash_senha('123456'), unidade='C1', tipo='morador')
    db.session.add_all([s, m]); db.session.commit()
    o = Ocorrencia(titulo='Vazamento', descricao='Vazamento no corredor', usuario_id=m.id)
    db.session.add(o); db.session.commit(); oid = o.id

    # D-01: status alterado por GET sem token CSRF
    c = app.test_client()
    with c.session_transaction() as ss:
        ss['usuario_id'] = s.id; ss['usuario_tipo'] = 'sindico'
    r = c.get(f'/atualizar-status/{oid}/Resolvido')
    db.session.expire_all()
    print('D-01 GET sem CSRF -> HTTP', r.status_code, '| status no banco:', db.session.get(Ocorrencia, oid).status)

    # D-02: login diferencia maiusculas/minusculas do e-mail
    c2 = app.test_client()
    with c2.session_transaction() as ss: ss['_csrf_token'] = 't'
    r = c2.post('/', data={'email': 'Sindico@X.com', 'senha': '123456', '_csrf_token': 't'})
    print('D-02 login com e-mail em caixa diferente -> HTTP', r.status_code, '(esperado 302)')

    # D-03: status invalido -> sem feedback ao usuario
    r = c.get(f'/atualizar-status/{oid}/Inexistente', follow_redirects=True)
    print('D-03 status invalido -> mensagem de erro exibida?', b'inv\xc3\xa1lido' in r.data or b'alert-warning' in r.data or b'alert-danger' in r.data)

    # D-04: cookies de sessao
    print('D-04 SESSION_COOKIE_SECURE =', app.config.get('SESSION_COOKIE_SECURE'),
          '| SAMESITE =', app.config.get('SESSION_COOKIE_SAMESITE'),
          '| HTTPONLY =', app.config.get('SESSION_COOKIE_HTTPONLY'))

    # D-05: tentativas de login ilimitadas
    c3 = app.test_client()
    with c3.session_transaction() as ss: ss['_csrf_token'] = 't'
    codes = [c3.post('/', data={'email':'sindico@x.com','senha':f'errada{i}','_csrf_token':'t'}).status_code for i in range(30)]
    print('D-05 30 tentativas erradas seguidas -> codigos distintos:', sorted(set(codes)), '(sem bloqueio)')
