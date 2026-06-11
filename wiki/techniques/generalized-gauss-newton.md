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
- optimisation
- bayesian-inference
- deep-learning
id: pkis:technique:generalized-gauss-newton
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- Hessian
- Laplace-approximation
- positive-definite
- curvature
- KFAC
title: Generalized Gauss-Newton (GGN) Approximation
understanding: 0
---

## Definition
For a neural network $f(x,\theta)$ with Jacobian $J_{\theta}(x) \in \mathbb{R}^{C\times P}$ and per-input noise curvature $\Lambda(y;f) = -\nabla_f^2 \log p(y|f)$, the GGN approximation to the negative Hessian of the log-likelihood drops the second-derivative network term:
$$\hat{H}_{\text{GGN}} = \sum_{n=1}^{N} J_{\theta^*}(x_n)^T\, \Lambda(y_n; f_n)\, J_{\theta^*}(x_n)$$
This replaces the full Hessian (Eq. 17.15) used in the Laplace approximation and is guaranteed positive semi-definite.

### Why it matters
The true Hessian of a DNN log-likelihood is non-convex and may be indefinite, making the raw Laplace approximation numerically unstable. GGN is always PSD, cheaper to compute (no second-order network derivatives), and is the standard curvature surrogate in scalable Laplace approximations and natural-gradient methods (e.g., KFAC). The SWAG and VOGN methods also relate to GGN-style curvature estimates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]