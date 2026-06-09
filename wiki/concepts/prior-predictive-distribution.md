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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:concept:prior-predictive-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch01
tags:
- bayesian
- prediction
- prior
- marginal-likelihood
- evidence
title: Prior Predictive Distribution
understanding: 0
---

## Definition
$$p(y) = \int p(y\mid\theta)\,p(\theta)\,d\theta.$$
The distribution of the observable data *before* any data are seen — the data model averaged over the prior. It is the marginal distribution of $y$, but the name 'prior predictive' is more informative: *prior* because it is not conditioned on previous observations, *predictive* because $y$ is observable.

### Relation to the evidence
As a function of the data, $p(y)$ is exactly the normalizing constant in Bayes' rule and, viewed across competing models, the marginal likelihood (model evidence) used in Bayesian model comparison. The same integral thus plays three roles: predictive distribution of future data, normalizer of the posterior, and evidence for the model.

### Prior predictive checks
Simulating $\theta^s\sim p(\theta)$ then $y^s\sim p(y\mid\theta^s)$ yields draws from the prior predictive. Inspecting these draws reveals whether the prior, pushed through the likelihood, implies data on a sensible scale — a cheap diagnostic for unintentionally informative or absurd priors before any fitting.

### Why it matters
The prior predictive turns an abstract prior on parameters into concrete, checkable statements about the data the model expects to see, and it is the quantity that governs how strongly observed data update beliefs (via the evidence). It is the natural complement to the posterior predictive, bracketing inference at the before-and-after-data ends of the workflow.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]