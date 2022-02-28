"""empty message

Revision ID: 9d7c44ce5032
Revises: 5e6326d84763
Create Date: 2022-02-28 10:26:13.357614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d7c44ce5032'
down_revision = '5e6326d84763'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_name', sa.String(length=30), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=False),
    sa.Column('github', sa.String(length=120), nullable=False),
    sa.Column('tag_urls', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###