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
id: pkis:concept:markov-blanket-directed
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
tags:
- conditional-independence
- local-computation
- Gibbs-sampling
- DAG
- graphical-model
title: Markov Blanket in Directed Graphs
understanding: 0
---

## Definition
The **Markov blanket** of node $x_i$ in a directed acyclic graph is the minimal set of nodes $\text{MB}(x_i)$ such that
$$x_i \perp\!\!\perp \mathbf{x}_{\{j \neq i\} \setminus \text{MB}(x_i)} \mid \text{MB}(x_i).$$
For a DAG, $\text{MB}(x_i)$ consists of:
- the **parents** of $x_i$,
- the **children** of $x_i$, and
- the **co-parents** (other parents of $x_i$'s children).

This follows from the DAG factorisation: the conditional $p(x_i \mid \mathbf{x}_{j \neq i})$ depends only on factors containing $x_i$, which are the node's own conditional and the conditionals of its children.

### Why it matters
The Markov blanket defines the local neighbourhood sufficient for all probabilistic queries about a node, which is central to local update rules (e.g., Gibbs sampling) and to active learning / sensor selection problems. For undirected graphs, the Markov blanket simplifies to the immediate neighbours.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]