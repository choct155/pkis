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
- machine-learning
- differential-geometry
id: pkis:technique:riemann-manifold-hmc
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- hmc
- riemannian-geometry
- mass-matrix
- fisher-information
- adaptive-mcmc
title: Riemann Manifold HMC (RM-HMC)
understanding: 0
---

## Definition
An extension of HMC in which the inverse mass matrix $\Sigma(\theta)$ varies with position, making the kinetic energy position-dependent:
$$\mathcal{K}(\theta, v) = \tfrac{1}{2}\log[(2\pi)^D|\Sigma(\theta)|] + \tfrac{1}{2}v^T\Sigma(\theta)v$$
Natural choices for $\Sigma(\theta)$ are the local Hessian $\nabla^2\mathcal{E}(\theta)$ or the Fisher information matrix $\mathbb{E}_{p(x|\theta)}[-\nabla^2\log p(x|\theta)]$.

### Why it matters
When the target has highly variable curvature (e.g., hierarchical models with funnel geometry), a constant mass matrix forces a compromise between regions requiring small vs. large steps. RM-HMC adapts the step geometry locally, allowing much larger effective steps in low-curvature regions. The cost is that Hamilton's equations for $\theta$ and $v$ are no longer separable, requiring a more complex (generalised leapfrog) integrator and heavier per-step computation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]