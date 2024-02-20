"""empty message

Revision ID: 8b88968f15fd
Revises: 7160acf9d6b7
Create Date: 2024-02-20 14:06:57.142690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b88968f15fd'
down_revision = '7160acf9d6b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    # ### end Alembic commands ###