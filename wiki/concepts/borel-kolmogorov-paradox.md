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
id: pkis:concept:borel-kolmogorov-paradox
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch15
tags:
- jaynes
- measure-zero
- conditional-density
- limit
- paradox
- great-circle
title: Borel-Kolmogorov Paradox
understanding: 0
uses:
- conditional-independence
---

## Definition
The paradox that the conditional density on a set of measure zero (a single point, line, or curve in a continuous sample space) is *not determined by the conditioning event alone* — it depends on which limiting sequence of positive-measure sets is used to approach that event. The canonical instance: for a bivariate normal pdf p(x,y), the conditional density of x given 'y=0' differs depending on whether 'y=0' is realized as the limit of horizontal strips |y|<eps (giving p(x) proportional to g(x)) or of wedges |y|<eps|x| (giving |x|g(x)); in general an arbitrary nonnegative factor f(x) can appear. Equivalently, changing variables to u = y/f(x) and then naively setting u=0 and renormalizing yields a density differing from the y=0 result by the factor f(x), even though u=0 is the *same event* as y=0.

## Resolution and the great-circle puzzle
Jaynes's resolution is an instance of the finite-sets policy: 'y=0' has measure zero and is meaningless as a bare condition; it acquires meaning only as the limit of a specified sequence of positive-measure propositions (e.g. A_eps: |y|<eps), and different sequences with the same set-theoretic limit yield different conditional-density limits, all legitimately. The famous geometric version: given a uniform density on a sphere's surface, the conditional density on a great circle is *uniform* if the circle is approached as the equator (|theta|<eps) but proportional to cos(theta) if approached as a meridian (|phi|<eps). The term 'great circle' is therefore ambiguous until the limiting operation is specified; the intuitive symmetry argument silently presupposes the equatorial limit. The only safe procedure is to pass to an explicitly defined limit; the answer will and must depend on which limit was chosen.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conditional-independence]] — uses: The paradox concerns conditional densities on measure-zero events; conditioning is the operation that becomes ambiguous.
[To be populated during integration]