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
- probability-theory
- machine-learning
id: pkis:concept:dirac-delta-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
tags:
- generalized-function
- empirical-distribution
- point-mass
title: Dirac Delta Distribution
understanding: 0
---

## Definition
The **Dirac delta** $\delta(x)$ is a generalized function satisfying
$$\delta(x) = 0 \;\text{ for } x \neq 0, \qquad \int_{-\infty}^{\infty} \delta(x)\,dx = 1.$$
Using it as a PDF, $p(x) = \delta(x - \mu)$, concentrates all probability mass at the single point $\mu$. It arises as the limit of increasingly narrow, tall distributions (e.g., Gaussians with $\sigma \to 0$).

### Why it matters
The Dirac delta is essential for defining the empirical distribution $\hat{p}(x)=\frac{1}{m}\sum_{i=1}^m \delta(x-x^{(i)})$ over a continuous dataset, which in turn is the distribution implicitly maximized by maximum likelihood estimation on training data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]