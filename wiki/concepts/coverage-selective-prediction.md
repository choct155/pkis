---
aliases: []
also_type: []
applies:
- human-in-the-loop
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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- decision-theory
- evaluation
extends:
- precision-recall-f-score
id: pkis:concept:coverage-selective-prediction
instantiates:
- decision-theory-foundations
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch11
tags:
- selective-prediction
- abstention
- confidence-threshold
- human-in-the-loop
title: Coverage (selective prediction)
understanding: 0
---

## Definition
**Coverage** is the fraction of input examples for which a machine learning system produces a prediction rather than abstaining:

$$\text{coverage} = \frac{|\{\mathbf{x} : p(\mathbf{y}|\mathbf{x}) \geq t\}|}{N}.$$

By raising or lowering the confidence threshold $t$, one can trade coverage for accuracy — accepting fewer inputs but with higher correctness on accepted inputs.

### Why it matters
In high-stakes deployment (medical diagnosis, map transcription), it is preferable to defer uncertain cases to human operators rather than commit to an erroneous prediction. Coverage formalises the fraction of work the system handles autonomously, and is the primary performance axis when accuracy is held fixed at a target level (e.g., 98% accuracy at 95% coverage in the Street View digit-transcription system).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[decision-theory-foundations]] — instantiates: Abstention is a decision action with defined cost
- [[human-in-the-loop]] — applies: Abstaining examples are routed to human operators
- [[precision-recall-f-score]] — extends: Coverage adds the option to abstain, creating a three-way tradeoff among accuracy, precision/recall, and coverage
[To be populated during integration]