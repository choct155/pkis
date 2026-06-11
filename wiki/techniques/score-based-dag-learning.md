---
aliases: []
also_type: []
applies:
- bayesian-networks
- causal-discovery
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- constraint-based-structure-learning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- machine-learning
- statistics
id: pkis:technique:score-based-dag-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch30
tags:
- DAG
- causal-discovery
- BIC
- score-function
- structure-learning
title: Score-Based DAG Structure Learning
understanding: 0
uses:
- information-criteria
- markov-equivalence-class
---

## Definition
$$\hat{G} = \arg\max_{G \in \mathrm{DAGs}} \; s(G, \mathbf{X})$$

where the score $s$ is typically the BIC, BDe, or a penalised log-likelihood, and the search space is restricted to directed acyclic graphs (DAGs). Because the number of DAGs is super-exponential in $D$, exact search via dynamic programming is feasible only for small $D$; approximate methods include greedy equivalence search (GES), hill-climbing over the Markov equivalence class, and continuous relaxations (e.g., NOTEARS).

### Why it matters
Score-based DAG learning is one of the two main paradigms for causal discovery (the other being constraint-based methods like PC). Continuous relaxations have recently made it scalable to hundreds of variables by reframing the DAG acyclicity constraint as a smooth equality: $h(W) = \operatorname{tr}(e^{W \circ W}) - D = 0$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[constraint-based-structure-learning]] — contrasts-with
- [[markov-equivalence-class]] — uses
- [[causal-discovery]] — applies
- [[information-criteria]] — uses
- [[bayesian-networks]] — applies
[To be populated during integration]