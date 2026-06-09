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
- agentic-ai
- reinforcement-learning
id: pkis:framework:peas-task-environment
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch02
tags:
- agent
- task-environment
- peas
- agent-design
- specification
title: PEAS Task Environment Specification
understanding: 0
---

## Definition
A task environment is the "problem" to which a rational agent is the "solution." The PEAS framework specifies a task environment fully along four headings before any agent is designed: Performance measure (criterion of success over environment-state sequences), Environment (the external world the agent operates in), Actuators (the means by which the agent acts), and Sensors (the means by which the agent perceives). Specifying the task environment as fully as possible is the mandatory first step in agent design.

The canonical worked examples are the two-square vacuum world and the automated taxi driver (roads, traffic, pedestrians; accelerator/brake/steering; cameras, lidar, GPS, speedometer). Agents are typically evaluated not on a single environment but over an environment class — many environments drawn from a distribution (e.g., varied traffic, weather, lighting) — reporting average performance via an environment simulator.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]