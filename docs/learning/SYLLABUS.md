# NEXUS Roadmap: every step

No calendar, no cuts. This covers **every part of the NEXUS Engineering Master Guide** (computer
architecture → OS → networks → DSA → databases → distributed systems → AI → security → languages →
software design → cloud/ops) and **every NEXUS phase (0–9)**, in an order where each foundation
comes right before the NEXUS component that uses it. Target pace: about 5 months (ADR-004); the pace
flexes, the content doesn't.

## How a step works
1. **Learn**: Claude explains the concept down to internals and failure modes (fast revision if you
   already know it) and gives 1–2 videos or primary docs, verified at the time we reach the step.
2. **You**: answer check questions and write the pseudocode / design.
3. **Claude builds**: code + tests from your pseudocode, committed and pushed to GitHub.
4. **Exit check**: you explain the result and one way it fails. 🟢 = next step; 🟡/🔴 = repeat.

🧪 **Test steps** (end of every stage): you hand-write code with no AI, under time limits, the way
interviews run. Real-world projects (Stage Z) are also hand-coded by you. Claude calls you for both.

Notation: `Learn → You → Build ✓ Exit`. "Lab" = a standalone experiment in `labs/`; everything else
lands in NEXUS itself.

---

## Stage A: Failure models and NEXUS design (guide Part I, Phase 0)
- **A1** System models, two generals (Kleppmann 2.1, 2.3) → 3 check questions + refund workflow pseudocode → skeleton ✅ + `PROBLEM.md` ✓ explain why a timeout ≠ failure
- **A2** Delivery guarantees: at-most / at-least / effectively-once → map each refund step to a guarantee → `GUARANTEES.md` ✓ choose a guarantee per step and defend it
- **A3** Idempotency keys (Brandur; Stripe *Idempotent requests*) → ledger states + retry behaviour pseudocode → in-memory idempotency ledger + tests ✓ walk a retry through every state
- **A4** Timeouts, retries, backoff + jitter (AWS Builders' Library) → classify errors transient / terminal / ambiguous → error taxonomy + retry policy + tests ✓ explain retry storms
- **A5** Durable execution: history, replay, determinism (Temporal *How it works*) → `WorkflowRun` / `TaskExecution` states → `STATE_MACHINES.md` ✓ name an invalid transition and why
- **A6** Requirements and NFRs (guide Appendix C) → fill availability, latency, durability, cost, scale targets → `NFR.md` ✓ justify each number
- **A7** Agent threat model (OWASP LLM01, LLM06) → trust boundaries + 5 abuse cases → `THREAT_MODEL.md` ✓ why the model can't authorize itself
- **A8** Domain model: the 11 core entities and 8 invariants → entity relationships → ERD draft ✓ trace an invariant to the entity that enforces it
- **A9** Architecture: modular monolith vs services, C4 model → component list → C4 context + container diagrams ✓ defend the monolith + worker split
- **A10** ADR writing → write ADR for the core design → ADR review ✓ explain alternatives rejected
- **A🧪** Hand-write: a retry function with capped exponential backoff + full jitter, and its tests

## Stage B: Computer architecture (guide Part II)
- **B1** Binary, hex, two's complement, overflow, endianness → predict outputs → Lab: base converter + bit masks + signed overflow demo (C) ✓ explain overflow at the bit level
- **B2** Boolean algebra, adders, multiplexers, latches, flip-flops → draw a 4-bit adder → Lab: logic-gate simulator ✓ combinational vs sequential
- **B3** CPU: ALU, registers, fetch-decode-execute, ISA vs microarchitecture → trace an instruction → CPU cycle diagram ✓ walk one instruction through the pipeline
- **B4** Compilation and assembly: calls, stack frames, addressing modes → read assembly → Lab: compile C at `-O0` vs `-O2`, annotate assembly ✓ explain what the optimizer did
- **B5** Stack vs heap, pointers, memory layout → predict addresses → Lab: address inspection + recursion depth ✓ where each variable lives
- **B6** Cache hierarchy, cache lines, locality → predict benchmark results → Lab: sequential vs random traversal benchmark ✓ explain the measured gap
- **B7** Associativity, false sharing → design a false-sharing case → Lab: false-sharing benchmark with threads ✓ fix it and measure
- **B8** Virtual memory, TLB, page faults, mmap → trace an address translation → Lab: mmap a file, count page faults ✓ explain TLB misses
- **B9** Branch prediction, pipelining, superscalar, SIMD → predict sorted vs unsorted branch cost → Lab: branch prediction benchmark ✓ explain the result
- **B10** Allocators: free lists, alignment, fragmentation → allocator design → Lab: simple free-list allocator + tests ✓ explain fragmentation in your allocator
- **B11** Profiling: CPU time, hardware counters, flame graphs → hypothesis first → Lab: profile a slow program, fix the hotspot ✓ evidence-based optimization story
- **B🧪** Hand-write: bit-manipulation problems (count bits, power of two, single number) + an LRU cache

## Stage C: Operating systems and Linux (guide Part III)
- **C1** Kernel vs user space, system calls → trace a file read → Lab: `strace`/`dtruss` a file read ✓ explain the mode switch
- **C2** File descriptors, signals, exceptions, interrupts → signal handling design → Lab: signal handler + graceful exit ✓ explain SIGTERM vs SIGKILL
- **C3** Processes, fork/exec, wait, zombies → process tree pseudocode → Lab: parent-child program ✓ how a zombie appears and is reaped
- **C4** Build a shell → parser + pipeline pseudocode → Lab: shell with args, pipes, exit status ✓ explain how a pipe connects processes
- **C5** Threads vs processes, context switching cost → measure plan → Lab: context-switch cost benchmark ✓ CPU-bound vs I/O-bound
- **C6** Scheduling: fairness, preemption, run queues, Linux CFS/EEVDF concepts → scheduling scenarios → notes + diagram ✓ explain priority inversion
- **C7** Race conditions, atomicity, memory visibility → design a race → Lab: reproduce a race under load, then fix it ✓ explain why it raced
- **C8** Mutexes, RW locks, semaphores, condition variables → bounded-buffer pseudocode → Lab: bounded producer-consumer queue ✓ explain spurious wakeups
- **C9** Thread pool → pool design → Lab: thread pool with bounded queue + shutdown ✓ explain backpressure in your pool
- **C10** Deadlock: the four conditions, avoidance, detection → construct one → Lab: deadlock + lock-ordering fix ✓ break each condition
- **C11** Lock-free concepts, CAS, starvation, contention → CAS counter pseudocode → Lab: CAS vs mutex benchmark ✓ ABA problem
- **C12** Async I/O vs parallelism, event loops, readiness → event-loop pseudocode → Lab: tiny event loop with `select`/`kqueue` ✓ why async ≠ parallel
- **C13** Memory management: paging, COW, swapping, malloc → COW scenario → Lab: COW observation after fork ✓ explain memory pressure
- **C14** Filesystems: inodes, links, page cache, fsync, journaling → durability scenario → Lab: write + fsync durability test ✓ what fsync guarantees
- **C15** IPC: pipes, Unix sockets, shared memory, message queues → pick IPC for NEXUS worker ↔ supervisor → Lab: Unix-socket IPC ✓ defend the choice
- **C16** `/proc`, `/sys`, limits → inspection plan → Lab: inspect a process's status, fds, maps, limits (Docker Linux) ✓ read a process's state
- **C17** Namespaces, cgroups, capabilities, seccomp → isolation design for tool execution → Lab: namespace-isolated process with cgroup limits ✓ container ≠ VM
- **C18** NEXUS: worker process lifecycle, concurrency limits, cancellation, SIGTERM draining → worker supervisor pseudocode → worker supervisor skeleton + tests ✓ drain without losing tasks
- **C🧪** Hand-write: thread-safe bounded blocking queue + a multithreaded counter with correct locking

## Stage D: Computer networks (guide Part IV)
- **D1** Encapsulation, OSI vs TCP/IP → trace one HTTP request down the layers → diagram ✓ what each layer adds
- **D2** Ethernet, MAC, ARP, switches → LAN delivery trace → notes ✓ router vs switch
- **D3** IP, CIDR, routing tables, NAT → subnet exercises → Lab: subnet calculator ✓ explain NAT port mapping
- **D4** TCP handshake, sequence numbers, retransmission → handshake trace → Lab: capture in Wireshark ✓ explain a retransmission
- **D5** Flow control, congestion control, head-of-line blocking → scenarios → notes ✓ why HOL blocking hurts HTTP/1.1 and HTTP/2-over-TCP
- **D6** UDP, sockets, ports → echo server design → Lab: TCP + UDP echo servers ✓ when to choose UDP
- **D7** Blocking I/O vs epoll/kqueue → server design → Lab: compare blocking vs event-driven server under load ✓ explain the C10k problem
- **D8** DNS: records, recursion, TTL, caching → resolution trace → Lab: `dig +trace` capture ✓ explain a stale-DNS incident
- **D9** TLS: certificates, CAs, handshake → handshake trace → Lab: capture TLS handshake + inspect a cert chain ✓ what TLS does and doesn't protect
- **D10** HTTP semantics: methods, status codes, caching, idempotent methods → API semantics for NEXUS → Lab: raw HTTP/1.1 server over sockets ✓ which methods are idempotent and why
- **D11** HTTP/2 multiplexing, HTTP/3 over QUIC → comparison → notes ✓ what QUIC fixes
- **D12** Cookies, sessions, CORS, CSRF, same-origin → threat cases → notes ✓ CSRF vs CORS
- **D13** WebSockets, SSE, gRPC → pick for NEXUS live run updates → Lab: SSE endpoint streaming run events ✓ defend SSE
- **D14** Reverse proxies, L4 vs L7 load balancing, health checks, draining, sticky sessions → proxy design → Lab: reverse proxy over two backends with health checks ✓ explain connection draining
- **D15** CDNs, cache-control, invalidation → caching policy → notes ✓ when not to cache
- **D16** Latency, throughput, jitter, tail latency, timeout budgets, connection pools, keep-alive → budget for a NEXUS request → timeout-budget doc ✓ explain deadline propagation
- **D17** Failure simulation: latency, loss, resets → experiment plan → Lab: inject faults (toxiproxy / `tc` in Docker), observe clients ✓ explain each observed failure
- **D🧪** Hand-write: minimal HTTP/1.1 request parser + a rate-limited TCP server

## Stage E: Data structures, algorithms, math (guide Part V, Part XII DSA sequence)
- **E1** Complexity: O/Ω/Θ, amortized analysis → analyse given code → notes ✓ prove amortized O(1) append
- **E2** Dynamic array → growth policy → Lab: dynamic array + benchmark ✓ why doubling
- **E3** Linked lists → pointer manipulation → Lab: list with deletion + reversal ✓ when lists beat arrays
- **E4** Hash tables: hashing, collisions, load factor, resizing → design → Lab: hash map (chaining + open addressing) ✓ explain resize cost → NEXUS: tool registry + idempotency prototype
- **E5** Stacks, queues, deques → implementations → Lab: ring-buffer queue ✓ ring-buffer full vs empty
- **E6** Binary heap / priority queue → sift-up/down, heapify → Lab: heap + invariant tests ✓ prove heapify is O(n) → NEXUS: priority scheduler
- **E7** BST and balanced trees (AVL / red-black) → rotations → Lab: AVL tree ✓ why balancing matters
- **E8** B-tree / B+ tree → node split/merge, page layout → Lab: B+ tree with range scan ✓ why databases use B+ trees
- **E9** Tries → prefix search → Lab: trie + compressed trie ✓ memory tradeoff → NEXUS: tool / capability lookup
- **E10** Union-Find → union by rank + path compression → Lab ✓ inverse Ackermann intuition → NEXUS: dependency grouping
- **E11** Segment / Fenwick trees → range query + update → Lab ✓ choose between them → NEXUS: time-window counters
- **E12** Sorting and selection, binary search on answers → problem set → Lab: quickselect ✓ search-space reasoning
- **E13** BFS, DFS, connected components, cycle detection → NEXUS DAG validator design → workflow DAG validator returning the cycle path + tests ✓ explain the colour-marking algorithm
- **E14** Topological sort (Kahn), SCCs → ready-task queue design → Kahn's algorithm + ready queue in NEXUS ✓ what Kahn's does with a cycle
- **E15** Shortest paths (Dijkstra, Bellman-Ford), MST → assumptions → Lab ✓ when Dijkstra breaks
- **E16** Longest path in a DAG / critical path → workflow duration estimate design → critical-path calculator in NEXUS ✓ why longest path is easy on DAGs
- **E17** Greedy, interval scheduling, exchange arguments → proofs → Lab ✓ prove one greedy choice
- **E18** Divide and conquer, recursion, backtracking, branch and bound → problem set → Lab ✓ pruning argument
- **E19** Dynamic programming: state design, memoization, tabulation → problem set → Lab ✓ define a DP state from scratch
- **E20** String matching: KMP, Rabin-Karp → implementations → Lab ✓ prefix function explanation
- **E21** Randomized algorithms, Bloom filters → false-positive math → Bloom filter dedup pre-check in NEXUS ✓ why it's never proof of existence
- **E22** Token bucket → refill, burst, clock handling → token-bucket limiter + burst tests ✓ token bucket vs leaky bucket
- **E23** Consistent hashing with virtual nodes → remapping experiment → Lab: measure key movement as workers join/leave ✓ why virtual nodes
- **E24** Cache policies: LRU, LFU, ARC → benchmark plan → Lab: LRU (hash map + doubly linked list) + policy benchmark ✓ hit rate vs memory
- **E25** Strict priority vs weighted fair queuing → scheduler comparison → Lab: WFQ scheduler + fairness measurement ✓ starvation under strict priority
- **E26** Discrete math: sets, relations, induction, invariants, proofs → prove a NEXUS invariant → proof write-up ✓ induction on state transitions
- **E27** Combinatorics + probability: Bayes, expectation, variance → problem set → notes ✓ explain a retry-amplification calculation
- **E28** Statistics: distributions, sampling, confidence intervals, hypothesis tests → benchmark statistics plan → Lab: compare two latency samples properly ✓ when a speedup is real
- **E29** Graph theory: cuts, flow → problem set → notes ✓ max-flow min-cut intuition
- **E30** Linear algebra: vectors, matrices, norms, projections, eigen concepts → exercises in NumPy → notebook ✓ cosine similarity geometrically
- **E31** Optimization and information theory: convexity, entropy, compression → exercises → notes ✓ explain cross-entropy loss
- **E🧪** Hand-write, timed: 6 LeetCode mediums + 2 hards (graphs, heaps, DP, intervals)

## Stage F: Databases and storage (guide Part VI)
- **F1** Relational model, keys, constraints → model NEXUS entities → ERD ✓ explain each constraint
- **F2** Normalization, functional dependencies, denormalization → normalize the ERD → revised ERD ✓ where you'd denormalize
- **F3** SQL depth: joins, CTEs, window functions, aggregates → query set over NEXUS data → query library + tests ✓ explain a window function
- **F4** Postgres in Docker, migrations tool choice → migration strategy → Postgres + migrations wired into NEXUS ✓ forward/backward compatibility
- **F5** Query plans: EXPLAIN/ANALYZE, cardinality estimates, scans → slow-query hypothesis → Lab: fix a slow query with an index ✓ read a plan aloud
- **F6** Storage engine: pages, slotted pages, buffer pool, dirty pages → page layout design → Lab: toy page-based record store ✓ explain eviction
- **F7** B+ tree indexes in practice, hash indexes, covering indexes → index plan for NEXUS → indexes + benchmarks ✓ when an index hurts
- **F8** Write-ahead logging, checkpoints, crash recovery → WAL design → Lab: toy append-only log + replay after simulated crash ✓ log-before-data rule
- **F9** ACID in practice → map to NEXUS writes → notes ✓ what "durable" means in Postgres
- **F10** Isolation levels and anomalies: dirty, non-repeatable, phantom, write skew → reproduce each → Lab: concurrent transactions showing lost update + write skew ✓ which level prevents which
- **F11** MVCC: snapshots, visibility, vacuum → visibility trace → Lab: observe xmin/xmax ✓ why vacuum exists
- **F12** Locking, deadlocks, optimistic concurrency with version columns → NEXUS run-update design → optimistic locking on runs + tests ✓ CAS update explained
- **F13** Unique constraints as concurrency control → idempotency ledger on Postgres → Postgres-backed idempotency ledger (replaces A3's in-memory one) ✓ why a unique index beats check-then-insert
- **F14** Online schema migration risks → migration plan for a column change → expand/contract migration ✓ zero-downtime steps
- **F15** Replication: sync vs async, lag, stale reads → read-routing design → notes ✓ read-your-writes problem
- **F16** Partitioning, sharding, hot partitions, rebalancing → shard key for tenants → design note ✓ hot-tenant mitigation
- **F17** Backups, PITR, restore drills → backup plan → Lab: backup + restore drill ✓ RPO vs RTO
- **F18** CAP and PACELC done right → classify NEXUS choices → notes ✓ what CAP does not say
- **F19** Data models: key-value, document, wide-column, graph, time-series → pick per NEXUS need → notes ✓ defend Postgres as source of truth
- **F20** Redis: data structures, persistence, eviction, replication → Redis role in NEXUS → Lab: Postgres vs Redis benchmark for two workloads ✓ why Redis isn't the source of truth
- **F21** Search: inverted indexes, tokenization, BM25 → BM25 by hand → Lab: BM25 search over documents ✓ explain the BM25 terms
- **F22** Vector search: distances, ANN, HNSW, IVF → HNSW pseudocode → Lab: toy HNSW + recall@k / latency / memory vs brute force ✓ recall-latency tradeoff
- **F🧪** Hand-write: 5 timed SQL problems (windows, CTEs, anti-joins) + an LSM vs B-tree design explanation on a whiteboard

## Stage G: NEXUS tenant-scoped API (Phase 1, guide 9.1 auth parts)
- **G1** Authentication vs authorization, sessions, token lifetimes → auth design → notes ✓ the difference in one sentence each
- **G2** OAuth 2.1 + OIDC flows → pick the flow for NEXUS → OIDC login against a dev identity provider ✓ walk through the authorization code + PKCE flow
- **G3** Tenants and principals → tenant model → tenant + principal tables + resolution middleware ✓ where tenant ID comes from and why not the client
- **G4** RBAC, ABAC, scopes, service identities → permission model → authorization layer + tests ✓ RBAC vs ABAC tradeoff
- **G5** Row-level security in Postgres → RLS policy design → RLS on tenant tables + cross-tenant tests failing closed ✓ defence in depth
- **G6** API design: resources, errors, pagination, idempotency headers, versioning → API contract → OpenAPI contract + error format ✓ cursor vs offset pagination
- **G7** Workflow-definition CRUD endpoints → handlers pseudocode → endpoints + tests ✓ immutability once referenced
- **G8** Password/secret storage, key rotation, audit trails → secret handling plan → audit-log table + secret config ✓ why audit logs are append-only
- **G9** Input validation and injection (SQLi, path traversal, SSRF) → abuse cases → validation + tests ✓ SSRF in tool adapters
- **G10** Exit criteria: authenticated, tenant-scoped API with tests → review → Phase 1 tag ✓ demo cross-tenant denial
- **G🧪** Hand-write: JWT verification + an RBAC check function with tests

## Stage H: NEXUS workflow core (Phase 2)
- **H1** Typed workflow definitions: nodes, edges, schemas → definition format → schema + parser ✓ why typed contracts
- **H2** Versioning and immutability → version design → versioned definitions + tests ✓ why a running version can't change
- **H3** DAG validation in the API (from E13) → integration → validation on create + error with cycle path ✓ error UX
- **H4** Run state machine (from A5) → transitions pseudocode → state machine with rejected invalid transitions ✓ property: no illegal path reachable
- **H5** Append-only event ledger, sequence numbers → event schema → events table + writer ✓ ordering guarantees
- **H6** Event sourcing: rebuild state from events → projection design → run projection + replay test ✓ when projections drift
- **H7** Deterministic local executor → executor loop pseudocode → in-process executor running a DAG ✓ determinism requirements
- **H8** Inputs/outputs and artifacts → artifact references → artifact store (local, object-store-ready) ✓ why store references not blobs
- **H9** Fan-out / fan-in, conditional edges → semantics → support + tests ✓ partial failure in fan-in
- **H10** Timers and deadlines → durable timer design → durable timers + tests ✓ clock choice
- **H11** Property-based tests for the engine → invariants list → Hypothesis tests ✓ which invariant caught a bug
- **H12** Exit criteria: valid DAG executes locally with deterministic transitions → review → Phase 2 tag ✓ demo
- **H🧪** Hand-write: topological sort with cycle reporting + a state-machine class, timed

## Stage I: Distributed systems theory (guide Part VII 7.1–7.5)
- **I1** Partial failure, partitions, slow nodes → failure catalogue for NEXUS → notes ✓ gray failure
- **I2** Latency distributions, p95/p99, tail amplification → fan-out math → notes ✓ why p99 matters with fan-out
- **I3** Clocks: wall vs monotonic, skew, NTP → clock usage audit of NEXUS → fixes ✓ never use wall clock for timeouts
- **I4** Logical clocks: Lamport, vector clocks (Kleppmann 4.x) → ordering exercises → Lab: vector clocks ✓ happens-before
- **I5** Consistency models: linearizable, sequential, causal, eventual, read-your-writes → classify NEXUS reads → notes ✓ linearizable vs serializable
- **I6** Broadcast and replication (Kleppmann 4–5) → exercises → notes ✓ total order broadcast = consensus
- **I7** Leader election, split brain → scenario → notes ✓ why two leaders happen
- **I8** Raft: terms, elections, log replication, safety → Raft pseudocode → Lab: toy Raft with tests under partitions ✓ explain log matching
- **I9** Paxos as a family; quorums, majority intersection → quorum math → notes ✓ why majorities intersect
- **I10** Service discovery, membership, gossip → design → notes ✓ SWIM-style failure detection
- **I11** Distributed locks: expiry, why fencing matters (Kleppmann vs Redlock) → lock scenario → notes ✓ the GC-pause scenario
- **I12** Leases, heartbeats, fencing tokens → lease design for NEXUS → design doc for Stage J ✓ stale owner rejected
- **I13** Transactional outbox / inbox → outbox design → design doc for Stage K ✓ dual-write problem
- **I14** Sagas and compensation → refund saga → saga design ✓ compensation vs rollback
- **I15** Circuit breakers, bulkheads, load shedding → policies → design notes ✓ breaker states
- **I16** Admission control, queue limits, backpressure → limits for NEXUS → design notes ✓ Little's law
- **I17** Work stealing, fair scheduling, tenant quotas → scheduler design → design notes ✓ noisy neighbour
- **I18** Graceful shutdown, draining, cancellation propagation → shutdown sequence → design notes ✓ cancellation tree
- **I🧪** Hand-write: Lamport clock + a lease manager with fencing tokens, with tests

## Stage J: NEXUS workers (Phase 3)
- **J1** Postgres queue with `FOR UPDATE SKIP LOCKED` → dequeue pseudocode → task queue + tests ✓ why SKIP LOCKED
- **J2** Separate worker process → worker loop → worker binary + supervisor (from C18) ✓ process boundaries
- **J3** Leases + heartbeats → lease renewal → leases + expiry reassignment + tests ✓ heartbeat interval vs lease length
- **J4** Fencing tokens → commit check → stale commit rejected + test ✓ demo the stale worker
- **J5** Retry policy with error classes (from A4) → integration → retries + dead-letter + tests ✓ poison task handling
- **J6** Cancellation → propagation → cancel API + cooperative cancellation ✓ cancel during side effect
- **J7** Priority + fair scheduling (from E6, E25) → integration → tenant-fair dequeue ✓ starvation test
- **J8** Graceful drain on SIGTERM → integration → drain + lease release ✓ deploy without lost work
- **J9** Concurrency limits per tenant and per tool → limits → semaphores in DB + tests ✓ distributed semaphore pitfalls
- **J10** Crash tests: kill -9 at every execution point → test plan → crash-injection test suite ✓ show zero lost tasks
- **J11** Exit criteria: worker crash recovery demonstrated in tests → review → Phase 3 tag ✓ demo
- **J🧪** Hand-write: a job queue with visibility timeout (SQS-style) in memory, with tests

## Stage K: NEXUS side-effect safety (Phase 5)
- **K1** Intent → attempt → external reference → outcome model → schema → execution ledger ✓ each state's meaning
- **K2** Tool adapter interface with idempotency keys → adapter contract → adapter base class + tests ✓ key derivation
- **K3** Fake payment provider with injected timeouts, 429s, 5xx, slow commits → provider design → fake provider ✓ every failure mode it produces
- **K4** Reconciliation of ambiguous outcomes → reconciler pseudocode → reconciler + tests ✓ the timeout-but-committed case
- **K5** Transactional outbox (from I13) → integration → outbox + relay ✓ no dual writes
- **K6** Inbox / dedup for incoming webhooks → design → inbox + tests ✓ duplicate webhook
- **K7** Saga for the refund workflow (from I14) → compensation steps → saga + tests ✓ partial failure walk-through
- **K8** Checkpointing and resume → checkpoint design → resume from checkpoint ✓ what isn't checkpointed
- **K9** Chaos run: thousands of refunds with injected failures → experiment → report: 0 duplicate refunds ✓ explain the numbers
- **K10** Exit criteria: ambiguous side-effect scenario safely handled → review → tag ✓ demo
- **K🧪** Hand-write: an idempotency-key middleware + a reconciliation loop, timed

## Stage L: ML and LLM foundations (guide 8.1–8.2)
- **L1** Vectors, matrices, matmul in NumPy → exercises → notebook ✓ shapes reasoning
- **L2** Probability for ML: distributions, likelihood → exercises → notebook ✓ MLE intuition
- **L3** Train/val/test, leakage, generalization → leakage scenarios → notes ✓ spot leakage
- **L4** Loss, gradient descent, backprop → backprop by hand → Lab: micrograd-style autograd ✓ chain rule on a graph
- **L5** Optimizers, overfitting, regularization, calibration → experiments → Lab ✓ calibration plot
- **L6** Neural network layers, activations, embeddings → MLP design → Lab: MLP from scratch ✓ why non-linearity
- **L7** Tokenization and BPE → BPE pseudocode → Lab: BPE tokenizer ✓ tokens ≠ words, cost implications
- **L8** Self-attention: Q/K/V, masking, multi-head → attention pseudocode → Lab: attention in NumPy with shape checks ✓ walk the shapes
- **L9** Positional info, residuals, layer norm → block diagram → Lab: one transformer block ✓ why residuals
- **L10** Pretraining, instruction tuning, preference optimization, fine-tuning → comparison → notes ✓ when to fine-tune vs prompt vs RAG
- **L11** Decoding: temperature, top-p, sampling → experiments → Lab ✓ determinism implications for NEXUS
- **L12** Context windows, KV cache, batching, quantization, inference latency → latency model → notes ✓ cost/latency math
- **L13** Capability, uncertainty, hallucination, prompt sensitivity → failure catalogue → notes ✓ why model output is untrusted data
- **L🧪** Hand-write: attention forward pass + BPE merge step in NumPy, timed

## Stage M: Retrieval-augmented generation (guide 8.3, 6.5)
- **M1** Ingestion, parsing, cleaning, metadata, permissions → pipeline design → ingestion pipeline ✓ permission metadata
- **M2** Chunking strategies → experiment plan → Lab: compare chunkers on recall ✓ chunk-size tradeoff
- **M3** Embedding model choice, normalization, distance metrics → comparison → Lab ✓ cosine vs dot product
- **M4** ANN in production (pgvector / HNSW) → index choice → vector store in NEXUS ✓ recall/latency/memory
- **M5** Hybrid search + reciprocal-rank fusion (BM25 from F21) → fusion design → hybrid retriever ✓ why RRF works
- **M6** Reranking, query rewriting, context assembly → pipeline → reranker stage ✓ context budget
- **M7** Tenant-aware, permission-aware retrieval → filter design → filtered retrieval + leak tests ✓ cross-tenant leak test
- **M8** Retrieval and groundedness evaluation (recall@k, citation correctness) → eval set → eval harness ✓ read the metrics
- **M9** NEXUS: evidence retrieval for the refund workflow → integration → evidence step ✓ demo grounded evidence
- **M🧪** Hand-write: BM25 scorer + RRF fusion, timed

## Stage N: NEXUS AI runtime and orchestration (Phase 4, guide 8.4)
- **N1** Agent vs workflow: probabilistic planning vs deterministic execution → boundary design → ADR ✓ where the line is
- **N2** Model adapters (provider-agnostic) → interface → adapters + fakes ✓ retry/timeout per provider
- **N3** Typed tool schemas + tool registry (from E4/E9) → schema design → registry ✓ risk classes
- **N4** MCP: protocol, tools, authorization → MCP integration design → MCP tool adapter ✓ trust boundary of an MCP server
- **N5** Planner proposes a typed plan → plan schema → planner + structured output validation ✓ invalid plan rejected
- **N6** Plan validation: graph, permissions, budget, risk → validator pseudocode → validator + tests ✓ each rejection reason
- **N7** Deterministic policy gate → policy language choice → policy engine + tests ✓ model can't grant itself permission
- **N8** Planner / executor / verifier / human roles → role design → verifier step ✓ verifier independence
- **N9** Model routing by capability, latency, cost, policy → router design → model router + budgets ✓ fallback chain
- **N10** Memory: short-term state vs long-term memory vs retrieval → boundaries → memory module ✓ what must never be in memory
- **N11** Multi-agent coordination: parallelism, shared state, conflicts → design → bounded multi-agent run ✓ conflict resolution
- **N12** LangGraph comparison → port one workflow → comparison note ✓ what NEXUS keeps outside the framework
- **N13** Exit criteria: model proposes, cannot bypass deterministic controls → review → Phase 4 tag ✓ demo
- **N🧪** Hand-write: a JSON-schema plan validator + a tiny policy evaluator, timed

## Stage O: AI safety and evaluation (guide 8.5)
- **O1** Direct and indirect prompt injection → attack catalogue → injection test corpus ✓ indirect via retrieved content
- **O2** Excessive agency, insecure tool use, data exposure → controls mapping → controls + tests ✓ least privilege per tool
- **O3** Output validation: model output as untrusted data → validation layer → tests ✓ schema + semantic checks
- **O4** Offline eval datasets, golden tests, regression → dataset design → eval suite ✓ dataset coverage
- **O5** Step-level vs trajectory-level evaluation → metrics → trajectory evaluator ✓ when step metrics lie
- **O6** LLM-as-judge and judge calibration → calibration plan → calibrated judge ✓ agreement with humans
- **O7** Cost–quality–latency tradeoffs, production feedback loops → dashboard design → eval reports in CI ✓ pick a model with data
- **O8** Red-team run: malicious retrieved instructions → experiment → report: unauthorized tool attempts blocked ✓ explain each block
- **O🧪** Hand-write: an eval runner computing accuracy + confusion matrix, timed

## Stage P: NEXUS governance (Phase 5)
- **P1** Human approval gates: pause, resume, expiry → approval flow → approvals API + tests ✓ approval expiry
- **P2** Budgets: time, tokens, cost, tool calls, concurrency → enforcement points → budget enforcement ✓ mid-step budget breach
- **P3** Rate limiting per tenant (token bucket from E22) → placement → limiter middleware ✓ distributed limiter pitfalls
- **P4** Admission control + backpressure (from I16) → policies → admission layer ✓ reject vs queue
- **P5** Tenant fairness under abuse → scenario → fairness tests ✓ one tenant floods
- **P6** Usage records and cost accounting → schema → usage ledger ✓ cost per run and per tenant
- **P7** Data retention, deletion, privacy boundaries → policy → retention jobs ✓ deletion vs audit tension
- **P8** Exit review → tag ✓ demo governance end to end
- **P🧪** Hand-write: sliding-window rate limiter + budget tracker, timed

## Stage Q: Security engineering (guide 9.1)
- **Q1** Threat modeling (STRIDE) for full NEXUS → update `THREAT_MODEL.md` ✓ residual risks
- **Q2** Hashing, HMAC, symmetric/asymmetric crypto → exercises → Lab: HMAC-signed webhooks ✓ HMAC vs signature
- **Q3** Signatures, PKI, certificates → cert chain lab → notes ✓ how trust is anchored
- **Q4** XSS, CSRF, SSRF, path traversal, insecure deserialization → audit NEXUS → fixes + tests ✓ SSRF in tool fetchers
- **Q5** Key management, secret rotation → rotation plan → rotation runbook ✓ rotation without downtime
- **Q6** Container hardening, network policies, supply-chain security (SBOM, pinning, signing) → plan → hardened image + SBOM ✓ supply-chain attack paths
- **Q7** Security review of NEXUS → checklist → review report ✓ top 3 risks
- **Q🧪** Hand-write: HMAC webhook verifier with constant-time compare + replay protection

## Stage R: Programming languages and runtimes (guide 9.2)
- **R1** Lexing, parsing, grammars, ASTs → NEXUS workflow DSL grammar → lexer + parser ✓ grammar ambiguity
- **R2** Interpreters → evaluator design → DSL interpreter producing workflow definitions ✓ AST walk
- **R3** Compilation, IR, bytecode → compile DSL to IR → Lab ✓ why an IR
- **R4** Static vs dynamic typing, type checking → type-check the DSL → type checker ✓ soundness intuition
- **R5** Garbage collection: refcounting, tracing, ownership → comparison → Lab: mark-and-sweep toy ✓ cycles and refcounting
- **R6** Python internals: bytecode, GIL, native extensions, free-threading → experiment → Lab: GIL contention benchmark ✓ when threads help in Python
- **R7** JavaScript event loop, tasks, microtasks, promises → ordering puzzles → notes ✓ predict output order
- **R8** Go goroutines, channels, scheduler → port a NEXUS hot path to Go only if profiling justifies → Lab ✓ M:N scheduling
- **R9** JIT and profiling → experiment → notes ✓ warm-up effects in benchmarks
- **R🧪** Hand-write: expression tokenizer + recursive-descent parser, timed

## Stage S: Software architecture and testing (guide 9.3)
- **S1** Modularity, cohesion, coupling → audit NEXUS modules → refactor plan ✓ worst coupling found
- **S2** SOLID, composition, dependency inversion → apply to adapters → refactor ✓ where DI helps
- **S3** Hexagonal architecture, ports and adapters → map NEXUS → restructure ✓ what's a port here
- **S4** DDD: bounded contexts, ubiquitous language → context map → doc ✓ context boundaries
- **S5** Design patterns used for real problems → catalogue NEXUS patterns → doc ✓ one pattern you removed
- **S6** API versioning, schema evolution, compatibility → policy → versioning + compatibility tests ✓ breaking vs non-breaking
- **S7** Testing pyramid: unit / integration / contract / e2e → test audit → contract tests ✓ test cost tradeoffs
- **S8** Property-based testing, fuzzing → targets → fuzz the DSL parser ✓ a fuzz finding
- **S9** Concurrency testing and chaos testing → targets → concurrency test harness ✓ flaky vs real race
- **S10** Code review, documentation, runbooks → review checklist → runbooks for top alerts ✓ runbook walkthrough
- **S🧪** Machine-coding round: design + hand-code a small system (e.g., rate-limited job scheduler) in 90 min

## Stage T: Observability (Phase 6, guide 10.3)
- **T1** Logs vs metrics vs traces → telemetry plan → structured logging with trace IDs ✓ which answers what
- **T2** OpenTelemetry instrumentation + context propagation → spans across API → worker → OTel tracing ✓ propagation across the queue
- **T3** RED and USE metrics → metric list → Prometheus metrics ✓ saturation signals
- **T4** Run timeline and cost per run → UI data model → run timeline endpoint ✓ explain a failed run from it
- **T5** SLIs, SLOs, error budgets, alert design → SLO doc → alerts with owners and runbooks ✓ burn-rate alerts
- **T6** Dashboards: rate, errors, p95/p99, queue age, worker saturation → Grafana dashboards ✓ read the dashboard
- **T7** Evaluation telemetry (from O) → integration → eval metrics in dashboards ✓ quality regression alert
- **T8** Exit criteria: operator explains a failed run from telemetry → drill → Phase 6 tag ✓ demo
- **T🧪** Hand-write: a percentile calculator over a stream (p50/p95/p99) + histogram buckets

## Stage U: Developer experience (Phase 7)
- **U1** SDK design → API surface → Python SDK ✓ ergonomic vs explicit
- **U2** Live status over SSE (from D13) → dashboard data flow → SSE status stream ✓ reconnection handling
- **U3** Dashboard (React + TypeScript) → screens → dashboard: runs, timeline, approvals ✓ demo
- **U4** Workflow version management UX → flows → version UI ✓ safe rollout of a new version
- **U5** Documentation site + examples (refund, support, billing) → docs plan → docs + examples ✓ a stranger can run the example
- **U6** Exit criteria: a developer can create and inspect a workflow → user test → Phase 7 tag ✓ demo
- **U🧪** Hand-write: SSE client with reconnect + last-event-id

## Stage V: Containers and Kubernetes (guide 10.1)
- **V1** Image layers, registries, tags, reproducible builds, scanning → Dockerfile design → multi-stage images + scan ✓ layer caching
- **V2** Runtime: namespaces, cgroups, capabilities (from C17) → hardening → non-root, read-only images ✓ what a container really is
- **V3** Kubernetes architecture: API server, etcd, scheduler, controllers, kubelet → trace a pod creation → notes ✓ reconciliation loops
- **V4** Pods, Deployments, StatefulSets, Services, Ingress → manifests → NEXUS on a local cluster (kind) ✓ Deployment vs StatefulSet
- **V5** ConfigMaps, Secrets, service accounts, RBAC, admission → config → secure config ✓ secret exposure paths
- **V6** Requests/limits, probes, autoscaling, PDBs, graceful termination → tuning → probes + HPA + PDB ✓ preStop and draining
- **V7** NetworkPolicies → policy design → policies ✓ default deny
- **V8** Persistent volumes, storage classes → Postgres on K8s vs managed → decision ✓ tradeoffs
- **V9** Helm charts → chart design → NEXUS Helm chart ✓ values design
- **V🧪** Hand-write: Deployment + Service + probes manifests from memory, then debug a broken pod

## Stage W: Cloud architecture and IaC (guide 10.2, Phase 8)
- **W1** Regions, AZs, VPCs, subnets, route tables, security groups → network design → diagram ✓ public vs private subnets
- **W2** IAM: roles, policies, workload identity, least privilege → IAM design → policies ✓ blast radius
- **W3** Compute choices: VMs, containers, managed Kubernetes → decision → ADR ✓ cost vs ops tradeoff
- **W4** Managed Postgres, object storage, caches, messaging → choices → ADR ✓ managed vs self-hosted
- **W5** Load balancers, DNS, certificates, private networking, egress control → design → diagram ✓ egress control for tools
- **W6** Secrets manager, KMS, audit logs, policy controls → design → configuration ✓ envelope encryption
- **W7** Terraform: state, modules, plans, drift → module design → Terraform for NEXUS ✓ remote state locking
- **W8** CI/CD: tests, scans, builds, deploys → pipeline design → GitHub Actions pipeline ✓ pipeline security
- **W9** Canary, blue-green, rolling deploys → strategy → canary deploy ✓ rollback trigger
- **W10** Backups restored in a test environment, DR drill → drill plan → DR runbook + drill ✓ measured RTO/RPO
- **W11** Exit criteria: repeatable deployment and recovery runbooks → review → Phase 8 tag ✓ demo
- **W🧪** Hand-write: a Terraform module for a VPC + security groups from memory

## Stage X: Event streaming with Kafka (guide 7.2)
- **X1** Queues vs logs, commands vs events → NEXUS event consumers → design ✓ when a log beats a queue
- **X2** Kafka topics, partitions, offsets, consumer groups, ordering scope → partition key design → Kafka in Docker + producer/consumer ✓ ordering per key only
- **X3** Replication, acks, ISR, retention → configuration → notes + config ✓ acks=all semantics
- **X4** Rebalances, offset commits, duplicate processing → scenario → idempotent consumer ✓ commit-before vs after processing
- **X5** DLQs, retry topics, poison messages, backpressure → design → retry/DLQ topology ✓ poison message handling
- **X6** Schema evolution and event versioning → schema registry choice → versioned events ✓ compatible change rules
- **X7** NEXUS: outbox relay → Kafka → analytics/cost consumers → integration → pipeline ✓ end-to-end exactly-once myth
- **X8** Broker outage experiment → plan → report ✓ backlog recovery
- **X🧪** Hand-write: a partitioned log with consumer-group offsets, in memory

## Stage Y: Validation and benchmarks (Phase 9, guide Part XII)
- **Y1** Benchmark methodology and reporting template → template → `benchmarks/README.md` ✓ what every report states
- **Y2** Throughput: stepped concurrency → harness → report ✓ the bottleneck found
- **Y3** Tail latency under sustained load → harness → p50/p95/p99/max report ✓ explain the tail
- **Y4** Worker crash at every execution point → harness → recovery-time + duplicate-effect report ✓ numbers explained
- **Y5** Broker / database outage and failover → harness → report ✓ ambiguous commit handling
- **Y6** Provider outage: timeouts, 429, 5xx → harness → fallback + retry amplification + cost report ✓ retry budget
- **Y7** Tenant abuse → harness → fairness + isolation report ✓ admission behaviour
- **Y8** Prompt-injection campaign → harness → blocked-attempts report ✓ residual risk
- **Y9** Database contention → harness → lock waits, deadlocks, throughput report ✓ fix and re-measure
- **Y10** Cost control → harness → cost per run, budget enforcement, completion rate ✓ cost story
- **Y11** Security review + production checklist (guide 10.4) → audit → signed-off checklist ✓ every item evidenced
- **Y12** Pilot: one narrow customer problem with measurable success → pilot plan → pilot report ✓ evidence of user value
- **Y🧪** Hand-write: a load generator with a fixed arrival rate (open model) + latency histogram

## Stage Z: Interview packaging and real-world project (you code)
- **Z1** README, architecture overview, demo video → polish → portfolio-ready repo ✓ stranger test
- **Z2** 5-minute and 15-minute design walk-throughs for every major component → scripts → recorded run-throughs ✓ clear under time
- **Z3** Failure-oriented deep dives: "what did you not build and why" → prep → Q&A doc ✓ mock grill
- **Z4** Mock system design interviews (NEXUS-adjacent and unrelated) → 6 mocks → feedback log ✓ consistent 🟢
- **Z5** Mock coding rounds (DSA + machine coding) → 10 mocks → feedback log ✓ consistent 🟢
- **Z6** Behavioural stories (STAR) from SureBright + NEXUS → story bank → doc ✓ Amazon LP coverage
- **Z7** Resume bullets with measured numbers → draft → final resume ✓ every claim backed by a report
- **Z8+** Real-world project, hand-coded by you, picked from what's in demand at the time

## Main references (from the guide, Part XV)
- *Computer Systems: A Programmer's Perspective*; *Operating Systems: Three Easy Pieces* (pages.cs.wisc.edu/~remzi/OSTEP); Linux man-pages; kernel docs
- *Computer Networking: A Top-Down Approach*; Beej's Guide to Network Programming; RFCs
- *Introduction to Algorithms* (CLRS); *Algorithms* (Sedgewick & Wayne)
- *Database System Concepts*; PostgreSQL docs; Redis docs
- *Designing Data-Intensive Applications*; Kleppmann's Cambridge *Distributed Systems* lectures (YouTube playlist `PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB`); Kafka, Temporal, Kubernetes, OpenTelemetry docs
- *Attention Is All You Need*; Full Stack Deep Learning; Hugging Face course; LangGraph docs; Model Context Protocol spec; OWASP Top 10 for LLM Applications
- AWS Well-Architected Framework; Terraform docs; Google SRE books
- Brandur Leach, *Implementing Stripe-like Idempotency Keys in Postgres*; AWS Builders' Library, *Timeouts, retries, and backoff with jitter*
