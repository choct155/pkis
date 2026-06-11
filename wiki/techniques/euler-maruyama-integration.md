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
- numerical-methods
- stochastic-processes
id: pkis:technique:euler-maruyama-integration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- SDE
- numerical-integration
- diffusion-sampling
- stochastic-process
title: Euler-Maruyama Integration
understanding: 0
uses:
- brownian-motion
---

## Definition
The simplest discretisation of a stochastic differential equation $dx = f(x,t)dt + g(t)dw$:

$$x(t+\Delta t) = x(t) + f(x(t),t)\,\Delta t + g(t)\sqrt{\Delta t}\,\mathcal{N}(0,I)$$

It is the stochastic analogue of Euler's method for ODEs, with local truncation error $O(\Delta t^{3/2})$.

### Why it matters
Euler-Maruyama is the default numerical solver used to simulate and sample from continuous-time diffusion/SDE models. Understanding its error properties motivates the use of higher-order solvers (e.g., Heun's method, DPM-Solver) to reduce the number of function evaluations needed for high-quality diffusion samples.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[brownian-motion]] — uses
[To be populated during integration]