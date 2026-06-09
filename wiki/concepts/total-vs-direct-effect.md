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
- social-science-methods
id: pkis:concept:total-vs-direct-effect
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch05
tags:
- mediation
- do-operator
- counterfactuals
- policy-analysis
- path-coefficients
title: Total vs. Direct vs. Indirect Effects
understanding: 0
---

## Definition
Operational, intervention-based definitions of causal-effect components (Pearl Defs 5.4.2-5.4.3). TOTAL effect of X on Y = P(y|do(x)): X held at x, all other variables free to run their natural course. DIRECT effect = P(y|do(x), do(s_XY)): X set to x AND all other observed variables S_XY physically held fixed (not statistically 'controlled for'). Crucially, intermediate variables are held constant by physical intervention, not by adjustment — adjusting for mediators can give the wrong answer (e.g., in Pearl's Fig. 5.10 adjusting for Z,W fails to yield the correct zero direct effect, whereas (d/dx)E(Y|do(x,z,w)) does). In linear/recursive models total and direct effects reduce to the familiar products and power-series of path-coefficient matrices, but the algebraic power-series definition fails in models with feedback (e.g., the total effect of X on Y in {y=bx+e, x=gy+d} is simply b, not b(1-ag)^{-1}). The INDIRECT effect requires nested counterfactuals and cannot be expressed via population averages alone (= total minus direct only in linear systems). Distinguishing the components matters for choosing among policies that act on different mediators.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]