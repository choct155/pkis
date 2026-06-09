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
- bayesian-stats
id: pkis:concept:partial-identification-bounds
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch08
tags:
- partial-identification
- bounds
- nonidentifiability
- natural-bounds
- sharp-bounds
- linear-programming
- manski-bounds
title: Partial Identification and Bounds
understanding: 0
---

## Definition
When a causal quantity such as ACE(X->Y) = P(y1|do(x1)) - P(y1|do(x0)) cannot be point-identified from the data (e.g., because of unmeasured confounding under imperfect compliance), one can still derive a range of admissible values -- a *bound* -- that exhausts our ignorance about the data-generating process and that does NOT shrink with sample size (it is a structural, not statistical, gap). The bound is found by treating identification as a constrained optimization: minimize and maximize the target functional over all latent-variable models P(u), P(y|x,u), P(x|z,u) consistent with the observed distribution P(y,x|z). After replacing the unbounded latent U by a canonical partition, the target and constraints become linear in the response-type probabilities q_jk, so the extremal values are obtained by *linear programming*, yielding closed-form symbolic bounds (Balke 1995).

Two grades of bound appear for the instrumental-variable / noncompliance model of Figure 8.1:

- **Natural bounds** (Robins 1989; Manski 1990; Pearl 1994a): the two leading LP terms, giving ACE >= [P(y1|z1)-P(y1|z0)] - P(y1,x0|z1) - P(y0,x1|z0) and ACE <= [P(y1|z1)-P(y1|z0)] + P(y0,x0|z1) + P(y1,x1|z0). Their width equals the noncompliance rate P(x1|z0)+P(x0|z1), and they are *optimal* when no subject is contrarian (a defier).
- **Sharp (tight) bounds** of (8.14a,b): the full LP solution, eight max/min terms each, which can be substantially narrower and may even *collapse to a point* (consistent identification) under 50% noncompliance -- e.g. when compliance rates match across arms and Y,Z are perfectly correlated in one treatment arm.

Bounds are decision-relevant: in the Lipid trial, despite 39% noncompliance the data guarantee ACE >= 0.392; in the PeptAid case the bound -0.23 <= ACE <= -0.15 proves the drug is beneficial to the population even though individual-level attribution runs the other way.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]