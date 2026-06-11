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
- mixture-models
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- generative-modeling
id: pkis:concept:mode-collapse
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- GAN
- training-failure
- underfitting
- diversity
title: Mode Collapse
understanding: 0
---

## Definition
Mode collapse in GAN training is the failure mode where the generator $G_\theta$ converges to a distribution that covers only a subset of the modes of the true data distribution $p^*(x)$, i.e., $\mathrm{supp}(q_\theta)\subsetneq\mathrm{supp}(p^*)$. A related phenomenon is **mode hopping**, where the generator sequentially covers different subsets of modes during training without stabilising.

### Why it matters
Mode collapse represents a fundamental underfitting of the learned distribution despite low discriminator loss. It arises from the adversarial dynamics: once the generator concentrates on regions the discriminator cannot distinguish, there is no gradient signal to expand coverage. Understanding and mitigating mode collapse (via diverse architectures, regularisation, large batches) is central to practical GAN training.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mixture-models]] — contrasts-with: Mode collapse is the failure to cover all mixture components of the data distribution.
- [[generative-adversarial-network-framework]] — applies
[To be populated during integration]