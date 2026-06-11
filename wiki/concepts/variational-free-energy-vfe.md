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
- machine-learning
- bayesian-inference
- physics
id: pkis:concept:variational-free-energy-vfe
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
tags:
- variational-free-energy
- ELBO
- KL-divergence
- free-energy-principle
title: Variational Free Energy
understanding: 0
---

## Definition
$$\mathcal{F}(\theta,\psi|x) = \mathbb{E}_{q_\psi(z)}[E_\theta(z)] - \mathbb{H}(q_\psi) \geq -\log p_\theta(x)$$

where $E_\theta(z)=-\log p_\theta(z,x)$ is the **energy**. The variational free energy (VFE) is the physics dual of the negative ELBO: minimizing the VFE is equivalent to maximizing the ELBO and minimizes $D_{\mathrm{KL}}(q_\psi\|p_\theta(\cdot|x))$. The VFE equals the free energy $-\log p_\theta(x)$ only when $q=p$ (zero KL).

### Why it matters
The physics framing connects VI to statistical mechanics (Helmholtz free energy minimization) and to predictive-coding / active-inference formulations of the brain (where minimizing VFE drives both perception and action). It also clarifies that VI provides an upper bound on the negative log-evidence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]