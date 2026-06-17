"""Concrete SQLAlchemy-backed OrderRepository.

Implements the app.ports.OrderRepository Protocol on top of the Order ORM
model. Takes a Session in its constructor; commits on create so the row is
durable and its server-assigned id is available to callers.
"""
from sqlalchemy.orm import Session

from app.models import Order


class OrderRepository:
    """Persists orders via a SQLAlchemy Session."""

    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, status: str = "pending") -> int:
        order = Order(status=status)
        self.session.add(order)
        self.session.commit()
        self.session.refresh(order)
        return order.id

    def get(self, order_id: int) -> dict | None:
        order = self.session.get(Order, order_id)
        if order is None:
            return None
        return {"id": order.id, "status": order.status}
