---
aliases: []
also_type: []
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
id: pkis:technique:constraint-propagation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[interval-algebra]]'
- '[[temporal-logic]]'
- '[[directed-graphical-models]]'
sources:
- '[[vilain-reasoning-time-1982]]'
- cimiano-ontology-nlp-ch07
tags:
- constraint-satisfaction
- inference
- consistency
- temporal-reasoning
- arc-consistency
- transitive-closure
title: Constraint Propagation
understanding: 0
---

A computational technique for maintaining consistency and deducing implicit information in a constraint network by iteratively applying composition rules to propagate known constraints across chains of related variables. In Vilain's (1982) temporal reasoning system, constraint propagation computes the transitive closure of interval relations: if A relates to B by R1, and B to C by R2, the composition rules derive A's relation to C, updating a complete picture of all pairwise interval relationships. The algebraic structure (resembling a semiring) over relational vectors enables this transitive closure in O(n³) time via a modification of Kleene's algorithm. Contradictions detected during propagation are resolved by backtracking and isolating the minimally inconsistent assertion set.

## Reading Path
- [[vilain-reasoning-time-1982]] (unread) — describes constraint propagation as the core deduction mechanism for temporal interval reasoning; includes consistency maintenance and contradiction detection