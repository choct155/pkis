---
aliases: []
also_type: []
applies:
- overfitting-and-underfitting
- model-selection-problem
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- machine-learning
- statistics
- probability
extends:
- hierarchical-bayesian-models
generalizes:
- latent-variable-models
id: pkis:framework:bayesian-nonparametric-models
instantiates:
- gaussian-process
- dirichlet-process
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch31
- kroese-statistical-modeling-ch11
specializes:
- bayesian-inference
tags:
- nonparametric
- stochastic-process
- prior
- bayesian
- infinite-dimensional
title: Bayesian Nonparametric Models
understanding: 0
uses:
- stochastic-process-as-prior
- kolmogorov-extension-theorem
---

## Definition
A Bayesian nonparametric (BNP) model places a prior distribution directly on infinite-dimensional objects of interest — functions, probability distributions, graphs, etc. — rather than on a finite-dimensional parameter vector. Formally, let $\mathcal{F}$ be a space of such objects (e.g., all measurable functions $f:\mathcal{X}\to\mathbb{R}$); BNP specifies a stochastic process $\Pi$ over $\mathcal{F}$ as the prior, with posterior $\Pi(\cdot \mid \mathcal{D}) \propto \mathcal{L}(\mathcal{D}\mid f)\,\Pi(df)$. The effective complexity of the model can grow with the data, avoiding underfitting, while Bayesian regularisation avoids overfitting the infinitely flexible prior.

In practice inference is always over a finite set of "projections" (e.g., function evaluations at observed inputs), which often renders computation tractable.

### Why it matters
BNP provides a principled, fully probabilistic alternative to model-selection procedures: instead of choosing the number of components, basis functions, or latent dimensions in advance, the posterior automatically adapts to the data. This subsumes Gaussian processes (priors on functions), Dirichlet processes (priors on distributions), and many other constructions under one umbrella.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[model-selection-problem]] — applies
- [[overfitting-and-underfitting]] — applies
- [[hierarchical-bayesian-models]] — extends
- [[bayesian-inference]] — specializes
- [[latent-variable-models]] — generalizes
- [[kolmogorov-extension-theorem]] — uses
- [[stochastic-process-as-prior]] — uses
- [[dirichlet-process]] — instantiates
- [[gaussian-process]] — instantiates
[To be populated during integration]