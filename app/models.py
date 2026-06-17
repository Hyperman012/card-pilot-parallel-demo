"""ORM models.

Starts empty. CARD01 (foundation) adds the bare table; consumer cards add the
columns they need via additive migrations.
"""
from app.db import Base  # noqa: F401  (re-exported so Alembic's env imports models)
