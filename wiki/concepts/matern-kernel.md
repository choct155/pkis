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
- statistics
- stochastic-processes
id: pkis:concept:matern-kernel
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch17
- murphy-pml2-advanced-ch18
tags:
- Matérn
- kernel
- smoothness
- GP
- Ornstein-Uhlenbeck
title: Matérn Kernel
understanding: 0
---

## Definition
The Matérn kernel is a stationary Mercer kernel parameterised by a smoothness parameter $\nu>0$ and length scale $\ell$:
$$K(r;\nu,\ell) = \frac{2^{1-\nu}}{\Gamma(\nu)}\left(\frac{\sqrt{2\nu}\,r}{\ell}\right)^\nu K_\nu\!\left(\frac{\sqrt{2\nu}\,r}{\ell}\right),$$
where $K_\nu$ is the modified Bessel function and $r=\|x-x'\|$. Sample paths are $k$-times mean-square differentiable iff $\nu>k$. Special cases:
- $\nu=\tfrac{1}{2}$: $K=\exp(-r/\ell)$ — continuous but non-differentiable (Ornstein-Uhlenbeck)
- $\nu=\tfrac{3}{2}$: $(1+\frac{\sqrt{3}r}{\ell})\exp(-\frac{\sqrt{3}r}{\ell})$
- $\nu=\tfrac{5}{2}$: $(1+\frac{\sqrt{5}r}{\ell}+\frac{5r^2}{3\ell^2})\exp(-\frac{\sqrt{5}r}{\ell})$
- $\nu\to\infty$: recovers the squared-exponential kernel

### Why it matters
The squared-exponential kernel produces infinitely smooth functions, often an unrealistically strong prior for real data. The Matérn family provides a principled spectrum of smoothness, with $\nu=5/2$ being a popular default in GP regression.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]