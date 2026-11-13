# Testing and Operations

_Last updated: 2026-11-14_

## Setup (verified)
Requires `uv`. From the repo root:

```bash
uv sync
```

## Tests (verified)
```bash
uv run pytest -q
```
Last run 2026-11-14 (nightly checkpoint): `1 passed, 1 warning` (Starlette `httpx` deprecation
warning, see CURRENT_STATE known issues). The first run after a while can take over a minute to start.

## Run the API (verified)
```bash
uv run uvicorn nexus.api.app:app --reload --port 8077
```
Then open http://localhost:8077/health or http://localhost:8077/docs.

## Known gaps
No lint/type-check config yet. No database yet.
