from flask import Blueprint, current_app, flash, redirect, render_template, request, session, url_for

from app.ocorrencias.service import OcorrenciaPersistenceError, OcorrenciaService
from app.services.validation_service import validar_ocorrencia_form
from app.utils.auth import login_obrigatorio, sindico_obrigatorio

ocorrencias_bp = Blueprint('ocorrencias', __name__)


@ocorrencias_bp.route('/nova-ocorrencia', methods=['GET', 'POST'])
@login_obrigatorio
def nova_ocorrencia():
    if request.method == 'POST':
        validacao = validar_ocorrencia_form(request.form)
        if not validacao.valido:
            for erro in validacao.erros:
                flash(erro, 'warning')
            return render_template('nova_ocorrencia.html'), 400

        service = OcorrenciaService()

        try:
            service.registrar_ocorrencia(
                titulo=validacao.dados['titulo'],
                descricao=validacao.dados['descricao'],
                usuario_id=session['usuario_id'],
            )
            flash('Ocorrência registrada com sucesso.', 'success')
            return redirect(url_for('dashboard.dashboard'))
        except OcorrenciaPersistenceError:
            current_app.logger.exception('Falha ao registrar ocorrência.')
            flash('Não foi possível registrar a ocorrência. Verifique os dados e tente novamente.', 'danger')
            return render_template('nova_ocorrencia.html'), 500

    return render_template('nova_ocorrencia.html')


@ocorrencias_bp.route('/atualizar-status/<int:id>/<novo_status>', methods=['POST'])
@sindico_obrigatorio
def atualizar_status(id, novo_status):
    service = OcorrenciaService()

    try:
        status_atualizado = service.atualizar_status(
            ocorrencia_id=id,
            novo_status=novo_status,
        )
        if status_atualizado:
            flash('Status atualizado com sucesso.', 'success')
        else:
            flash('Não foi possível atualizar: ocorrência inexistente ou status inválido.', 'warning')
    except OcorrenciaPersistenceError:
        current_app.logger.exception('Falha ao atualizar status da ocorrência %s.', id)
        flash('Não foi possível atualizar o status. Tente novamente.', 'danger')

    return redirect(url_for('dashboard.dashboard'))
