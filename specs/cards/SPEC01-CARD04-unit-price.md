# CARD04: Line item unit_price column

**Status:** READY
**Last Updated:** 2026-06-17
**Spec:** [SPEC01](../SPEC01-line-items.md)
**Commit:** `feat: add unit_price to line_items`

**Lane:** `app/models.py` (LineItem), `alembic/versions/`, `tests/test_unit_price.py`
**Direction:** n/a
**Provides:** `line_items.unit_price`
**Consumes:** none

## Description

Add an additive nullable `unit_price` column to `line_items`. Runs concurrently
with CARD05 (which adds a column to `orders`) — both generate Alembic revisions,
so generation is serialized through the migration hub; if two heads result, run
`alembic merge heads`.

## Acceptance Criteria

AC1: `line_items` has a nullable `unit_price` (numeric/float) column.
    - Technical: a `LineItem` can be created with a `unit_price`; defaults to None when omitted.
AC2: An additive migration adds the column.
    - Technical: `uv run alembic upgrade head` applies cleanly; single head after.

## Task Breakdown

1. **Failing test** — `tests/test_unit_price.py`: a line item persists with a unit_price, and defaults to None. RED first (column missing). **Verify:** `uv run pytest tests/test_unit_price.py`
2. **Add column + migration** — edit `LineItem` in `app/models.py`; `uv run alembic revision --autogenerate -m "add unit_price to line_items"` (rebase onto the current head first; merge heads if needed). **Verify:** `rm -f app.db && uv run alembic upgrade head && uv run pytest`

## How to Verify

- `rm -f app.db && uv run alembic upgrade head && uv run pytest tests/test_unit_price.py`
