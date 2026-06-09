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
- optimization
- reinforcement-learning
id: pkis:framework:robotics-decision-making
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch26
tags:
- robotics
- mdp
- pomdp
- embodied-agent
title: Robotics as Continuous, Partially-Observable, Multi-Agent Decision Making
understanding: 0
---

## Definition
The overarching framing in which a robot is a physically embodied agent that maximizes expected utility by actuating effectors to assert physical forces in the world. The general robotics problem is simultaneously stochastic (handled as an MDP), partially observable (a POMDP), and multi-agent (a game), and is made harder by continuous, high-dimensional state and action spaces and by operating in the real world, which runs no faster than real time and offers no 'undo' for damage. Because solving the full problem end-to-end (raw sensor feeds in, motor currents out) is intractable, roboticists decouple it into a hierarchy: task planning, motion planning, and control, plus separate preference learning and people prediction. Each decoupling reduces complexity but sacrifices the ability of the pieces to inform one another, motivating ongoing reintegration.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]