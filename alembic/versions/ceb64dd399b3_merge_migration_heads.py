"""merge migration heads

Revision ID: ceb64dd399b3
Revises: 69d1e70c45e9, 88234cb2d8e3
Create Date: 2026-06-17 10:00:36.547947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceb64dd399b3'
down_revision: Union[str, Sequence[str], None] = ('69d1e70c45e9', '88234cb2d8e3')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
