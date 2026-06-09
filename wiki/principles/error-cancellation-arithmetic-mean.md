---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- statistical-learning
id: pkis:principle:error-cancellation-arithmetic-mean
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch07
tags:
- probability-theory
- estimation
- location-parameter
title: Error Cancellation and the Optimality of the Arithmetic Mean
understanding: 0
---

## Definition
When a location parameter is estimated by a normalized linear combination of observations $(\mu)_{est}=\sum w_i y_i$ with $\sum w_i = 1$, and the errors are assigned independent identical variance $\sigma^2$, the expected square error is $\langle\Delta^2\rangle = \sigma^2\sum_i w_i^2$. Writing $w_i = 1/n + q_i$ with $\sum q_i = 0$ gives $\langle\Delta^2\rangle = \sigma^2(1/n + \sum q_i^2)$, which is minimized uniquely at $q_i=0$, i.e. uniform weighting $w_i = 1/n$ — the arithmetic mean. The minimum expected square error is $\sigma^2/n$.

## Interpretation
Uniform weighting affords the maximum possible opportunity for errors to cancel; the result holds whatever the individual error distribution. Combined with Gauss's theorem that the Gaussian sampling distribution is the unique one whose maximum-likelihood estimate equals the arithmetic mean, this explains the 'ubiquitous success' of the Gaussian: among all distributions that estimate a location by the arithmetic mean, the Gaussian gives maximum error cancellation. The actual error in the mean is exactly the average of the true errors, $\Delta = \bar e$, regardless of how the errors are distributed.

## Generalization (correlated errors)
With a general positive-definite covariance matrix $C_{ij}=\langle e_i e_j\rangle$, the minimizing weights are $w_i = \sum_j K_{ij} / \sum_{ij} K_{ij}$ where $K = C^{-1}$, achieving $\langle\Delta^2\rangle_{min} = (\sum_{ij} K_{ij})^{-1}$, recovering $\sigma^2/n$ in the i.i.d. case.

## Relation to Euler's mistake and the $\sqrt{N}$ rule
The cancellation phenomenon is why summed errors grow as $\sqrt N$ not $N$; failing to see this, Euler concentrated on the worst case and concluded (wrongly) that averaging 'multiplies the errors'.

## Connections
- [[gaussian-distribution]] — the Gaussian uniquely couples the arithmetic mean to maximum-likelihood estimation
- [[central-limit-theorem]] — the $\sqrt N$ growth of summed errors
- [[regression-to-the-mean]] — contrasts: a distinct Galtonian phenomenon

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]