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
id: pkis:concept:weight-degeneracy-sis
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- particle-filter
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- particle-filter
- importance-sampling
- degeneracy
- effective-sample-size
title: Weight Degeneracy in Sequential Importance Sampling
understanding: 0
uses:
- effective-sample-size
---

## Definition
In sequential importance sampling (SIS) without resampling, the normalized weights $W_t^i$ concentrate on a single particle exponentially fast in $t$: as more observations are incorporated, all but the single best trajectory accumulate negligible weight.

**Cause**: each particle must explain the entire observation sequence $y_{1:t}$ as a product of likelihoods, so weight differences grow exponentially.

**Diagnosis**: the effective sample size $\mathrm{ESS}(W^{1:N}) = 1 / \sum_n (W^n)^2$ drops toward 1.

### Why it matters
Weight degeneracy is the fundamental failure mode motivating the resampling step in SISR/particle filters and the adaptive resampling strategy. Understanding it clarifies why the bootstrap filter needs at least $O(N)$ particles to track a nonlinear system, and motivates better proposals (guided filters).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[effective-sample-size]] — uses
- [[particle-filter]] — prerequisite-of
[To be populated during integration]