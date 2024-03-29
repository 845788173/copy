"""empty message

Revision ID: cbac707aa50e
Revises: 7eb09bf14781
Create Date: 2018-11-15 16:00:02.198999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbac707aa50e'
down_revision = '7eb09bf14781'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('g_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('s_name', sa.String(length=20), nullable=True),
    sa.Column('s_score', sa.Integer(), nullable=True),
    sa.Column('s_age', sa.Integer(), nullable=True),
    sa.Column('s_grade', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['s_grade'], ['grade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('grade')
    # ### end Alembic commands ###
