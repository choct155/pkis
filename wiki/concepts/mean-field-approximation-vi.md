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
- machine-learning
- bayesian-inference
id: pkis:concept:mean-field-approximation-vi
instantiates:
- conditional-independence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
specializes:
- mean-field-approximation
tags:
- mean-field
- variational-inference
- factorized-posterior
- CAVI
title: Mean Field Approximation (Variational)
understanding: 0
uses:
- markov-blanket
- kl-divergence
---

## Definition
$$q_\psi(z) = \prod_{j=1}^{J} q_j(z_j)$$

The mean field approximation assumes the variational posterior fully factorizes over $J$ groups of latent variables. No functional form for each $q_j$ need be specified in advance; the optimal form is derived by maximizing the ELBO coordinate-wise, yielding $q_j^*(z_j) \propto \exp\bigl(\mathbb{E}_{z_{\mathrm{mb}_j}}[\log \tilde{p}(z_j, z_{\mathrm{mb}_j})]\bigr)$, where $z_{\mathrm{mb}_j}$ denotes the Markov blanket of $z_j$.

### Why it matters
Mean field is the backbone of **free-form VI** (CAVI) and trades exact dependency structure for analytical tractability. Its main known failure mode is posterior over-confidence / variance underestimation, because minimizing $D_{\mathrm{KL}}(q\|p)$ is mode-seeking rather than mass-covering.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conditional-independence]] — instantiates: Mean field assumes full conditional independence across all latent variable groups.
- [[kl-divergence]] — uses: Mean field VI minimizes forward KL, leading to mode-seeking/over-confident posteriors.
- [[markov-blanket]] — uses: CAVI optimal update for each factor depends only on the Markov blanket of that variable.
- [[mean-field-approximation]] — specializes: The mean field approximation here is the variational/statistical specialization of the general mean-field concept.
[To be populated during integration]