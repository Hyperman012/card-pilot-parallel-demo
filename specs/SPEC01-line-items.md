# SPEC01: Order line items

## Problem

Orders currently have no line items. We want to attach line items to an order
and expose them via the API — built in parallel to exercise the trunk-based
fan-out.

## Proposal

A `line_items` table (one row per item on an order), a `LineItemRepository`
port + implementation, and `POST`/`GET /orders/{id}/items` endpoints. Two later
cards add columns (`unit_price`, and an order `note`) concurrently to stress the
migration hub.

## Plan

Built in parallel after the foundation. Each card's lane is disjoint; the two
migration cards race Alembic revisions on purpose.

| Card | Summary | Lane | Direction | Provides / Consumes |
|---|---|---|---|---|
| CARD01 | Foundation: bare `line_items` table + `LineItemRepository` port + skipped acceptance test | models.py (LineItem), alembic, ports.py, tests/test_line_items_acceptance.py | — | Provides: `line_items` table, `LineItemRepository` port |
| CARD02 | Implement `LineItemRepository` (add/list) | app/line_item_repo.py, tests/test_line_item_repo.py | inside-out | Provides: `LineItemRepository.add/list` |
| CARD03 | `POST`/`GET /orders/{id}/items` endpoints; un-skip the acceptance test | app/line_items_api.py, app/main.py (router append), tests/test_line_items_acceptance.py | outside-in | Consumes: `LineItemRepository` |
| CARD04 | Add additive `unit_price` column to `line_items` | models.py (LineItem), alembic, tests/test_unit_price.py | n/a | Provides: `line_items.unit_price` |
| CARD05 | Add additive `note` column to `orders` | models.py (Order), alembic, tests/test_note.py | n/a | Provides: `orders.note` |

CARD03 consumes the port CARD02 provides — the hot seam (CARD03 builds against
the port, CARD02 prioritizes landing it). CARD04 + CARD05 both add migrations →
the migration hub (serialized generation; merge heads if they collide).
