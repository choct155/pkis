---
aliases: []
also_type: []
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
- probability-theory
generalizes:
- directed-graphical-models
- undirected-graphical-models
id: pkis:concept:structured-probabilistic-model
instantiates:
- probabilistic-graphical-models
- bayesian-networks
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch03
tags:
- graphical-model
- factorization
- directed
- undirected
- Bayesian-network
title: Structured Probabilistic Model (Graphical Model)
understanding: 0
uses:
- conditional-independence
- partition-function
- latent-variable-models
---

## Definition
A **structured probabilistic model** (graphical model) represents a joint distribution over variables $\{x_1,\ldots,x_n\}$ by a graph $G$ whose nodes are variables and whose edges encode direct probabilistic dependencies. Two families exist:

- **Directed** (Bayesian network): $p(\mathbf{x})=\prod_i p(x_i\mid \text{Pa}_G(x_i))$.
- **Undirected** (Markov random field): $p(\mathbf{x})=\frac{1}{Z}\prod_i \varphi^{(i)}(C^{(i)})$ over cliques $C^{(i)}$.

Both families drastically reduce the number of parameters required relative to a fully tabular joint, since each factor depends only on a small subset of variables.

### Why it matters
Graphical models provide a language for expressing independence assumptions in probabilistic ML systems. They underlie variational autoencoders, Bayesian networks, Markov random fields, and many generative models used throughout deep learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[latent-variable-models]] — uses
- [[partition-function]] — uses: normalizing constant Z in undirected models
- [[bayesian-networks]] — instantiates
- [[conditional-independence]] — uses
- [[undirected-graphical-models]] — generalizes
- [[directed-graphical-models]] — generalizes
- [[probabilistic-graphical-models]] — instantiates
[To be populated during integration]