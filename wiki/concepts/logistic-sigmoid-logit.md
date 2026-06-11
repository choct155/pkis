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
id: pkis:concept:logistic-sigmoid-logit
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch04
tags:
- sigmoid
- logit
- log-odds
- activation-function
- binary-classification
- generalized-linear-model
title: Logistic Sigmoid and Logit Function
understanding: 0
---

## Definition
$$\sigma(a) = \frac{1}{1+\exp(-a)}, \qquad \sigma(-a) = 1 - \sigma(a), \qquad \frac{d\sigma}{da} = \sigma(1-\sigma).$$

The inverse (logit) is $a = \ln\!\left(\frac{\sigma}{1-\sigma}\right)$, the log-odds of the positive class. The sigmoid 'squashes' the entire real line into $(0,1)$, making it the canonical activation function for Bernoulli/binary probabilistic outputs.

### Why it matters
The logistic sigmoid arises naturally from Bayes' theorem when class-conditional densities belong to the exponential family with shared dispersion: the log-ratio of class posteriors is linear in the input, and the sigmoid is the inverse of that log-odds map. Its self-referential derivative $\sigma(1-\sigma)$ is key to efficient gradient computation in logistic regression and neural networks, and it is the canonical link function for Bernoulli GLMs.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]