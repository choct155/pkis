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
- bayesian-stats
id: pkis:concept:marked-point-process
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- resnick-stochastic-processes-ch04
tags:
- stochastic-processes
- point-processes
- poisson-process
- marking
- marking-theorem
title: Marked Point Process
understanding: 0
---

## Definition
A marked point process attaches to each point X_n of a base point process an auxiliary random element (mark) J_n living in a second space E_2, producing the point process Σ_n ε_{(X_n, J_n)} on the product space E_1 × E_2. The marking theorem (Resnick Prop. 4.4.1 / 4.10.1) gives the key Poisson-preservation result: if Σ_n ε_{X_n} is PRM(μ) and the marks {J_n} are iid with common law F, independent of the base process, then Σ_n ε_{(X_n, J_n)} is PRM with mean measure μ × F. The result generalizes: full independence is not required — conditional independence via a transition kernel K(x, dy) suffices (the mark's law may depend on its own point but no others), giving mean measure μ_1(dx, dy) = μ(dx) K(x, dy). Marking enlarges the dimension of the points while retaining the Poisson structure, and is the engine behind thinning (Bernoulli/multinomial marks), compound Poisson and Lévy processes (real-valued jump marks), random translation of points, and record-value processes.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]