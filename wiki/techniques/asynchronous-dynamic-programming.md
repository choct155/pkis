---
aliases: []
also_type: []
applies:
- markov-decision-processes
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- curse-of-dimensionality
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
extends:
- value-iteration
id: pkis:technique:asynchronous-dynamic-programming
instantiates:
- generalized-policy-iteration
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch04
tags:
- dynamic-programming
- in-place
- scalability
title: Asynchronous Dynamic Programming
understanding: 0
---

## Definition
Asynchronous DP comprises in-place iterative DP algorithms that update states in an arbitrary order — possibly stochastic and using out-of-date values — rather than in systematic full sweeps of the state set.

### Operational mechanism
Instead of updating every state once per sweep, an asynchronous method updates whichever states it chooses, using whatever neighboring values are currently available. For example, asynchronous value iteration updates a single state $s_k$ per step $k$ via the value-iteration update. Some states may be updated many times before others are updated at all.

### Conditions and convergence
Correctness requires that *every* state continue to be updated infinitely often — no state may be permanently ignored. Under this condition and $0 \le \gamma < 1$, asymptotic convergence to $v_*$ holds even for randomly ordered updates.

### Why it matters
Full sweeps are infeasible when the state set is enormous — backgammon has over $10^{20}$ states, where one sweep would take a thousand years at a million updates per second. Asynchronous DP avoids being locked into long sweeps, lets value information propagate efficiently, and — crucially — allows DP computation to be interleaved with real-time agent interaction, focusing updates on the states the agent actually visits. This focusing is a recurring theme across reinforcement learning.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[curse-of-dimensionality]] — contrasts-with: Mitigates the cost of huge state sets by avoiding full sweeps.
- [[markov-decision-processes]] — applies: Solves large finite MDPs without full sweeps.
- [[value-iteration]] — extends: Drops systematic sweeps; updates states in arbitrary order.
- [[generalized-policy-iteration]] — instantiates: Fine-grained, per-state interleaving of evaluation and improvement.
[To be populated during integration]