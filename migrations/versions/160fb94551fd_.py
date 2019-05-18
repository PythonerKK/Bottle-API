"""empty message

Revision ID: 160fb94551fd
Revises: c35833aaebb2
Create Date: 2019-05-18 22:06:33.577320

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '160fb94551fd'
down_revision = 'c35833aaebb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('app_secret', table_name='user')
    op.drop_column('user', 'app_secret')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('app_secret', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=128), nullable=True))
    op.create_index('app_secret', 'user', ['app_secret'], unique=True)
    # ### end Alembic commands ###