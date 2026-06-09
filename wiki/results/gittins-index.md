---
aliases: []
also_type: []
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
- reinforcement-learning
- optimization
id: pkis:result:gittins-index
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch17
tags:
- bandits
- gittins-index
- optimal-stopping
- exploration-exploitation
- index-policy
- restart-mdp
title: Gittins Index
understanding: 0
---

## Definition
An index assigned to each arm of a multi-armed bandit that yields a remarkably simple optimal policy: at each step pull the arm with the highest Gittins index, then update the indices. The index of arm M in state s is defined by λ = max_{T>0} E(Σ_{t=0}^{T-1} γ^t R_t) / E(Σ_{t=0}^{T-1} γ^t) — the maximum obtainable utility per unit of discounted time, where T ranges over stopping rules. Equivalently it is the constant-reward arm M_λ that makes an optimal strategy exactly indifferent between continuing with M and switching to the fixed arm. Operationally, the index equals (1−γ) times the value of an optimal policy for the 'restart MDP' M^s — the arm augmented with an action that restarts it from its initial state s — which can be solved by ordinary MDP methods (Katehakis & Veinott 1987). Because each arm's index depends only on that arm's own dynamics, the first decision costs O(n) and each subsequent decision O(1). The index decomposes a coupled n-armed decision problem into n independent single-arm computations; this decomposability is special to bandit processes (where arms are Markov reward processes) and fails for selection problems and bandit superprocesses, for which no index function exists. Due to John Gittins (Gittins & Jones 1974).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]