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
contrasts-with:
- f-divergence
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- functional-analysis
generalizes:
- wasserstein-distance
- maximum-mean-discrepancy
id: pkis:concept:integral-probability-metric
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- Wasserstein
- MMD
- GAN
- distributional-distance
- metric
title: Integral Probability Metric
understanding: 0
---

## Definition
An integral probability metric (IPM) measures the discrepancy between distributions $p$ and $q$ by the supremum of expected function differences over a constrained function class $\mathcal{F}$:
$$I_\mathcal{F}(p,q)=\sup_{f\in\mathcal{F}}\left|\mathbb{E}_p[f(x)]-\mathbb{E}_q[f(x)]\right|$$
IPMs are symmetric and satisfy the triangle inequality. Key instances:
- **Wasserstein-1 / Earth Mover distance**: $\mathcal{F}=\{f:\|f\|_{\mathrm{Lip}}\le 1\}$
- **Maximum Mean Discrepancy (MMD)**: $\mathcal{F}=\{f:\|f\|_{\mathrm{RKHS}}\le 1\}$

The critic $f$ is a witness function that reveals where the two distributions differ.

### Why it matters
Unlike f-divergences, IPMs provide meaningful gradient signal even when $p$ and $q$ have non-overlapping support, because the Lipschitz or RKHS constraint induces smoothness in the critic. This property motivated WassersteinGAN and MMD-based generative models as more stable alternatives to the original GAN.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[f-divergence]] — contrasts-with: IPMs use difference of expectations (smooth witnesses); f-divergences use ratios of densities.
- [[maximum-mean-discrepancy]] — generalizes
- [[wasserstein-distance]] — generalizes
[To be populated during integration]