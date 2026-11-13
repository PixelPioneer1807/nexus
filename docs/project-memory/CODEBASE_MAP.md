# Codebase Map

_Last updated: 2026-11-14_

| Path | Responsibility |
|---|---|
| `pyproject.toml` | Package metadata, deps (fastapi, uvicorn; dev: pytest, httpx), pytest config |
| `src/nexus/api/app.py` | FastAPI app; `GET /health` liveness only |
| `tests/test_health.py` | Health endpoint test |
| `docs/learning/` | `SYLLABUS.md` (step roadmap, tracked) and `STUDY_LOG.md` (private, gitignored) |
| `docs/book/` | Public study chapters (ADR-005). Only an empty local folder `A-failure-and-design/` so far; nothing tracked in git yet |
| `docs/project-memory/` | Project memory (this folder); ADRs in `decisions/` |
| `uv.lock` | Locked dependency versions for `uv sync` |

Planned layout from the guide (not created yet): `services/`, `packages/` (graph engine, ledger,
queue, policy), `ai/`, `benchmarks/`.
