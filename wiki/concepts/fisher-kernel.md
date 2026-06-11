---
aliases: []
also_type: []
applies:
- generative-vs-discriminative-models
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
- kernel-methods
- information-geometry
id: pkis:concept:fisher-kernel
instantiates:
- kernel-construction-rules
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
specializes:
- generative-model-kernels
tags:
- Fisher-kernel
- generative-discriminative
- Fisher-information
- information-geometry
- score-function
title: Fisher Kernel
understanding: 0
uses:
- fisher-information
---

## Definition
Given a parametric generative model $p(\mathbf{x}|\boldsymbol{\theta})$, the Fisher score is
$$g(\boldsymbol{\theta},\mathbf{x}) = \nabla_{\boldsymbol{\theta}}\ln p(\mathbf{x}|\boldsymbol{\theta}),$$
and the **Fisher kernel** is
$$k(\mathbf{x},\mathbf{x}') = g(\boldsymbol{\theta},\mathbf{x})^T\,\mathbf{F}^{-1}\,g(\boldsymbol{\theta},\mathbf{x}'),$$
where $\mathbf{F} = \mathbb{E}_{\mathbf{x}}\!\left[g g^T\right]$ is the Fisher information matrix.

The Fisher information matrix acts as a whitening transform; its inclusion makes the kernel invariant under any smooth re-parameterisation $\boldsymbol{\theta}\to\psi(\boldsymbol{\theta})$.

### Why it matters
The Fisher kernel is the canonical bridge between generative and discriminative learning: a generative model (e.g., HMM, mixture model) defines the feature map via its score function, and a discriminative classifier (e.g., SVM) is then applied in that feature space, typically outperforming either paradigm alone.

### Connection to Fisher information
Dropping $\mathbf{F}^{-1}$ gives the non-invariant inner-product kernel $k = g^T g'$, which corresponds to whitened Fisher scores when $\mathbf{F}$ is estimated by the sample covariance of the scores.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-vs-discriminative-models]] — applies
- [[generative-model-kernels]] — specializes
- [[kernel-construction-rules]] — instantiates
- [[fisher-information]] — uses
[To be populated during integration]