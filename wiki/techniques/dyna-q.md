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
contrasts-with:
- decision-time-planning
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:technique:dyna-q
instantiates:
- model-based-rl
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
tags:
- reinforcement-learning
- planning
- q-learning
- integrated-architecture
- model-learning
title: Dyna-Q
understanding: 0
uses:
- planning-rl
---

## Definition
A simple architecture (Sutton, 1990) that integrates planning, acting, model-learning, and direct reinforcement learning in an online agent, all proceeding continually and (conceptually) in parallel. Tabular Dyna-Q uses one-step tabular Q-learning as both the direct RL method (on real transitions) and the planning method (on simulated transitions from the model). After each real step it (d) applies Q-learning to the real transition, (e) updates a deterministic table model Model(S,A) <- R,S', then (f) performs n planning iterations: sample a previously observed state-action pair, query the model, and apply the same Q-learning update. The reinforcement learning update is thus the 'final common path' for learning and planning. Larger n dramatically accelerates convergence (e.g. on a gridworld maze, n=50 reaches optimal in ~3 episodes vs. ~25 for n=0). Dyna-Q+ adds an exploration bonus r + kappa*sqrt(tau), where tau is time since a state-action pair was last tried, encouraging detection of environment changes (e.g. the shortcut maze) at the cost of extra exploration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[decision-time-planning]] — contrasts-with: Dyna-Q exemplifies background planning (improving a global value function), opposed to decision-time planning.
- [[planning-rl]] — uses: Dyna-Q performs n background-planning Q-learning updates per real step on simulated experience.
- [[model-based-rl]] — instantiates: Dyna-Q is a concrete integrated model-based RL architecture (model-learning + planning + direct RL).
[To be populated during integration]