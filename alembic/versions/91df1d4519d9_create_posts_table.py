"""create posts table

Revision ID: 91df1d4519d9
Revises: 
Create Date: 2021-12-10 15:00:27.038071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91df1d4519d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
