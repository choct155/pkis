---
aliases: []
also_type: []
applies:
- distribution-shift
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
- deep-learning
- uncertainty-quantification
- gaussian-processes
id: pkis:technique:sngp
instantiates:
- bayesian-deep-learning
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
tags:
- spectral-normalisation
- OOD-detection
- Lipschitz
- distance-preserving
- GP-layer
title: SNGP (Spectrally Normalized Gaussian Process)
understanding: 0
uses:
- gaussian-process
- regularization
---

## Definition
SNGP combines a spectrally-normalised DNN feature extractor with a GP output layer. Spectral normalisation constrains each layer's weight matrix so that $\|W\|_2 \leq 1$, bounding the Lipschitz constant of the feature map $\phi$:
$$\|\phi(x_1)-\phi(x_2)\| \leq L\|x_1-x_2\|$$
The GP final layer then provides calibrated predictive uncertainty.

### Why it matters
Standard DNN feature extractors can *collapse* distances between inputs—points far apart in input space may be projected close together, causing OOD inputs to appear near training data to the final layer. SNGP preserves inter-point distances through the network, ensuring that OOD inputs remain identifiably distant, producing well-calibrated uncertainty and near-zero confidence far from training support. It provides GP-like OOD behaviour at DNN scale without full GP inference overhead.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[regularization]] — uses: Spectral normalisation bounds Lipschitz constant of feature extractor
- [[distribution-shift]] — applies
- [[bayesian-deep-learning]] — instantiates
- [[gaussian-process]] — uses
[To be populated during integration]