---
aliases: []
also_type: []
applies:
- restricted-boltzmann-machine
- energy-based-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- deep-learning
- statistical-learning
extends:
- boltzmann-machine-learning-rule
id: pkis:technique:contrastive-divergence
instantiates:
- positive-negative-phase-learning
- boltzmann-machine-learning-rule
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch17
tags:
- boltzmann-machine
- restricted-boltzmann-machine
- gibbs-sampling
- approximate-gradient
- energy-based-models
title: Contrastive Divergence
understanding: 0
uses:
- gibbs-sampler
- spurious-modes
- mcmc
- kl-divergence
---

## Definition
Contrastive divergence (CD; Hinton, 2002) is an approximate gradient-learning rule for energy-based undirected models such as (restricted) Boltzmann machines. The exact maximum-likelihood gradient for an edge parameter has the form E_hat(X_j X_k) (data/clamped expectation) minus E_Theta(X_j X_k) (model expectation). The first term is cheap, but the second requires sampling from the model distribution, which in principle means running a Gibbs sampler all the way to stationarity -- prohibitively slow because the Markov chain mixes more and more slowly as the network weights grow.

Hinton's empirical observation is that learning still works well if the model expectation is estimated by starting the Markov chain AT THE DATA and running it for only a few steps rather than to convergence. In a restricted Boltzmann machine this is one short alternating sweep: sample H given (V1, V2), then sample (V1, V2) given H, then sample H given the reconstructed visibles again, and use these short-run statistics in place of the equilibrium expectation. The intuition is that when parameters are far from the optimum it is wasteful to equilibrate the sampler -- a single (or few) iteration already reveals a good direction to move the estimates. CD trades an unbiased-but-intractable gradient for a biased-but-fast one, and is the workhorse that made training and greedy layer-wise stacking of RBMs feasible (e.g., the MNIST feature-learning pipeline of Hinton et al., 2006).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[kl-divergence]] — uses: CD_T minimizes KL(p0||p∞) - KL(pT||p∞)
- [[mcmc]] — uses: CD runs short MCMC chains initialized at data points
- [[energy-based-model]] — applies: CD is a training algorithm for EBMs
- [[boltzmann-machine-learning-rule]] — instantiates
- [[spurious-modes]] — uses
- [[positive-negative-phase-learning]] — instantiates
- [[boltzmann-machine-learning-rule]] — extends: Replaces the intractable equilibrium model expectation in the BM learning rule with a few-step approximation.
- [[gibbs-sampler]] — uses: Runs a short Gibbs chain started at the data to approximate the model expectation.
- [[restricted-boltzmann-machine]] — applies: Contrastive divergence is the practical learning rule for RBMs.
[To be populated during integration]