# CARD01: Line items foundation

**Status:** IN PROGRESS
**Last Updated:** 2026-06-17
**Spec:** [SPEC01](../SPEC01-line-items.md)
**Commit:** `feat: add line_items foundation table and repository port`

**Lane:** `app/models.py` (LineItem), `alembic/versions/`, `app/ports.py` (LineItemRepository), `tests/test_line_items_acceptance.py`
**Direction:** n/a
**Provides:** `line_items` table, `app.ports.LineItemRepository` port
**Consumes:** none

## Description

The minimal foundation for line items: a bare `line_items` table and the
`LineItemRepository` port consumers build against, plus a skipped acceptance
test for the items API. Nothing else — columns and behavior come from later cards.

## Acceptance Criteria

AC1: A `LineItem` model exists with an `id` and an `order_id`.
    - Technical: `from app.models import LineItem`; columns `id` (pk), `order_id` (int, not null).
AC2: An additive migration creates the `line_items` table.
    - Technical: `uv run alembic upgrade head` creates `line_items`.
AC3: A `LineItemRepository` port is defined.
    - Technical: `from app.ports import LineItemRepository`; runtime_checkable Protocol with `add(order_id) -> int` and `list(order_id) -> list[dict]`.
AC4: A skipped acceptance test for the items API exists.
    - Technical: `tests/test_line_items_acceptance.py` with `@pytest.mark.skip`.

## Task Breakdown

1. **Add LineItem model** — `app/models.py`: `LineItem` with `id` pk, `order_id` int not null. **Verify:** `uv run python -c "from app.models import LineItem"`
2. **Generate migration** — `uv run alembic revision --autogenerate -m "create line_items"`. **Verify:** `rm -f app.db && uv run alembic upgrade head`
3. **Add port** — `app/ports.py`: `LineItemRepository` runtime_checkable Protocol (`add`, `list`). **Verify:** import works.
4. **Skipped acceptance test** — `tests/test_line_items_acceptance.py`: skipped test for POST then GET items. **Verify:** `uv run pytest` collects it as skipped.

## How to Verify

- `rm -f app.db && uv run alembic upgrade head && uv run pytest`
