---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
contrasts-with:
- probability-theory
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
id: pkis:result:cox-theorem
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- product-rule
- sum-rule
- probability-as-extended-logic
related_concepts: []
sources:
- jaynes-probability-ch02
- jaynes-probability-appA
tags:
- foundations
- probability-as-logic
- consistency
title: Cox's Theorem
understanding: 0
uses:
- probability-theory
---

## Definition
Cox's theorem establishes that any system for representing degrees of plausibility by real numbers that satisfies a small set of qualitative consistency desiderata is necessarily isomorphic to the standard rules of probability theory. Following Jaynes (Ch. 2), the desiderata are: (I) degrees of plausibility are represented by real numbers; (II) qualitative correspondence with common sense (monotonic, continuous dependence on the underlying plausibilities); and (III) consistency, which has three faces: (IIIa) structural consistency — if a conclusion can be reasoned out in more than one way, every admissible path must yield the same value; (IIIb) propriety — all relevant evidence is used; and (IIIc) equivalence — equivalent states of knowledge get equivalent plausibility assignments.

The constructive core is that structural consistency forces functional equations whose solutions are essentially unique. Requiring the plausibility of a conjunction to be a function of the appropriate conditional plausibilities, (AB|C) = F[(B|C),(A|BC)], and demanding that this be consistent under the associativity of the logical product ABC = (AB)C = A(BC), yields **the Associativity Equation** F[F(x,y),z] = F[x,F(y,z)]. Its general monotonic solution (Abel 1826; Aczel 1966; the differentiable proof is due to Cox 1961) is w[F(x,y)] = w(x)w(y) for some positive continuous monotonic function w. This is the **product rule** w(AB|C) = w(A|BC)w(B|C). A second consistency argument relating w(A|B) to w(not-A|B) via a self-reciprocal function S (where S[S(x)] = x) forces S(x) = (1 - x^m)^{1/m}, equivalently the **sum rule** w^m(A|B) + w^m(not-A|B) = 1. Rescaling p(x) = w^m(x) absorbs the free exponent m, giving the canonical product and sum rules. Thus the rules of probability are not arbitrary axioms but the *unique* consistent calculus of plausible inference.

The scope is finite sets of propositions: Jaynes stresses that the consistency theorems are established only on finite sets, and that extension to infinite sets is legitimate only as a well-defined limit of finite-set results (the 'finite-sets policy'). Cox's theorem is the foundational justification for the Bayesian / probability-as-extended-logic program, paralleling and re-deriving the Kolmogorov axioms from consistency requirements rather than positing them.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[probability-theory]] — uses: Cox's theorems characterize exactly the standard probability rules.
- [[probability-as-extended-logic]] — prerequisite-of: Cox's consistency theorems supply the derivation that turns the extended-logic desiderata into the standard probability rules.
- [[probability-theory]] — contrasts-with: derives the Kolmogorov axioms from consistency rather than positing measure-theoretic axioms
- [[sum-rule]] — prerequisite-of: Cox's theorem is the derivation that yields the sum rule
- [[product-rule]] — prerequisite-of: Cox's theorem is the derivation that yields the product rule
[To be populated during integration]