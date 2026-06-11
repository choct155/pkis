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
- statistics
- statistical-learning-theory
id: pkis:concept:bayes-error
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch05
tags:
- irreducible-error
- Bayes-optimal
- generalization
- lower-bound
title: Bayes Error
understanding: 0
uses:
- generalization-error-training-error
- data-generating-distribution
---

## Definition
The **Bayes error** is the irreducible minimum error achievable by any classifier or regressor when predicting from the true data-generating distribution $p(\mathbf{x}, y)$:

$$\epsilon^* = \mathbb{E}_{(\mathbf{x},y)\sim p_{\text{data}}}\bigl[\mathbf{1}[f^*(\mathbf{x})\neq y]\bigr]$$

where $f^*$ is the Bayes-optimal predictor. It arises from inherent stochasticity or from relevant latent variables absent from $\mathbf{x}$.

### Why it matters
Bayes error is the lower bound all learning algorithms must respect. Parametric models with sub-optimal capacity converge to a generalization error strictly above Bayes error regardless of training-set size, quantifying the cost of misspecification.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[data-generating-distribution]] — uses
- [[generalization-error-training-error]] — uses
[To be populated during integration]