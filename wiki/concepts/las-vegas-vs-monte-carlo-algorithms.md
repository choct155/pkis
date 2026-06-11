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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- algorithms
- statistics
generalizes:
- monte-carlo-estimator
id: pkis:concept:las-vegas-vs-monte-carlo-algorithms
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
tags:
- randomized-algorithms
- monte-carlo
- approximation
- computational-complexity
title: Las Vegas vs Monte Carlo Algorithms
understanding: 0
---

## Definition
$$\text{Las Vegas: } \Pr[\text{output is correct}] = 1, \quad \text{cost} \sim \text{random}$$
$$\text{Monte Carlo: } \text{output} \approx \text{correct with random error}, \quad \text{cost fixed}$$

Randomized algorithms split into two families: Las Vegas algorithms always return the exact answer but consume random resources (time/memory), while Monte Carlo algorithms return answers whose error can be reduced by spending more computation.

### Why it matters
This dichotomy clarifies when approximation is a design choice versus a necessity. Most ML inference problems are intractable, ruling out exact Las Vegas solutions and forcing Monte Carlo or deterministic approximations. Understanding the trade-off guides algorithm selection: Monte Carlo methods trade correctness guarantees for bounded computational budgets.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[monte-carlo-estimator]] — generalizes: Monte Carlo algorithms as a class encompass all Monte Carlo estimators
[To be populated during integration]