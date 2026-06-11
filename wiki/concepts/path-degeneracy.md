---
aliases: []
also_type: []
applies:
- particle-filter
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
id: pkis:concept:path-degeneracy
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch13
tags:
- particle-filter
- smoothing
- coalescence
- degeneracy
title: Path Degeneracy in Particle Filtering
understanding: 0
---

## Definition
Path degeneracy is the phenomenon whereby, after many resampling steps, all surviving particles trace back to a single common ancestor at some earlier time, called the **coalescence time**. As $t$ grows, the genealogical tree of particles collapses, so the particle approximation of the joint smoothing distribution $\pi_t(z_{1:t})$ degrades even when the filtering marginal $\pi_t(z_t)$ is well-approximated.

### Why it matters
Path degeneracy limits the accuracy of fixed-lag and full smoothing estimates derived from a particle filter. It motivates extensions such as particle smoothing (backward simulation), the resample-move algorithm (MCMC rejuvenation), and backward-simulation smoothers. It is distinct from weight degeneracy: resampling cures weight degeneracy but causes path degeneracy.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[particle-filter]] — applies
[To be populated during integration]