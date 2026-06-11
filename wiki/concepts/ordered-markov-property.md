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
- probability-theory
generalizes:
- markov-chains
id: pkis:concept:ordered-markov-property
instantiates:
- bayesian-networks
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch04
specializes:
- d-separation
tags:
- DAG
- conditional-independence
- Markov-property
- factorization
title: Ordered Markov Property (DAGs)
understanding: 0
uses:
- conditional-independence
---

## Definition
$$x_i \perp x_{\text{pred}(i)\setminus\text{pa}(i)} \mid x_{\text{pa}(i)}$$

A node is conditionally independent of all its predecessors in a topological ordering given only its parents, justifying the factorization $p(x_{1:N}) = \prod_{i=1}^N p(x_i \mid x_{\text{pa}(i)})$.

### Why it matters
This property is the foundational justification for representing any joint distribution as a product of local CPDs in a DAG, enabling exponential compression of parameters from $O(K^N)$ to $O(N \cdot K^{N_P+1})$ for sparse graphs. It is equivalent to the directed local Markov property and the directed global Markov property (d-separation).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-chains]] — generalizes
- [[d-separation]] — specializes
- [[conditional-independence]] — uses
- [[bayesian-networks]] — instantiates
[To be populated during integration]