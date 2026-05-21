---
title: "Timed Automata"
knowledge_type: framework
also_type: [concept]
domain: [formal-methods, systems-theory]
tags: [timed-automata, clock-constraints, guards, reachability, real-time-systems, hybrid-systems]
related_concepts: [discrete-event-systems, finite-automata, timed-petri-nets, hybrid-systems]
sources: ["[[cassandras-des-intro]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

Timed automata (in the sense of Cassandras-Lafortune) are finite automata extended with deterministic clock structures assigning timing to events, enabling modeling of when events occur; the Alur-Dill variant adds real-valued clock variables with guard constraints enabling decidable reachability analysis and formal verification of real-time properties.

## Reading Path
- [[cassandras-des-intro-ch05]] (unread) — primary treatment: clock structures, event-timing dynamics, timed automata with guards (Alur-Dill), parallel composition, untiming, hybrid automata
