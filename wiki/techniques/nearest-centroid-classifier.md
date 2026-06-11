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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
id: pkis:technique:nearest-centroid-classifier
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- classification
- metric-learning
- one-shot-learning
- mahalanobis-distance
title: Nearest Centroid Classifier
understanding: 0
---

## Definition
$$\hat{y}(x) = \operatorname*{argmin}_c\; (x - \mu_c)^\top \Sigma^{-1}(x - \mu_c)$$

Under a uniform class prior, the MAP decision rule of LDA assigns $x$ to the class whose mean $\mu_c$ is nearest in **Mahalanobis distance**. The classifier can be generalised to any metric $d^2(x,\mu_c) = \|W(x-\mu_c)\|^2$ by learning a projection $W$ discriminatively.

### Why it matters
Nearest-centroid classifiers are extremely fast at test time (one distance evaluation per class) and admit **one-shot learning**: once a good metric $W$ is learned, a new class $c$ is added by simply computing its prototype $\mu_c$ from a single labelled example. This makes them attractive for few-shot recognition settings.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]