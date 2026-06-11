---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- deep-learning
- probabilistic-inference
id: pkis:result:depth-improves-mcmc-mixing
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- goodfellow-deeplearning-ch17
tags:
- mcmc
- mixing
- deep-learning
- latent-variable-models
- representation-learning
title: Depth Improves MCMC Mixing in Latent Variable Models
understanding: 0
---

## Definition
**Empirical finding (Bengio et al., 2013):** Deeper stacks of regularised autoencoders or RBMs produce a top-level latent representation $\mathbf{h}$ whose marginal distribution is more uniform and unimodal than the original data distribution over $\mathbf{x}$, reducing the effective energy barriers between modes in $\mathbf{h}$-space and allowing Gibbs sampling to mix faster.

### Formal intuition
If $p(\mathbf{h} | \mathbf{x})$ is concentrated (high mutual information), then $p(\mathbf{x} | \mathbf{h})$ is also concentrated and the chain barely moves. A deep representation that spreads $\mathbf{h}$ more uniformly trades representation precision for mixing speed:
$$\text{Mixing quality} \uparrow \iff H(\mathbf{h} | \mathbf{x}) \uparrow \iff I(\mathbf{h}; \mathbf{x}) \downarrow$$

### Why it matters
This result motivates using deep generative models (deep Boltzmann machines, VAEs) rather than shallow ones when tractable sampling is required. It also reveals a fundamental tension: the better the model encodes data, the harder it is to sample from, informing research into generative adversarial and diffusion-based alternatives.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]