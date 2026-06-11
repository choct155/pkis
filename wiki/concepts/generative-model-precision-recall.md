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
- generative-models
- evaluation
id: pkis:concept:generative-model-precision-recall
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch20
tags:
- evaluation
- generative-models
- precision
- recall
- mode-collapse
- GAN
title: Generative Model Precision and Recall
understanding: 0
---

## Definition
Precision and recall for generative models are defined in terms of nearest-neighbor membership in feature space. Let $\Phi_\text{model}$ and $\Phi_\text{data}$ be sets of feature vectors from model samples and real data respectively, and let $f_k(\phi, \Phi) = \mathbf{1}[\exists \phi' \in \Phi : \|\phi - \phi'\|_2 \leq \|\phi' - NN_k(\phi', \Phi)\|_2]$. Then
$$\text{precision} = \frac{1}{|\Phi_\text{model}|}\sum_{\phi \in \Phi_\text{model}} f_k(\phi, \Phi_\text{data}),$$
$$\text{recall} = \frac{1}{|\Phi_\text{data}|}\sum_{\phi \in \Phi_\text{data}} f_k(\phi, \Phi_\text{model}).$$

**Precision** measures sample fidelity (are generated samples realistic?); **recall** measures coverage (does the model capture all modes?).

### Why it matters
FID conflates fidelity and diversity into a single number, making it hard to diagnose failure modes such as mode collapse (low recall, high precision) or blurry over-smoothed outputs (high recall, low precision). Separate precision and recall metrics enable targeted model improvement and form a trade-off curve analogous to the ROC curve in classification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]