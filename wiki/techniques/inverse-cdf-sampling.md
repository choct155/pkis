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
- probability
- simulation
id: pkis:technique:inverse-cdf-sampling
instantiates:
- inverse-transform-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- rejection-sampling
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
tags:
- sampling
- quantile
- univariate
- exact-sampling
title: Inverse CDF Sampling (Inverse Probability Transform)
understanding: 0
---

## Definition
$$\text{If } U \sim \text{Unif}(0,1) \text{ and } F \text{ is a CDF, then } F^{-1}(U) \sim F.$$

To sample from any univariate distribution: draw $u \sim U(0,1)$, then return $x = F^{-1}(u)$ (the quantile function evaluated at $u$).

### Why it matters
Provides an exact, exact-in-distribution sampler for any univariate distribution whose inverse CDF (quantile function) is analytically tractable, e.g., exponential, Cauchy, logistic. It is a fundamental building block used within more complex samplers.

### Proof sketch
$\Pr(F^{-1}(U)\leq x) = \Pr(U \leq F(x)) = F(x)$, using monotonicity of $F$ and uniformity of $U$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[rejection-sampling]] — prerequisite-of
- [[inverse-transform-sampling]] — instantiates
[To be populated during integration]