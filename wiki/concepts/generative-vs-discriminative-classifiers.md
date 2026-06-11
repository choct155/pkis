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
id: pkis:concept:generative-vs-discriminative-classifiers
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch09
tags:
- classification
- model-comparison
- joint-vs-conditional-likelihood
- generative
- discriminative
title: Generative vs. Discriminative Classifiers
understanding: 0
uses:
- generative-classifier
- logistic-regression
- distribution-shift
- missing-data-mechanisms
---

## Definition
A **generative classifier** models the joint $p(x,y) = p(y)\,p(x\mid y)$ and classifies via Bayes' rule; a **discriminative classifier** directly models $p(y\mid x)$.

The two paradigms lead to identical functional forms (e.g., both LDA and logistic regression give a linear logit in $x$) but are fitted by optimising different objectives: the **joint likelihood** $\prod_n p(x_n, y_n \mid \theta)$ vs. the **conditional likelihood** $\prod_n p(y_n \mid x_n, \theta)$.

### Why it matters
**Discriminative advantages**: higher predictive accuracy (simpler target distribution); handles feature pre-processing; better-calibrated probabilities when generative assumptions are violated.

**Generative advantages**: easy/closed-form fitting; natural handling of missing inputs by marginalisation; classes fitted independently (incremental class addition); compatible with semi-supervised learning; may be more robust to spurious features and distribution shift by capturing causal structure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[missing-data-mechanisms]] — uses
- [[distribution-shift]] — uses
- [[logistic-regression]] — uses
- [[generative-classifier]] — uses
[To be populated during integration]