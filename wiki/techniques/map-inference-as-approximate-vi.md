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
- probabilistic-inference
id: pkis:technique:map-inference-as-approximate-vi
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch19
tags:
- MAP
- Dirac-distribution
- sparse-coding
- ELBO
- latent-variables
title: MAP Inference as Approximate Variational Inference
understanding: 0
---

## Definition
$$\mathbf{h}^* = \arg\max_h p(h | v) = \arg\max_\mu \log p(h = \mu, v)$$

MAP inference can be derived as a special case of variational inference by restricting $q$ to the family of Dirac distributions $q(h|v) = \delta(h - \mu)$. Dropping entropy terms (which equal $-\infty$ for a Dirac), maximizing the ELBO collapses to maximizing the joint $\log p(h, v)$, recovering the MAP objective.

### Why it matters
This framing connects MAP inference to the broader variational framework: MAP is coordinate ascent on $\mathcal{L}$ using the most degenerate possible variational family. Alternating MAP inference (for $q$) with parameter updates (for $\theta$) gives a tractable learning procedure for models like sparse coding, where the full posterior $p(h|v)$ is intractable. The resulting algorithm is equivalent to minimizing a penalized reconstruction loss.

### Limitations
Because the Dirac distribution has differential entropy of $-\infty$, the ELBO lower bound is infinitely loose. MAP learning thus lacks the probabilistic calibration of full variational inference and may poorly capture posterior uncertainty.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]