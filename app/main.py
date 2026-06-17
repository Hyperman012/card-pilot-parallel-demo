"""FastAPI application.

The /health endpoint is the walking-skeleton proof that the app boots. Cards
register their routers here (an append-only hub edit).
"""
from fastapi import FastAPI

app = FastAPI(title="card-pilot parallel demo")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


from app.line_items_api import router as line_items_router

app.include_router(line_items_router)
