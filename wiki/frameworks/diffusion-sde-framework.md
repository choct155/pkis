---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- stochastic-processes
- generative-models
id: pkis:framework:diffusion-sde-framework
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch25
tags:
- SDE
- ODE
- probability-flow
- score-function
- continuous-time
- Brownian-motion
title: Stochastic Differential Equation (SDE) Framework for Diffusion
understanding: 0
---

## Definition
The continuous-time generalisation of discrete diffusion models, written in Itô form:

$$dx = \underbrace{f(x,t)}_{\text{drift}}\,dt + \underbrace{g(t)}_{\text{diffusion}}\,dw$$

DDPM corresponds to the **variance-preserving** SDE $dx=-\frac{1}{2}\beta(t)x\,dt+\sqrt{\beta(t)}\,dw$; SGM corresponds to the **variance-exploding** SDE $dx=\sqrt{d[\sigma(t)^2]/dt}\,dw$. Anderson's (1982) reversal theorem gives the reverse-time SDE:

$$dx=\bigl[f(x_t,t)-g(t)^2\nabla_x\log q_t(x)\bigr]dt + g(t)\,d\bar w$$

where the unknown score $\nabla_x\log q_t(x)$ is approximated by the learned score network $s_\theta(x_t,t)$. Deterministic generation uses the **probability flow ODE** obtained by removing the Langevin noise term.

### Why it matters
Casting diffusion as an SDE unlocks the entire arsenal of numerical ODE/SDE solvers (Euler-Maruyama, Heun, DPM-Solver) for faster sampling, enables exact likelihood computation via the continuous normalizing flow perspective, and provides semantic latent-space interpolation through the deterministic ODE encoding.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]