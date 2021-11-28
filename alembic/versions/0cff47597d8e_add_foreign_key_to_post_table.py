"""add foreign key to post table

Revision ID: 0cff47597d8e
Revises: 54f4b8a69ead
Create Date: 2021-11-28 15:28:24.594752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cff47597d8e'
down_revision = '54f4b8a69ead'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key(
        'posts_users_fk',source_table='posts',referent_table='users',
        local_cols=['owner_id'],remote_cols=['id'],ondelete='CASCADE'
    )
    pass


def downgrade():
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
