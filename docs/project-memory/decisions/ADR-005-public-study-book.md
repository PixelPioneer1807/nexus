# ADR-005 — Public study book of chapters

- Date: 2026-11-13 · Status: Accepted (requested by Shivam); implementation not started
- Recorded by the nightly checkpoint on 2026-11-14 from the decision already written in
  `CURRENT_STATE.md` (commit `bcb6f42`). Alternatives considered were not recorded.

## Context
Shivam wants his study materials public, as blog-style chapters for a portfolio website he will
build after the project.

## Decision
- One full blog chapter per step: `docs/book/<Stage>-<slug>/<StepID>-<slug>.md`.
- Each chapter covers the lesson written out (problem, core idea, internals, failure modes, NEXUS
  usage, exercises, his pseudocode, what we built, interview questions, further reading).
- YAML frontmatter for the website: step, title, slug, part, status (draft/published), date, tags,
  summary, resources, artifacts.
- A generated table of contents + `index.json` for the website.
- `docs/learning/STUDY_LOG.md` stays private (profile, grades, tutor notes).

## Follow-ups (open)
`_TEMPLATE.md`, chapter A1, the ToC/index generator script + test, SYLLABUS "How a step works"
update, and both checkpoint prompts updated to maintain the book. See `CURRENT_STATE.md` next step 0.
