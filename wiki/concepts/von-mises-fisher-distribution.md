---
aliases: []
also_type: []
analogous-to:
- gaussian-distribution
applies:
- word-embeddings
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
- probability-theory
- statistics
- machine-learning
id: pkis:concept:von-mises-fisher-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch02
tags:
- von-mises-fisher
- directional-statistics
- spherical
- normalized-embeddings
- concentration
title: Von Mises–Fisher Distribution
understanding: 0
uses:
- pmf-and-pdf
- mixture-models
---

## Definition
The **von Mises–Fisher (vMF) distribution** is the analog of the Gaussian for data on the unit sphere $\mathbb{S}^{D-1} \subset \mathbb{R}^D$:
$$\mathrm{vMF}(\mathbf{x} \mid \boldsymbol{\mu}, \kappa) = \frac{\kappa^{D/2-1}}{(2\pi)^{D/2} I_{D/2-1}(\kappa)} \exp(\kappa\, \boldsymbol{\mu}^\top \mathbf{x}),$$
where $\|\boldsymbol{\mu}\|=1$ is the mean direction, $\kappa \geq 0$ is the concentration parameter (analogous to inverse variance), and $I_r$ is the modified Bessel function of order $r$. For $D=2$ it reduces to the von Mises distribution on the circle.

### Why it matters
The vMF distribution is the correct distribution for directional data and $\ell_2$-normalized embeddings (e.g., word/sentence embeddings, image descriptors). It is used in spherical $k$-means and spherical topic models, and in variational autoencoders with hyperspherical latent spaces.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mixture-models]] — uses
- [[word-embeddings]] — applies
- [[pmf-and-pdf]] — uses
- [[gaussian-distribution]] — analogous-to
[To be populated during integration]