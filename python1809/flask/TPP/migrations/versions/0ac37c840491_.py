"""empty message

Revision ID: 0ac37c840491
Revises: e2b4a754aed7
Create Date: 2018-11-21 10:14:40.276935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ac37c840491'
down_revision = 'e2b4a754aed7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('token', sa.String(length=256), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.Column('isactive', sa.Boolean(), nullable=True),
    sa.Column('icon', sa.String(length=40), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
