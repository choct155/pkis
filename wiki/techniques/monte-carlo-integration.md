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
- numerical-methods
id: pkis:technique:monte-carlo-integration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
tags:
- integration
- sampling
- variance
- CLT
- numerical
title: Monte Carlo Integration
understanding: 0
---

## Definition
$$\hat{\mu} = \frac{1}{N_s}\sum_{n=1}^{N_s} f(x_n), \quad x_n \sim p(x)$$

Approximates the expectation $\mu = E[f(X)] = \int f(x)p(x)dx$ by averaging function evaluations at random draws from $p$, concentrating effort where probability mass is non-negligible.

### Why it matters
Unlike quadrature on a fixed grid, the $O(1/\sqrt{N_s})$ error rate is theoretically dimension-independent (a consequence of the CLT), making it the dominant approach for high-dimensional integration in statistics, ML, and physics. The empirical standard error $\sqrt{\hat{\sigma}^2/N_s}$ provides a built-in uncertainty estimate.

### Accuracy
For independent samples, $(\hat{\mu}-\mu)\to N(0,\sigma^2/N_s)$ where $\sigma^2=V[f(X)]$. To achieve $\pm\epsilon$ accuracy at 95% confidence, $N_s \geq 4\hat{\sigma}^2/\epsilon^2$ samples suffice — regardless of the dimension of $x$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]