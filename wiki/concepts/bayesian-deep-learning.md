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
- deep-learning
- bayesian-inference
- uncertainty-quantification
id: pkis:concept:bayesian-deep-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- BDL
- posterior-predictive
- model-averaging
- underspecification
title: Bayesian Deep Learning (BDL)
understanding: 0
---

## Definition
$$p(y|x, D) = \int p(y|x, \theta)\, p(\theta|D)\, d\theta, \quad p(\theta|D) \propto p(\theta)\, p(D|\theta)$$

Bayesian Deep Learning applies Bayesian inference—specifically, posterior predictive integration—to deep neural networks, treating the (very high-dimensional) weight vector $\theta$ as a random variable rather than a point estimate.

### Why it matters
Single-parameter (MAP/MLE) deep nets suffer from *underspecification*: many weight configurations fit training data equally well yet generalise differently. BDL averages over this posterior mass, improving calibration, uncertainty quantification, and robustness to distribution shift. The main challenges are specifying suitable priors and tractable posterior inference at scale.

### Contrast with Deep Bayesian Learning
*Deep Bayesian Learning* (DBL) is the complementary direction: using deep models (e.g., amortised inference networks) to *speed up* Bayesian inference for classical models, not performing Bayes inside a DNN.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]