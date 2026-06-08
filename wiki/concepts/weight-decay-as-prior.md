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
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
- bayesian-stats
id: pkis:concept:weight-decay-as-prior
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch41
tags:
- weight-decay
- gaussian-prior
- regularization
- map-estimation
- hyperparameter
title: Weight Decay as a Gaussian Prior
understanding: 0
---

## Definition
The standard quadratic weight-decay regularizer is exactly the negative log of a zero-mean isotropic Gaussian prior over the weights. With
$$E_W(w)=\tfrac{1}{2}\sum_i w_i^2,$$
the implied prior is
$$P(w\mid\alpha)=\frac{1}{Z_W(\alpha)}\exp(-\alpha E_W)=\left(\frac{\alpha}{2\pi}\right)^{K/2}\exp\!\Big(-\tfrac{\alpha}{2}\textstyle\sum_i w_i^2\Big),$$
a product of $K$ independent Gaussians each with variance $\sigma_W^2 = 1/\alpha$. Thus the decay rate $\alpha$ is an *inverse prior variance*: large $\alpha$ is a tight prior pulling weights toward zero; small $\alpha$ is a vague prior permitting large weights.

### Consequences
Because $\alpha$ controls the prior, it is not a free knob to be tuned by validation alone — within the evidence framework it can be inferred from the data by maximizing the marginal likelihood. The correspondence also generalizes: an $L_1$ penalty corresponds to a Laplacian prior, and structured penalties to structured priors.

### Why it matters
It dissolves the apparent arbitrariness of weight decay. Choosing a regularizer is choosing a belief about plausible weights *before* seeing data, which makes the choice interpretable, comparable, and — crucially — inferable rather than merely guessed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]