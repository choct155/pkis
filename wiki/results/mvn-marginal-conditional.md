---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- probability
- statistics
id: pkis:result:mvn-marginal-conditional
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- multiple-imputation
related_concepts: []
sources:
- murphy-pml1-intro-ch03
specializes:
- multivariate-normal-model
tags:
- multivariate-gaussian
- schur-complement
- bayesian-inference
- conditioning
title: MVN Marginal and Conditional Distributions
understanding: 0
uses:
- mahalanobis-distance
- conditional-independence
- marginalization
---

## Definition
For a jointly Gaussian vector $(y_1, y_2)$ with joint parameters $(\mu, \Sigma, \Lambda = \Sigma^{-1})$ partitioned conformally:
$$p(y_1) = \mathcal{N}(y_1 | \mu_1, \Sigma_{11})$$
$$p(y_1 | y_2) = \mathcal{N}(y_1 | \mu_{1|2}, \Sigma_{1|2})$$
$$\mu_{1|2} = \mu_1 + \Sigma_{12}\Sigma_{22}^{-1}(y_2 - \mu_2) = \mu_1 - \Lambda_{11}^{-1}\Lambda_{12}(y_2 - \mu_2)$$
$$\Sigma_{1|2} = \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21} = \Lambda_{11}^{-1}$$

Both marginals and conditionals of an MVN are themselves Gaussian, with the conditional mean being a linear function of the observed variable and the conditional covariance being independent of that observation.

### Why it matters
This closed-form result is the engine behind Gaussian process regression, Kalman filtering, linear Gaussian state-space models, and missing-value imputation. The Schur complement $\Sigma_{1|2}$ appears universally when block-inverting precision or covariance matrices.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[multiple-imputation]] — prerequisite-of
- [[marginalization]] — uses
- [[conditional-independence]] — uses
- [[mahalanobis-distance]] — uses
- [[multivariate-normal-model]] — specializes
[To be populated during integration]