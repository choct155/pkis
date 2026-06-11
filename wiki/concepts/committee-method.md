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
id: pkis:concept:committee-method
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch14
tags:
- ensemble
- variance-reduction
- averaging
- bagging
title: Committee Method (Model Averaging)
understanding: 0
---

## Definition
$$y_{\text{COM}}(x) = \frac{1}{M}\sum_{m=1}^{M} y_m(x)$$

A committee combines the predictions of $M$ independently trained models by simple (or weighted) averaging, reducing prediction variance without increasing bias.

### Why it matters
Under the idealized assumption of zero-mean, uncorrelated errors across models, committee averaging reduces the expected squared error by a factor of $M$ relative to the average individual error: $E_{\text{COM}} = \frac{1}{M} E_{\text{AV}}$. In practice errors are correlated so the gain is smaller, but Jensen's inequality guarantees $E_{\text{COM}} \leq E_{\text{AV}}$ for any convex loss. Bootstrap aggregation (bagging) is the canonical technique for constructing the required diverse models from a single dataset.

### Connections
Distinct from Bayesian model averaging: committees assign *each data point* to a potentially different component, whereas BMA treats a single model as responsible for the entire dataset.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]