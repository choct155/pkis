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
- bayesian-inference
id: pkis:technique:amortized-vi
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch10
tags:
- amortized-inference
- recognition-network
- VAE
- inference-compilation
title: Amortized Variational Inference
understanding: 0
---

## Definition
$$q_\phi(z_n|x_n) \triangleq q\!\left(z_n\,|\,f^{\mathrm{inf}}_\phi(x_n)\right)$$

Instead of optimizing separate variational parameters $\psi_n$ for every data point, an **inference network** (recognition network) $f^{\mathrm{inf}}_\phi$ with shared parameters $\phi$ maps each observation $x_n$ directly to the parameters of $q$. The cost of per-example inference is amortized across the dataset.

### Why it matters
Amortized VI is the inference half of the VAE (Kingma & Welling, 2014) and enables end-to-end gradient training of deep generative models. It eliminates the inner optimization loop of SVI, though at the cost of an **amortization gap** — systematic suboptimality relative to per-example optimization — which semi-amortized methods (warm-starting the optimizer from the network's output) aim to close.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]