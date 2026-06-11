---
aliases: []
also_type: []
analogous-to:
- language-model
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
- deep-learning
- generative-models
- density-estimation
generalizes:
- sigmoid-belief-network
id: pkis:concept:autoregressive-generative-network
instantiates:
- directed-graphical-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- autoregressive
- chain-rule
- FVBN
- NADE
- density-estimation
title: Auto-Regressive Generative Network (NADE / FVBN)
understanding: 0
uses:
- chain-rule-multivariate
---

## Definition
A directed generative model with no latent variables that factorises the joint distribution via the chain rule:
$$p(\mathbf{x})=\prod_{d=1}^D p(x_d\mid x_{d-1},\ldots,x_1),$$
where each conditional $p(x_d|\mathbf{x}_{<d})$ is represented by a neural network (logistic regression, MLP, or weight-tied NADE network). The complete graph structure means all variables are dependent.

### Why it matters
Auto-regressive networks (FVBNs, NADE, PixelRNN, WaveNet) provide tractable exact likelihoods without a partition function, making them strong density estimators and competitive generative models. Parameter sharing across conditionals (as in NADE) gives both statistical and computational efficiency, and the framework generalises to continuous, discrete, and sequential data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[chain-rule-multivariate]] — uses
- [[language-model]] — analogous-to: Autoregressive sequence models share the chain-rule factorisation structure.
- [[sigmoid-belief-network]] — generalizes: FVBNs/NADE generalise logistic-regression-per-conditional to neural network conditionals.
- [[directed-graphical-models]] — instantiates
[To be populated during integration]