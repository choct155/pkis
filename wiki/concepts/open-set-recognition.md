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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
id: pkis:concept:open-set-recognition
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch16
tags:
- OOD
- novelty-detection
- open-world
- continual-learning
- few-shot
title: Open-Set Recognition and Novelty Detection
understanding: 0
---

## Definition
A recognition setting in which, at test time, inputs may belong to classes *not* present during training ($y \notin C_{\text{train}}$). The system must simultaneously classify known inputs and detect novel ones, rather than forcing every input into a closed set of $C$ categories.

### Why it matters
Closed-set classifiers assign high confidence to any input, including out-of-distribution ones, making them unsafe in deployed systems (face recognition, autonomous driving, medical diagnosis). Open-set recognition requires a distance or confidence threshold to declare novelty, naturally motivating metric-learning approaches where distance to the nearest gallery exemplar signals familiarity. It also subsumes OOD detection, few-shot class incremental learning, and entity disambiguation.

### Related concepts
- **Novelty detection**: identifying inputs from unseen classes.
- **OOD detection**: identifying inputs from entirely different distributions.
- **Incremental / continual learning**: expanding $C_t$ over time as new classes are encountered.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]