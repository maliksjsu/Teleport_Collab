"""empty message

Revision ID: 7d3bd5d51c5e
Revises: f1ddc39e1d05
Create Date: 2016-06-07 21:07:12.911539

"""

# revision identifiers, used by Alembic.
revision = '7d3bd5d51c5e'
down_revision = 'f1ddc39e1d05'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author', sa.Column('email_confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('author', 'email_confirmed')
    ### end Alembic commands ###