---
aliases: []
also_type: []
applies:
- gaussian-distribution
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- bayesian-stats
- information-theory
- statistical-learning
id: pkis:result:gaussian-maximum-entropy-characterization
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch07
- lange-applied-probability-ch16
specializes:
- exponential-family-ml-maxent-duality
tags:
- probability-theory
- maximum-entropy
- information-theory
title: Gaussian as Maximum-Entropy Distribution for Fixed Mean and Variance
understanding: 0
uses:
- entropy
---

## Definition
Among all probability distributions on the real line with a prescribed first moment $\langle e\rangle = \alpha$ and second moment $\langle e^2\rangle = \alpha^2+\beta^2$, the one of maximum entropy $H = -\int de\, p(e)\log p(e)$ is uniquely the Gaussian $p(e) = (2\pi\beta^2)^{-1/2}\exp\{-(e-\alpha)^2/2\beta^2\}$. Equivalently, the Gaussian has higher entropy than any other distribution with the same variance.

## Significance for inference (Jaynes)
This is the deepest justification for the ubiquitous use of Gaussian sampling distributions. When a scientist knows only the first two moments of the noise (e.g. a mean-square error fixed by the Nyquist thermal-fluctuation law) and nothing else, assigning a Gaussian represents that state of knowledge most honestly: it imposes the known constraints and assumes nothing further. Because any distribution assigned by maximum entropy yields Bayesian inferences depending only on the constrained quantities, using a Gaussian guarantees that all properties of the errors beyond their first two moments are made *irrelevant* to the inference — not that the error frequencies are correctly represented. This dissolves the long puzzle (de Morgan, Feller, Barnard) of why the Gaussian succeeds even when actual error frequencies are non-Gaussian.

## Stability connection
Because the Gaussian maximizes entropy at fixed variance, any operation that discards information while conserving variance drives a distribution toward the Gaussian. This is the mechanism behind the central limit theorem (repeated convolution) and behind the general 'gravitation' of distributions to the central form.

## Connections
- [[exponential-family-ml-maxent-duality]] — specializes: Gaussian is the maxent/exponential-family member for first-two-moment constraints
- [[gaussian-distribution]] — applies: characterizes the Gaussian as the unique maxent distribution at fixed mean and variance
- [[entropy]] — uses: the quantity being maximized under moment constraints
- [[entropy]] — uses: the objective being maximized
- [[gaussian-distribution]] — the unique maximizer
- [[central-limit-theorem]] — explained as variance-conserving, entropy-increasing convolution

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]