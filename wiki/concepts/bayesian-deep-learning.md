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
contrasts-with:
- deep-reinforcement-learning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- deep-learning
- bayesian-inference
- uncertainty-quantification
id: pkis:concept:bayesian-deep-learning
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch17
specializes:
- bayesian-neural-networks
tags:
- BDL
- posterior-predictive
- model-averaging
- underspecification
title: Bayesian Deep Learning (BDL)
understanding: 0
uses:
- bayesian-model-averaging
- variational-inference
- laplace-approximation
- hmc
- neural-network-gaussian-process-limit
- weight-decay-as-prior
- automatic-priors
- transfer-learning
---

## Definition
$$p(y|x, D) = \int p(y|x, \theta)\, p(\theta|D)\, d\theta, \quad p(\theta|D) \propto p(\theta)\, p(D|\theta)$$

Bayesian Deep Learning applies Bayesian inference—specifically, posterior predictive integration—to deep neural networks, treating the (very high-dimensional) weight vector $\theta$ as a random variable rather than a point estimate.

### Why it matters
Single-parameter (MAP/MLE) deep nets suffer from *underspecification*: many weight configurations fit training data equally well yet generalise differently. BDL averages over this posterior mass, improving calibration, uncertainty quantification, and robustness to distribution shift. The main challenges are specifying suitable priors and tractable posterior inference at scale.

### Contrast with Deep Bayesian Learning
*Deep Bayesian Learning* (DBL) is the complementary direction: using deep models (e.g., amortised inference networks) to *speed up* Bayesian inference for classical models, not performing Bayes inside a DNN.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[transfer-learning]] — uses: Bayesian transfer learning uses posterior from D1 as prior for fine-tuning on D2
- [[automatic-priors]] — uses: Empirical Bayes / evidence maximisation to learn prior hyperparameters
- [[weight-decay-as-prior]] — uses: Gaussian weight prior corresponds to L2 regularisation / weight decay in MAP training
- [[neural-network-gaussian-process-limit]] — uses: Infinite-width limit gives analytic prior over functions
- [[deep-reinforcement-learning]] — contrasts-with: BDL is Bayesian inference over DNN weights; deep RL is a separate use of DNNs
- [[hmc]] — uses
- [[laplace-approximation]] — uses
- [[variational-inference]] — uses
- [[bayesian-model-averaging]] — uses: Posterior predictive is a Bayesian model average over DNN weights
- [[bayesian-neural-networks]] — specializes
[To be populated during integration]