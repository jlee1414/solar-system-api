"""add planets model

Revision ID: 74c6d9d78394
Revises: 
Create Date: 2022-04-29 15:22:00.943615

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74c6d9d78394'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_colonized', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planet')
    # ### end Alembic commands ###
