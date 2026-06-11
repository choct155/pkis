---
aliases: []
also_type: []
analogous-to:
- score-matching
- denoising-autoencoder
applies:
- manifold-hypothesis
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
- deep-learning
- representation-learning
- manifold-learning
id: pkis:technique:contractive-autoencoder
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch14
- murphy-pml1-intro-ch20
specializes:
- autoencoder
tags:
- Jacobian
- manifold-tangent
- score-matching
- regularization
- contraction
title: Contractive Autoencoder (CAE)
understanding: 0
uses:
- gradient-and-jacobian
- regularization
---

## Definition
A contractive autoencoder regularises the encoder $f$ by penalising the Frobenius norm of the encoder Jacobian at each training point:
$$\mathcal{L}(x,\, g(f(x))) + \lambda\left\|\frac{\partial f(x)}{\partial x}\right\|_F^2$$
where $\left\|\cdot\right\|_F^2 = \sum_{i,j}\left(\frac{\partial h_i}{\partial x_j}\right)^2$.

This forces the encoder mapping to be (locally) a contraction, i.e. to map small neighbourhoods of inputs to smaller neighbourhoods of codes, unless the input variation lies along data-manifold directions.

### Why it matters
The singular vectors of the Jacobian with the largest singular values estimate the tangent directions of the data manifold (Rifai et al., 2011), providing a principled geometric account of what the autoencoder has learned. The CAE also has formal connections to both score matching and the denoising autoencoder: in the limit of small Gaussian noise, DAE training is equivalent to a contractive penalty on the reconstruction function.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses
- [[gradient-and-jacobian]] — uses
- [[manifold-hypothesis]] — applies
- [[denoising-autoencoder]] — analogous-to: In the limit of small Gaussian noise, DAE training is equivalent to a contractive penalty on the reconstruction function
- [[score-matching]] — analogous-to: Contractive penalty on f(x) is closely related to score matching objective
- [[autoencoder]] — specializes
[To be populated during integration]