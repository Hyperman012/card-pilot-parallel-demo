"""Line items API — outside-in lane.

Defines POST/GET /orders/{id}/items against the app.ports.LineItemRepository
port. The concrete repository (CARD02) is imported LAZILY inside
get_line_item_repository so importing this module — and therefore app.main —
never fails even if the concrete repo hasn't landed yet.
"""
from collections.abc import Iterator

from fastapi import APIRouter, Depends, status

from app.db import get_session
from app.ports import LineItemRepository

router = APIRouter()


def get_line_item_repository(session=Depends(get_session)) -> Iterator[LineItemRepository]:
    """Provide a LineItemRepository.

    Imports the concrete repo lazily so this module imports cleanly even when
    CARD02's app.line_item_repo hasn't landed. Tests override this dependency
    with an in-memory fake to stay green independently.
    """
    from app.line_item_repo import SqlLineItemRepository

    yield SqlLineItemRepository(session)


@router.post("/orders/{order_id}/items", status_code=status.HTTP_201_CREATED)
def add_item(
    order_id: int,
    repo: LineItemRepository = Depends(get_line_item_repository),
) -> dict[str, int]:
    item_id = repo.add(order_id)
    return {"id": item_id}


@router.get("/orders/{order_id}/items")
def list_items(
    order_id: int,
    repo: LineItemRepository = Depends(get_line_item_repository),
) -> list[dict]:
    return repo.list(order_id)
