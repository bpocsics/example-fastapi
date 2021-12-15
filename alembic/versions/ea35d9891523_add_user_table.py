"""add user table

Revision ID: ea35d9891523
Revises: 1045bbb446f2
Create Date: 2021-12-10 15:59:35.791836

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import PrimaryKeyConstraint


# revision identifiers, used by Alembic.
revision = 'ea35d9891523'
down_revision = '1045bbb446f2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                        sa.Column('id', sa.Integer(), nullable=False),
                        sa.Column('email', sa.String(), nullable=False),
                        sa.Column('password', sa.String(), nullable=False),
                        sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default= sa.text('now()'), nullable=False),
                        sa.PrimaryKeyConstraint('id'),
                        sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
