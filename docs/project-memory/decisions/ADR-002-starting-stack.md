# ADR-002 — Starting stack

- Date: 2026-11-12 · Status: Proposed

## Decision
Python 3.12+ / FastAPI for the API, PostgreSQL as source of truth (state, events, queue via
`FOR UPDATE SKIP LOCKED`, leases, idempotency ledger), separate worker process. Redis optional.

## Why
Matches the guide and Shivam's production experience (FastAPI, Azure OpenAI). Postgres-as-queue keeps
the first milestone to one durable store, so transactional guarantees are easy to reason about.

## Alternatives
Temporal/DBOS (would hide the internals we want to learn), Kafka (premature), Go (only if profiling
justifies it).
