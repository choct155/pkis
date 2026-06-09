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
id: pkis:framework:agent-program-architectures
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch02
tags:
- agent
- agent-program
- reflex-agent
- goal-based
- utility-based
- agent-architecture
title: Agent Program Architectures
understanding: 0
---

## Definition
agent = architecture + program. The agent function (the abstract percept-sequence-to-action mapping) is realized by a concrete agent program running on an architecture (sensors, actuators, compute). A table-driven agent that looks up the action for every percept sequence is provably infeasible (the lookup table is astronomically large — over 10^600,000,000,000 entries for an hour of taxi camera input), so the central challenge of AI is to produce rational behavior from a small program rather than a vast table.

Four basic skeleton designs of increasing capability:
- **Simple reflex agents**: select actions from the current percept alone via condition–action rules (e.g., "if car-in-front-is-braking then initiate-braking"). Work only in fully observable environments; can fall into infinite loops under partial observability, partly escapable by randomization.
- **Model-based reflex agents**: maintain internal state tracking the unobserved world, updated via a transition model (how the world evolves and how actions change it) and a sensor model (how state maps to percepts) — the standard way to handle partial observability.
- **Goal-based agents**: combine the model with explicit goal information describing desirable states, choosing actions (via search and planning) that consider the future; more flexible because goals are represented explicitly.
- **Utility-based agents**: replace binary goals with an internalized utility function approximating the performance measure, choosing actions that maximize expected utility — handling conflicting goals and uncertain outcomes. This turns the global definition of rationality into a local, program-expressible constraint.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]