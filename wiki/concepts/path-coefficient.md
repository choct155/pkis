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
- econometrics
id: pkis:concept:path-coefficient
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch05
specializes:
- total-vs-direct-effect
tags:
- sem
- direct-effect
- structural-parameter
- do-operator
title: Path Coefficient
understanding: 0
---

## Definition
The coefficient alpha associated with a directed edge X->Y in a structural equation / path diagram, representing the DIRECT causal effect of X on Y. Operationally (Pearl, eq. 5.24) beta = (partial / partial x) E[Y | do(x)] — the rate of change of E(Y) under external control of X, invariant to whether X and the error are correlated in observational data, and emphatically NOT in general equal to the regression coefficient r_YX or to E(Y|x). A path coefficient is identified-as-a-regression-coefficient exactly when the single-door criterion holds. It is invariant to local interventions (changes in the value x), not merely to changes in the variance of X — distinguishing Pearl's definition from Cartwright's 'capacity' (the ratio E(YX)/E(X^2)). The regression coefficient decomposes as r_YX = alpha + I_YX, where I_YX collects contributions from all other (back-door and bidirected) paths.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[total-vs-direct-effect]] — specializes: A path coefficient is the direct effect on a single edge.
[To be populated during integration]