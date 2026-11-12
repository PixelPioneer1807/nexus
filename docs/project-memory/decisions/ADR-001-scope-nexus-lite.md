# ADR-001 — Scope: NEXUS-lite first

- Date: 2026-11-12 · Status: **Superseded by ADR-004** (Shivam rejected cutting scope)

## Context
The guide plans 10 phases over 9–12 months, including Kafka, Kubernetes and Terraform. The goal is a
strong SDE-2/SDE-3 interview story. Unfinished large projects hurt more than small finished ones.

## Decision
Build guide Phases 0–6 plus the benchmark/failure-injection program (Part XII) in ~12 weeks.
Production infra (Phase 8) only as Docker Compose + CI. Kafka/K8s/Terraform deferred.

## Alternatives
- Full guide plan: more breadth, high risk of never finishing.
- No project: weaker senior-level story.

## Consequences
Depth on durable execution and side-effect safety; less infra breadth. Revisit after Week 12.
