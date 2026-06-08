---
aliases: []
also_type: []
applies:
- blind-source-separation
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- principal-component-analysis
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- statistical-learning
- deep-learning
id: pkis:technique:independent-component-analysis
instantiates:
- latent-variable-models
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch34
tags:
- latent-variables
- blind-source-separation
- non-gaussianity
- maximum-likelihood
- mackay-itila
- natural-gradient
title: Independent Component Analysis (ICA)
understanding: 0
uses:
- natural-gradient
- maximum-likelihood-estimation
---

## Definition
Independent component analysis is the simplest latent variable model with continuous latents. Each observation is modelled as a noise-free linear mixture of independent sources,

$$\mathbf{x} = G\mathbf{s},\qquad P(\mathbf{s}\mid H)=\prod_i p_i(s_i),$$

with mixing matrix $G$ unknown and (in the simplest case) square, $I=J$. The goal is to recover the unmixing matrix $W \equiv G^{-1}$ (up to scaling and permutation) from samples of $\mathbf{x}$ alone. The single-example log likelihood is

$$\ln P(\mathbf{x}\mid G,H) = \ln|\det W| + \sum_i \ln p_i(W_{ij}x_j),$$

yielding the gradient learning rule $\Delta W \propto [W^{T}]^{-1} + \mathbf{z}\mathbf{x}^{T}$, where $z_i = \varphi_i(a_i)$, $a_i = W_{ij}x_j$, and $\varphi_i = d\ln p_i/da$.

### The role of non-Gaussianity
The choice of $\varphi$ implicitly fixes the source prior. A linear $\varphi_i(a_i)=-\kappa a_i$ assumes Gaussian sources, which are rotation-invariant, so the alignment of $G$ is unrecoverable. ICA only works because real sources are non-Gaussian; the popular $\varphi=-\tanh(a)$ encodes a heavy-tailed $p(s)\propto 1/\cosh(s)$.

### Why it matters
ICA solves blind source separation — recovering hidden signals (the cocktail-party problem, EEG sources) from mixtures with no knowledge of the mixing — and is a canonical demonstration that independence plus non-Gaussianity yields identifiability where second-order methods like PCA cannot.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[principal-component-analysis]] — contrasts-with: ICA assumes independent non-Gaussian sources and recovers mixing directions; PCA assumes Gaussian latents and only fixes a variance-ordered subspace.
- [[maximum-likelihood-estimation]] — uses: ICA's learning rule is steepest ascent on the marginal log likelihood of the mixtures.
- [[natural-gradient]] — uses: The covariant ICA update is the natural-gradient form of the maximum-likelihood ascent.
- [[blind-source-separation]] — applies: ICA is the workhorse algorithm for solving the BSS problem.
- [[latent-variable-models]] — instantiates: ICA is the simplest latent variable model with continuous latents.
[To be populated during integration]