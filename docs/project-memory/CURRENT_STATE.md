# Current State — NEXUS

_Last updated: 2026-11-14 (nightly checkpoint)_

## Phase
Stage A (failure models + Phase 0 design), step A1 in progress. Roadmap is step-based (ADR-004).

## Implemented and verified
- Python project skeleton (`pyproject.toml`, uv-managed `.venv`, Python 3.15.2 picked by uv).
- `GET /health` in `src/nexus/api/app.py`; `tests/test_health.py` passes (`uv run pytest -q` → 1 passed, re-run 2026-11-14).
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

## Where we stopped (2026-11-13, ~00:45)
- A1 lesson given; still waiting for Shivam's 3 answers + refund-workflow pseudocode.
- **In progress: public "book" of study chapters** (Shivam's request: his study materials should be
  public as blog-style chapters for his future portfolio website). Decided shape:
  - `docs/book/<Stage>-<slug>/<StepID>-<slug>.md`, one full blog chapter per step (the lesson written
    out: problem, core idea, internals, failure modes, NEXUS usage, exercises, his pseudocode, what we
    built, interview questions, further reading), YAML frontmatter for the website (step, title, slug,
    part, status draft/published, date, tags, summary, resources, artifacts).
  - A generated table of contents + `index.json` for the website (script not written yet).
  - `docs/learning/STUDY_LOG.md` stays private (profile, grades, tutor notes).
- On disk now: empty `docs/book/A-failure-and-design/` (local only: git does not track empty folders);
  `_TEMPLATE.md` and chapter A1 NOT written yet. Decision recorded as ADR-005.
- No NEXUS session after this point on 2026-11-13 (checked 2026-11-14). Working tree clean; HEAD `bcb6f42`
  before the checkpoint commit.

## Next steps
0. Finish the book setup: `_TEMPLATE.md`, chapter A1 as a full blog chapter, ToC/index generator
   script + test, update SYLLABUS "How a step works" (write chapter → publish on 🟢), memory, and
   both checkpoint prompts to maintain the book. Commit + push.
1. A1: grade Shivam's answers, write `docs/phase0/PROBLEM.md` from his pseudocode.
2. A2: delivery guarantees per refund step, `docs/phase0/GUARANTEES.md`.
3. A3: in-memory idempotency ledger + tests.

## Files to read first when resuming
`docs/learning/STUDY_LOG.md`, then this file, then `DECISIONS.md`.
