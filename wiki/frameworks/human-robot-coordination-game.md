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
- robotics
- reinforcement-learning
id: pkis:framework:human-robot-coordination-game
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- game-theory
- human-robot-interaction
- prediction
title: Human-Robot Coordination as a Game
understanding: 0
---

## Definition
A formulation of a robot acting around people as an incomplete-information game over continuous state (x = (x_R, x_H)) and actions, where each agent has a cost (J_R, J_H) depending on the joint state and both agents' actions. Because the recursion of beliefs ('what I think you think I think') is intractable for humans and robots alike, the game is decomposed into prediction—modeling people as noisily-rational agents whose action likelihood follows a softmax in negative Q-value, P(u_H | x, J_H) ∝ exp(−Q(x, u_H; J_H)), and using their ongoing actions to Bayes-update a belief over their objective—and action, where the robot solves the resulting MDP. This split (like separating estimation from control) sacrifices the robot's awareness that its own actions influence human behavior. When J_H = J_R the game becomes collaboration, handled by computing a joint plan and adapting via MPC to human deviations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]