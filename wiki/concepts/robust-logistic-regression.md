---
aliases: []
also_type: []
applies:
- distribution-shift
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
- statistics
extends:
- binary-logistic-regression
- cross-entropy-loss
id: pkis:concept:robust-logistic-regression
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- label-noise
- bi-tempered
- mixture-model
- outlier-robustness
- loss-function
title: Robust Logistic Regression
understanding: 0
uses:
- mixture-models
---

## Definition
A modification of standard logistic regression designed to resist the influence of label noise or outliers. The canonical mixture-model form is
$$p(y|x) = \pi\,\text{Ber}(y|0.5) + (1-\pi)\,\text{Ber}(y|\sigma(w^Tx))$$
where $\pi$ is the probability that a label is generated uniformly at random (noise rate). An alternative approach, **bi-tempered logistic regression**, uses a tempered log $\log_t(x)=\frac{x^{1-t}-1}{1-t}$ in the loss ($t_1<1$ bounds the loss for far-from-boundary outliers) and a tempered softmax $\exp_{t_2}$ with $t_2>1$ for heavy-tailed probabilities near the boundary.

### Why it matters
Standard cross-entropy loss is unbounded, so a single confidently mislabelled example can dominate the gradient. Robust variants are essential for real-world datasets with annotation errors, and transfer directly to DNNs by modifying only the loss and output activation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[distribution-shift]] — applies
- [[cross-entropy-loss]] — extends
- [[mixture-models]] — uses
- [[binary-logistic-regression]] — extends
[To be populated during integration]