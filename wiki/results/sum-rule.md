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
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
id: pkis:result:sum-rule
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch02
tags:
- foundations
- probability-as-logic
title: Sum Rule (Plausibility)
understanding: 0
uses:
- product-rule
---

## Definition
The sum rule relates the plausibility of a proposition to that of its negation: p(A|B) + p(not-A|B) = 1. In Jaynes's derivation it follows from requiring that the function S relating w(A|B) to w(not-A|B) be self-reciprocal (S[S(x)] = x) and consistent with the product rule; the resulting functional equation forces S(x) = (1 - x^m)^{1/m}, i.e. w^m(A|B) + w^m(not-A|B) = 1, which the regrading p = w^m reduces to the primitive sum rule.

Its most useful applied form is the **extended (generalized) sum rule** for the logical sum: p(A + B|C) = p(A|C) + p(B|C) - p(AB|C), obtained by repeated application of the product and primitive sum rules. The primitive sum rule is the special case B = not-A. For n mutually exclusive propositions the cross terms vanish, giving p(A_1 + ... + A_m|B) = sum_i p(A_i|B); if the propositions are also exhaustive, the total is 1. Jaynes emphasizes that conventional expositions *postulate* this additivity as the basic axiom, whereas here it is *derived* from qualitative consistency — the very viewpoint he wishes to avoid taking as primitive.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[product-rule]] — uses: the extended sum rule is derived using the product rule
[To be populated during integration]