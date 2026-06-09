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
id: pkis:concept:probability-of-necessity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch09
tags:
- counterfactuals
- attribution
- but-for
- epidemiology
- legal-reasoning
title: Probability of Necessity (PN)
understanding: 0
---

## Definition
For binary X, Y in a structural causal model, the probability that the effect y would not have occurred in the absence of the cause x, given that both x and y did in fact occur: PN = P(Y_x = false | X = true, Y = true) = P(y'_{x'} | x, y) (Definition 9.2.1). PN formalises the counterfactual 'but-for' notion of causation predominant in tort law (the plaintiff must prove y would not have occurred but for x) and the epidemiological 'probability of causation' of Robins and Greenland. It is a singular-causation measure: it conditions on the specific observed case and emphasises the absence of alternative processes that could have produced y. PN is in general nonidentifiable, blocked by confounding and by sensitivity to the generative mechanism; the familiar excess-risk-ratio estimate PN = [P(y|x) - P(y|x')]/P(y|x) is valid only under exogeneity AND monotonicity (Theorem 9.2.14, eq. 9.22). Under monotonicity with identified causal effects but possible confounding, PN = [P(y) - P(y_{x'})]/P(x,y) (Theorem 9.2.15, eq. 9.29), which corrects the excess-risk-ratio by an additive confounding term. Pearl, Causality 2nd ed., Ch. 9.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]