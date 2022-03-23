"""First migrations

Revision ID: 115f8964ac2b
Revises: 
Create Date: 2022-03-23 09:23:20.579639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '115f8964ac2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('seats', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_index(op.f('ix_tables_id'), 'tables', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tables_id'), table_name='tables')
    op.drop_table('tables')
    # ### end Alembic commands ###