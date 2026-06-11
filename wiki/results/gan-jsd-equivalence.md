---
aliases: []
also_type: []
applies:
- generative-adversarial-network-framework
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
- information-theory
- machine-learning
- game-theory
id: pkis:result:gan-jsd-equivalence
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- GAN
- Nash-equilibrium
- Jensen-Shannon
- convergence
title: GAN–Jensen-Shannon Divergence Equivalence
understanding: 0
uses:
- jensen-shannon-divergence
- density-ratio-estimation
---

## Definition
For the original GAN with Bernoulli log-loss, the value function at the optimal discriminator equals the Jensen-Shannon divergence minus a constant:
$$V^*(q_\theta,p^*)=\mathrm{JSD}(p^*,q_\theta)-\log 2$$
where the optimal discriminator is $D^*(x)=p^*(x)/(p^*(x)+q_\theta(x))$ and $\mathrm{JSD}(p^*,q_\theta)=\tfrac{1}{2}D_{\mathrm{KL}}(p^*\|\frac{p^*+q_\theta}{2})+\tfrac{1}{2}D_{\mathrm{KL}}(q_\theta\|\frac{p^*+q_\theta}{2})$. Consequently, the minimax GAN objective minimises the JSD, and $q_\theta=p^*$, $D^*=1/2$ is the global Nash equilibrium.

### Why it matters
This result grounds the GAN objective in information-theoretic divergence minimisation, providing convergence guarantees under infinite capacity and optimal discriminator assumptions. It also reveals why f-divergence saturation for non-overlapping supports motivated WassersteinGAN.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[density-ratio-estimation]] — uses
- [[jensen-shannon-divergence]] — uses
- [[generative-adversarial-network-framework]] — applies
[To be populated during integration]