---
aliases: []
also_type: []
analogous-to:
- kalman-filter
applies:
- hidden-markov-model
- dynamic-bayesian-network
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
- probabilistic-graphical-models
- machine-learning
- statistics
id: pkis:technique:forwards-backwards-algorithm
instantiates:
- filtering-prediction-smoothing
- message-passing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch09
specializes:
- sum-product-algorithm-trees
tags:
- HMM
- smoothing
- message-passing
- dynamic-programming
- sequential-inference
title: Forwards-Backwards Algorithm (HMM Smoothing)
understanding: 0
uses:
- em-algorithm
- markov-chains
---

## Definition
$$\gamma_t(j) = p(z_t = j \mid y_{1:T}) \propto \alpha_t(j)\,\beta_t(j)$$

where the forward messages $\alpha_t(j) = p(z_t = j \mid y_{1:t})$ are computed left-to-right and the backward messages $\beta_t(j) = p(y_{t+1:T} \mid z_t = j)$ are computed right-to-left via
$$\beta_{t-1} = A(\lambda_t \odot \beta_t), \quad \beta_T = \mathbf{1}.$$

The smoothed marginals are obtained by element-wise multiplication and renormalization of the forward and backward passes. Two-slice marginals are given by $\xi_{t,t+1}(i,j) \propto A_{ij}\,[\alpha_t(i)](\lambda_{t+1}(j)\beta_{t+1}(j))$.

Intuition: each time step's posterior is a product of "what do we know from the past" and "what does the future tell us."

### Why it matters
The forwards-backwards (FB) algorithm is the canonical $O(K^2 T)$ algorithm for exact posterior inference in HMMs and, more broadly, any chain-structured graphical model. It is the discrete-state special case of the Kalman smoother and forms the E-step of the Baum-Welch (EM) algorithm for learning HMM parameters. The numerically stable, normalized form avoids underflow by maintaining conditional distributions rather than joint probabilities.

### Variants
- **Forwards filtering / backwards smoothing** replaces the backward $\beta$ pass with a recursion on the smoothed marginals $\gamma_t$, useful when $\beta_t$ is ill-defined (continuous state spaces).
- **Forwards filtering / backwards sampling** draws posterior samples rather than computing marginals.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kalman-filter]] — analogous-to: FB is the discrete-state analogue of the Kalman smoother
- [[markov-chains]] — uses
- [[em-algorithm]] — uses: FB is the E-step of Baum-Welch EM for HMM parameter learning
- [[message-passing]] — instantiates
- [[sum-product-algorithm-trees]] — specializes
- [[dynamic-bayesian-network]] — applies
- [[filtering-prediction-smoothing]] — instantiates
- [[hidden-markov-model]] — applies
[To be populated during integration]