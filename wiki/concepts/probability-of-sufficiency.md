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
id: pkis:concept:probability-of-sufficiency
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch09
specializes:
- probability-of-causation
tags:
- counterfactuals
- attribution
- epidemiology
- policy-analysis
- susceptibility
title: Probability of Sufficiency (PS)
understanding: 0
uses:
- counterfactuals
---

## Definition
For binary X, Y in a structural causal model, the probability that setting x would produce y in a situation where x and y are in fact both absent: PS = P(Y_x = true | X = false, Y = false) = P(y_x | x', y') (Definition 9.2.2). PS measures the capacity of x to produce y -- the presence of an active causal process -- and is the relevant facet of causation in policy analysis (assessing the danger an exposure poses to the healthy), AI explanation, and psychology. Conditioning on x',y' selects worlds in which all other causes of y are suppressed. Under exogeneity and monotonicity PS is identifiable as the epidemiologists' 'relative difference' PS = [P(y|x) - P(y|x')]/[1 - P(y|x')] (Theorem 9.2.14, eq. 9.23), which coincides with Khoury et al.'s susceptibility and Cheng's 'causal power' P(q). PS is insensitive to the introduction of independent alternative causes of y (Lemma 9.2.8). Pearl, Causality 2nd ed., Ch. 9.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[counterfactuals]] — uses: PS = P(y_x | x', y') is a counterfactual probability
- [[probability-of-causation]] — specializes: PS is one of the three core probabilities of causation
[To be populated during integration]