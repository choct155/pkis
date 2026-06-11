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
- probabilistic-modelling
- bayesian-inference
id: pkis:framework:model-based-ml
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch01
tags:
- data-generating-process
- probabilistic-models
- bayesian
- generative
- latent-variables
- decision-making
title: Model-Based Machine Learning (MBML)
understanding: 0
---

## Definition
$$p(\mathcal{D}, \theta) = p(\theta)\prod_{i}p(x_i|\theta)$$

Model-based machine learning treats every learning problem as specifying a probabilistic model of the data-generating process (DGP) and performing Bayesian or approximate inference within that model, rather than directly fitting a mapping $f: X \to Y$.

### Why it matters
By encoding structural assumptions about the DGP explicitly — rather than absorbing them implicitly into an architecture — MBML yields representations that generalise better under distribution shift, are more data-efficient, and support causal / scientific reasoning. It unifies prediction, generation, latent-variable discovery, and decision-making under a single inferential lens.

### Key tasks covered
Four canonical task types follow from choosing different model families: (1) **prediction** $p(y|x)$, (2) **generation** $p(x)$ or $p(x|c)$, (3) **discovery** via latent-variable models $p(z,x)$, and (4) **control / decision-making** under uncertainty.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]