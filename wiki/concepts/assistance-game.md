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
- multi-agent-systems
- ai-alignment
- reinforcement-learning
id: pkis:concept:assistance-game
instantiates:
- cooperative-game
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- provably-beneficial-ai
- preference-uncertainty
- off-switch
- cooperative-irl
- POMDP
title: Assistance Game
understanding: 0
uses:
- markov-decision-processes
- nash-equilibrium
---

## Definition
A two-player cooperative game (Hadfield-Menell et al. 2017, as cooperative inverse reinforcement learning) formalizing provably beneficial AI: a human (Harriet) observes her own preference parameter θ and acts on it, while a robot (Robbie) holds a prior P(θ) and shares an identical payoff defined by θ — both maximize the human's payoff. The robot, by solving the game, infers preference information from the human's actions; behaviors such as teaching, demonstrating, asking permission, deferring, and being switched off emerge as equilibrium strategies rather than being scripted. The illustrative *paperclip game* shows a unique Nash equilibrium (found by myopic best response) in which Harriet's choices teach Robbie a code for her preferences, letting him act optimally without learning θ exactly. Solving an assistance game reduces to a structured POMDP over the game state plus the human's preference parameters.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[nash-equilibrium]] — uses
- [[markov-decision-processes]] — uses
- [[cooperative-game]] — instantiates
[To be populated during integration]