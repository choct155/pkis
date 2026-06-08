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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- deep-learning
extends:
- gradient-descent
id: pkis:technique:natural-gradient
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch34
tags:
- optimization
- covariance
- curvature
- gradient-descent
- mackay-itila
- information-geometry
title: Natural Gradient (Covariant Optimization)
understanding: 0
---

## Definition
The natural gradient is a covariant ascent direction obtained by preconditioning the ordinary gradient with a positive-definite metric $M$:

$$\Delta w_i = \eta \sum_{i'} M_{ii'}\,\frac{\partial L}{\partial w_{i'}},$$

where $M_{ii'}$ has dimensions $[w_i w_{i'}]$. This repairs a defect of plain steepest descent $\Delta w_i = \eta\,\partial L/\partial w_i$, which is *dimensionally inconsistent* and not covariant under rescaling of the parameters, so it can converge extremely slowly on ill-conditioned objectives.

### Where the metric comes from
A suitable $M$ can be drawn from a natural metric on parameter space or from the curvature $A \equiv -\nabla\nabla L$; taking $M=A^{-1}$ recovers the Newton step (exact in one step for quadratic $L$). When curvature has data-dependent and data-independent parts, one may build $M$ from the data-independent terms — still covariant, though no longer an exact Newton step.

### Application to ICA
Steepest ascent in $W$ for ICA is non-covariant and requires an awkward matrix inverse $[W^{T}]^{-1}$. Approximating the curvature gives the metric $M_{(ij)(kl)} = W_{mj}W_{ml}\delta_{ik}$, producing the inverse-free covariant rule $\Delta W_{ij} = \eta(W_{ij} + x'_j z_i)$ with $x'_j = W_{i'j}a_{i'}$ — the *natural gradient* version of ICA.

### Why it matters
Covariance is a design principle: a consistent algorithm should give the same results regardless of the units of measurement, and respecting it dramatically accelerates convergence on poorly-scaled problems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gradient-descent]] — extends: Natural gradient repairs the non-covariance and dimensional inconsistency of plain steepest descent via a metric preconditioner.
[To be populated during integration]