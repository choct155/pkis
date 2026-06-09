---
aliases: []
also_type: []
applies:
- transformation-group-priors
component_scores:
  formulation: null
  instances: null
  solution_landscape: null
  why_hard: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
- information-theory
id: pkis:problem:the-well-posed-problem-bertrand
instantiates:
- principle-of-indifference
knowledge_type: problem
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch12
tags:
- bertrand-paradox
- principle-of-indifference
- geometric-probability
- ill-posed
- invariance
- jaynes
title: Bertrand's Paradox (The Well-Posed Problem)
understanding: 0
---

## Definition
## Statement
Bertrand (1889): a 'random' chord is drawn across a circle; what is the probability it is longer than the side of the inscribed equilateral triangle? Three natural ways of making 'at random' precise give different answers:

- (A) uniform on the radial distance of the chord's midpoint: $p_A=1/2$;
- (B) uniform on the angle of intersection on the circumference: $p_B=1/3$;
- (C) uniform on the midpoint over the disk area: $p_C=1/4$.

For a century this was cited as proof that the principle of indifference is logically inconsistent and that probabilities can only come from frequencies in a random experiment.

## Why it is canonical
It is 'a simple crystallization of a deeper paradox' pervading applied probability: real problems (predict gas viscosity from density and energy; compute poker odds) routinely look *underdetermined*, with apparently essential things unspecified, yet physicists have repeatedly extracted correct, nontrivial predictions by 'pure thought'. Bertrand's puzzle is the clean test case for whether such reasoning is legitimate.

## Jaynes's resolution
If the problem is *assumed* to have a definite solution despite what is left unspecified, then the unspecified circumstances (size and location of the circle, observer orientation) automatically become invariance requirements. Demanding the prior be invariant under rotations, changes of scale, and translations of the circle eliminates B (fails scale invariance) and C (fails translational invariance), leaving uniquely

$$f(r,\theta)=\frac{1}{2\pi R r},\qquad p(x)\,dx=\frac{x\,dx}{\sqrt{1-x^2}},$$

i.e. solution A ($p=1/2$), confirming Borel's 1909 conjecture. A frequency correspondence then follows: any rain of straws *not* obeying this law must give different distributions on different circles, which a low-skill tosser cannot achieve. Jaynes and Tyler verified it experimentally (128 tosses onto a 5-inch circle, low chi-squared).

### Significance
The paradox dissolves once 'well-posed' is read as 'has a unique invariant solution': an apparently underdetermined problem is reclassified as either uniquely determined (invariances compatible) or overdetermined (incompatible), never genuinely ambiguous. This is the motivating exhibit for the transformation-group method and for relocating the principle of indifference from events to problems.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[transformation-group-priors]] — applies: Solved by rotational, scale, and translational invariance.
- [[principle-of-indifference]] — instantiates: Canonical case exposing the ambiguity, then resolution, of the principle.
[To be populated during integration]