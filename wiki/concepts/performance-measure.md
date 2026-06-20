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
date_updated: '2026-06-20'
domain:
- agentic-ai
- reinforcement-learning
id: pkis:concept:performance-measure
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch02
- gulli-agentic-design-patterns-ch11
- gulli-agentic-design-patterns-ch19
tags:
- agent
- objective
- consequentialism
- objective-misspecification
- king-midas-problem
title: Performance Measure
understanding: 0
---

## Definition
An objective function that evaluates any given sequence of environment states, capturing the designer's (or user's) notion of which state-sequences are desirable. It is the criterion against which an agent's rationality is judged. Crucially, the performance measure lives "in the mind of the designer" or user rather than inside the agent: some agent designs internalize it explicitly (as a utility function), while in others it remains entirely implicit.

A general design rule is to specify the performance measure according to what one actually wants achieved in the environment, not according to how one thinks the agent should behave — otherwise a rational agent will exploit the literal specification (e.g., a vacuum agent dumping and re-cleaning dirt to maximize "dirt cleaned"). Misspecification is the King Midas / Norbert Wiener problem of "putting the wrong purpose into the machine." Because designers cannot always write the measure correctly or anticipate individual users' preferences, agents may need to reflect uncertainty about the true performance measure and learn it over time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]