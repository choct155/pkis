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
- causality
- statistics
id: pkis:concept:causal-vs-anticausal-prediction
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- distribution-shift
- causal-inference
- generative-vs-discriminative
- robustness
title: Causal vs. Anticausal Prediction
understanding: 0
uses:
- structural-causal-models
- generative-vs-discriminative-models
---

## Definition
A **causal (discriminative) prediction** problem has the data-generating structure $X \to Y$: changing $X$ causes a change in $Y$. An **anticausal (generative) prediction** problem has the structure $Y \to X$: the label $Y$ generates the observation $X$.

### Why it matters
The causal direction determines which component of the joint distribution is stable under distribution shift. In causal prediction, $p(y|x)$ is stable but $p(x)$ may shift (covariate shift). In anticausal prediction, $p(x|y)$ is stable but $p(y)$ may shift (label shift). Misidentifying the causal direction leads to applying the wrong adaptation technique. The distinction also determines whether a discriminative or generative model is more robust.

### Examples
- $X$=image, $Y$=manual annotation $\Rightarrow$ causal ($X \to Y$).
- $X$=medical image, $Y$=disease state $\Rightarrow$ anticausal ($Y \to X$).
- $X$=movie review text, $Y$=star rating $\Rightarrow$ anticausal ($Y \to X$).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[generative-vs-discriminative-models]] — uses
- [[structural-causal-models]] — uses
[To be populated during integration]