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
- statistics
id: pkis:concept:kurtosis-and-tail-behavior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- kurtosis
- heavy-tails
- super-gaussian
- sub-gaussian
- leptokurtic
- platykurtic
- moments
title: Kurtosis and Tail Behavior
understanding: 0
---

## Definition
The **kurtosis** of a random variable $Z$ with mean $\mu$ and standard deviation $\sigma$ is the normalized 4th central moment:
$$\mathrm{kurt}(Z) = \frac{\mu_4}{\sigma^4} = \frac{\mathbb{E}[(Z-\mu)^4]}{(\mathbb{E}[(Z-\mu)^2])^2}.$$
The **excess kurtosis** is $\mathrm{kurt}(Z) - 3$ (subtracting the Gaussian baseline of 3). Distributions with positive excess kurtosis (**leptokurtic / super-Gaussian**, e.g., Laplace, Student-$t$) have heavier tails than the Gaussian; those with negative excess kurtosis (**platykurtic / sub-Gaussian**, e.g., uniform) have lighter tails.

### Why it matters
Kurtosis governs outlier probability and is critical in robust statistics and ICA: super-Gaussian sources produce sparse, peaky signals while sub-Gaussian sources produce flat signals, enabling the identification of independent components by maximizing non-Gaussianity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]