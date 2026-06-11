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
- information-theory
- statistics
- machine-learning
id: pkis:concept:f-divergence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- divergence
- convex-analysis
- variational-bound
- f-GAN
title: f-Divergence
understanding: 0
---

## Definition
For a convex function $f$ with $f(1)=0$, the f-divergence between distributions $p^*$ and $q$ is:
$$D_f[p^*\|q]=\int q(x)\,f\!\left(\frac{p^*(x)}{q(x)}\right)dx$$
Special cases include KL ($f(u)=u\log u$), reverse-KL ($f(u)=-\log u$), and Jensen-Shannon ($f(u)=u\log u-(u+1)\log\frac{u+1}{2}$) divergences. The variational (Fenchel dual) lower bound is:
$$D_f[p^*\|q]\ge\sup_{t\in\mathcal{T}}\mathbb{E}_{p^*}[t(x)]-\mathbb{E}_q[f^\dagger(t(x))]$$
where $f^\dagger$ is the convex conjugate of $f$.

### Why it matters
f-Divergences unify a large family of distributional discrepancies under a single framework. The variational bound converts an intractable ratio-based divergence into a sample-based minimax objective, forming the basis of f-GANs and connecting proper scoring rules to distributional distances.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]