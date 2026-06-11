---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
- probabilistic-modeling
id: pkis:framework:linear-factor-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch13
tags:
- generative-models
- latent-variables
- representation-learning
- dimensionality-reduction
title: Linear Factor Model
understanding: 0
---

## Definition
$$\mathbf{x} = \mathbf{W}\mathbf{h} + \mathbf{b} + \boldsymbol{\epsilon}, \quad \mathbf{h} \sim \prod_i p(h_i), \quad \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \boldsymbol{\psi})$$

A family of probabilistic generative models in which observed data $\mathbf{x}$ is produced by a linear transformation of latent factors $\mathbf{h}$ drawn from a factorial prior, plus independent noise. Different choices of $p(\mathbf{h})$ and $\boldsymbol{\psi}$ yield probabilistic PCA, factor analysis, ICA, and sparse coding as special cases.

### Why it matters
Linear factor models are the simplest latent-variable generative models and provide the conceptual foundation for representation learning, autoencoders, and deep generative models. They make explicit the decomposition of observed covariance into signal (captured by $\mathbf{W}\mathbf{W}^\top$) and noise ($\boldsymbol{\psi}$), and show how identifiability depends critically on the choice of prior over latent variables.

### Key variants
| Model | $p(\mathbf{h})$ | $\boldsymbol{\psi}$ |
|---|---|---|
| Factor analysis | $\mathcal{N}(\mathbf{0},\mathbf{I})$ | diagonal, heterogeneous |
| Probabilistic PCA | $\mathcal{N}(\mathbf{0},\mathbf{I})$ | $\sigma^2\mathbf{I}$ (isotropic) |
| ICA | non-Gaussian factorial | 0 (deterministic decoder) |
| Sparse coding | Laplace / Student-t | $\frac{1}{\beta}\mathbf{I}$ |

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]