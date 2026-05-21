---
title: "Model Checking"
knowledge_type: technique
also_type: []
domain: [formal-methods, systems-theory]
tags: [model-checking, formal-verification, temporal-logic, automata-theory, state-space-exploration, reachability]
related_concepts: [discrete-event-systems, finite-automata, temporal-logic, supervisory-control]
sources: ["[[cassandras-des-intro]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Model checking is an automated formal verification technique that takes a finite-state model (automaton) of a system and a temporal-logic specification, and decides by exhaustive state-space exploration whether the model satisfies the specification; in DES, it is used to verify safety, liveness, and security (opacity) properties of controlled automata models.

## Reading Path
- [[cassandras-des-intro-ch02]] (unread) — DES model checking context: formal verification of automata models, connection to temporal logic specifications
