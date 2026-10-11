from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app import db
from app.models import Usuario
from app.services.auth_service import gerar_hash_senha
from app.services.validation_service import validar_usuario_form
from app.utils.auth import sindico_obrigatorio

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/cadastro', methods=['GET', 'POST'])
@sindico_obrigatorio
def cadastro():
    if request.method == 'POST':
        validacao = validar_usuario_form(request.form)
        if not validacao.valido:
            for erro in validacao.erros:
                flash(erro, 'warning')
            return render_template('cadastro.html'), 400

        if Usuario.query.filter_by(email=validacao.dados['email']).first():
            flash('Já existe um usuário cadastrado com este e-mail.', 'warning')
            return render_template('cadastro.html'), 400

        novo_u = Usuario(
            nome=validacao.dados['nome'],
            email=validacao.dados['email'],
            senha=gerar_hash_senha(validacao.dados['senha']),
            unidade=validacao.dados['unidade'],
            tipo=validacao.dados['tipo']
        )

        try:
            db.session.add(novo_u)
            db.session.commit()
            flash('Usuário cadastrado com sucesso.', 'success')
            return redirect(url_for('dashboard.dashboard'))
        except IntegrityError:
            db.session.rollback()
            current_app.logger.exception('E-mail duplicado ao cadastrar usuário.')
            flash('Já existe um usuário cadastrado com este e-mail.', 'warning')
        except SQLAlchemyError:
            db.session.rollback()
            current_app.logger.exception('Falha ao cadastrar usuário.')
            flash('Não foi possível cadastrar o usuário. Verifique os dados e tente novamente.', 'danger')

    return render_template('cadastro.html')


@usuarios_bp.route('/usuarios')
@sindico_obrigatorio
def lista_usuarios():
    pagina = request.args.get('pagina', default=1, type=int)
    paginacao = Usuario.query.order_by(Usuario.nome).paginate(
        page=pagina,
        per_page=20,
        error_out=False,
    )
    return render_template('usuarios.html', paginacao=paginacao)
