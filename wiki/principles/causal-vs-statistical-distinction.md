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
date_updated: '2026-06-09'
domain:
- causal-analysis
id: pkis:principle:causal-vs-statistical-distinction
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch01
tags:
- causality
- statistical-parameter
- causal-parameter
- identifiability
- causal-assumptions
- estimand
title: Causal vs. Statistical Distinction
understanding: 0
---

## Definition
A demarcation between two non-mixing classes of quantities, concepts, and assumptions: those definable from a joint distribution of observed variables alone, and those requiring a causal model.

One-line intuition: behind every causal claim lies a causal assumption that is not testable from the data distribution — and the two kinds of claim must never be conflated.

### The definitions
- A **statistical parameter** is any quantity defined in terms of the joint distribution of *observed* variables, with no assumption about unobserved variables (e.g. $E(Y \mid x)$, the regression coefficient $r_{YX}$).
- A **causal parameter** is any quantity defined in terms of a causal model $\{x_i=f_i(pa_i,u_i)\}$ that is *not* a statistical parameter (e.g. $E(Y \mid \mathrm{do}(X=0))$, a path coefficient $a_{ik}$, whether $X_9$ influences $X_3$).
- A **causal assumption** is any constraint on a causal model not realizable by a statistical assumption (e.g. $U_i \perp U_j$, $f_i$ linear, $x_3$ absent from $f_4$).

The exclusion of latent variables from "statistical" is deliberate: it stops one from smuggling causal content in under the guise of unmeasured variables.

### Consequences
Causal parameters cannot be discerned from statistical parameters unless causal assumptions are invoked. Concepts like randomization, confounding, exogeneity, spurious correlation, instrumental variables, and effect are *causal*; correlation, regression, conditional independence, likelihood, propensity score, and even Granger causality are *statistical*. Standard probability calculus (expectation, conditioning, marginalization) cannot even express "symptoms do not cause diseases."

### Why it matters
This principle motivates the whole project of causal analysis: it forces investigators to make their untestable causal assumptions explicit and to extend probability notation (e.g. with $\mathrm{do}(\cdot)$) so that causal claims can be stated and manipulated at all.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]