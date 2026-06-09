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
id: pkis:concept:task-environment-properties
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch02
tags:
- task-environment
- observability
- stochastic
- episodic
- agent-design
title: Task Environment Properties
understanding: 0
---

## Definition
A small set of dimensions along which task environments are categorized; the categorization largely determines the appropriate agent design and which implementation techniques apply.

- **Fully observable vs. partially observable** (vs. unobservable): whether the sensors give access to the complete (or all action-relevant) state; partial observability arises from noisy/limited sensors and forces the agent to maintain internal state.
- **Single-agent vs. multiagent** (competitive / cooperative): whether another entity is best modeled as maximizing a performance measure that depends on the agent's behavior; multiagent settings can make communication and randomized behavior rational.
- **Deterministic vs. nondeterministic**: whether the next state is fully determined by current state and action. "Stochastic" is reserved for models that quantify possibilities with probabilities; "nondeterministic" lists possibilities without quantifying them.
- **Episodic vs. sequential**: whether each decision is independent (atomic episodes) or current decisions affect future ones (requiring lookahead).
- **Static vs. dynamic** (vs. semidynamic): whether the environment can change while the agent deliberates; semidynamic if only the performance score changes with time (e.g., chess with a clock).
- **Discrete vs. continuous**: applies to states, time, percepts, and actions.
- **Known vs. unknown**: a property of the agent's/designer's knowledge of the environment's "laws of physics," *not* of the environment itself; orthogonal to observability.

The hardest case is partially observable, multiagent, nondeterministic, sequential, dynamic, continuous, and unknown.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]