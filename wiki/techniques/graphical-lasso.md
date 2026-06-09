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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- optimization
id: pkis:technique:graphical-lasso
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch17
tags:
- sparse-precision-matrix
- l1-regularization
- covariance-selection
- coordinate-descent
- structure-estimation
title: Graphical Lasso
understanding: 0
---

## Definition
The graphical lasso (Friedman, Hastie and Tibshirani, 2008, building on Banerjee et al., 2008) estimates a sparse Gaussian graphical model by maximizing the L1-penalized Gaussian log-likelihood

    log det Theta - trace(S Theta) - lambda ||Theta||_1,

where ||Theta||_1 is the sum of absolute values of the entries of the precision matrix and S is the empirical covariance. The negative of this objective is convex. The L1 penalty drives entries of Theta exactly to zero, simultaneously estimating the conditional-independence graph (which edges are present) and the edge parameters, with sparsity controlled by lambda.

The key insight is that the problem can be solved one row/column at a time by a sequence of lasso regressions. The sub-gradient (KKT) condition Theta^{-1} - S - lambda * Sign(Theta) = 0 reduces, for each block, to W_{11} beta - s_{12} + lambda * Sign(beta) = 0, which is exactly the estimating equation of an ordinary lasso regression in which Z^T Z is replaced by W_{11}, the current model-based estimate of the covariance among the predictors (NOT the raw cross-product S_{11}). This coupling through the common W is what makes the p regressions a single coherent estimation problem rather than p independent ones. Each block lasso is solved by pathwise coordinate descent with the soft-threshold update beta_j <- S(s_{12j} - sum_{k!=j} V_{kj} beta_k, lambda)/V_{jj}, where S(x,t)=sign(x)(|x|-t)_+ is the soft-threshold operator and V = W_{11}.

The algorithm cycles over all p variables until convergence; the diagonal of the solution is fixed at w_{jj} = s_{jj} + lambda. It is extremely fast (a moderately sparse 1000-node problem in under a minute), delivers both Sigma_hat and Theta_hat, supports edge-specific penalties lambda_{jk} (setting lambda_{jk}=infinity forces a structural zero, so it subsumes the fixed-structure constrained-MLE algorithm), and yields the full solution path as a function of lambda. A simpler 'neighborhood selection' alternative (Meinshausen and Buhlmann, 2006) fits a separate lasso of each variable on the others and declares edge ij present by an AND/OR rule on the two coefficients, consistently recovering the support but not the parameter values. Hoefling and Tibshirani (2008) extend the graphical lasso to discrete (Ising/Boltzmann) Markov networks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]