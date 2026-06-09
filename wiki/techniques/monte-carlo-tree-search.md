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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- deep-learning
id: pkis:technique:monte-carlo-tree-search
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch08
tags:
- reinforcement-learning
- decision-time-planning
- rollout
- tree-search
- go
- alphago
title: Monte Carlo Tree Search (MCTS)
understanding: 0
---

## Definition
A decision-time planning method (Coulom, 2006; Kocsis & Szepesvari, 2006) that extends rollout algorithms by accumulating value estimates from Monte Carlo simulations to successively direct simulations toward more highly-rewarding trajectories; executed afresh at each new state. It maintains action-value estimates on the edges of a tree rooted at the current state, covering the most likely next-step state-action pairs. Each iteration has four steps: (1) Selection - a tree policy (e.g. UCB/epsilon-greedy, balancing exploration and exploitation) traverses the tree from the root to a leaf; (2) Expansion - the tree is grown by adding child node(s) from the leaf; (3) Simulation - a complete episode is run from there using a simple rollout policy outside the tree; (4) Backup - the simulated return updates the action values on the traversed tree edges (nothing is saved beyond the tree). After the compute budget is exhausted, the root action with the best statistic (highest value or visit count) is executed; descendant subtrees may be reused next step. MCTS effectively grows a partial action-value lookup table focused on high-yield trajectory prefixes, avoiding global function approximation. It drove computer Go from weak amateur (2005) to grandmaster (2015) and, combined with deep-network value learning, underpinned AlphaGo's 2016 victories.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]