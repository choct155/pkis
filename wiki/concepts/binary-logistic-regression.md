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
generalizes:
- perceptron-learning-algorithm
id: pkis:concept:binary-logistic-regression
instantiates:
- logistic-regression-nll-convexity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
specializes:
- logistic-regression
tags:
- classification
- discriminative-model
- sigmoid
- logit
- decision-boundary
title: Binary Logistic Regression
understanding: 0
uses:
- logit-pre-activation
- activation-functions
- cross-entropy-loss
- maximum-likelihood-estimation
- linear-separability
- irls
---

## Definition
$$p(y|x,\theta) = \text{Ber}(y|\sigma(w^Tx + b))$$

where $\sigma(a) = 1/(1+e^{-a})$ is the sigmoid function, $a = w^Tx + b$ is the **logit** (log-odds), and $\theta=(w,b)$. The model defines a linear decision boundary $\{x: w^Tx+b=0\}$ in input space; the magnitude $\|w\|$ controls the steepness of the probabilistic transition across that boundary.

### Why it matters
Binary logistic regression is the canonical discriminative linear classifier: it produces calibrated probabilities, its NLL is convex in $w$ (guaranteeing a unique global MLE), and its gradient has the intuitive form $(\mu_n - y_n)x_n$ — prediction error times input. It is the starting point for multinomial logistic regression, GLMs with Bernoulli responses, and the perceptron.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[perceptron-learning-algorithm]] — generalizes
- [[irls]] — uses
- [[logistic-regression-nll-convexity]] — instantiates
- [[linear-separability]] — uses
- [[maximum-likelihood-estimation]] — uses
- [[cross-entropy-loss]] — uses
- [[activation-functions]] — uses
- [[logit-pre-activation]] — uses
- [[logistic-regression]] — specializes
[To be populated during integration]