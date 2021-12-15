"""add foreign-key to posts table

Revision ID: 6537fe077735
Revises: ea35d9891523
Create Date: 2021-12-12 10:59:57.287515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6537fe077735'
down_revision = 'ea35d9891523'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table= "posts", referent_table= "users", local_cols= ['owner_id'], remote_cols= ['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
