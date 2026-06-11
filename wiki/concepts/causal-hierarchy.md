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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- statistics
id: pkis:concept:causal-hierarchy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- ladder-of-causation
- interventional
- counterfactual
- observational
- pearl
title: Causal Hierarchy (Ladder of Causation)
understanding: 0
---

## Definition
The causal hierarchy, popularized by Pearl, stratifies causal queries into three levels of increasing expressiveness:

$$\text{Level 1: Observational} \quad P(Y \mid X = x)$$
$$\text{Level 2: Interventional} \quad P(Y \mid \mathrm{do}(X = x))$$
$$\text{Level 3: Counterfactual} \quad P(Y_x \mid Y_{x'} = y', X = x')$$

Level 1 (association) concerns statistical patterns in observed data. Level 2 (intervention) asks what would happen if we actively set a variable. Level 3 (counterfactual) asks what *would have* happened to a specific unit under an alternative scenario, requiring the joint distribution of potential outcomes within individuals.

### Why it matters
The hierarchy determines the *minimal assumptions* needed to answer a query: Level 1 requires only a joint distribution; Level 2 requires a causal DAG (plus overlap); Level 3 requires functional-form assumptions on the SCM because it depends on cross-world joint distributions of potential outcomes that are never simultaneously observed. Recognising which level a query inhabits prevents over- or under-assuming.

### Distinguishing Levels 2 and 3
The ATE $\mathbb{E}[Y(1)-Y(0)]$ lives at Level 2—it requires only marginal distributions of potential outcomes. A query such as $\mathbb{E}[Y(0) \mid Y(1)=1, A=1]$ (the effect among those who responded) lives at Level 3 because it conditions on the realisation of one potential outcome and requires their joint distribution.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]