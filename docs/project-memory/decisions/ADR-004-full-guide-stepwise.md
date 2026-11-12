# ADR-004 — Full guide, step by step, nothing cut

- Date: 2026-11-13 · Status: **Accepted** (decided by Shivam) · Supersedes: ADR-001

## Context
ADR-001 proposed a 12-week "NEXUS-lite" that deferred Kafka, Kubernetes, Terraform and most CS
foundations. Shivam rejected cutting scope: he wants every part of the guide, in maximum detail.

## Decision
- Cover every part of the guide (Parts I–XV, Appendices) and every NEXUS phase (0–9).
- Organise work as **steps** grouped into Stages A–Z (`docs/learning/SYLLABUS.md`), not days or weeks.
- A step is done only when its exit check passes. Each stage ends with a hand-coded 🧪 test step.
- Target pace about 5 months; pace may flex, content may not.

## Consequences
Far larger scope than ADR-001; foundations are placed right before the NEXUS component that uses
them. Kafka, Kubernetes and Terraform are back in scope (Stages V, W, X).
