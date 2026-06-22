---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-22'
domain:
- bayesian-stats
- information-theory
id: pkis:principle:symmetry-as-positive-knowledge
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- physical-vs-epistemic-probability
related_concepts: []
sources:
- jaynes-probability-ch10
- lange-applied-probability-ch02
specializes:
- noninformative-prior
tags:
- jaynes
- principle-of-indifference
- priors
- group-theory
- invariance
title: Symmetry as Positive Knowledge for Prior Assignment
understanding: 0
uses:
- symmetry-groups
---

## Definition
Jaynes's correction and generalization of the principle of indifference: the compelling assignment of equal probabilities to heads and tails is *not* a mere 'equal distribution of ignorance' ('I see no reason to prefer either'), but rests on *positive knowledge of the symmetry* of the problem. The verbal formulation: if interchanging heads and tails maps problem P1 into a problem P2 in which one's state of knowledge is identical except for the interchange, then consistency demands assigning to heads-in-P1 the same probability as tails-in-P2; when the problem is symmetric under this operation, equal probabilities follow — *regardless of any observed frequencies*. This is formalized group-theoretically: a consistent rule for priors must assign equivalent priors to equivalent states of knowledge, so the prior must be *invariant under the symmetry group* of the problem and may be specified arbitrarily only on the group's fundamental domain Theta_0; when there are as many continuous symmetry operations as dimensions, the fundamental domain shrinks to a point and the prior is *uniquely determined by symmetry alone*. The power of symmetry arguments, as in the conservation laws of physics and group-theoretic results in atomic/nuclear structure, is that they are undeterred by arbitrary complication in the details. Symmetry also licenses deductive (not merely plausible) inference: given that a die is known to be physically symmetric, any nonuniformity in observed face frequencies is *proof* of a corresponding nonuniformity in the method of tossing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[physical-vs-epistemic-probability]] — prerequisite-of: The 1/2 assignment for an honest coin rests on positive symmetry knowledge, not on frequencies — the constructive complement to the no-physical-probability critique.
- [[noninformative-prior]] — specializes: Symmetry/transformation-group reasoning supplies a principled, often unique, noninformative prior where 'equal ignorance' alone is ambiguous.
- [[symmetry-groups]] — uses: Prior must be invariant under the problem's transformation group; specifiable only on the group's fundamental domain.
[To be populated during integration]