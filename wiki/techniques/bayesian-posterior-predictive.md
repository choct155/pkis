---
aliases: []
also_type: []
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
- bayesian-methods
- machine-learning
id: pkis:technique:bayesian-posterior-predictive
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- posterior-predictive
- marginalization
- overfitting
- bayesian
- prediction
title: Posterior Predictive Distribution (Bayesian)
understanding: 0
---

## Definition
$$p(y|x, D) = \int p(y|x,\theta)\,p(\theta|D)\,d\theta$$

The Bayesian posterior predictive distribution averages predictions over the full posterior on parameters, rather than committing to a single point estimate. For the Bernoulli–Beta model this reduces to $$p(y=1|D)=E[\theta|D]=\hat{\alpha}/(\hat{\alpha}+\hat{\beta})$$, which yields Laplace's rule of succession under a uniform prior.

### Why it matters
Marginalising out parameter uncertainty (i) reduces overfitting relative to the plug-in approximation, (ii) yields calibrated predictive uncertainty that grows where data are sparse, and (iii) is the principled Bayesian answer to prediction. The plug-in approximation $p(y|x,\hat{\theta})$ is the degenerate limit $p(\theta|D)\approx\delta(\theta-\hat{\theta})$ obtained via the Dirac sifting property.

### Connection to active learning
Because epistemic uncertainty is retained in the predictive distribution, the posterior predictive is the basis for acquisition functions in Bayesian optimisation and active learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]