"""Acceptance test for the full orders API flow.

Skipped at the foundation — the endpoints don't exist yet. The consumer card
that adds POST/GET /orders un-skips this. Keeping it here (skipped) lands the
contract early while CI stays green.
"""
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.skip(reason="un-skipped by the orders-API card (outside-in lane)")
def test_create_then_get_order():
    created = client.post("/orders", json={})
    assert created.status_code == 201
    order_id = created.json()["id"]

    fetched = client.get(f"/orders/{order_id}")
    assert fetched.status_code == 200
    assert fetched.json() == {"id": order_id, "status": "pending"}
