"""add tag and question_tag tables

Revision ID: 315bfd77dc3c
Revises:
Create Date: 2026-03-17

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "315bfd77dc3c"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "tag",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "question_tag",
        sa.Column("question_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["question_id"],
            ["question.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["tag.id"],
        ),
        sa.PrimaryKeyConstraint("question_id", "tag_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("question_tag")
    op.drop_table("tag")
    # ### end Alembic commands ###
