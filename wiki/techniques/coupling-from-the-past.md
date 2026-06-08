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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- bayesian-stats
- statistical-learning
id: pkis:technique:coupling-from-the-past
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch32
tags:
- mcmc
- exact-sampling
- perfect-sampling
- propp-wilson
- markov-chains
- coalescence
title: Coupling from the Past
understanding: 0
---

## Definition
**Coupling from the past (CFTP)**, due to Propp and Wilson (1996), is an algorithm that draws a sample *exactly* from the equilibrium distribution $P$ of a Markov chain, with no asymptotic-convergence error. Run a copy of the chain from *every* possible initial state, all driven by a single shared random-number stream, starting at a time $T_0$ in the past and simulating up to the present ($t = 0$). If all trajectories have *coalesced* into one state by $t = 0$, that state $x(0)$ is an unbiased draw from $P$; if not, restart from a more distant $T_0$ (conveniently doubling each time), reusing the *same* random numbers at each shared timestep.

$$x(0) \sim P \quad\text{once all initial conditions map to a single state at } t=0.$$

### Why it works
If every start state at $T_0$ funnels to one state at $t=0$, then a chain run from the infinite past would also arrive there; that state is therefore a genuine equilibrium draw. Sampling *forward* until coalescence does not work, because the coalescence state is biased (e.g. it always lands on a wall).

### Why it matters
CFTP converts the unanswerable practical question 'has my MCMC chain converged?' into a checkable event. It eliminates burn-in bias entirely. The catch: naively it requires simulating from all states, which is infeasible for large state spaces unless extra structure (monotonicity) is exploited.

### Reusing random numbers
The random bits used at a given clock time $t$ must be identical across all runs from every $T_0$; using fresh randomness when $T_0$ changes destroys the validity of the method.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]