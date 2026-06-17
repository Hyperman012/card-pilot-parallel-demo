# CARD03: Line items API

**Status:** READY
**Last Updated:** 2026-06-17
**Spec:** [SPEC01](../SPEC01-line-items.md)
**Commit:** `feat: add line items API endpoints`

**Lane:** `app/line_items_api.py`, `app/main.py` (router include — append only), `tests/test_line_items_acceptance.py`
**Direction:** outside-in
**Provides:** `POST /orders/{id}/items`, `GET /orders/{id}/items`
**Consumes:** `app.ports.LineItemRepository`

## Description

The items API. Outside-in: starts at the HTTP boundary and builds against the
`LineItemRepository` port. If the concrete repo (CARD02) hasn't landed yet, build
against the port (a stub/dependency override) and rebase when it lands. Un-skips
the acceptance test from CARD01.

## Acceptance Criteria

AC1: `POST /orders/{id}/items` creates a line item, returns 201 with its id.
AC2: `GET /orders/{id}/items` returns the order's items.
AC3: The CARD01 acceptance test is un-skipped and passes.
    - Technical: remove the `@pytest.mark.skip` and make it green.

## Task Breakdown

1. **Wire the endpoints against the port** — `app/line_items_api.py`: an APIRouter with POST/GET using a `LineItemRepository` dependency. **Verify:** import works.
2. **Register the router** — `app/main.py`: `app.include_router(...)` (append-only hub edit). **Verify:** `GET /openapi.json` lists the routes.
3. **Un-skip the acceptance test** — make `tests/test_line_items_acceptance.py` green. **Verify:** `uv run pytest tests/test_line_items_acceptance.py`

## How to Verify

- `rm -f app.db && uv run alembic upgrade head && uv run pytest`
