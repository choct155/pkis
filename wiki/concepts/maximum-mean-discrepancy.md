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
- kernel-methods
id: pkis:concept:maximum-mean-discrepancy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- kernel
- RKHS
- generative-model
- two-sample-test
- MMD
title: Maximum Mean Discrepancy
understanding: 0
---

## Definition
The maximum mean discrepancy (MMD) between distributions $p$ and $q$ is the IPM with $\mathcal{F}=\{f:\|f\|_{\mathcal{H}_K}\le 1\}$ for a reproducing kernel Hilbert space $\mathcal{H}_K$ with kernel $K$:
$$\mathrm{MMD}^2(p,q)=\mathbb{E}_{p}\mathbb{E}_{p'}K(x,x')-2\mathbb{E}_p\mathbb{E}_q K(x,y)+\mathbb{E}_q\mathbb{E}_{q'}K(y,y')$$
This can be estimated from samples without a separately trained critic. A learned kernel $K(\zeta_\phi(x),\zeta_\phi(x'))$ with an injective feature map $\zeta_\phi$ is also valid and leads to a minimax objective.

### Why it matters
MMD provides a closed-form (kernel-based) sample estimator that avoids the instability of adversarial critic training. It underpins generative matching networks and serves as a theoretically grounded alternative to GAN objectives for training implicit generative models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]