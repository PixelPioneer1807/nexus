# Testing and Operations

_Last updated: 2026-11-13_

## Setup (verified)
Requires `uv`. From the repo root:

```bash
uv sync
```

## Tests (verified)
```bash
uv run pytest -q
```

## Run the API (verified)
```bash
uv run uvicorn nexus.api.app:app --reload --port 8077
```
Then open http://localhost:8077/health or http://localhost:8077/docs.

## Known gaps
No lint/type-check config yet. No database yet.
