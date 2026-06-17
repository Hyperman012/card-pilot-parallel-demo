# CARD05: Order note column

**Status:** READY
**Last Updated:** 2026-06-17
**Spec:** [SPEC01](../SPEC01-line-items.md)
**Commit:** `feat: add note to orders`

**Lane:** `app/models.py` (Order), `alembic/versions/`, `tests/test_note.py`
**Direction:** n/a
**Provides:** `orders.note`
**Consumes:** none

## Description

Add an additive nullable `note` column to `orders`. Runs concurrently with CARD04
(which adds a column to `line_items`) — both generate Alembic revisions, so
generation is serialized through the migration hub; if two heads result, run
`alembic merge heads`. Touches the `Order` class (CARD04 touches `LineItem`), so
the only shared surface is `models.py` + the migrations dir.

## Acceptance Criteria

AC1: `orders` has a nullable `note` (string) column.
    - Technical: an `Order` can be created with a `note`; defaults to None when omitted.
AC2: An additive migration adds the column.
    - Technical: `uv run alembic upgrade head` applies cleanly; single head after.

## Task Breakdown

1. **Failing test** — `tests/test_note.py`: an order persists with a note, and defaults to None. RED first (column missing). **Verify:** `uv run pytest tests/test_note.py`
2. **Add column + migration** — edit `Order` in `app/models.py`; `uv run alembic revision --autogenerate -m "add note to orders"` (rebase onto the current head first; merge heads if needed). **Verify:** `rm -f app.db && uv run alembic upgrade head && uv run pytest`

## How to Verify

- `rm -f app.db && uv run alembic upgrade head && uv run pytest tests/test_note.py`
