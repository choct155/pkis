---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- interpretability
- statistics
id: pkis:technique:partial-dependence-plots
instantiates:
- partial-dependence
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch18
tags:
- interpretability
- visualization
- feature-effect
- ensemble
- marginal-effect
title: Partial Dependence Plots
understanding: 0
uses:
- feature-importance-tree-ensembles
- marginalization
---

## Definition
The partial dependence function for feature $k$ marginalises the model prediction over all other features using the empirical distribution:

$$\bar{f}_k(x_k) = \frac{1}{N} \sum_{n=1}^N f(x_{n,-k},\, x_k)$$

plotted against $x_k$. For binary classifiers it is common to convert to log-odds. Two-way partial dependence captures pairwise interactions:

$$\bar{f}_{jk}(x_j, x_k) = \frac{1}{N} \sum_{n=1}^N f(x_{n,-jk},\, x_j, x_k)$$

Partial dependence shows the average marginal effect of a feature (or pair of features) on the model output after averaging out all other inputs.

### Why it matters
Partial dependence plots are a model-agnostic post-hoc interpretation tool, commonly applied to opaque ensembles (random forests, gradient-boosted trees). They are easy to compute and visualise but assume feature independence; when features are correlated, the marginalization may evaluate the model at unrealistic feature combinations. ICE (individual conditional expectation) plots extend PDP to show heterogeneous effects.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[marginalization]] — uses
- [[feature-importance-tree-ensembles]] — uses: typically applied after identifying top features
- [[partial-dependence]] — instantiates
[To be populated during integration]