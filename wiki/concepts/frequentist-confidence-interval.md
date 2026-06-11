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
- frequentist-statistics
id: pkis:concept:frequentist-confidence-interval
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
tags:
- confidence-interval
- frequentist
- coverage
- sampling-distribution
- uncertainty
title: Frequentist Confidence Interval
understanding: 0
---

## Definition
A $100(1-\alpha)\%$ **confidence interval** (CI) is any interval $I(\tilde{D})=(\ell(\tilde{D}), u(\tilde{D}))$ satisfying:
$$\Pr\bigl(\theta\in I(\tilde{D})\mid\tilde{D}\sim\theta\bigr)=1-\alpha$$
The probability is over hypothetical repeated datasets $\tilde{D}$; the parameter $\theta$ is treated as a fixed (unknown) constant.

Crucially, once a specific dataset $D$ is observed, the realised interval either contains $\theta$ or it does not — there is no probability statement about this single interval. This contrasts with a Bayesian credible interval, for which $\Pr(\theta\in C_\alpha|D)=1-\alpha$ is a direct posterior probability.

### Why it matters
The CI is widely misinterpreted as a posterior probability statement. Its frequentist meaning is a long-run coverage guarantee across repeated experiments, which can yield paradoxes: an interval that clearly contains or excludes $\theta$ based on the observed data still retains its nominal coverage probability.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]