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
id: pkis:framework:petri-nets
knowledge_type: framework
maturity: settled
related_concepts:
- discrete-event-systems
- finite-automata
- supervisory-control
sources:
- '[[cassandras-des-intro]]'
- cassandras-des-intro-ch04
- cassandras-des-intro-ch05
tags:
- petri-nets
- concurrency
- reachability
- liveness
- marking
- tokens
- formal-methods
title: Petri Nets
understanding: 0
---

Petri nets are a graphical and mathematical formalism for modeling concurrent, distributed, and parallel systems, consisting of places (conditions), transitions (events), arcs (flow relation), and tokens (marking of places); they are strictly more expressive than finite automata for modeling concurrency but at the cost of decidability for general properties.

## Reading Path
- [[cassandras-des-intro-ch04]] (unread) — primary treatment: Petri net basics, markings, dynamics, languages, comparison with automata, coverability analysis, linear-algebraic techniques, supervisory control of Petri nets