"""add last few columns to posts table

Revision ID: 952d038fba94
Revises: 0cff47597d8e
Create Date: 2021-11-28 15:35:16.204128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '952d038fba94'
down_revision = '0cff47597d8e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'posts',
        sa.Column('published',sa.Boolean(),nullable=False,server_default='True')
    )
    op.add_column(
        'posts',
        sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()'))
    )
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
