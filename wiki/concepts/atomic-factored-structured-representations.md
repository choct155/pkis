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
- knowledge-representation
id: pkis:concept:atomic-factored-structured-representations
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch02
tags:
- representation
- expressiveness
- state-representation
- factored
- structured
- localist-distributed
title: Atomic, Factored, and Structured Representations
understanding: 0
---

## Definition
An axis of increasing expressive power along which an agent's components can represent the world, with a tradeoff: more expressive representations are at least as concise (often far more concise) but make reasoning and learning more complex.

- **Atomic**: each world state is indivisible, a "black box" with no internal structure, distinguishable only as identical to or different from another. Underlies search, game-playing, hidden Markov models, and Markov decision processes.
- **Factored**: each state is a fixed set of variables/attributes with values; two states can share some attributes and differ in others. Underlies constraint satisfaction, propositional logic, planning, Bayesian networks, and much of machine learning.
- **Structured**: the world contains objects and explicit relationships among them. Underlies relational databases, first-order logic, first-order probability models, and natural language understanding. Real-world systems may need to operate at all points on the axis simultaneously.

A distinct second axis concerns the mapping of concepts to memory: a **localist** representation maps each concept one-to-one to a memory location, whereas a **distributed** representation spreads each concept over many locations (each location shared across concepts), making it more robust to noise and information loss because corrupted bits move to a nearby, similar-meaning point.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]