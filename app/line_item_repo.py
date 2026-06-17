"""Concrete SQLAlchemy-backed LineItemRepository.

Implements the app.ports.LineItemRepository Protocol on top of the LineItem
ORM model. Takes a Session in its constructor; commits on add so the row is
durable and its server-assigned id is available to callers.
"""
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import LineItem


class SqlLineItemRepository:
    """Persists line items via a SQLAlchemy Session."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, order_id: int) -> int:
        item = LineItem(order_id=order_id)
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item.id

    def list(self, order_id: int) -> list[dict]:
        stmt = (
            select(LineItem)
            .where(LineItem.order_id == order_id)
            .order_by(LineItem.id)
        )
        items = self.session.scalars(stmt).all()
        return [{"id": item.id, "order_id": item.order_id} for item in items]
