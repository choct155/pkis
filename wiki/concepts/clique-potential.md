---
aliases: []
also_type: []
analogous-to:
- factor-graph
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
id: pkis:concept:clique-potential
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- partition-function
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
tags:
- undirected-models
- MRF
- markov-random-field
- factorization
- partition-function
title: Clique Potential (Factor in Undirected Models)
understanding: 0
uses:
- undirected-graphical-models
- hammersley-clifford-theorem
---

## Definition
$$\tilde{p}(\mathbf{x}) = \prod_{C \in \mathcal{G}} \phi(C)$$

A non-negative function $\phi(C)$ defined over the variables in a clique $C$ of an undirected graphical model that encodes the affinity of those variables for each joint configuration; multiplying all clique potentials yields the unnormalized joint distribution.

### Why it matters
Clique potentials are the fundamental building blocks of Markov random fields. They are not required to be normalized or to have probabilistic interpretations individually, which gives considerable modeling flexibility. The requirement that all $\phi(C) \geq 0$ is satisfied automatically by energy-based parameterization $\phi(C) = \exp(-E_C)$. The scope of each potential determines the conditional independence structure of the model: two variables not sharing any clique are conditionally independent given their Markov blanket.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[factor-graph]] — analogous-to
- [[hammersley-clifford-theorem]] — uses
- [[partition-function]] — prerequisite-of
- [[undirected-graphical-models]] — uses
[To be populated during integration]