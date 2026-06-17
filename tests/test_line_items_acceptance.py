"""Acceptance test for the full line-items API flow.

Un-skipped by the line-items-API card (outside-in lane). Stays green on its own
by overriding the get_line_item_repository dependency with an in-memory fake
that implements the app.ports.LineItemRepository port — no dependency on
CARD02's concrete repo or on the orders-API lane.
"""
from fastapi.testclient import TestClient

from app.line_items_api import get_line_item_repository
from app.main import app


class FakeLineItemRepository:
    """In-memory LineItemRepository for the acceptance test."""

    def __init__(self) -> None:
        self._items: list[dict] = []
        self._next_id = 1

    def add(self, order_id: int) -> int:
        item_id = self._next_id
        self._next_id += 1
        self._items.append({"id": item_id, "order_id": order_id})
        return item_id

    def list(self, order_id: int) -> list[dict]:
        return [item for item in self._items if item["order_id"] == order_id]


def test_add_then_list_items():
    fake = FakeLineItemRepository()
    app.dependency_overrides[get_line_item_repository] = lambda: fake
    try:
        client = TestClient(app)
        order_id = 1

        added = client.post(f"/orders/{order_id}/items", json={})
        assert added.status_code == 201
        item_id = added.json()["id"]

        listed = client.get(f"/orders/{order_id}/items")
        assert listed.status_code == 200
        assert listed.json() == [{"id": item_id, "order_id": order_id}]
    finally:
        app.dependency_overrides.pop(get_line_item_repository, None)
