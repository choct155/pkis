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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:technique:particle-resampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- particle-filter
- resampling
- stratified
- systematic
- multinomial
- effective-sample-size
title: Resampling Methods for Particle Filters
understanding: 0
---

## Definition
Resampling converts a weighted particle set $\{(W^i, z^i)\}_{i=1}^N$ into an (approximately) equally-weighted set $\{z^{A_i}\}$ by drawing ancestor indices $A_{1:N}$ from the categorical distribution defined by $W^{1:N}$.

**Common schemes** (all unbiased in expectation):
- **Multinomial**: $N$ independent draws; variance $\propto \sum_i W_i(1-W_i)$.
- **Stratified**: sample one $U^i \sim \mathrm{Unif}((i-1)/N, i/N)$; reduces variance.
- **Systematic**: single $u \sim \mathrm{Unif}(0,1)$; $U^i = (i-1)/N + u/N$; lowest implementation cost.

**Adaptive resampling**: resample only when $\mathrm{ESS}(W^{1:N}) < N/2$, balancing weight degeneracy against path degeneracy.

### Why it matters
The choice of resampling scheme directly affects Monte Carlo variance; systematic resampling is empirically preferred. Adaptive resampling reduces unnecessary path degeneracy when weights are already near-uniform.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]