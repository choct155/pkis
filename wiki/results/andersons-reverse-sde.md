---
aliases: []
also_type: []
applies:
- diffusion-sde-framework
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
- stochastic-processes
- machine-learning
- generative-models
id: pkis:result:andersons-reverse-sde
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- score-based-generative-model
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- SDE
- reverse-diffusion
- score-function
- theoretical-result
title: Anderson's Reverse-Time SDE Theorem
understanding: 0
---

## Definition
**Theorem (Anderson 1982):** For any Itô SDE of the form $dx = f(x,t)dt + g(t)dw$ with marginal densities $\{q_t\}$, there exists an exact **reverse-time** SDE:

$$dx = \bigl[f(x_t,t) - g(t)^2\nabla_x\log q_t(x)\bigr]\,dt + g(t)\,d\bar w$$

where $\bar w$ is a Wiener process running backwards in time, $dt < 0$. The reverse process has the same marginals $\{q_t\}$ as the forward process.

### Why it matters
This theorem is the theoretical cornerstone of continuous-time diffusion generation: it guarantees that a learnable reverse diffusion process exists and that approximating the intractable score $\nabla_x\log q_t(x)$ with a neural network $s_\theta(x_t,t)$ is sufficient to generate exact samples (in the limit of perfect score estimation). It also establishes that the **probability flow ODE** (the deterministic counterpart) preserves the same marginals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[score-based-generative-model]] — prerequisite-of
- [[diffusion-sde-framework]] — applies
[To be populated during integration]