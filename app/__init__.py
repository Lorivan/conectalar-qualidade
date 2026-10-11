# app/__init__.py
from flask import Flask, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.utils.csrf import generate_csrf_token, validate_csrf_for_request
from config import Config

db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address, default_limits=[])


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.ocorrencias.routes import ocorrencias_bp
    from app.usuarios.routes import usuarios_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(ocorrencias_bp)
    app.register_blueprint(usuarios_bp)


    app.jinja_env.globals['csrf_token'] = generate_csrf_token
    app.before_request(validate_csrf_for_request)

    if app.config.get('AUTO_CREATE_DB'):
        # Fluxo recomendado apenas para desenvolvimento local.
        with app.app_context():
            try:
                db.create_all()
            except SQLAlchemyError as exc:
                app.logger.error('Falha ao executar db.create_all() no startup: %s', exc)

    @app.get('/healthz')
    def healthz():
        try:
            db.session.execute(text('SELECT 1'))
            return jsonify({'status': 'ok'}), 200
        except SQLAlchemyError:
            return jsonify({'status': 'degraded'}), 503

    @app.errorhandler(400)
    def bad_request(error):
        return render_template('error.html', code=400, message=str(error.description)), 400

    @app.errorhandler(403)
    def forbidden(_error):
        return render_template('error.html', code=403, message='Acesso negado.'), 403

    @app.errorhandler(404)
    def not_found(_error):
        return render_template('error.html', code=404, message='Página não encontrada.'), 404

    @app.errorhandler(429)
    def too_many_requests(_error):
        return render_template(
            'error.html',
            code=429,
            message='Muitas tentativas. Aguarde alguns minutos e tente novamente.',
        ), 429

    @app.errorhandler(500)
    def internal_error(_error):
        return render_template('error.html', code=500, message='Erro interno no servidor.'), 500


    return app


app = create_app()
