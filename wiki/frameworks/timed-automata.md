---
aliases: []
also_type:
- concept
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- formal-methods
- systems-theory
id: pkis:framework:timed-automata
knowledge_type: framework
maturity: settled
related_concepts:
- discrete-event-systems
- finite-automata
- timed-petri-nets
- hybrid-systems
sources:
- '[[cassandras-des-intro]]'
- cassandras-des-intro-ch01
- cassandras-des-intro-ch05
- cassandras-des-intro-ch06
tags:
- timed-automata
- clock-constraints
- guards
- reachability
- real-time-systems
- hybrid-systems
title: Timed Automata
understanding: 0
---

Timed automata (in the sense of Cassandras-Lafortune) are finite automata extended with deterministic clock structures assigning timing to events, enabling modeling of when events occur; the Alur-Dill variant adds real-valued clock variables with guard constraints enabling decidable reachability analysis and formal verification of real-time properties.

## Reading Path
- [[cassandras-des-intro-ch05]] (unread) — primary treatment: clock structures, event-timing dynamics, timed automata with guards (Alur-Dill), parallel composition, untiming, hybrid automata