---
aliases: []
also_type: []
applies:
- polynomial-curve-fitting
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
- unbiasedness
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
id: pkis:concept:likelihood-function
instantiates:
- maximum-likelihood-estimation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- prior-likelihood-posterior
- bayesian-inference
related_concepts: []
sources:
- bishop-prml-ch01
tags:
- maximum-likelihood
- frequentist
- bias
- estimation
- log-likelihood
title: Likelihood Function and Maximum Likelihood Estimation
understanding: 0
uses:
- kl-nonnegativity-ml-equivalence
---

## Definition
Given a parametric model $p(\mathcal{D}|\mathbf{w})$, the **likelihood function** is this quantity viewed as a function of $\mathbf{w}$ for fixed observed data $\mathcal{D}$:
$$\mathcal{L}(\mathbf{w}) = p(\mathcal{D}|\mathbf{w}).$$
**Maximum likelihood** sets $\mathbf{w}_{\mathrm{ML}}=\arg\max_{\mathbf{w}}\mathcal{L}(\mathbf{w})$, equivalently minimising the negative log-likelihood (the *error function*).

For i.i.d. data from $\mathcal{N}(x|\mu,\sigma^2)$:
$$\mu_{\mathrm{ML}}=\frac{1}{N}\sum_n x_n, \qquad \sigma^2_{\mathrm{ML}}=\frac{1}{N}\sum_n(x_n-\mu_{\mathrm{ML}})^2.$$

### Why it matters
ML is the dominant frequentist point-estimation strategy. The sample variance estimator $\sigma^2_{\mathrm{ML}}$ is biased downward by a factor $(N-1)/N$, foreshadowing the broader over-fitting problem of maximum likelihood for complex models. Minimising KL divergence between the empirical distribution and $q(x|\theta)$ is equivalent to maximising the likelihood.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[unbiasedness]] — contrasts-with
- [[polynomial-curve-fitting]] — applies
- [[kl-nonnegativity-ml-equivalence]] — uses
- [[bayesian-inference]] — prerequisite-of
- [[prior-likelihood-posterior]] — prerequisite-of
- [[maximum-likelihood-estimation]] — instantiates
[To be populated during integration]