# Codebase Map

_Last updated: 2026-11-13_

| Path | Responsibility |
|---|---|
| `pyproject.toml` | Package metadata, deps (fastapi, uvicorn; dev: pytest, httpx), pytest config |
| `src/nexus/api/app.py` | FastAPI app; `GET /health` liveness only |
| `tests/test_health.py` | Health endpoint test |
| `docs/learning/` | Syllabus and daily study log |
| `docs/project-memory/` | Project memory (this folder) |

Planned layout from the guide (not created yet): `services/`, `packages/` (graph engine, ledger,
queue, policy), `ai/`, `benchmarks/`.
