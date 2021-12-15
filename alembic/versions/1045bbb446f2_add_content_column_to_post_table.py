"""add content column to post table

Revision ID: 1045bbb446f2
Revises: 91df1d4519d9
Create Date: 2021-12-10 15:52:39.309240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1045bbb446f2'
down_revision = '91df1d4519d9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
