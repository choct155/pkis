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
- monte-carlo-dropout
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- bayesian-inference
- deep-learning
- variational-inference
id: pkis:technique:bayes-by-backprop
instantiates:
- bayesian-deep-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
specializes:
- variational-inference
tags:
- ELBO
- reparameterisation-trick
- mean-field
- diagonal-Gaussian
- weight-uncertainty
title: Bayes by Backprop (BBB)
understanding: 0
uses:
- elbo
- reparameterization-trick
- backpropagation
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
- [[monte-carlo-dropout]] — contrasts-with: BBB explicitly maintains a variational posterior; MCD uses implicit approximation via dropout
- [[backpropagation]] — uses
- [[reparameterization-trick]] — uses
- [[elbo]] — uses
- [[variational-inference]] — specializes
- [[bayesian-deep-learning]] — instantiates
[To be populated during integration]