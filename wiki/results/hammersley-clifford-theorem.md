---
aliases: []
also_type: []
applies:
- markov-random-field
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- bayesian-stats
id: pkis:result:hammersley-clifford-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- undirected-graphical-models
related_concepts: []
sources:
- hastie-esl-ch17
tags:
- markov-random-field
- clique-potentials
- factorization
- gibbs-distribution
- conditional-independence
title: Hammersley-Clifford Theorem
understanding: 0
uses:
- partition-function
- conditional-independence
---

## Definition
The Hammersley-Clifford theorem (Hammersley and Clifford, 1971; Clifford, 1990) establishes the equivalence between the Markov (conditional-independence) properties of an undirected graph and a clique-based factorization of the joint density. For a Markov network G with a strictly positive density, the density factorizes over the maximal cliques of the graph:

    f(x) = (1/Z) * prod_{C in C} psi_C(x_C),

where C is the set of maximal cliques, each psi_C is a positive clique potential (an affinity scoring configurations, not in general a density), and Z = sum_x prod_C psi_C(x_C) is the normalizing constant (partition function). Conversely, any density of this product-over-cliques form has the conditional-independence structure encoded by those cliques.

The theorem is the formal backbone of undirected graphical models: it guarantees that the two natural specifications of an MRF -- by its local Markov independencies (missing edges = conditional independencies) and by its global factorization into local potentials -- describe exactly the same class of distributions, provided the distribution is positive. This justifies decomposing inference and estimation into per-clique computations (e.g., the junction/join-tree algorithm) and accumulating across the graph. The positivity condition is essential; without it the equivalence can fail.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[markov-random-field]] — applies
- [[conditional-independence]] — uses: Links conditional-independence (Markov) structure to the product-over-cliques form.
- [[partition-function]] — uses: The factorization is normalized by the partition function Z.
- [[undirected-graphical-models]] — prerequisite-of: Establishes the clique-factorization <-> Markov-property equivalence that defines undirected graphical models.
[To be populated during integration]