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
- causal-analysis
- statistical-learning
id: pkis:concept:intransitive-triplet
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch02
tags:
- v-structure
- collider
- virtual-control
- orientation
- no-causation-without-manipulation
title: Intransitive Triplet (Virtual Control)
understanding: 0
---

## Definition
The minimal statistical signature -- requiring three variables -- that lets nonexperimental data establish causal *direction* and nonspuriousness. The pattern: a and b are each dependent on a third variable c, yet a and b are (conditionally) independent of each other, e.g. (a indep b | empty), (a dep c), (b dep c). In a stable distribution a common cause would induce dependence among its effects, so c cannot be a cause of both a and b; it must be their common *effect* (collider a->c<-b) or be linked to them through hidden common causes (a<->c<->b). This is exactly the trigger for the collider-orientation step of the IC/IC* algorithms. Pearl interprets the third variable as a *virtual control*: it plays the role an experimenter's manipulation would play, but is supplied by Nature within the data rather than by intervention -- a data-side echo of 'no causation without manipulation' (Holland 1986). The intuition: we insist rain causes wet grass and not vice versa because we can find another means (a sprinkler) of wetting the grass independently of rain; transferred to a chain a-c-b, finding another lever b on c that does not affect a precludes c from causing a. Intransitive triplets underpin every causal definition in the chapter -- potential cause, genuine cause (one triplet), and spurious association (two triplets (Z1,X,Y) and (X,Y,Z2)).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]