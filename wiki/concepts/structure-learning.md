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
- probabilistic-graphical-models
- machine-learning
id: pkis:concept:structure-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
tags:
- graphical-models
- model-selection
- greedy-search
- bayesian-network
- score-function
title: Structure Learning
understanding: 0
---

## Definition
**Structure learning** is the problem of inferring the graph topology $\mathcal{G}$ of a probabilistic graphical model from data, as opposed to parameter learning which assumes $\mathcal{G}$ is given.

Most algorithms perform a *greedy search* in graph space: propose a structure, score it by a criterion that trades off training-set likelihood against model complexity (e.g., BIC, BDe), then explore neighbours obtained by adding, removing, or reversing single edges.

### Why it matters
Learning graph structure directly from data can discover conditional independence relationships without requiring domain experts to specify them. However, the search space is super-exponential in the number of variables, making exact search intractable. In deep learning, the alternative of using *latent variables with a fixed structure* sidesteps structure learning by implicitly capturing the required dependencies through the latent layer, which is one reason deep models favour latent-variable approaches over adaptive structure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]