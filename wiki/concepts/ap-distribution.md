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
- bayesian-stats
id: pkis:concept:ap-distribution
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch18
tags:
- jaynes
- foundations
- prior
- de-finetti
- epistemic-state
- robot
title: Ap-Distribution
understanding: 0
---

## Definition
Jaynes's device for representing the *stability* of a probability assignment, not just its value. One introduces a special (non-Aristotelian) proposition $A_p$ defined by $P(A\mid A_p E)\equiv p$ for any further evidence $E$ — verbally, 'regardless of anything else you may have been told, the probability of $A$ is $p$.' Because the family $\{A_p:0\le p\le 1\}$ is mutually exclusive and exhaustive, Bayes' theorem can move $A_p$ to the left of the conditioning bar, yielding a density $(A_p\mid E)$ over $p$. The ordinary probability is its first moment, $P(A\mid E)=\int_0^1 p\,(A_p\mid E)\,dp$, so the density carries *more* information than the single number $P(A\mid E)$: its width measures how stable the assignment is under new evidence.

### Why 'probability of a probability' misses the point
Jaynes resolves the apparent paradox with a two-level reading: an 'outer robot' reasons about the external world with Aristotelian propositions, while an 'inner robot' reasons about the activity of the outer robot. $(A_p\mid E)$ is the inner robot's state; the two probabilities live at different levels, so no circular 'probability of a probability' is involved. This explains the penny-vs-Mars puzzle (same $P(A)=1/2$, very different stability = very different $(A_p\mid E)$) and the Mr A / Mr B coin example (identical $P=1/2$ from positive knowledge vs ignorance, distinguished only by the width of $(A_p\mid E)$).

### What it buys you
(1) **Memory economy**: everything the robot needs about $A$ for future updating is summarized in the single function $(A_p\mid E)$ — it can forget the millions of isolated facts that produced it (Eq. 18.16). (2) **Weight of evidence**: combining two bodies of evidence multiplies their densities, $(A_p\mid EF)\propto (A_p\mid E)(A_p\mid F)$; a much sharper factor dominates, formalizing why one strong datum can swamp much vague evidence. (3) **Pre-prior / ignorance**: the uniform $(A_p\mid X)=1$ encodes 'A is possible either way', while the Haldane measure $dp/[p(1-p)]$ is the 'pre-prior' for complete ignorance about whether A is even possible. (4) It is the generating device behind Laplace's rule of succession and the binomial/multinomial connection between probability and frequency.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]