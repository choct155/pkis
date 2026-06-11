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
- statistics
- machine-learning
id: pkis:technique:canonical-correlation-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch20
tags:
- multi-view-learning
- paired-data
- dimensionality-reduction
- factor-analysis
- correlation
title: Canonical Correlation Analysis (CCA)
understanding: 0
---

## Definition
$$\max_{w_x, w_y} \frac{w_x^T \Sigma_{xy} w_y}{\sqrt{w_x^T \Sigma_{xx} w_x \cdot w_y^T \Sigma_{yy} w_y}}$$

CCA finds successive pairs of linear projections $(w_x, w_y)$ of two paired views $(x, y)$ that maximise their mutual correlation; it is the MLE for a linear-Gaussian FA model with shared and private latent variables for each view.

### Why it matters
CCA is the canonical method for discovering shared structure between two multivariate data sources (e.g., images and text, neural signals and stimuli). Its probabilistic FA interpretation (Bayesian CCA) enables extensions to multiple views (generalised CCA), nonlinear mappings (deep CCA), and exponential-family likelihoods. PLS and supervised PCA are related but restrict the private noise differently.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]