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
- variational-inference
- probabilistic-programming
- automatic-differentiation
id: pkis:technique:advi
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
- murphy-pml2-advanced-ch10
tags:
- ADVI
- change-of-variables
- automatic-differentiation
- variational-inference
- unconstrained-parameterisation
title: Automatic Differentiation Variational Inference (ADVI)
understanding: 0
---

## Definition
$$\theta = T^{-1}(z), \quad z \sim \mathcal{N}(\mu, \text{diag}(\sigma^2)), \quad \text{ELBO}(\mu,\sigma) = \mathbb{E}_{q(z)}\left[\log p(D, T^{-1}(z)) + \log\left|\det J_{T^{-1}}\right| - \log q(z)\right]$$

ADVI automatically transforms constrained model parameters to an unconstrained space via differentiable bijections $T$, fits a Gaussian variational posterior in that space, and optimises the ELBO using automatic differentiation and stochastic gradient ascent.

### Why it matters
ADVI converts arbitrary probabilistic models into a standardised variational inference problem without user-designed variational families, enabling "turn-key" approximate Bayesian inference. It is the inference backend of Stan's `variational` mode and similar PPL systems. The Jacobian correction $|\det J_{T^{-1}}|$ ensures the density is correctly transformed, addressing the MAP reparameterisation problem.

### Limitations
The Gaussian assumption in the unconstrained space may poorly approximate multimodal or heavy-tailed posteriors; normalising flows and other richer families have been proposed as extensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]