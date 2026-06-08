---
aliases: []
also_type: []
contrasts-with:
- maxima-are-atypical
coverage: 1
date_created: 2026-05-20
date_updated: '2026-06-08'
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

## Prediction by Marginalization over Weights
The point of Bayesian learning is not a single trained weight vector but an *ensemble*: rather than fix $w$ to its optimum $w_{MP}$, one predicts a new target by integrating the network output against the weight posterior,
$$P(t^{(N+1)}{=}1\mid x^{(N+1)},D,\alpha)=\int d^K w\; y(x^{(N+1)};w)\,\tfrac{1}{Z_M}e^{-M(w)}.$$
This marginalization is what fixes the central pathology of point prediction: networks fixed to $w_{MP}$ give *over-confident* outputs far from the data. MacKay's example — two test points A and B with the same $w_{MP}\!\cdot\!x$ receive the same MAP probability, yet B (far from the training data) should be far less certain — shows why. Marginalizing over the posterior automatically moderates predictions toward 0.5 exactly where parameter uncertainty is large, with no ad hoc downweighting factor.

MacKay names three families for computing the integral: Monte Carlo sampling from the posterior (Langevin and Hamiltonian Monte Carlo), the Laplace/Gaussian approximation around $w_{MP}$, and variational methods. For realistic networks ($K$ in the thousands) only the approximate routes are feasible.

## Monte Carlo Inference: Langevin and Hamiltonian
When the weight posterior is too high-dimensional for exact or Gaussian methods, the predictive integral is estimated by sampling weights $\{w^{(r)}\}\sim\tfrac{1}{Z_M}e^{-M(w)}$ and averaging the network outputs, $\langle y\rangle\simeq\tfrac{1}{R}\sum_r y(x;w^{(r)})$.

The **Langevin Monte Carlo** method is the simplest gradient-based sampler — 'gradient descent with added noise': a unit-variance Gaussian momentum $p$ is drawn, the gradient $g=\nabla M$ is computed, and a Metropolis-corrected step combines descent with diffusion (descent rate $\eta=\tfrac12\epsilon^2$). Its mean trajectory tracks ordinary gradient descent, but it explores the full posterior rather than collapsing to $w_{MP}$.

**Hamiltonian Monte Carlo** (introduced to neural nets by Neal, 1996) augments each proposal with a dynamical trajectory of many gradient steps in $(w,p)$ space, dramatically reducing autocorrelation — on MacKay's toy problem it is at least ten times more efficient than Langevin. A diagnostic worth remembering: during sampling $M(w)$ almost never returns close to its minimum $M(w_{MP})$, because the *typical set* of the posterior lives away from the mode — a concrete instance of why optimized parameters are unrepresentative.