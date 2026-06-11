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
- machine-learning
- optimization
- statistics
id: pkis:technique:distributionally-robust-optimization
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- robustness
- minimax
- covariate-shift
- worst-case-optimization
title: Distributionally Robust Optimization (DRO)
understanding: 0
---

## Definition
$$\min_{f\in\mathcal{F}}\max_{\mathbf{w}\in\mathcal{W}} \frac{1}{N}\sum_{n=1}^N w_n\,\ell(f(x_n),y_n)$$

Distributionally robust optimization (DRO) minimizes the worst-case weighted empirical risk over a robustness set $\mathcal{W}$ of sample-weight vectors, seeking a predictor that performs well under a family of distributions near the training distribution.

### Why it matters
DRO guards against covariate shift and spurious correlations by explicitly optimizing for the hardest re-weighting of the training data within $\mathcal{W}$. Common choices for $\mathcal{W}$ include an $\ell_2$-ball around the input, a KL-divergence ball in distribution space (CVaR), or perturbations defined by a structural causal model.

### Relation to other frameworks
DRO generalizes standard ERM (which sets all $w_n=1/N$) and is a special case of the min–max optimization paradigm. It is distinct from importance-weighted ERM in that the adversarial weights are chosen *pessimistically* rather than estimated from data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]