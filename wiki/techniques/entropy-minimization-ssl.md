---
aliases: []
also_type: []
analogous-to:
- pseudo-labeling
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
- semi-supervised-learning
- information-theory
id: pkis:technique:entropy-minimization-ssl
instantiates:
- semi-supervised-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch19
tags:
- semi-supervised
- cluster-assumption
- mutual-information
- confidence
- low-data
title: Entropy Minimization for Semi-Supervised Learning
understanding: 0
uses:
- entropy
- mutual-information
---

## Definition
Entropy minimization encourages a classifier to make confident (low-entropy) predictions on unlabeled data:
$$L = -\sum_{c=1}^C p_\theta(y=c|x)\log p_\theta(y=c|x)$$
This loss is minimised when $p_\theta$ concentrates all probability mass on a single class. It is justified by the **cluster assumption** (decision boundaries should lie in low-density regions) and by maximising the input–output mutual information $I(y;x)$, which decomposes as:
$$I(y;x) = \underbrace{-\mathbb{E}_x\left[\sum_c p_\theta(y_c|x)\log p_\theta(y_c|x)\right]}_{\text{entropy minimization}} + \underbrace{\sum_c \mathbb{E}_x[p_\theta(y_c|x)]\log\mathbb{E}_x[p_\theta(y_c|x)]}_{\text{marginal entropy maximization}}$$

### Why it matters
Entropy minimization unifies several SSL objectives: online pseudo-labeling minimizes the cross-entropy to the hard $\arg\max$ target; sharpening (temperature $T<1$) interpolates between soft and hard targets. The MixMatch method builds on this idea with temperature-sharpened pseudo-labels.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[pseudo-labeling]] — analogous-to: Online pseudo-labeling minimises cross-entropy to hard argmax target; entropy minimization uses soft target.
- [[mutual-information]] — uses: Maximizing I(y;x) = entropy minimization term + marginal entropy maximization term.
- [[entropy]] — uses
- [[semi-supervised-learning]] — instantiates
[To be populated during integration]