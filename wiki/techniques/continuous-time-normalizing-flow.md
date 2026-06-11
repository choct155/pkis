---
aliases: []
also_type: []
analogous-to:
- diffusion-processes
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
- differential-equations
- generative-models
id: pkis:technique:continuous-time-normalizing-flow
instantiates:
- normalizing-flows
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- neural-ODE
- FFJORD
- flow-matching
- continuous-normalizing-flow
title: Continuous-Time Normalizing Flow (Neural ODE Flow)
understanding: 0
uses:
- instantaneous-change-of-variables
- hutchinson-trace-estimator
---

## Definition
A continuous-time flow defines $x(T)$ as the solution at time $T$ of the ODE
$$\frac{dx}{dt}(t) = F(x(t), t),$$
starting from $x(0) = u \sim p(u)$. The log Jacobian determinant evolves as
$$\frac{dL}{dt}(t) = \mathrm{tr}[J(F(\cdot,t))(x(t))],$$
and is solved simultaneously with the state ODE (**instantaneous change-of-variables formula**). Inversion is free: re-run the ODE backward in time. The **neural ODE** parameterises $F$ with a neural net and uses the **adjoint sensitivity method** for gradient computation; **FFJORD** adds the Hutchinson trace estimator for scalable training.

### Why it matters
Continuous-time flows eliminate the discrete layering constraint, offering architecturally flexible bijections, symmetric forward/inverse cost, and connections to physics-based dynamics. They underpin modern flow-matching / score-based methods.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[diffusion-processes]] — analogous-to
- [[hutchinson-trace-estimator]] — uses
- [[instantaneous-change-of-variables]] — uses
- [[normalizing-flows]] — instantiates
[To be populated during integration]