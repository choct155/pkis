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
- statistics
- statistical-physics
id: pkis:concept:markov-random-field
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
- murphy-pml2-advanced-ch04
tags:
- undirected-graph
- clique-potential
- partition-function
- Ising-model
- Hammersley-Clifford
title: Markov Random Field (Undirected Graphical Model)
understanding: 0
---

## Definition
$$p(\mathbf{x}) = \frac{1}{Z} \prod_{C} \psi_C(\mathbf{x}_C), \qquad Z = \sum_{\mathbf{x}} \prod_C \psi_C(\mathbf{x}_C)$$
where the product runs over maximal cliques $C$ of an undirected graph, $\psi_C \geq 0$ are clique potential functions, and $Z$ is the partition function.

An undirected graphical model represents the joint distribution as a product of non-negative potential functions over maximal cliques; conditional independence is determined by simple graph separation (removing conditioning nodes disconnects the graph).

### Why it matters
MRFs elegantly express **soft constraints** and spatial/symmetric dependencies (e.g., Ising models, image priors) where there is no natural causal direction. The Hammersley–Clifford theorem guarantees equivalence between graph-separation-based CI statements and the clique factorisation (for strictly positive potentials). The main limitation is the intractable partition function $Z$, which is exponential in the number of variables in the worst case and must be handled by approximate inference.

### Boltzmann / energy form
Writing $\psi_C(\mathbf{x}_C) = \exp\{-E(\mathbf{x}_C)\}$ gives the Boltzmann distribution; the joint energy is the sum of clique energies.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]