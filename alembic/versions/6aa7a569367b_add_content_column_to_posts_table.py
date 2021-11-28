"""add content column to posts table

Revision ID: 6aa7a569367b
Revises: 44d2d9e722d1
Create Date: 2021-11-28 15:14:15.877910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6aa7a569367b'
down_revision = '44d2d9e722d1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
