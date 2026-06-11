---
aliases: []
also_type: []
applies:
- hierarchical-bayesian-models
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
- machine-learning
- bayesian-inference
id: pkis:concept:variational-bayes
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
specializes:
- variational-inference-framework
tags:
- variational-Bayes
- parameter-posterior
- mean-field
- CAVI
title: Variational Bayes
understanding: 0
uses:
- cavi
- conjugate-prior
- marginal-likelihood
---

## Definition
**Variational Bayes** (Attias 2000) applies variational inference specifically to Bayesian parameter posterior approximation: treat model parameters $\theta$ as latent variables and approximate $p(\theta|\mathcal{D})$ via a factorized family
$$q(\theta|\psi_\theta)=\prod_j q(\theta_j|\psi_{\theta_j})$$
by maximizing the ELBO $\mathcal{L}(\psi_\theta|\mathcal{D})=\mathbb{E}_{q(\theta)}[\log p(\theta,\mathcal{D})]+\mathbb{H}(q(\theta))$. Updates are derived via CAVI, and the optimal forms fall out from the model's conjugate structure.

### Why it matters
Variational Bayes provides a principled, computationally tractable route to full Bayesian parameter inference in complex models (GMMs, HMMs, LDA), avoiding MCMC's mixing difficulties. It is closely related to empirical Bayes when prior hyperparameters $\xi$ are also optimized via the ELBO.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[marginal-likelihood]] — uses: Variational Bayes maximizes a lower bound on the marginal likelihood (ELBO) rather than the marginal likelihood directly.
- [[conjugate-prior]] — uses: Conjugate priors allow CAVI updates in variational Bayes to be derived in closed form.
- [[hierarchical-bayesian-models]] — applies
- [[variational-inference-framework]] — specializes: Variational Bayes specializes VI to parameter posterior approximation in Bayesian models.
- [[cavi]] — uses: Variational Bayes applies CAVI to iteratively update each parameter-group's variational distribution.
[To be populated during integration]