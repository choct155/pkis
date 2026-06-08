---
aliases: []
also_type: []
contrasts-with:
- maxima-are-atypical
coverage: 1
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- bayesian-stats
- deep-learning
id: pkis:concept:bayesian-neural-networks
knowledge_type: concept
maturity: evolving
related_concepts:
- '[[variational-inference]]'
- '[[neural-networks]]'
- '[[probability-theory]]'
sources:
- '[[yellapragada-variational-bayes]]'
tags:
- variational-methods
- approximate-inference
- deep-learning
- uncertainty-quantification
title: Bayesian Neural Networks
understanding: 0
uses:
- marginalization
- hmc
- laplace-approximation
---

Neural networks that place probability distributions over weights rather than point estimates, enabling principled uncertainty quantification in predictions; inference over the weight posterior is typically intractable and requires approximate methods such as variational inference, MCMC, or Monte Carlo dropout.

## Connections
- [[maxima-are-atypical]] — contrasts-with: Marginalization fixes the over-confidence of MAP point prediction that maxima-are-atypical warns about.
- [[laplace-approximation]] — uses: The Gaussian approximation around w_MP gives a deterministic route to BNN predictions.
- [[hmc]] — uses: Hamiltonian (and Langevin) Monte Carlo sample the weight posterior to estimate the predictive integral.
- [[marginalization]] — uses: Bayesian prediction integrates the network output over the weight posterior.

- [[variational-inference]] — used-by: VI is the dominant approximate inference approach for BNNs (Bayes by Backprop, AEVB, multiplicative normalizing flows)
- [[neural-networks]] — extends: BNNs extend standard NNs with a prior and approximate posterior over weights
- [[reparameterization-trick]] — used-by: Bayes by Backprop and related VI methods for BNNs rely on reparameterization to backpropagate through the weight distribution

## Reading Path

- [[yellapragada-variational-bayes]] (unread) — central subject; reviews five VI approaches to BNN inference; applications in RL exploration and continual learning