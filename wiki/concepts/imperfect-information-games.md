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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- optimization
- knowledge-representation
- bayesian-stats
id: pkis:concept:imperfect-information-games
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch05
specializes:
- adversarial-search
tags:
- adversarial-search
- partial-observability
- belief-state
- kriegspiel
- poker
- averaging-over-clairvoyance
title: Imperfect-Information Games (Belief-State Search)
understanding: 0
uses:
- expectiminimax
---

## Definition
Games in which players lack full access to the state -- either through deterministic partial observability (uncertainty arises only from the opponent's hidden choices, e.g. Kriegspiel, Battleship, Stratego, Phantom Go) or stochastic partial observability (missing information from random dealing, e.g. poker, bridge, whist). The state is replaced by a *belief state*: the set of all board states logically consistent with the percept history; tracking it is the problem of state estimation. A strategy must specify a move for every possible *percept sequence* (not every opponent move). For deterministic partial observability, AND-OR search over belief-state space finds a *guaranteed checkmate* (works for every state in the belief state, against any opponent who could even see all pieces); a *probabilistic checkmate* (unique to imperfect-information games) succeeds with probability 1 (or 1-epsilon) through randomization of the winning player's moves. Optimal play requires deliberate randomization to minimize information leaked to the opponent (and to bluff, gather information, or signal a partner), so state probabilities and the optimal randomized strategy are mutually defined -- a conundrum resolved only by the game-theoretic notion of an equilibrium, generally too expensive to compute. A tractable approximation for stochastic games, *averaging over clairvoyance*, treats the deal as a root chance node and averages EXPECTIMINIMAX over deals (or a sampled subset of N deals, with abstraction grouping similar hands); but it systematically errs because it assumes future states are perfectly known, so it never gathers information, hides information, or bluffs. Programs reach superhuman play in poker (Libratus, via abstraction + equilibrium computation) but humans retain an edge in bridge bidding and general Kriegspiel.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[adversarial-search]] — specializes: Imperfect-information game play is adversarial search under partial observability via belief states.
- [[expectiminimax]] — uses: Averaging over clairvoyance treats the deal as a root chance node and averages EXPECTIMINIMAX over deals.
[To be populated during integration]