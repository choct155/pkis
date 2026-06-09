---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
- optimization
id: pkis:principle:log-scale-computation
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch10
tags:
- numerical-stability
- overflow
- underflow
- log-density
- implementation
title: Log-Scale Computation
understanding: 0
---

## Definition
To avoid computational overflow and underflow, one should compute with the LOGARITHMS of densities (and probabilities) whenever possible, exponentiating only when necessary and as late as possible. Posterior densities are products of many factors (prior times likelihood over many data points), so their raw values can be astronomically small or large and lose all floating-point precision; working in log space turns these products into numerically stable sums. A canonical instance is the Metropolis acceptance ratio of two densities: rather than forming each density and dividing, compute the ratio as the EXPONENTIAL OF THE DIFFERENCE of the two log-densities. This is a general implementation discipline underlying essentially all practical probabilistic computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]