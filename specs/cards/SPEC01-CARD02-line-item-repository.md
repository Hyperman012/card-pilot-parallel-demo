# CARD02: LineItemRepository implementation

**Status:** READY
**Last Updated:** 2026-06-17
**Spec:** [SPEC01](../SPEC01-line-items.md)
**Commit:** `feat: implement LineItemRepository`

**Lane:** `app/line_item_repo.py`, `tests/test_line_item_repo.py`
**Direction:** inside-out
**Provides:** `LineItemRepository.add`, `LineItemRepository.list`
**Consumes:** none (builds on the `line_items` table + port from CARD01)

## Description

Concrete SQLAlchemy implementation of the `LineItemRepository` port. Inside-out:
starts at the data layer. This is the hot seam CARD03 consumes — land it early.

## Acceptance Criteria

AC1: `add(order_id)` inserts a line item and returns its id.
    - Technical: `SqlLineItemRepository(session).add(order_id) -> int`.
AC2: `list(order_id)` returns the order's line items as dicts.
    - Technical: returns `[{"id": ..., "order_id": ...}, ...]`.
AC3: The implementation satisfies the port.
    - Technical: `isinstance(SqlLineItemRepository(session), LineItemRepository)` is True.

## Task Breakdown

1. **Test add→list round-trip** — `tests/test_line_item_repo.py`: add two items to an order, list returns both. Write first, see RED. **Verify:** `uv run pytest tests/test_line_item_repo.py`
2. **Implement** — `app/line_item_repo.py`: `SqlLineItemRepository(session)` with `add`/`list`. **Verify:** tests green.
3. **Port conformance test** — assert isinstance against `app.ports.LineItemRepository`. **Verify:** green.

## How to Verify

- `rm -f app.db && uv run alembic upgrade head && uv run pytest tests/test_line_item_repo.py`
