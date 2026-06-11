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
- statistics
- optimization
- machine-learning
id: pkis:result:bonnets-and-prices-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch06
tags:
- Gaussian
- natural-gradient
- expectation-gradient
- variational-inference
- exponential-family
title: Bonnet's Theorem and Price's Theorem
understanding: 0
---

## Definition
For $z \sim \mathcal{N}(m, V)$ and a sufficiently smooth function $\tilde{L}$:

**Bonnet's theorem:**
$$\frac{\partial}{\partial m_i}\mathbb{E}\!\left[\tilde{L}(z)\right] = \mathbb{E}\!\left[\frac{\partial \tilde{L}(z)}{\partial z_i}\right]$$

**Price's theorem:**
$$\frac{\partial}{\partial V_{ij}}\mathbb{E}\!\left[\tilde{L}(z)\right] = c_{ij}\,\mathbb{E}\!\left[\frac{\partial^2 \tilde{L}(z)}{\partial z_i\,\partial z_j}\right]$$
where $c_{ij} = \tfrac{1}{2}$ if $i=j$ and $c_{ij}=1$ otherwise.

Together these relate gradients of an expected loss w.r.t. Gaussian parameters to expectations of the loss's own derivatives.

### Why it matters
Bonnet's and Price's theorems provide closed-form, analytically tractable natural gradients for Gaussian distributions used in variational inference and natural evolutionary strategies. They show that the natural gradient of a Gaussian ELBO requires computing expectations of first- and second-order derivatives of the loss — linking information geometry to classical calculus of variations and enabling efficient gradient-based inference.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]