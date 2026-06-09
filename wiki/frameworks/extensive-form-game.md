---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- decision-theory
extends:
- normal-form-game
id: pkis:framework:extensive-form-game
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- game-tree
- imperfect-information
- information-set
- sequential-game
title: Extensive-Form Game
understanding: 0
uses:
- monte-carlo-tree-search
---

## Definition
A representation of sequential, possibly stochastic, possibly partially observable games as a game tree: an initial state, a PLAYER function, ACTIONS, a RESULT transition, and a UTILITY payoff defined on terminal states. A distinguished player Chance models stochastic moves. Crucially, the extensive form captures *imperfect information* via *information sets* — sets of decision nodes a player cannot distinguish — letting it represent partial observability, simultaneous moves (by hiding earlier moves from later players), and perfect-recall assumptions. It can model most hard environment properties at once. Solution methods include backward induction (perfect information), conversion to normal form (exponential in information sets), and the sequence form (linear in tree size). Limitations: it does not handle continuous states/actions well and assumes the structure of the game is known.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[monte-carlo-tree-search]] — uses
- [[normal-form-game]] — extends
[To be populated during integration]