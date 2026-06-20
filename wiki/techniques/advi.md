---
aliases: []
also_type: []
applies:
- map-reparameterisation-noninvariance
- probabilistic-programming-language
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- normalizing-flows
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- variational-inference
- probabilistic-programming
- automatic-differentiation
extends:
- normalizing-flows
id: pkis:technique:advi
instantiates:
- variational-inference-framework
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
- murphy-pml2-advanced-ch10
- kucukelbir-automatic-2016
specializes:
- variational-inference
tags:
- ADVI
- change-of-variables
- automatic-differentiation
- variational-inference
- unconstrained-parameterisation
title: Automatic Differentiation Variational Inference (ADVI)
understanding: 0
uses:
- mean-field-approximation
- automatic-differentiation
- change-of-variables-for-densities
- elbo
- reparameterized-vi
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
- [[normalizing-flows]] — extends: ADVI can be combined with normalizing flows for richer posterior approximations.
- [[reparameterized-vi]] — uses: ADVI applies reparameterization in the unconstrained space after transforming parameters via bijections.
- [[variational-inference-framework]] — instantiates: ADVI is an automatic instantiation of Gaussian VI using differentiable bijections to handle constraints.
- [[probabilistic-programming-language]] — applies
- [[normalizing-flows]] — contrasts-with
- [[elbo]] — uses
- [[map-reparameterisation-noninvariance]] — applies: ADVI works in unconstrained space to sidestep reparameterisation sensitivity
- [[change-of-variables-for-densities]] — uses
- [[automatic-differentiation]] — uses
- [[mean-field-approximation]] — uses
- [[variational-inference]] — specializes
[To be populated during integration]