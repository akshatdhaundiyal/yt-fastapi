"""add user table

Revision ID: 54f4b8a69ead
Revises: 6aa7a569367b
Create Date: 2021-11-28 15:19:34.442649

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.operators import nulls_last_op


# revision identifiers, used by Alembic.
revision = '54f4b8a69ead'
down_revision = '6aa7a569367b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
