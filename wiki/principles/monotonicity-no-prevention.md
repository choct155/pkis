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
- bayesian-stats
id: pkis:principle:monotonicity-no-prevention
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch09
tags:
- identification
- counterfactuals
- epidemiology
- assumptions
title: Monotonicity (No-Prevention Assumption)
understanding: 0
---

## Definition
A causal-modelling assumption stating that the response function Y_x(u) is monotonic in x for every unit u -- equivalently, y'_x AND y_x' = false (Definition 9.2.13). Intuitively: changing X from false to true can never, for any individual, flip Y from true to false. In epidemiology this is the 'no prevention' assumption -- no individual can be helped by the exposure. Monotonicity is the key assumption that renders the (otherwise nonidentifiable) probabilities of causation identifiable: under exogeneity AND monotonicity, PNS = P(y|x) - P(y|x'), PN equals the excess risk ratio, and PS equals the relative difference (Theorem 9.2.14); under monotonicity with confounding but identifiable causal effects P(y_x), P(y_{x'}), PN, PS, PNS are still identified by eqs. 9.28-9.30 (Theorem 9.2.15). Crucially it is a global property of all X->Y pathways and is not testable in general, though it must rest on substantive knowledge; the combined-data inequalities P(y_x) >= P(y) >= P(y_{x'}) (eq. 9.32) provide a weak empirical test. Stochastic monotonicity is too weak to aid identification (Robins-Greenland). Pearl, Causality 2nd ed., Ch. 9.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]