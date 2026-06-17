"""Acceptance test for the full line-items API flow.

Skipped at the foundation — the endpoints don't exist yet. The consumer card
that adds POST/GET /orders/{id}/items un-skips this. Keeping it here (skipped)
lands the contract early while CI stays green.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.skip(reason="un-skipped by the line-items-API card (outside-in lane)")
def test_add_then_list_items():
    order = client.post("/orders", json={})
    assert order.status_code == 201
    order_id = order.json()["id"]

    added = client.post(f"/orders/{order_id}/items", json={})
    assert added.status_code == 201
    item_id = added.json()["id"]

    listed = client.get(f"/orders/{order_id}/items")
    assert listed.status_code == 200
    assert listed.json() == [{"id": item_id, "order_id": order_id}]
