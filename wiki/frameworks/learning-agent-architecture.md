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
id: pkis:framework:learning-agent-architecture
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch02
tags:
- agent
- learning-agent
- critic
- problem-generator
- performance-element
- exploration
title: Learning Agent Architecture
understanding: 0
---

## Definition
A decomposition (Turing 1950; classic in ML) of any agent into four conceptual components that let it operate in initially unknown environments and exceed its built-in knowledge. Any agent type (reflex, model-based, goal-based, utility-based) can be built as a learning agent.

- **Performance element**: what was previously considered the whole agent — takes percepts and selects external actions.
- **Learning element**: makes improvements to the performance element using feedback from the critic; its design depends on the performance element's design.
- **Critic**: judges how well the agent is doing against a fixed external performance standard. The standard must be fixed and conceptually outside the agent (so the agent cannot modify it to fit its behavior); it distinguishes part of the percept as reward/penalty (cf. pain and hunger as hard-wired standards).
- **Problem generator**: suggests exploratory, possibly suboptimal actions to gain new and informative experiences (analogous to a scientist running experiments), trading short-run performance for long-run discovery.

Learning is the modification of each agent component to bring it into closer agreement with available feedback, improving overall performance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]