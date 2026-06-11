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
- probability
id: pkis:framework:bayesian-nonparametric-models
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
tags:
- nonparametric
- stochastic-process
- prior
- bayesian
- infinite-dimensional
title: Bayesian Nonparametric Models
understanding: 0
---

## Definition
A Bayesian nonparametric (BNP) model places a prior distribution directly on infinite-dimensional objects of interest — functions, probability distributions, graphs, etc. — rather than on a finite-dimensional parameter vector. Formally, let $\mathcal{F}$ be a space of such objects (e.g., all measurable functions $f:\mathcal{X}\to\mathbb{R}$); BNP specifies a stochastic process $\Pi$ over $\mathcal{F}$ as the prior, with posterior $\Pi(\cdot \mid \mathcal{D}) \propto \mathcal{L}(\mathcal{D}\mid f)\,\Pi(df)$. The effective complexity of the model can grow with the data, avoiding underfitting, while Bayesian regularisation avoids overfitting the infinitely flexible prior.

In practice inference is always over a finite set of "projections" (e.g., function evaluations at observed inputs), which often renders computation tractable.

### Why it matters
BNP provides a principled, fully probabilistic alternative to model-selection procedures: instead of choosing the number of components, basis functions, or latent dimensions in advance, the posterior automatically adapts to the data. This subsumes Gaussian processes (priors on functions), Dirichlet processes (priors on distributions), and many other constructions under one umbrella.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]