"""Tests for the concrete SQLAlchemy LineItemRepository.

Contract (from app.ports.LineItemRepository):
- add(order_id) inserts a LineItem and returns its id.
- list(order_id) returns the order's line items as [{"id": ..., "order_id": ...}, ...].
"""
from app.db import SessionLocal
from app.line_item_repo import SqlLineItemRepository
from app.ports import LineItemRepository as LineItemRepositoryPort
from app.repository import OrderRepository


def test_satisfies_port():
    session = SessionLocal()
    try:
        repo = SqlLineItemRepository(session)
        assert isinstance(repo, LineItemRepositoryPort)
    finally:
        session.close()


def test_add_returns_id_and_list_round_trips():
    session = SessionLocal()
    try:
        order_id = OrderRepository(session).create()
        repo = SqlLineItemRepository(session)

        first = repo.add(order_id)
        second = repo.add(order_id)
        assert isinstance(first, int)
        assert isinstance(second, int)

        items = repo.list(order_id)
        assert items == [
            {"id": first, "order_id": order_id},
            {"id": second, "order_id": order_id},
        ]
    finally:
        session.close()


def test_list_only_returns_items_for_the_given_order():
    session = SessionLocal()
    try:
        orders = OrderRepository(session)
        order_a = orders.create()
        order_b = orders.create()
        repo = SqlLineItemRepository(session)

        item_a = repo.add(order_a)
        repo.add(order_b)

        assert repo.list(order_a) == [{"id": item_a, "order_id": order_a}]
    finally:
        session.close()
