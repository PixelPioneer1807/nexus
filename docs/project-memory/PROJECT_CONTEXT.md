# Project Context — NEXUS

_Last updated: 2026-11-13_

## Purpose
NEXUS is a reliability and governance layer for AI systems that perform real business operations
(example workflow: a customer refund investigation). It accepts a task, gets or validates a typed
execution plan, schedules work, enforces permissions, calls tools, records evidence, recovers from
failures and reports the outcome.

It is also a learning project: each component is used to study the computer science underneath it
(source: `NEXUS_Engineering_Master_Guide.pdf`, v1.0, Nov 2026).

## The hard problem
An external API can commit a side effect while the caller times out before the response arrives.
A timeout does not mean failure. NEXUS must track intent → attempt → external reference → confirmed
outcome, use idempotency keys where the provider supports them, and reconcile ambiguous states.
Exactly-once across arbitrary external systems is not a realistic guarantee.

## Scope (ADR-004)
Every part of the guide and every NEXUS phase (0–9), step by step in Stages A–Z
(`docs/learning/SYLLABUS.md`): durable workflow engine, workers with leases/fencing, side-effect
safety, AI runtime behind a policy gate, RAG, governance, observability, SDK + dashboard, Docker /
Kubernetes / Terraform on AWS, Kafka where justified, benchmarks and failure injection.
Kafka and microservices are introduced only when a measured need justifies them.

## Planned architecture (proposed, not built)
- Modular monolith (FastAPI) + separate worker process(es).
- PostgreSQL = source of truth (state, events, leases, idempotency ledger, audit).
- Redis only for cache / rate limiting if needed (never the source of truth).

## Key invariants (from the guide)
1. Every resource access is tenant-scoped and authorized server-side.
2. A workflow definition is immutable once a run references its version.
3. State transitions are validated; invalid transitions are rejected.
4. Workers may execute a task more than once; business effects must be idempotent or reconciled.
5. Leases expire; a stale worker must not commit after losing ownership.
6. High-impact tool actions are authorized by deterministic policy, never by the model.
7. Every run has bounded time, token, cost, concurrency and tool-call budgets.
8. Execution history is enough to explain what happened and to recover.

## Unknowns
- Exact stack versions, auth provider and deployment target — decided when each phase starts.
