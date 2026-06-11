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
- machine-learning
- statistics
- information-theory
id: pkis:concept:parsimony-in-representation-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch01
tags:
- occams-razor
- regularisation
- mdl
- model-complexity
- generalisation
title: Parsimony in Representation Learning
understanding: 0
---

## Definition
The principle that a learned model should be the *simplest* (fewest parameters, lowest complexity) representation consistent with the data:
$$\hat{\theta} = \arg\min_{\theta} \left[-\log p(\mathcal{D}|\theta) + \Omega(\theta)\right],$$
where $\Omega(\theta)$ penalises complexity (e.g., MDL, Bayesian model evidence, $\ell_1/\ell_2$ regularisation).

Parsimony operationalises Occam's razor: prefer compact representations that still explain the data well, because they are more likely to capture genuine structure rather than noise.

### Why it matters
Parsimonious models generalise better, are more interpretable, and are more scientifically meaningful. In probabilistic ML, parsimony is naturally encoded via priors and Bayesian model comparison (marginal likelihood).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]