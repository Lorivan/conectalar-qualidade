"""Create the initial ConectaLar schema when tables do not exist.

Revision ID: 20261011_0001
Revises:
"""
from alembic import op
import sqlalchemy as sa


revision = '20261011_0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if not inspector.has_table('usuarios'):
        op.create_table(
            'usuarios',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('nome', sa.String(length=100), nullable=False),
            sa.Column('email', sa.String(length=120), nullable=False),
            sa.Column('senha', sa.String(length=128), nullable=False),
            sa.Column('unidade', sa.String(length=20), nullable=False),
            sa.Column('tipo', sa.String(length=20), nullable=True),
            sa.UniqueConstraint('email', name='uq_usuarios_email'),
        )
    if not inspector.has_table('ocorrencias'):
        op.create_table(
            'ocorrencias',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('titulo', sa.String(length=100), nullable=False),
            sa.Column('descricao', sa.Text(), nullable=False),
            sa.Column('data_criacao', sa.DateTime(), nullable=False),
            sa.Column('status', sa.String(length=20), nullable=True),
            sa.Column('usuario_id', sa.Integer(), nullable=False),
            sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id']),
        )


def downgrade():
    raise RuntimeError(
        'A revisão baseline não pode ser revertida automaticamente; '
        'crie migrações explícitas para alterações de schema posteriores.'
    )
