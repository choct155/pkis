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
- nonparametric-statistics
- regression
id: pkis:technique:nadaraya-watson-model
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch06
tags:
- kernel-regression
- Nadaraya-Watson
- nonparametric
- local-averaging
- Parzen-window
title: Nadaraya–Watson Kernel Regression
understanding: 0
---

## Definition
$$y(\mathbf{x}) = \sum_{n=1}^N k(\mathbf{x},\mathbf{x}_n)\,t_n, \qquad k(\mathbf{x},\mathbf{x}_n) = \frac{g(\mathbf{x}-\mathbf{x}_n)}{\sum_{m=1}^N g(\mathbf{x}-\mathbf{x}_m)}, \qquad \sum_n k(\mathbf{x},\mathbf{x}_n)=1$$

where $g$ is a non-negative localised function (e.g., Gaussian). The estimator is derived from a Parzen density estimate of the joint distribution $p(x,t)$: the conditional mean $\mathbb{E}[t|x]$ evaluates to the normalised weighted average of training targets.

### Why it matters
Nadaraya–Watson (1964) is the foundational nonparametric regression estimate. It arises naturally from three distinct perspectives: (1) kernel density estimation of the joint distribution, (2) regularisation theory via Green's functions of isotropic differential operators, and (3) optimisation under input noise. Its normalised kernel satisfies an exact partition-of-unity property, preventing the degenerate extrapolation of unnormalised RBF networks.

### Connections
It is the nonparametric analogue of the equivalent-kernel predictor in Bayesian linear regression (Section 3.3.3) and is a special case of local constant kernel smoothing.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]