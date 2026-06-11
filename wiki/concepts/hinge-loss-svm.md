---
aliases: []
also_type: []
analogous-to:
- epsilon-insensitive-loss
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
- cross-entropy-loss
- logistic-regression
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
id: pkis:concept:hinge-loss-svm
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch07
tags:
- loss-function
- classification
- svm
- sparsity
title: Hinge Loss
understanding: 0
---

## Definition
The hinge loss for a classifier with output $y$ and target $t \in \{-1,+1\}$ is
$$E_{\text{SV}}(yt) = [1 - yt]_+ = \max(0,\, 1-yt).$$
It is zero when the example is correctly classified with a margin of at least 1, and grows linearly with the margin violation. The SVM objective (soft-margin) can be written as
$$\sum_n [1 - y_n t_n]_+ + \lambda\|\mathbf{w}\|^2.$$

The flat region for $yt \geq 1$ is the key structural feature that yields sparse support vectors.

### Why it matters
The hinge loss is a convex, piecewise-linear upper bound on the 0–1 misclassification loss. Its flat region for correctly-classified, well-separated points means that such points receive zero gradient and do not appear in the dual solution, producing sparsity. Compared with the logistic loss, the hinge loss gives sparser solutions at the cost of non-probabilistic outputs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[logistic-regression]] — contrasts-with
- [[cross-entropy-loss]] — contrasts-with: Hinge loss yields sparse solutions; cross-entropy does not
- [[epsilon-insensitive-loss]] — analogous-to
[To be populated during integration]