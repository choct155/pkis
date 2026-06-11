---
aliases: []
also_type: []
applies:
- generative-adversarial-network-framework
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
- reproducing-kernel-hilbert-space
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- optimal-transport
- statistics
- machine-learning
id: pkis:concept:wasserstein-distance
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
specializes:
- integral-probability-metric
tags:
- optimal-transport
- Lipschitz
- WassersteinGAN
- distributional-distance
title: Wasserstein Distance
understanding: 0
---

## Definition
The Wasserstein-1 (Earth Mover) distance between distributions $p$ and $q$ over a metric space is:
$$W_1(p,q)=\inf_{\gamma\in\Pi(p,q)}\mathbb{E}_{(x,y)\sim\gamma}[\|x-y\|]$$
By the Kantorovich–Rubinstein duality this equals:
$$W_1(p,q)=\sup_{\|f\|_{\mathrm{Lip}}\le 1}\mathbb{E}_p[f(x)]-\mathbb{E}_q[f(x)]$$
For implicit models, a parametric 1-Lipschitz critic $D_\phi$ (enforced via gradient penalties or spectral normalisation) provides a lower bound, yielding the WassersteinGAN objective:
$$\min_\theta\max_{\phi:\|D_\phi\|_{\mathrm{Lip}}\le 1}\mathbb{E}_{p^*}[D_\phi(x)]-\mathbb{E}_{q(z)}[D_\phi(G_\theta(z))]$$

### Why it matters
Wasserstein distance provides informative gradients even for distributions with disjoint supports, addressing a key failure mode of JSD-based GANs. Its geometric interpretation as the cost of transporting mass makes it a principled choice for distribution matching.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-adversarial-network-framework]] — applies: WassersteinGAN replaces JSD with W1 to provide non-saturating gradients.
- [[reproducing-kernel-hilbert-space]] — contrasts-with: Wasserstein uses 1-Lipschitz functions; MMD uses RKHS unit ball.
- [[integral-probability-metric]] — specializes
[To be populated during integration]