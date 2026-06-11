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
- deep-learning
id: pkis:technique:temperature-scaling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch14
tags:
- calibration
- post-hoc
- deep-learning
- Platt-scaling
- softmax
title: Temperature Scaling
understanding: 0
---

## Definition
$$q = \mathrm{softmax}(z / T), \qquad T > 0$$

Temperature scaling recalibrates a multi-class classifier by dividing the pre-softmax logit vector $z$ by a single scalar temperature $T$, estimated via maximum likelihood on a held-out validation set. $T > 1$ softens (flattens) the distribution; $T < 1$ sharpens it.

### Why it matters
Temperature scaling is the simplest and empirically best-performing post-hoc calibration method for DNNs (Guo et al., 2017). It requires fitting only one parameter, does not change the argmax, and therefore cannot hurt accuracy while consistently reducing ECE.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]