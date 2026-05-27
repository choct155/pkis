---
id: "pkis:concept:temporal-interval-logic"
aliases: []
title: "Temporal Interval Logic"
knowledge_type: concept
also_type: [framework]
domain: [knowledge-representation]
tags: [temporal-reasoning, interval-algebra, formal-logic, qualitative-reasoning, time]
related_concepts: ["[[interval-algebra]]", "[[temporal-logic]]", "[[constraint-propagation]]"]
sources: ["[[vilain-reasoning-time-1982]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A formal language for representing and reasoning about temporal relationships using intervals as the primary temporal primitives, rather than time points. Vilain (1982) presents an early instantiation using 13 primitive interval relations (before/after, during/contains, begins/begun-by, ends/ended-by, overlaps/overlapped-by, equals) combined into relational vectors for partial knowledge representation. The interval-based approach contrasts with point-based temporal logics (LTL, CTL) that take instants as primitives; intervals capture the duration and overlap structure of events more naturally for planning and natural language semantics. Classification note: assigned as concept (a defined formal language with specific semantics) but also_type framework (an organizing system for temporal inference and planning applications).

## Reading Path
- [[vilain-reasoning-time-1982]] (unread) — primary historical source; §2–3 present the 13 primitive interval relations, relational vectors, and composition rules; §4 extends to time points and absolute dates; predecessor to Allen (1983) interval temporal logic
