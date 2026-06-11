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
- statistics
- machine-learning
id: pkis:concept:incremental-importance-weights
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- importance-sampling
- particle-filter
- sequential-monte-carlo
title: Incremental Importance Weights
understanding: 0
---

## Definition
$$\alpha_t(z_{1:t}) = \frac{\tilde{\gamma}_t(z_{1:t})}{\tilde{\gamma}_{t-1}(z_{1:t-1})\, q_t(z_t|z_{1:t-1})}$$

The incremental importance weight is the one-step multiplicative update to an unnormalized particle weight: $\tilde{w}_t = \tilde{w}_{t-1} \cdot \alpha_t$. For a Markovian SSM it simplifies to $\alpha_t = p(y_t|z_{1:t})p(z_t|z_{t-1})/q_t(z_t|z_{t-1})$.

### Why it matters
Decomposing the weight update into increments enables the recursive weight computation that is central to all SMC algorithms. It also reveals the role of the proposal $q_t$: a proposal that closely matches the locally optimal $\pi_t(z_t|z_{1:t-1})$ makes $\alpha_t$ nearly constant across particles, maximising the ESS.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]