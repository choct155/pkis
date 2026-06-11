---
aliases: []
also_type: []
applies:
- robust-inference
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- exponential-family-distribution
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability
- statistics
- machine-learning
generalizes:
- gaussian-distribution
id: pkis:concept:students-t-distribution
instantiates:
- t-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch02
tags:
- heavy-tails
- robust-statistics
- gaussian-mixture
- degrees-of-freedom
title: Student's t-Distribution
understanding: 0
uses:
- gamma-distribution
- em-algorithm
---

## Definition
$$\text{St}(x|\mu,\lambda,\nu) = \frac{\Gamma(\nu/2+1/2)}{\Gamma(\nu/2)}\left(\frac{\lambda}{\pi\nu}\right)^{1/2}\left[1+\frac{\lambda(x-\mu)^2}{\nu}\right]^{-\nu/2-1/2}$$

Obtained by marginalising a Gaussian's precision over a Gamma prior: $\text{St}(x|\mu,\lambda,\nu)=\int_0^\infty \mathcal{N}(x|\mu,(\eta\lambda)^{-1})\text{Gam}(\eta|\nu/2,\nu/2)\,d\eta$. Reducing to the Cauchy at $\nu=1$ and approaching Gaussian as $\nu\to\infty$.

### Why it matters
The t-distribution has heavier tails than the Gaussian, giving it **robustness** to outliers: its maximum likelihood fit is far less distorted by a few anomalous data points. This makes it the preferred likelihood for robust regression and classification. The multivariate generalisation replaces $(x-\mu)^2$ with the squared Mahalanobis distance $\Delta^2$. The EM algorithm provides a convenient iterative fitting method via the Gaussian-scale-mixture representation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exponential-family-distribution]] — contrasts-with: t-distribution is NOT in the exponential family
- [[em-algorithm]] — uses: EM via Gaussian-scale-mixture representation
- [[robust-inference]] — applies: Heavy tails give robustness to outliers
- [[gamma-distribution]] — uses: Gamma prior on precision marginalised to yield t
- [[t-distribution]] — instantiates
- [[gaussian-distribution]] — generalizes: Limit nu->inf recovers Gaussian
[To be populated during integration]