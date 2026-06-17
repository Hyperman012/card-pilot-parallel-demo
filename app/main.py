"""FastAPI application.

The /health endpoint is the walking-skeleton proof that the app boots. Cards
register their routers here (an append-only hub edit).
"""
from fastapi import FastAPI

app = FastAPI(title="card-pilot parallel demo")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
