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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- bayesian-stats
id: pkis:concept:latent-variable-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch34
tags:
- generative-model
- latent-variables
- unsupervised-learning
- mackay-itila
- marginalization
title: Latent Variable Model
understanding: 0
---

## Definition
A latent variable model is a generative model that specifies a full joint probability over observed variables $\mathbf{x}$ and unobserved (latent) variables $\mathbf{s}$, where the observables are explained as arising from the latents via a generative process with parameters $\theta$:

$$P(\mathbf{x}, \mathbf{s} \mid \theta) = P(\mathbf{x} \mid \mathbf{s}, \theta)\, P(\mathbf{s} \mid \theta).$$

The latents typically have a simple, often separable, prior $P(\mathbf{s}) = \prod_i p_i(s_i)$, so fitting the model amounts to finding a description of the data in terms of *independent components*. Inference about parameters proceeds through the likelihood obtained by marginalizing the latents:

$$P(\mathbf{x} \mid \theta) = \int P(\mathbf{x} \mid \mathbf{s}, \theta)\, P(\mathbf{s} \mid \theta)\, d\mathbf{s}.$$

### Canonical instances
Mixture models (latents = unknown class labels), hidden Markov models, factor analysis, and independent component analysis are all latent variable models. Even decoding an error-correcting code can be cast this way, with the codeword as latent and the encoding matrix $G$ as the (here known) parameter; in latent variable modelling $G$ is instead inferred from data.

### Why it matters
The paradigm unifies an enormous swath of unsupervised learning under one recipe: posit a low-complexity hidden cause, define a generative map to observables, then invert. The choice of latent prior (Gaussian vs. heavy-tailed) and noise model determines whether the recovered structure is identifiable, distinguishing PCA, factor analysis, and ICA as siblings within a single family.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]