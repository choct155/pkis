---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- differential-equations
extends:
- change-of-variables-for-densities
id: pkis:result:instantaneous-change-of-variables
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- continuous-time-normalizing-flow
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- neural-ODE
- FFJORD
- continuous-normalizing-flow
- change-of-variables
title: Instantaneous Change-of-Variables Formula (Continuous Flows)
understanding: 0
---

## Definition
For a continuous-time flow defined by $\dot{x}(t) = F(x(t), t)$ and $L(t) = \log|\det J(f_t)(x_0)|$,
$$\frac{dL}{dt}(t) = \mathrm{tr}[J(F(\cdot,t))(x(t))].$$
Integrating from $0$ to $T$ with $L(0)=0$ gives the log Jacobian determinant of the full flow $f_T$.

### Why it matters
This ODE replaces the expensive $O(D^3)$ determinant computation of discrete flows with a trace-of-Jacobian computation that scales as $O(D)$ with the Hutchinson estimator, enabling continuous-time flows on high-dimensional data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[change-of-variables-for-densities]] — extends
- [[continuous-time-normalizing-flow]] — prerequisite-of
[To be populated during integration]