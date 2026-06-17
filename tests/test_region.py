"""Additive `region` column on the orders table.

Contract: an Order has a nullable `region` string. It persists when supplied and
defaults to None when omitted.
"""
from app.db import Base, SessionLocal, engine
from app.models import Order


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_order_persists_given_region():
    session = SessionLocal()
    try:
        order = Order(region="us-west")
        session.add(order)
        session.commit()
        session.refresh(order)
        assert order.id is not None
        assert order.region == "us-west"
    finally:
        session.close()


def test_order_region_defaults_to_none_when_omitted():
    session = SessionLocal()
    try:
        order = Order()
        session.add(order)
        session.commit()
        session.refresh(order)
        assert order.region is None
    finally:
        session.close()
