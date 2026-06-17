"""Tests for the concrete SQLAlchemy OrderRepository.

Contract (from app.ports.OrderRepository):
- create(status="pending") inserts an Order and returns its id.
- get(order_id) round-trips it as {"id": ..., "status": ...}, or None if absent.
"""
from app.db import SessionLocal
from app.ports import OrderRepository as OrderRepositoryPort
from app.repository import OrderRepository


def test_satisfies_port():
    session = SessionLocal()
    try:
        repo = OrderRepository(session)
        assert isinstance(repo, OrderRepositoryPort)
    finally:
        session.close()


def test_create_returns_id_and_get_round_trips_default_status():
    session = SessionLocal()
    try:
        repo = OrderRepository(session)
        order_id = repo.create()
        assert isinstance(order_id, int)
        assert repo.get(order_id) == {"id": order_id, "status": "pending"}
    finally:
        session.close()


def test_create_honors_explicit_status():
    session = SessionLocal()
    try:
        repo = OrderRepository(session)
        order_id = repo.create(status="shipped")
        assert repo.get(order_id) == {"id": order_id, "status": "shipped"}
    finally:
        session.close()


def test_get_missing_returns_none():
    session = SessionLocal()
    try:
        repo = OrderRepository(session)
        assert repo.get(999_999) is None
    finally:
        session.close()
