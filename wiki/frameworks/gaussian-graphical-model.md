---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- statistical-learning
- bayesian-stats
id: pkis:framework:gaussian-graphical-model
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch17
tags:
- graphical-models
- multivariate-gaussian
- precision-matrix
- conditional-independence
- covariance-selection
title: Gaussian Graphical Model
understanding: 0
---

## Definition
A Gaussian graphical model is an undirected graphical model in which the vertices are continuous random variables assumed to follow a multivariate Gaussian distribution N(mu, Sigma). Because the Gaussian represents at most second-order relationships, it automatically encodes a pairwise Markov graph: the conditional-independence structure is read directly off the inverse covariance (precision) matrix Theta = Sigma^{-1}. The ij-th entry of Theta is (proportional to) the negative partial correlation between variables i and j given all the rest, so Theta_{ij} = 0 if and only if variables i and j are conditionally independent given the remaining variables. Hence the sparsity pattern of Theta IS the graph: a missing edge corresponds to a structural zero in the precision matrix.

The role of Theta becomes explicit through the regression view: partitioning X = (Z, Y) with Y the last variable, the conditional distribution Y | Z is Gaussian whose mean is the population multiple linear regression of Y on Z, with coefficient vector beta = Sigma_{ZZ}^{-1} sigma_{ZY} = -theta_{ZY}/theta_{YY}. The dependence of Y on the rest lives entirely in this mean term, and zero elements of beta (equivalently of theta_{ZY}) mark conditional independencies. Thus Theta is the natural parameter of the model: it carries all second-order structural and quantitative information needed to describe each node's conditional distribution given the rest, and dependence structure can be learned through multiple linear regression.

Given N realizations with empirical covariance S, the log-likelihood (profiled over the mean) is l(Theta) = log det Theta - trace(S Theta), a concave function of Theta whose unconstrained maximizer is Sigma_hat = S. Estimating a sparse graph means maximizing this likelihood subject to pre-specified zeros in Theta (an equality-constrained convex problem solvable by a coupled-regression / 'positive definite completion' procedure, or by iterative proportional fitting), or, when the structure is unknown, adding an L1 penalty and solving the graphical lasso. Contrast with the covariance graph (relevance network), whose edges encode nonzero marginal covariance rather than partial covariance, and whose negative log-likelihood is non-convex.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]