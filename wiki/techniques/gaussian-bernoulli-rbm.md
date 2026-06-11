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
- deep-learning
- generative-models
- energy-based-models
extends:
- restricted-boltzmann-machine
id: pkis:technique:gaussian-bernoulli-rbm
instantiates:
- exponential-family
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch20
tags:
- real-valued-data
- RBM
- Gaussian
- energy-based
title: Gaussian-Bernoulli RBM
understanding: 0
---

## Definition
An RBM variant with binary hidden units $\mathbf{h}$ and real-valued visible units $\mathbf{v}$, where the conditional distribution over visible units is Gaussian:
$$p(\mathbf{v}|\mathbf{h})=\mathcal{N}(\mathbf{v};\mathbf{W}\mathbf{h},\beta^{-1}).$$
The energy function (precision parametrisation, no bias) is:
$$E(\mathbf{v},\mathbf{h})=\tfrac{1}{2}\mathbf{v}^{\top}(\beta\odot\mathbf{v})-(\mathbf{v}\odot\beta)^{\top}\mathbf{W}\mathbf{h}-\mathbf{b}^{\top}\mathbf{h}.$$
Inference in both directions remains tractable via sigmoid activations, and training uses contrastive divergence or SML.

### Why it matters
Gaussian-Bernoulli RBMs are the canonical energy-based model for continuous (e.g., image, audio) data and a standard building block for DBNs and DBMs applied to real-valued inputs. Their limitation—only modelling conditional mean, not conditional covariance—motivates mcRBM, mPoT, and ssRBM extensions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exponential-family]] — instantiates: Gaussian conditionals are in the exponential family; generalisation to other exp-family distributions is immediate.
- [[restricted-boltzmann-machine]] — extends
[To be populated during integration]