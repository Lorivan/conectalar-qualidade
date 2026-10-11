from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for

from app import limiter
from app.models import Usuario
from app.services.auth_service import verificar_senha
from sqlalchemy.exc import SQLAlchemyError

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/', methods=['GET', 'POST'])
@limiter.limit('5 per minute', methods=['POST'])
def login():
    if request.method == 'POST':
        email_digitado = (request.form.get('email') or '').strip().lower()
        senha_digitada = request.form.get('senha')

        try:
            usuario = Usuario.query.filter_by(email=email_digitado).first()
        except SQLAlchemyError:
            current_app.logger.exception('Falha ao consultar usuário durante o login.')
            flash('Erro ao consultar usuário. Tente novamente em instantes.', 'danger')
            return render_template('login.html')

        if usuario and verificar_senha(senha_digitada, usuario.senha):
            session.clear()
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome
            session['usuario_tipo'] = usuario.tipo

            return redirect(url_for('dashboard.dashboard'))

        flash('Email ou senha inválidos', 'danger')

    return render_template('login.html')


@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
