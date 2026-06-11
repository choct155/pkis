---
aliases: []
also_type: []
applies:
- beta-binomial-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
generalizes:
- maximum-likelihood-estimation
id: pkis:technique:map-estimation
instantiates:
- ridge-regression
- weight-decay-as-prior
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch04
specializes:
- bayesian-inference
tags:
- posterior-mode
- regularisation
- Bayesian
- prior
title: MAP Estimation
understanding: 0
uses:
- conjugate-prior
- regularization
---

## Definition
$$\hat{\theta}_{\text{map}} = \operatorname*{argmax}_{\theta} \log p(\theta|\mathcal{D}) = \operatorname*{argmax}_{\theta} \left[\log p(\mathcal{D}|\theta) + \log p(\theta)\right]$$

MAP estimation finds the mode of the posterior distribution, equivalently minimising the NLL plus a regularisation term $-\log p(\theta)$ derived from the prior.

### Why it matters
MAP bridges pure MLE (uniform prior → MAP = MLE) and full Bayesian inference (posterior mode rather than full posterior). With a Gaussian prior on weights it yields $\ell_2$ / ridge regression; with a Laplace prior it yields $\ell_1$ / lasso. MAP is computationally as cheap as MLE while reducing overfitting, making it a workhorse regularised estimator. For the Bernoulli–Beta model the MAP estimate is $\hat{\theta} = (N_1 + a - 1)/(N + a + b - 2)$, reducing to add-one smoothing when $a=b=2$.

### Relationship to regularisation
The regularised objective $\mathcal{L}(\theta;\lambda) = \text{NLL}(\theta) + \lambda C(\theta)$ is equivalent to MAP when $C(\theta) = -\log p(\theta)$ and $\lambda = 1$ (after rescaling the prior appropriately).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[weight-decay-as-prior]] — instantiates
- [[ridge-regression]] — instantiates: Ridge regression is MAP with Gaussian prior on weights
- [[beta-binomial-model]] — applies
- [[bayesian-inference]] — specializes: MAP is the mode of the posterior, a point approximation to full Bayesian inference
- [[regularization]] — uses: MAP = NLL + log-prior penalty = regularised MLE
- [[conjugate-prior]] — uses
- [[maximum-likelihood-estimation]] — generalizes
[To be populated during integration]