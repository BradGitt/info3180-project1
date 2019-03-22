"""empty message

Revision ID: ee047ab547ec
Revises: 2e731f54c102
Create Date: 2019-03-22 09:34:40.923868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee047ab547ec'
down_revision = '2e731f54c102'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('date', sa.String(length=30), nullable=True))
    op.add_column('user_profiles', sa.Column('upload', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'upload')
    op.drop_column('user_profiles', 'date')
    # ### end Alembic commands ###