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
- statistics
- machine-learning
id: pkis:concept:density-ratio-estimation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- f-divergence
related_concepts: []
sources:
- murphy-pml2-advanced-ch26
tags:
- binary-classification
- importance-weighting
- GAN
- likelihood-ratio
title: Density Ratio Estimation
understanding: 0
uses:
- logistic-regression
- scoring-rules
---

## Definition
Density ratio estimation recovers the ratio $r(x)=p^*(x)/q_\theta(x)$ from samples of two distributions without evaluating either density. The key identity relating the ratio to a binary classifier $D(x)\in[0,1]$ is:
$$\frac{p^*(x)}{q_\theta(x)}=\frac{D(x)}{1-D(x)}$$
with optimal classifier $D^*(x)=p^*(x)/(p^*(x)+q_\theta(x))$. Training $D$ by minimising a proper scoring rule (e.g., binary cross-entropy) on the mixed dataset yields an estimator of this ratio from samples alone.

### Why it matters
Density ratio estimation converts an intractable density evaluation problem into a tractable classification problem, bridging implicit generative models, f-divergence estimation, importance weighting, and covariate shift correction. It is the conceptual foundation underlying the GAN discriminator.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[f-divergence]] — prerequisite-of
- [[scoring-rules]] — uses
- [[logistic-regression]] — uses: Binary classifier with Bernoulli loss provides the density ratio estimate.
[To be populated during integration]