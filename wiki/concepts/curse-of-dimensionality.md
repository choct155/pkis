---
aliases: []
also_type: []
contrasts-with:
- exact-inference-by-complete-enumeration
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-08'
domain:
- statistical-learning
id: pkis:concept:curse-of-dimensionality
knowledge_type: concept
maturity: settled
related_concepts:
- '[[bias-variance-tradeoff]]'
- '[[regularization]]'
sources:
- '[[hastie-esl]]'
- '[[domingos-useful-things]]'
- '[[liu-kan-2024]]'
tags:
- probability-theory
- high-dimensional-statistics
title: Curse of Dimensionality
understanding: 0
illustrated-by:
- typical-set-explainer
---

## Reading Path
- [[hastie-esl]] (unread) — mathematical treatment: exponential data requirements, kernel smoothing breakdown
- [[domingos-useful-things]] (unread) — §6: intuitive geometric examples (hypersphere/hypercube volumes, Gaussian shells); the "blessing of non-uniformity" counterpoint — data concentrates on lower-dimensional manifolds in practice
- [[liu-kan-2024]] (unread) — KANs claim to beat COD for functions with compositional/KA structure: splines only approximate 1D functions, so scaling exponent is independent of input dimension; caveat: constant depends on the representation's structure

The phenomenon whereby local methods (nearest neighbors, kernel smoothers) break down in high-dimensional spaces because neighborhoods that are "local" in each dimension become globally sparse, requiring exponentially more data to maintain the same coverage as dimensionality grows.

## Connections
- [[exact-inference-by-complete-enumeration]] — contrasts-with: The $10^K$ grid-point blow-up is the limiting factor that makes complete enumeration infeasible beyond low-dimensional spaces.

## Curse of Dimensionality in Brute-Force Integration
A distinct face of the curse appears in Bayesian computation via complete enumeration. To evaluate a posterior or marginal likelihood by gridding the parameter space, one sums $P(\theta)\,P(\mathcal{D}\mid\theta,\mathcal{H})$ over a grid of $\theta$ values. If observing the data sharpens each of $K$ parameters by, say, a factor of ten, then a grid fine enough to resolve the posterior needs at least $10^K$ points. This exponential growth of computation with model size is why MacKay (ITILA Ch. 21) notes that complete enumeration is rarely a feasible computational strategy: a five-parameter Gaussian mixture already strains it, and a ten-component mixture in twenty dimensions is hopeless. Unlike the local-methods version of the curse (sparse neighborhoods for nearest neighbors / kernel smoothing), this is a curse of *integration*: the cost of brute-force Bayesian evidence and posterior computation scales as the volume of a high-dimensional grid, which is the central motivation for sampling-based (MCMC) and variational approximations.