"""Second

Revision ID: b613bc27d956
Revises: 9fac66015276
Create Date: 2022-03-23 16:17:45.726318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b613bc27d956'
down_revision = '9fac66015276'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'booking', ['id'])
    op.create_unique_constraint(None, 'queue', ['id'])
    op.create_unique_constraint(None, 'tables', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tables', type_='unique')
    op.drop_constraint(None, 'queue', type_='unique')
    op.drop_constraint(None, 'booking', type_='unique')
    # ### end Alembic commands ###
