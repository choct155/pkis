---
aliases: []
also_type: []
applies:
- exponential-family
- variational-inference
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
- optimization
- information-geometry
extends:
- stochastic-gradient-descent
id: pkis:technique:natural-gradient-descent
instantiates:
- natural-gradient
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
tags:
- second-order
- Fisher-information
- Riemannian
- information-geometry
- preconditioning
title: Natural Gradient Descent
understanding: 0
uses:
- fisher-information
- kl-divergence
---

## Definition
Natural gradient descent (NGD) preconditions the gradient by the inverse Fisher information matrix (FIM):
$$\theta_{t+1} = \theta_t - \eta_t\, \mathbf{F}(\theta_t)^{-1}\, g_t, \qquad \tilde{\nabla} L(\theta) \triangleq \mathbf{F}^{-1}\nabla L(\theta)$$
where $\mathbf{F}(\theta) = \mathbb{E}_{p_\theta}\!\left[(\nabla_\theta \log p_\theta)(\nabla_\theta \log p_\theta)^\top\right]$. The update solves
$$\min_\delta\; L(\theta) + g_t^\top \delta \quad\text{s.t.}\quad \delta^\top \mathbf{F}\,\delta \leq \epsilon$$
which is a trust-region step measured by KL divergence between successive distributions.

For exponential families, the natural gradient w.r.t. natural parameters $\lambda$ equals the ordinary gradient w.r.t. moment parameters $\mu$: $\tilde{\nabla}_\lambda L = \nabla_\mu L$.

### Why it matters
NGD is invariant to reparameterization of $\theta$ and can navigate highly correlated or poorly scaled loss surfaces that stymie ordinary gradient descent. It converges faster on curved manifolds (Riemannian geometry) and is connected to trust-region methods, the Gauss-Newton method, and online Bayesian inference via the extended Kalman filter.

### Practical approximations
Exact FIM inversion is $O(p^3)$; practical variants include diagonal approximation, KFAC (Kronecker-factored approximate curvature), and Hessian-free optimization using conjugate gradients.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variational-inference]] — applies
- [[natural-gradient]] — instantiates
- [[exponential-family]] — applies
- [[kl-divergence]] — uses
- [[stochastic-gradient-descent]] — extends
- [[fisher-information]] — uses
[To be populated during integration]