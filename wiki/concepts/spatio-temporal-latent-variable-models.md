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
- spatial-statistics
id: pkis:concept:spatio-temporal-latent-variable-models
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch27
tags:
- spatiotemporal
- latent-variables
- sequences
- state-space-models
- discovery
title: Spatio-Temporal Latent Variable Models
understanding: 0
---

## Definition
An extension of sequential latent variable models to data indexed over both space and time, $x_{s,t}$ where $s$ indexes spatial location and $t$ indexes time. The generative model posits latent factors $z_{s,t}$ that evolve according to spatial and temporal dynamics:

$$p(x_{1:S,1:T}) = \int \prod_{s,t} p(x_{s,t}|z_{s,t})\, p(z_{s,t}|z_{s',t'},\, (s',t') \in \mathcal{N}(s,t))\, dz$$

### Why it matters
Many real-world discovery tasks involve data with joint spatial and temporal structure: climate science, neuroimaging (fMRI), epidemiology, traffic, and environmental monitoring. Spatio-temporal LVMs allow latent causes to be localised in both space and time, enabling richer and more interpretable decompositions than purely temporal or purely spatial models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]