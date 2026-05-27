---
id: "pkis:concept:temporal-logic"
aliases: []
title: "Temporal Logic"
knowledge_type: concept
also_type: [framework]
domain: [formal-methods, systems-theory]
tags: [temporal-logic, ltl, ctl, formal-verification, model-checking, specification]
related_concepts: [discrete-event-systems, finite-automata, model-checking]
sources: ["[[cassandras-des-intro]]", "[[vilain-reasoning-time-1982]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: settled
---

Temporal logic is a family of formal specification languages for expressing properties of system behavior over time — specifically, properties like "event A always eventually follows event B" (liveness) or "bad state S is never reached" (safety); in DES, temporal logic serves as the specification language for model checking and formal verification of automaton models.

Classification note: assigned as concept but also_type framework because temporal logic is both a mathematical concept (a class of logics with a semantics) and an organizing framework for formal specification and verification methodology.

## Reading Path
- [[cassandras-des-intro-ch02]] (unread) — temporal logic in the context of DES formal verification and model checking
- [[vilain-reasoning-time-1982]] (unread) — alternative, interval-based approach to temporal reasoning; the 13 primitive interval relations and composition rules represent a qualitative temporal algebra that pre-dates but complements propositional temporal logics; highlights the choice between point-based TL and interval-based relational approaches
