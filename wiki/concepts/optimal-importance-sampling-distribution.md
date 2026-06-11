---
aliases: []
also_type: []
analogous-to:
- kl-divergence
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
- probabilistic-inference
extends:
- importance-sampling
id: pkis:concept:optimal-importance-sampling-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
tags:
- importance-sampling
- variance-reduction
- optimal-proposal
- monte-carlo
title: Optimal Importance Sampling Distribution
understanding: 0
---

## Definition
$$q^*(x) = \frac{p(x)|f(x)|}{Z}, \quad Z = \int p(x)|f(x)|\,dx$$

The variance-minimising proposal for the importance sampling estimator $\hat{s}_q = \frac{1}{n}\sum_i \frac{p(x^{(i)})f(x^{(i)})}{q(x^{(i)})}$. Under $q^*$, $\operatorname{Var}[\hat{s}_{q^*}] = 0$ when $f$ does not change sign (a single sample suffices in theory).

### Why it matters
Characterising $q^*$ makes explicit why good importance sampling proposals concentrate mass where $|p(x)f(x)|$ is large. The result is practically unattainable (computing $Z$ solves the original problem), but it motivates variance-reduction heuristics such as control variates, annealed IS, and learned proposals in amortized inference.

### Limitations in high dimensions
Simple proposal distributions $q$ fail to track $p|f|$ in high dimensions, causing catastrophic variance: rare events with $q(x) \ll p(x)|f(x)|$ produce enormous weights that dominate the estimator while typical samples waste computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kl-divergence]] — analogous-to: minimising IS variance is related to minimising a divergence between proposal and target
- [[importance-sampling]] — extends: characterises the variance-minimising proposal for IS
[To be populated during integration]