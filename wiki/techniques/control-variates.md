---
aliases: []
also_type: []
applies:
- reinforce
- variational-inference
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
- simulation
extends:
- monte-carlo-integration
id: pkis:technique:control-variates
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
tags:
- variance-reduction
- baseline
- stochastic-gradient
- REINFORCE
- MC-efficiency
title: Control Variates
understanding: 0
uses:
- covariance-and-correlation
---

## Definition
$$m^*(X) = m(X) + c\,(b(X) - E[b(X)])$$

Augments a Monte Carlo estimator $m(X)$ with a baseline $b(X)$ whose mean is known, with coefficient chosen optimally as
$$c^* = -\frac{\text{Cov}[m(X),b(X)]}{V[b(X)]}$$

yielding variance reduction factor $(1-\rho^2_{m,b})$.

### Why it matters
Provides an unbiased estimator with lower variance whenever $b$ is correlated with $m$. Widely used in stochastic optimization and variational inference (e.g., REINFORCE baseline, blackbox VI) to reduce gradient variance. The optimal $c^*$ can be estimated from the same samples used for the main estimate.

### Key formula
$$V[m^*(X)] = (1-\rho^2_{m,b})\,V[m(X)]$$

If $\rho^2_{m,b}\approx 1$, variance is nearly eliminated.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[covariance-and-correlation]] — uses
- [[variational-inference]] — applies
- [[reinforce]] — applies: Baseline in REINFORCE is a control variate
- [[monte-carlo-integration]] — extends
[To be populated during integration]