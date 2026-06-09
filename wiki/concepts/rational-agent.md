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
- agentic-ai
- reinforcement-learning
generalizes:
- agent-environment-interface
id: pkis:concept:rational-agent
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch02
tags:
- agent
- rationality
- consequentialism
- expected-performance
- autonomy
title: Rational Agent
understanding: 0
uses:
- performance-measure
---

## Definition
An agent that does the right thing, where "right" is defined consequentially: for each possible percept sequence, a rational agent selects the action that is expected to maximize its performance measure, given the evidence provided by the percept sequence to date and whatever built-in knowledge the agent has. Rationality at any moment depends on four things — (i) the performance measure that defines success, (ii) the agent's prior knowledge of the environment, (iii) the actions available to the agent, and (iv) the percept sequence to date.

An agent perceives its environment through sensors and acts through actuators; its behavior is described mathematically by the agent function mapping any percept sequence to an action. Rationality is carefully distinguished from omniscience: it maximizes *expected* performance given available information, not actual outcomes (perfection), since the rational choice depends only on the percept sequence so far. A rational agent should also gather information (e.g., looking before crossing) and learn from percepts to compensate for partial or incorrect prior knowledge, which yields autonomy — the degree to which behavior depends on the agent's own experience rather than the designer's built-in knowledge.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[agent-environment-interface]] — generalizes: AIMA's general rational agent (any performance measure, any environment) generalizes the reinforcement-learning agent–environment interface (scalar reward, state/action loop).
- [[performance-measure]] — uses: A rational agent acts to maximize the expected value of the performance measure.
[To be populated during integration]