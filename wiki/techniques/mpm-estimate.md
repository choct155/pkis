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
contrasts-with:
- maximum-a-posteriori-estimation-map
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- statistics
- machine learning
id: pkis:technique:mpm-estimate
instantiates:
- posterior-risk
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
specializes:
- bayesian-point-estimation
tags:
- Hamming loss
- posterior marginals
- Bayes estimator
- discrete estimation
- MAP vs MPM
title: Maximizer of Posterior Marginals (MPM Estimate)
understanding: 0
uses:
- marginalization
---

## Definition
$$\hat{\theta}_d = \operatorname*{arg\,max}_{\theta_d} \int_{\theta_{-d}} p(\theta | \mathcal{D})\, d\theta_{-d}, \quad d = 1,\ldots,D$$

The MPM estimate selects, independently for each component, the most probable marginal value; it is the Bayes-optimal estimator under **Hamming loss** $\ell(\theta,\hat{\theta}) = \sum_d \mathbb{I}(\theta_d \neq \hat{\theta}_d)$. Unlike MAP, it gives partial credit to estimates that are correct on a subset of coordinates.

### Why it matters
For discrete or structured parameters the MAP estimate can be isolated in probability space (all nearest neighbours have zero probability), making it unrepresentative of the posterior. MPM, by marginalising over all other components, acts as a centroid estimator and is typically more robust. It requires marginalisation (not just maximisation), so it depends on the global distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-point-estimation]] — specializes
- [[marginalization]] — uses
- [[maximum-a-posteriori-estimation-map]] — contrasts-with
- [[posterior-risk]] — instantiates
[To be populated during integration]