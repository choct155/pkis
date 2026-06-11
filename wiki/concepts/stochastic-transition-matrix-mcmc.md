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
- probability-theory
- linear-algebra
- statistics
id: pkis:concept:stochastic-transition-matrix-mcmc
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
tags:
- markov-chain
- transition-matrix
- mixing-time
- stochastic-matrix
- perron-frobenius
title: Stochastic Transition Matrix (MCMC)
understanding: 0
---

## Definition
$$A_{i,j} = T(x' = i \mid x = j), \quad \sum_i A_{i,j} = 1 \;\forall j$$
$$v^{(t)} = A^t v^{(0)}$$

A column-stochastic matrix $A$ encodes the Markov chain transition operator $T(x'|x)$; iterating it amounts to exponentiating $A$, so the distribution $v^{(t)}$ over states evolves as a linear dynamical system.

### Why it matters
The eigendecomposition perspective explains MCMC convergence: by the Perron–Frobenius theorem the largest eigenvalue of $A$ is 1 (unique under irreducibility and aperiodicity), and all other eigenvalues satisfy $|\lambda_k| < 1$. The magnitude of the second-largest eigenvalue $|\lambda_2|$ controls the **mixing time**: the smaller $1 - |\lambda_2|$, the slower the convergence to stationarity.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]