"""empty message

Revision ID: 5e6326d84763
Revises: 19dd7c133135
Create Date: 2022-02-25 23:58:21.727355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e6326d84763'
down_revision = '19dd7c133135'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tech_stack',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(length=30), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(length=240), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tech_stack')
    # ### end Alembic commands ###
