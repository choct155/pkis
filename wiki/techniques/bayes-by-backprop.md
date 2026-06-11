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
- bayesian-inference
- deep-learning
- variational-inference
id: pkis:technique:bayes-by-backprop
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- ELBO
- reparameterisation-trick
- mean-field
- diagonal-Gaussian
- weight-uncertainty
title: Bayes by Backprop (BBB)
understanding: 0
---

## Definition
Bayes by Backprop parameterises a factored Gaussian variational posterior $q_\psi(\theta) = \prod_i \mathcal{N}(\theta_i|\mu_i, \sigma_i^2)$ over all DNN weights and optimises the ELBO:
$$\mathcal{L}(\psi) = \mathbb{E}_{q_\psi}[\log p(D|\theta)] - D_{\text{KL}}(q_\psi \| p(\theta))$$
using the reparameterisation trick $\theta = \mu + \sigma \odot \epsilon,\; \epsilon\sim\mathcal{N}(0,I)$ to obtain low-variance ELBO gradients via backpropagation.

### Why it matters
BBB [Blundell et al. 2015] was the first practical large-scale variational BNN, demonstrating that a diagonal Gaussian posterior—doubling the parameter count—can meaningfully represent weight uncertainty in deep networks. It provides a clean bridge between weight-space VI and standard SGD training, inspiring local reparameterisation, VOGN, and NAGVAC extensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]