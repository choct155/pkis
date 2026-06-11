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
- variational-inference
id: pkis:technique:inverse-autoregressive-flow
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch23
tags:
- normalizing-flow
- IAF
- variational-inference
- parallel-wavenet
title: Inverse Autoregressive Flow (IAF)
understanding: 0
---

## Definition
An inverse autoregressive bijection conditions the scalar bijection parameters on *previous inputs* rather than previous outputs:
$$x_i = h(u_i;\,\Theta_i(u_{1:i-1})), \quad i = 1, \ldots, D.$$
This swaps the computational asymmetry of a standard autoregressive flow: the forward pass (sampling) is parallelisable, while the inverse pass (density evaluation of externally provided points) is sequential.

### Why it matters
IAF is ideally suited for variational inference: drawing samples from $q_\theta(z|x)$ and evaluating their log-density (needed for the ELBO) are both efficient. It is the basis of **Parallel WaveNet**, which trains an IAF to mimic a slow-to-sample WaveNet model by minimising $D_{KL}(p_s \| p_t)$, achieving high-quality audio generation at inference time.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]