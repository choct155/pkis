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
- statistics
- robotics
generalizes:
- filtering-prediction-smoothing
- hidden-markov-model
- particle-filter
id: pkis:technique:bayes-filter
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch08
tags:
- bayesian-filtering
- sequential-inference
- predict-update
- state-estimation
- belief-state
title: Bayes Filter (Predict-Update Cycle)
understanding: 0
uses:
- markov-chains
---

## Definition
$$\underbrace{p(\mathbf{z}_t|\mathbf{y}_{1:t-1})}_\text{predict} = \int p(\mathbf{z}_t|\mathbf{z}_{t-1})\, p(\mathbf{z}_{t-1}|\mathbf{y}_{1:t-1})\, d\mathbf{z}_{t-1}$$
$$\underbrace{p(\mathbf{z}_t|\mathbf{y}_{1:t})}_\text{update} = \frac{p(\mathbf{y}_t|\mathbf{z}_t)\, p(\mathbf{z}_t|\mathbf{y}_{1:t-1})}{Z_t}, \quad Z_t = p(\mathbf{y}_t|\mathbf{y}_{1:t-1})$$

The general recursive algorithm for computing the belief state $p(\mathbf{z}_t|\mathbf{y}_{1:t})$ in a hidden Markov / state-space model. The predict step applies the **Chapman–Kolmogorov equation**, and the update step applies Bayes' rule; each step requires $O(1)$ memory relative to $t$. The normalization constants $Z_t$ yield the sequence log-likelihood $\log p(\mathbf{y}_{1:T}) = \sum_t \log Z_t$.

### Why it matters
The Bayes filter is the universal template for online state estimation. Special cases include the Kalman filter (linear-Gaussian), HMM forward algorithm (discrete states), and the particle filter (general nonlinear/non-Gaussian). The smoother is derived by a subsequent backwards pass using the filtered distributions.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[particle-filter]] — generalizes
- [[hidden-markov-model]] — generalizes: HMM forward algorithm is a special case
- [[markov-chains]] — uses
- [[filtering-prediction-smoothing]] — generalizes
[To be populated during integration]