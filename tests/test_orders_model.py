"""Foundation: the bare orders table.

Contract (inferred — spec is the demo's own design): an Order has an integer id
and a status that defaults to "pending" when not given.
"""
from app.db import Base, engine
from app.models import Order


def setup_module():
    Base.metadata.create_all(bind=engine)


def test_order_defaults_status_to_pending():
    from app.db import SessionLocal

    session = SessionLocal()
    try:
        order = Order()
        session.add(order)
        session.commit()
        session.refresh(order)
        assert order.id is not None
        assert order.status == "pending"
    finally:
        session.close()
