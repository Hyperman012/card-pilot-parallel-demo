"""Ports — the seams consumer cards build against.

CARD01 commits these interfaces so outside-in cards (e.g. the API) can build
against them immediately, stubbed, while an inside-out card lands the real
implementation. Adding a concrete OrderRepository is a later card's job.
"""
from typing import Protocol, runtime_checkable


@runtime_checkable
class OrderRepository(Protocol):
    """Persistence port for orders."""

    def create(self, status: str = "pending") -> int:
        """Create an order, return its id."""
        ...

    def get(self, order_id: int) -> dict | None:
        """Fetch an order as a dict, or None if it doesn't exist."""
        ...


@runtime_checkable
class LineItemRepository(Protocol):
    """Persistence port for line items."""

    def add(self, order_id: int) -> int:
        """Add a line item to an order, return its id."""
        ...

    def list(self, order_id: int) -> list[dict]:
        """List the line items for an order as dicts."""
        ...
