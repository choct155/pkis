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
- machine-learning
- generative-models
id: pkis:technique:residual-flow
instantiates:
- normalizing-flows
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- normalizing-flow
- residual-network
- iResNet
- Hutchinson-estimator
title: Residual Flow
understanding: 0
uses:
- residual-network
- hutchinson-trace-estimator
- weinstein-aronszajn-identity
---

## Definition
A residual flow is composed of invertible residual connections $f(u) = u + F(u)$. Invertibility is guaranteed when $F$ is a **contraction** (Lipschitz constant $L < 1$, by Banach's fixed-point theorem). The log Jacobian determinant is estimated via the power-series identity
$$\log|\det J(f)| = \sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k}\,\mathrm{tr}[J(F)^k],$$
which converges when $\|J(F)\| < 1$ and can be approximated efficiently using the **Hutchinson trace estimator**. The inverse is computed iteratively via $u_n = x - F(u_{n-1})$.

### Why it matters
Residual flows (e.g., **iResNet**) allow standard ResNet architectures to be used as flow layers by enforcing spectral normalisation. They impose no restriction on variable ordering, unlike autoregressive or coupling flows, and support the low-rank variant (Weinstein–Aronszajn identity) for $O(M^3)$-cost determinants when the residual block has an $M$-dimensional bottleneck.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weinstein-aronszajn-identity]] — uses
- [[hutchinson-trace-estimator]] — uses
- [[residual-network]] — uses
- [[normalizing-flows]] — instantiates
[To be populated during integration]