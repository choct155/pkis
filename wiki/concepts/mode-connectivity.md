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
- deep-learning
- optimisation
id: pkis:concept:mode-connectivity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- deep-ensembles
- swa-swag
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- loss-landscape
- flat-minima
- ensembles
- BMA
- loss-surface
title: Mode Connectivity
understanding: 0
uses:
- effective-dimensionality-bnn
---

## Definition
Two independently trained SGD solutions $\hat{\theta}_1$ and $\hat{\theta}_2$ in parameter space are *mode connected* if there exists a smooth curve $\gamma:[0,1]\to\mathbb{R}^P$ with $\gamma(0)=\hat{\theta}_1$, $\gamma(1)=\hat{\theta}_2$ along which the training loss remains near-zero throughout.

### Why it matters
Mode connectivity (Garipov et al. 2018) reveals that the DNN loss landscape is far less fragmented than a naive picture of isolated sharp minima would suggest: entire low-loss *surfaces* (simplexes) connect different solutions. This has several implications: (1) ensemble members trained separately represent genuinely diverse functions despite being on the same loss surface; (2) Bayesian model averaging over these curves further improves performance over any single point; (3) methods like SWA that average along such curves find flat, well-generalising solutions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[effective-dimensionality-bnn]] — uses
- [[swa-swag]] — prerequisite-of
- [[deep-ensembles]] — prerequisite-of
[To be populated during integration]