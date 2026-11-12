"""HTTP entry point. Only a liveness check for now; workflow endpoints arrive in Phase 1."""

from fastapi import FastAPI

app = FastAPI(title="NEXUS", version="0.0.1")


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness: the process is up. Says nothing about the database (that becomes /ready later)."""
    return {"status": "ok"}
