"""create content column to posts

Revision ID: 2df9e456b672
Revises: 6ba8feb53302
Create Date: 2022-11-22 20:25:47.951062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2df9e456b672'
down_revision = '6ba8feb53302'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
