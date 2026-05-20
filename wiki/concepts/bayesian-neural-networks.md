---
title: "Bayesian Neural Networks"
knowledge_type: concept
also_type: []
domain: [bayesian-stats, deep-learning]
tags: [variational-methods, approximate-inference, deep-learning, uncertainty-quantification]
related_concepts: ["[[variational-inference]]", "[[neural-networks]]", "[[probability-theory]]"]
sources: ["[[yellapragada-variational-bayes]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: evolving
---

Neural networks that place probability distributions over weights rather than point estimates, enabling principled uncertainty quantification in predictions; inference over the weight posterior is typically intractable and requires approximate methods such as variational inference, MCMC, or Monte Carlo dropout.

## Connections

- [[variational-inference]] — used-by: VI is the dominant approximate inference approach for BNNs (Bayes by Backprop, AEVB, multiplicative normalizing flows)
- [[neural-networks]] — extends: BNNs extend standard NNs with a prior and approximate posterior over weights
- [[reparameterization-trick]] — used-by: Bayes by Backprop and related VI methods for BNNs rely on reparameterization to backpropagate through the weight distribution

## Reading Path

- [[yellapragada-variational-bayes]] (unread) — central subject; reviews five VI approaches to BNN inference; applications in RL exploration and continual learning
