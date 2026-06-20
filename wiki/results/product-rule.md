---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- bayesian-stats
- information-theory
id: pkis:result:product-rule
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- bayesian-inference
related_concepts: []
sources:
- jaynes-probability-ch02
- kroese-statistical-modeling-ch01
tags:
- foundations
- probability-as-logic
title: Product Rule (Plausibility)
understanding: 0
---

## Definition
The product rule expresses the plausibility of a conjunction in terms of conditional plausibilities: p(AB|C) = p(A|C) p(B|AC) = p(B|C) p(A|BC). In Jaynes's development it is not assumed but *derived*: requiring (AB|C) = F[(B|C),(A|BC)] and imposing structural consistency under the associativity of the logical product (ABC = (AB)C = A(BC)) produces the Associativity Equation F[F(x,y),z] = F[x,F(y,z)], whose general monotonic solution gives w(AB|C) = w(A|BC)w(B|C). After the monotonic regrading p(x) = w^m(x), this becomes the familiar product rule.

Two qualitative boundary conditions fix the scale: if A is certain given C then w(A|C) = 1 (certainty maps to 1); if A is impossible given C then w(A|C) = 0. The product rule, together with the sum rule, is an *adequate set* for plausible inference — because conjunction and negation suffice to build every Boolean function, repeated application of the product and sum rules determines the plausibility of any logic function of the propositions. The product rule specializes to Bayes' theorem on solving for p(A|BC), and is the source of the deductive syllogisms of Aristotelian logic in the limit p -> 0 or p -> 1.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-inference]] — prerequisite-of: Bayes' theorem is the product rule solved for a conditional
[To be populated during integration]