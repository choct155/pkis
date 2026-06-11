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
id: pkis:concept:multi-label-classification
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
specializes:
- supervised-learning
tags:
- classification
- multi-label
- binary-output
- Bernoulli
- image-tagging
title: Multi-label Classification
understanding: 0
uses:
- binary-logistic-regression
---

## Definition
A supervised learning setting where each input $x$ is associated with a **subset** of a label set $\{1,\ldots,C\}$, represented as a binary vector $y\in\{0,1\}^C$. The model independently predicts each label:
$$p(y|x,\theta) = \prod_{c=1}^C \text{Ber}(y_c|\sigma(w_c^Tx))$$
This contrasts with **multi-class** (multinomial) classification, where labels are mutually exclusive and normalised via softmax.

### Why it matters
Many real tasks require multi-label outputs: image tagging, gene-function prediction, document annotation. The factored Bernoulli model decouples classes, simplifying inference, but ignores label correlations; more expressive models (e.g., conditional graphical models) can capture dependencies at the cost of complexity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[supervised-learning]] — specializes
- [[binary-logistic-regression]] — uses
[To be populated during integration]