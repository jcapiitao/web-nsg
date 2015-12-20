"""empty message

Revision ID: 5175173f40f
Revises: 31a05f14ef3
Create Date: 2015-12-19 19:22:38.925515

"""

# revision identifiers, used by Alembic.
revision = '5175173f40f'
down_revision = '31a05f14ef3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'excelFile')
    op.drop_column('project', 'templateFile')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('templateFile', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('project', sa.Column('excelFile', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    ### end Alembic commands ###