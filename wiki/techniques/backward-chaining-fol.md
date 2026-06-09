---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:technique:backward-chaining-fol
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch09
tags:
- first-order-logic
- logical-inference
- logic-programming
- russell-norvig-aima
title: Backward Chaining (First-Order)
understanding: 0
---

## Definition
A goal-directed inference algorithm over definite clauses that works backward from a query, treating it as AND/OR search: a goal can be proved by any rule whose head unifies with it (OR), and all conjuncts in that rule's body must then be proved (AND). Implemented as a generator over substitutions; it is depth-first with linear space but, unlike forward chaining, suffers from repeated states and incompleteness (infinite loops).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]