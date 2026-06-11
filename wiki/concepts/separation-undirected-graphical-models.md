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
id: pkis:concept:separation-undirected-graphical-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch16
tags:
- conditional-independence
- markov-random-field
- MRF
- graphical-models
- inference
title: Separation in Undirected Graphical Models
understanding: 0
---

## Definition
In an undirected graphical model, a set $A$ is **separated** from a set $B$ given observed set $S$ if every path between a node in $A$ and a node in $B$ passes through at least one node in $S$. Paths through unobserved nodes are *active*; paths through observed nodes are *inactive*.

$$A \perp B \mid S \iff \text{all paths } A \leadsto B \text{ are blocked by } S$$

### Why it matters
Separation is the undirected analogue of d-separation and provides a graphical criterion for reading off all conditional independences implied by a Markov random field. It underpins the Hammersley–Clifford theorem and is strictly simpler than d-separation because there are no v-structures to track. Algorithms that exploit separation (e.g., belief propagation, Gibbs sampling over Markov blankets) are the basis for efficient inference in sparse undirected models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]