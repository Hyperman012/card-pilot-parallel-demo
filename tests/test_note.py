"""Additive `note` column on the orders table.

Contract: an Order has a nullable `note` string. It persists when supplied and
defaults to None when omitted.
"""
from app.db import Base, SessionLocal, engine
from app.models import Order


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_order_persists_given_note():
    session = SessionLocal()
    try:
        order = Order(note="rush delivery")
        session.add(order)
        session.commit()
        session.refresh(order)
        assert order.id is not None
        assert order.note == "rush delivery"
    finally:
        session.close()


def test_order_note_defaults_to_none_when_omitted():
    session = SessionLocal()
    try:
        order = Order()
        session.add(order)
        session.commit()
        session.refresh(order)
        assert order.note is None
    finally:
        session.close()
