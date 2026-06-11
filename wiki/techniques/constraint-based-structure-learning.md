---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- statistics
- machine-learning
id: pkis:technique:constraint-based-structure-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
tags:
- PC-algorithm
- conditional-independence
- Markov-equivalence
- causal-discovery
- DAG
title: Constraint-Based Structure Learning (PC Algorithm)
understanding: 0
---

## Definition
Constraint-based methods infer graph structure by performing a sequence of conditional independence (CI) tests on the data and using the results to orient edges:

1. Start with a complete undirected graph.
2. Remove edge $(i,j)$ if $\exists\, S \subseteq V \setminus \{i,j\}$ such that $X_i \perp X_j \mid X_S$ (using $\chi^2$, Fisher-$z$, or kernel-based CI tests).
3. Orient v-structures (colliders) and propagate orientations via Meek rules.

The PC algorithm is sound and complete under the Causal Markov Condition and Faithfulness assumptions, recovering the Markov equivalence class (CPDAG) of the true DAG.

### Why it matters
Constraint-based methods are computationally efficient for sparse graphs (the number of CI tests scales polynomially with $D$ under sparsity), provide explicit statistical tests, and are the primary alternative to score-based methods for learning causal structure from observational data.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]