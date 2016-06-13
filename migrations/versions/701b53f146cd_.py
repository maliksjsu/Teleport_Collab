"""empty message

Revision ID: 701b53f146cd
Revises: 3cff00b5d1bf
Create Date: 2016-05-24 20:42:47.208628

"""

# revision identifiers, used by Alembic.
revision = '701b53f146cd'
down_revision = '3cff00b5d1bf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nickname', sa.String(length=64), nullable=False))
    op.add_column('user', sa.Column('social_id', sa.String(length=64), nullable=False))
    op.create_unique_constraint(None, 'user', ['social_id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'social_id')
    op.drop_column('user', 'nickname')
    ### end Alembic commands ###
