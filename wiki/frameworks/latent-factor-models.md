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
- probabilistic-modeling
- unsupervised-learning
generalizes:
- mixture-models
- factor-analysis
id: pkis:framework:latent-factor-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- variational-autoencoder
related_concepts: []
sources:
- murphy-pml2-advanced-ch28
specializes:
- latent-variable-models
tags:
- latent-variables
- dimensionality-reduction
- generative-model
- decoder
title: Latent Factor Models
understanding: 0
uses:
- exponential-family
- generative-vs-discriminative-models
---

## Definition
$$z \sim p(z), \quad x \mid z \sim \text{ExpFam}(x \mid f(z))$$

A latent factor model posits a single hidden layer of continuous latent variables $z$ and a decoder $f$ that maps $z$ to the parameters of an exponential-family likelihood for the observed $x$. When $f$ is linear and $p(z)=\mathcal{N}(0,I)$, the family unifies factor analysis, probabilistic PCA, and mixtures of factor analyzers as special cases depending on the form of $\Psi$.

### Why it matters
Latent factor models provide a principled probabilistic language for dimensionality reduction, density estimation, and posterior inference over meaningful low-dimensional representations. By varying the prior $p(z)$ and the likelihood $p(x\mid z)$, one can derive a large taxonomy of classical models (Table 28.1 in Murphy PML2).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variational-autoencoder]] — prerequisite-of
- [[factor-analysis]] — generalizes
- [[mixture-models]] — generalizes
- [[generative-vs-discriminative-models]] — uses
- [[exponential-family]] — uses
- [[latent-variable-models]] — specializes
[To be populated during integration]