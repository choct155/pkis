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
- statistics
- physics
- machine-learning
id: pkis:technique:swendsen-wang
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch12
tags:
- mcmc
- auxiliary-variable
- ising-model
- cluster-sampling
- critical-slowing-down
title: Swendsen-Wang Algorithm
understanding: 0
---

## Definition
An auxiliary-variable cluster MCMC algorithm for ferromagnetic Ising/Potts models that introduces binary **bond variables** $v_e \in \{0,1\}$ per edge and alternates between two Gibbs steps:
1. **Sample bonds given spins**: for edge $e=(i,j)$, set $v_e=1$ with probability $p = 1 - e^{-2J}$ if $x_i = x_j$, else $v_e = 0$.
2. **Sample spins given bonds**: find connected components induced by active bonds; independently assign each component a uniformly random spin $\pm 1$.

The extended joint $p(x,v) \propto \prod_e \Psi(x_e, v_e)$ marginalises to the original Ising model $p(x)$.

### Why it matters
Gibbs sampling on Ising models suffers from critical slowing-down near the phase transition temperature $T_c$, where correlation lengths diverge and mixing becomes exponentially slow. Swendsen-Wang overcomes this by making *cluster-wide* spin flips that are exponentially larger than single-site updates, mixing rapidly at all temperatures for ferromagnetic models ($J>0$). It is the canonical example showing that auxiliary-variable augmentation can reduce mixing time from exponential to polynomial.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]