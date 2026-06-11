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
id: pkis:concept:jensen-shannon-divergence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
specializes:
- f-divergence
tags:
- divergence
- GAN
- information-theory
- symmetry
title: Jensen-Shannon Divergence
understanding: 0
uses:
- kl-divergence
---

## Definition
The Jensen-Shannon divergence (JSD) between distributions $p$ and $q$ is the symmetrized, bounded variant of KL divergence:
$$\mathrm{JSD}(p\|q)=\tfrac{1}{2}D_{\mathrm{KL}}\!\left(p\Big\|\tfrac{p+q}{2}\right)+\tfrac{1}{2}D_{\mathrm{KL}}\!\left(q\Big\|\tfrac{p+q}{2}\right)\in[0,\log 2]$$
It is symmetric ($\mathrm{JSD}(p,q)=\mathrm{JSD}(q,p)$) and its square root is a metric. Under the optimal binary classifier $D^*(x)=p^*(x)/(p^*(x)+q_\theta(x))$, the GAN value function satisfies $V^*(q_\theta,p^*)=\mathrm{JSD}(p^*,q_\theta)-\log 2$.

### Why it matters
JSD is the natural divergence minimised by the original GAN with Bernoulli log-loss. Unlike KL, it remains finite when supports overlap partially, but still saturates to $\log 2$ for non-overlapping supports, motivating Wasserstein and f-GAN alternatives.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[f-divergence]] — specializes
- [[kl-divergence]] — uses: JSD is the average of two symmetrised KL terms to a mixture distribution.
[To be populated during integration]