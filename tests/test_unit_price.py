"""Additive `unit_price` column on the line_items table.

Contract: a LineItem has a nullable `unit_price` float. It persists when supplied
and defaults to None when omitted.
"""
from app.db import Base, SessionLocal, engine
from app.models import LineItem


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_line_item_persists_given_unit_price():
    session = SessionLocal()
    try:
        item = LineItem(order_id=1, unit_price=9.99)
        session.add(item)
        session.commit()
        session.refresh(item)
        assert item.id is not None
        assert item.unit_price == 9.99
    finally:
        session.close()


def test_line_item_unit_price_defaults_to_none_when_omitted():
    session = SessionLocal()
    try:
        item = LineItem(order_id=1)
        session.add(item)
        session.commit()
        session.refresh(item)
        assert item.unit_price is None
    finally:
        session.close()
