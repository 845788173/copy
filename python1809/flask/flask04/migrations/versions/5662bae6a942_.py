"""empty message

Revision ID: 5662bae6a942
Revises: 5fe6cfa1d8c1
Create Date: 2018-10-27 18:41:20.970765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5662bae6a942'
down_revision = '5fe6cfa1d8c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grade',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('g_name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('g_name')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('s_name', sa.String(length=20), nullable=True),
    sa.Column('s_age', sa.Integer(), nullable=True),
    sa.Column('s_grade_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['s_grade_id'], ['grade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('grade')
    # ### end Alembic commands ###
