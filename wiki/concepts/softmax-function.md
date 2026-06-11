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
id: pkis:concept:softmax-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
- murphy-pml1-intro-ch01
- murphy-pml1-intro-ch02
tags:
- multiclass
- normalized-exponential
- categorical-distribution
- canonical-link
title: Softmax Function
understanding: 0
---

## Definition
$$p(C_k|\mathbf{x}) = \frac{\exp(a_k)}{\sum_j \exp(a_j)}, \qquad a_k = \ln p(\mathbf{x}|C_k)p(C_k).$$

The softmax is the multiclass generalization of the logistic sigmoid; it maps a vector of real-valued 'activations' $\mathbf{a}$ to a probability simplex. Its Jacobian satisfies $\partial y_k/\partial a_j = y_k(\delta_{kj} - y_j)$, which appears in the gradient of cross-entropy loss.

### Why it matters
Softmax is the canonical output layer for $K$-class probabilistic classifiers. Combined with the multiclass cross-entropy loss, it yields the same clean gradient form—$(y_{nj}-t_{nj})\boldsymbol{\phi}_n$—as the logistic sigmoid does in the binary case, a consequence of the softmax being the canonical link for the categorical exponential-family distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]