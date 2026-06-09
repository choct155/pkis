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
id: pkis:concept:probability-of-necessity-and-sufficiency
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch09
tags:
- counterfactuals
- attribution
- identification
- bounds
title: Probability of Necessity and Sufficiency (PNS)
understanding: 0
---

## Definition
The probability that the effect y would respond to the cause x in both directions -- occurring when x is set true and not occurring when x is set false: PNS = P(y_x, y'_{x'}) (Definition 9.2.3). PNS measures both the sufficiency and the necessity of x for y, and is unconditional (not conditioned on the observed case), so it characterises a randomly chosen individual. It ties the three probabilities of causation together: in general PNS = P(x,y)*PN + P(x',y')*PS (Lemma 9.2.6), and under exogeneity PN = PNS/P(y|x) and PS = PNS/P(y'|x') (Theorem 9.2.11). Under exogeneity PNS is bounded by max[0, P(y|x)-P(y|x')] <= PNS <= min[P(y|x), P(y'|x')], with both bounds sharp (Theorem 9.2.10); these bounds propagate to PN and PS, fixing the limits of identifiability from data. Under monotonicity (and identified causal effects), PNS collapses to the risk difference P(y_x) - P(y_{x'}) (Theorems 9.2.14-9.2.15). Pearl, Causality 2nd ed., Ch. 9.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]