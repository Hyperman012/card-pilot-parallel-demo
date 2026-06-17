"""ORM models.

Starts empty. CARD01 (foundation) adds the bare table; consumer cards add the
columns they need via additive migrations.
"""
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Order(Base):
    """An order. Foundation table — consumer cards add their own columns."""

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(nullable=False, default="pending")
    region: Mapped[str | None] = mapped_column(nullable=True, default=None)


class LineItem(Base):
    """A line item. Foundation table — consumer cards add their own columns."""

    __tablename__ = "line_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(nullable=False)
    unit_price: Mapped[float | None] = mapped_column(nullable=True, default=None)
