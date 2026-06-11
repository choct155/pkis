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
id: pkis:concept:semiparametric-gp
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch18
tags:
- GP
- trend
- mixed-model
- nonparametric
- Bayesian
title: Semiparametric GP
understanding: 0
---

## Definition
A **semiparametric GP** combines a parametric global mean (trend) model with a nonparametric GP residual:
$$g(x) = f(x) + \beta^T\phi(x), \quad f(x) \sim \mathcal{GP}(0, K), \quad \beta \sim \mathcal{N}(b, B)$$

Integrating out $\beta$ gives a new GP: $g(x) \sim \mathcal{GP}(\phi(x)^T b,\; K(x,x') + \phi(x)^T B\phi(x'))$. In the uninformative prior limit $B \to \infty I$, the posterior mean supplements the standard GP prediction with a GLS-type correction from the linear trend.

### Why it matters
Semiparametric GPs allow domain knowledge about global structure (e.g., linear trends, seasonal components) to be encoded parametrically while delegating local residual variation to a nonparametric GP. The posterior accounts for uncertainty in both the trend and the local function, providing better extrapolation than a pure GP with a zero mean function.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]