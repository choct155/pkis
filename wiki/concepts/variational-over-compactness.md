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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:concept:variational-over-compactness
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch33
tags:
- variational-methods
- kl-divergence
- mode-seeking
- reverse-kl
- approximation-bias
title: Variational Over-Compactness (Zero-Forcing)
understanding: 0
---

## Definition
Approximations obtained by minimizing the variational free energy — equivalently the **reverse** KL divergence $D_{KL}(Q\|P)$ — systematically come out **more compact** (narrower) than the true distribution $P$. The asymmetry of KL is the cause: $D_{KL}(Q\|P)=\sum_x Q\ln(Q/P)$ pays an enormous penalty wherever $Q>0$ but $P\approx 0$, so $Q$ is forced to vanish off the support of $P$ (zero-forcing / mode-seeking).

### A precise example
Approximate an axis-skewed 2D Gaussian $P$ with variances $\sigma_1^2,\sigma_2^2$ by a spherical $Q$ of variance $\sigma_Q^2$. Minimizing $\tilde F = D_{KL}(Q\|P)$ gives

$$\frac{1}{\sigma_Q^2} = \tfrac12\!\left(\frac{1}{\sigma_1^2}+\frac{1}{\sigma_2^2}\right),$$

the **mean inverse variance**: $\sigma_Q$ tracks the *shortest* length scale of $P$. By contrast, minimizing the forward KL $G=D_{KL}(P\|Q)$ gives $\sigma_Q^2 = \tfrac12(\sigma_1^2+\sigma_2^2)$, the **mean variance**, which is mass-covering. For $\sigma_1{=}10,\sigma_2{=}1$: reverse KL gives $\sigma_Q\approx\sqrt2$, forward KL gives $\sigma_Q\approx 10/\sqrt2$.

### Why it matters
This bias is predictable and consequential: variational posteriors **understate uncertainty**. It explains why a VI posterior makes a poor importance-sampling proposal (a good proposal must be *heavier*-tailed than the target, not lighter). It is also a manifestation of premature concentration — fit dominating spread. Note that $G$ is usually not computable, since it requires expectations under the intractable $P$; this asymmetry is precisely why variational practice uses the reverse direction.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]