"""merge tag heads

Revision ID: 9c63c89b00e7
Revises: 472e0f587b95, 315bfd77dc3c
Create Date: 2026-03-21 09:00:10.926249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c63c89b00e7'
down_revision: Union[str, Sequence[str], None] = ('472e0f587b95', '315bfd77dc3c')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
