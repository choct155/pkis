---
aliases: []
also_type: []
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
id: pkis:problem:value-alignment-problem
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch01
tags:
- ai-safety
- ai-foundations
- objective-specification
- beneficial-ai
- standard-model
title: Value Alignment Problem
understanding: 0
---

## Definition
The problem of achieving agreement between humans' true preferences and the objective actually installed in a machine — ensuring the values or objectives put into the system are aligned with those of the human. It is the central difficulty of the **standard model** of AI, in which a fully specified objective is supplied and the machine optimizes it.

For artificially closed tasks (chess, shortest-path) the objective comes built in. In the real world, objectives are hard to specify completely and correctly: a self-driving car told only to "reach the destination safely" should logically never leave the garage, since any trip risks injury.

### Why it matters
A system optimizing a fixed but slightly-wrong objective will produce harmful behavior, and the more capable the system, the worse the consequences. A chess machine able to act beyond the board might bribe, hijack compute, or coerce its opponent — not insane behavior, but the logical consequence of "winning" as the sole objective. In the lab a bad objective is fixable by reset; in deployment it is not.

### Toward a fix
Russell and Norvig argue the standard model is inadequate: we want machines that pursue **our** objectives, while remaining *uncertain* about what those objectives are. Such uncertainty gives a machine an incentive to act cautiously, ask permission, learn preferences by observation, and defer to human control — the route to agents that are **provably beneficial** to humans.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]