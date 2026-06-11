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
contrasts-with:
- exploration-exploitation-tradeoff
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- representation-learning
- information-theory
id: pkis:technique:infonce-loss
instantiates:
- contrastive-representation-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch32
specializes:
- cross-entropy-loss
tags:
- contrastive-learning
- SimCLR
- CLIP
- MoCo
- mutual-information
- NT-Xent
title: InfoNCE Loss
understanding: 0
uses:
- mutual-information
---

## Definition
$$\mathcal{L}_{\text{InfoNCE}} = -\mathbb{E}_{x,x^+,x^-_{1:M}}\left[\log \frac{\exp f_\theta(x)^\top g_\phi(x^+)}{\exp f_\theta(x)^\top g_\phi(x^+) + \sum_{i=1}^{M} \exp f_\theta(x)^\top g_\phi(x^-_i)}\right]$$

The loss equals the negative log probability that the positive example $x^+$ is correctly identified among $M+1$ candidates. With $\ell_2$-normalised embeddings and temperature $\tau$, it is also called the **NT-Xent loss**. It provides a lower bound on mutual information: $I(X;Z) \geq \log M - \mathcal{L}_{\text{InfoNCE}}$.

### Why it matters
InfoNCE is the dominant training objective for contrastive representation learning (SimCLR, MoCo, CLIP). It avoids the margin hyperparameter of contrastive/triplet losses, naturally scales with the number of negatives, and has a clean information-theoretic interpretation as a lower bound on mutual information.

### Connections
- [[exploration-exploitation-tradeoff]] — contrasts-with: Hard negative mining vs random negatives trades exploitation for exploration in the negative space
- [[cross-entropy-loss]] — specializes
- [[contrastive-representation-learning]] — instantiates
- [[mutual-information]] — uses: I(X;Z) >= log M - L_InfoNCE
Related to the multiclass N-pair loss; motivated by the InfoMax principle; used in SimCLR where the batch itself supplies negatives, and in MoCo where a memory queue supplies additional negatives.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]