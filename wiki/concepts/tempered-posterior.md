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
- bayesian-inference
- deep-learning
id: pkis:concept:tempered-posterior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- power-posterior
- alpha-posterior
- likelihood-tempering
- calibration
- misspecification
title: Tempered / Cold Posterior
understanding: 0
---

## Definition
$$\log p_{\text{tempered}}(\theta|D) = \alpha \log p(y|X,\theta) + \log p(\theta) + \text{const}$$
$$\log p_{\text{cold}}(\theta|D) = \frac{1}{T}\log p(y|X,\theta) + \frac{1}{T}\log p(\theta) + \text{const}, \quad T<1$$

The tempered ($\alpha$-) or cold posterior rescales the likelihood by a factor $\alpha = 1/T < 1$ before combining with the prior, sharpening the posterior relative to the standard Bayes update.

### Why it matters
In practice, BNN classifiers trained with softmax likelihoods often achieve better predictive accuracy when $\alpha > 1$ (cold posteriors). The primary cause is *underrepresentation of aleatoric label uncertainty*: the softmax likelihood over-assigns uncertainty to well-labelled training points. With a Gaussian prior, the cold posterior is equivalent to the tempered posterior with a rescaled prior variance ($\sigma^2_{\text{tempered}} = T\sigma^2_{\text{cold}}$). Using a Dirichlet observation model to explicitly model label noise eliminates the need for tempering.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]