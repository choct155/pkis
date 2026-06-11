---
aliases: []
also_type: []
applies:
- random-variable
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
- probability-theory
- machine-learning
id: pkis:concept:probability-mass-function
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- full-joint-probability-distribution
- probability-theory
- bernoulli-distribution
- binomial-distribution
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
- murphy-pml1-intro-ch02
specializes:
- probability-theory
tags:
- discrete
- distribution
- normalization
- fundamentals
title: Probability Mass Function (PMF)
understanding: 0
uses:
- random-variable
---

## Definition
A **probability mass function** maps each state $x_i$ of a discrete random variable $\mathbf{x}$ to a probability:
$$P: \text{dom}(\mathbf{x}) \to [0,1], \quad \sum_{x \in \mathbf{x}} P(x) = 1.$$
It fully specifies a probability distribution over a discrete variable by assigning a non-negative, normalized weight to every possible outcome.

### Why it matters
PMFs are the foundational representation of discrete distributions in machine learning — from Bernoulli outputs to categorical cross-entropy losses. Understanding their normalization and domain requirements is prerequisite to constructing valid probabilistic models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[binomial-distribution]] — prerequisite-of
- [[bernoulli-distribution]] — prerequisite-of
- [[probability-theory]] — prerequisite-of
- [[random-variable]] — uses
- [[full-joint-probability-distribution]] — prerequisite-of
- [[probability-theory]] — specializes
- [[random-variable]] — applies
[To be populated during integration]