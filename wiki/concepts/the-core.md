---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- economics
id: pkis:concept:the-core
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- cooperative-game
- stability
- imputation
- individual-rationality
- linear-programming
title: The Core
understanding: 0
---

## Definition
The set of all *imputations* (payoff vectors that distribute the grand coalition's full value v(N) and satisfy individual rationality, x_i ≥ v({i})) such that x(C) ≥ v(C) for every coalition C — i.e., no coalition could profitably defect from the grand coalition. The core formalizes stability of the grand coalition: if an imputation is not in the core, some subset of players can do better on their own and will refuse to join. If the core is empty, the grand coalition cannot form at all (even superadditive games can have an empty core). The core is defined by an exponential system of linear inequalities, so checking non-emptiness takes exponential time in general (often co-NP-complete for specific game classes). The core says *when* a grand coalition can form, but not *how* its value should be divided fairly.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]