---
id: "pkis:framework:interval-algebra"
aliases: []
title: "Interval Algebra"
knowledge_type: framework
also_type: [concept]
domain: [knowledge-representation]
tags: [temporal-reasoning, qualitative-reasoning, constraint-networks, ai-planning, allen-interval-algebra]
related_concepts: ["[[temporal-logic]]", "[[constraint-propagation]]", "[[temporal-interval-logic]]"]
sources: ["[[vilain-reasoning-time-1982]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A formal system for representing and reasoning about temporal relationships between time intervals using a set of primitive relational operators. Vilain (1982) introduced the earliest computational realization using 13 primitive relations (before, after, during, contains, begins, begun-by, ends, ended-by, overlaps, overlapped-by, equals) that collectively cover all possible ways two intervals can be related. Allen (1983) later extended and formalized this into what became known as Allen's interval algebra. Deductions proceed via composition rules (169 total, one per pair of primitives) forming a semiring-like algebraic structure that enables polynomial-time (O(n³)) transitive closure computation. Classification note: assigned as framework because interval algebra is a coherent organizing system for temporal representation and inference; also_type concept because it is a well-defined mathematical object.

## Reading Path
- [[vilain-reasoning-time-1982]] (unread) — original AAAI 1982 paper introducing interval-based temporal reasoning with 13 primitives, composition rules, consistency maintenance, and extension to time points and absolute dates
