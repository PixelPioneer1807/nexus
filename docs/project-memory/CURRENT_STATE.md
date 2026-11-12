# Current State — NEXUS

_Last updated: 2026-11-13_

## Phase
Stage A (failure models + Phase 0 design), step A1 in progress. Roadmap is step-based (ADR-004).

## Implemented and verified
- Python project skeleton (`pyproject.toml`, uv-managed `.venv`, Python 3.15.2 picked by uv).
- `GET /health` in `src/nexus/api/app.py`; `tests/test_health.py` passes (`uv run pytest -q` → 1 passed).
- Manual smoke test: `uvicorn` on port 8077 returned `{"status":"ok"}`.

## Repository
- Branch `main`; remote `origin` = https://github.com/PixelPioneer1807/nexus.git (public).
- Claude commits and pushes for this repo (Shivam's decision, 2026-11-13). `gh` CLI not installed.
- Automatic checkpoints keep these docs in sync: a 3-hourly session job and a nightly scheduled
  task (`nexus-daily-checkpoint`).
- `docs/learning/STUDY_LOG.md` is gitignored on purpose (private profile, grades, streak).

## Known issues
- Starlette prints a deprecation warning about `httpx` in its test client. Harmless. Switching to the
  suggested replacement package was blocked pending a check that it's the legitimate package.

## Not implemented
- Everything else in `docs/learning/SYLLABUS.md` (Stages A–Z).

## Working agreement
Shivam writes pseudocode / design; Claude writes the code and tests; Shivam explains back (ADR-003).

## Where we stopped
A1 lesson given. Waiting for Shivam's quick-check answers and refund-workflow pseudocode.
Then: write `docs/phase0/PROBLEM.md` from his pseudocode.

## Next steps
1. A1: grade Shivam's answers, write `docs/phase0/PROBLEM.md` from his pseudocode.
2. A2: delivery guarantees per refund step, `docs/phase0/GUARANTEES.md`.
3. A3: in-memory idempotency ledger + tests.

## Files to read first when resuming
`docs/learning/STUDY_LOG.md`, then this file, then `DECISIONS.md`.
