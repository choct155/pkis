---
aliases: []
also_type: []
analogous-to:
- em-algorithm
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- hierarchical-mixtures-of-experts
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- probabilistic-models
extends:
- feed-forward-neural-network
generalizes:
- heteroscedastic-neural-network
id: pkis:framework:mixture-density-network
instantiates:
- mixture-models
- ml-cost-design-neural-networks
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch05
- goodfellow-deeplearning-ch06
tags:
- density-estimation
- multimodal
- inverse-problems
- heteroscedastic
title: Mixture Density Network
understanding: 0
uses:
- gaussian-mixture-models
- cross-entropy-loss
- softmax-output-unit
---

## Definition
A neural network that outputs the parameters of a conditional mixture model:
$$p(\mathbf{t}|\mathbf{x}) = \sum_{k=1}^{K}\pi_k(\mathbf{x})\,\mathcal{N}\!\left(\mathbf{t}\mid\boldsymbol{\mu}_k(\mathbf{x}),\sigma_k^2(\mathbf{x})\mathbf{I}\right)$$
where the mixing coefficients $\pi_k(\mathbf{x})$ (via softmax), means $\boldsymbol{\mu}_k(\mathbf{x})$, and variances $\sigma_k^2(\mathbf{x})$ (via exp) are all outputs of a shared neural network with input $\mathbf{x}$. The network has $(K+2)L$ output units for $L$ components and $K$-dimensional targets.

Training minimises the negative log-likelihood $E(\mathbf{w}) = -\sum_n \ln\sum_k \pi_k(\mathbf{x}_n)\mathcal{N}(\mathbf{t}_n|\boldsymbol{\mu}_k,\sigma_k^2)$ via backpropagation using posterior responsibilities $\gamma_k = \pi_k N_{nk}/\sum_l \pi_l N_{nl}$.

### Why it matters
Addresses the fundamental limitation of least-squares neural networks on *inverse problems*: when the conditional distribution $p(\mathbf{t}|\mathbf{x})$ is multimodal, minimising MSE predicts the conditional mean, which may correspond to no plausible output. MDNs model the full conditional density, enabling uncertainty quantification and mode-seeking for multi-valued mappings (e.g. robot inverse kinematics).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[ml-cost-design-neural-networks]] — instantiates
- [[heteroscedastic-neural-network]] — generalizes
- [[softmax-output-unit]] — uses: Mixture weights are produced by softmax.
- [[hierarchical-mixtures-of-experts]] — contrasts-with
- [[em-algorithm]] — analogous-to
- [[cross-entropy-loss]] — uses
- [[mixture-models]] — instantiates
- [[feed-forward-neural-network]] — extends
- [[gaussian-mixture-models]] — uses
[To be populated during integration]