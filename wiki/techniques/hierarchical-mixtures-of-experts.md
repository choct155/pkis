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
id: pkis:technique:hierarchical-mixtures-of-experts
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch09
tags:
- mixture-models
- soft-splits
- em-algorithm
- tree-based
title: Hierarchical Mixtures of Experts (HME)
understanding: 0
---

## Definition
A tree-structured model in which the splits are soft (probabilistic) rather than hard decisions: at each non-terminal node a softmax gating network g_j(x, gamma_j) = exp(gamma_j^T x) / sum_k exp(gamma_k^T x) routes an observation to branch j with a probability depending on a linear combination of the inputs, and terminal nodes (experts) fit a full model (Gaussian linear regression for regression, logistic regression for classification) rather than a constant. The total response probability is a mixture, Pr(y|x,Psi) = sum_j g_j(x,gamma_j) sum_l g_{l|j}(x,gamma_{jl}) Pr(y|x,theta_{jl}), so the HME is formally a hierarchical mixture model with input-dependent mixing weights. Soft splits make the log-likelihood a smooth function of the parameters, amenable to numerical optimization (unlike CART's discrete split-point search), and let the model capture gradual low-to-high response transitions. Parameters are estimated by maximum likelihood via the EM algorithm: latent branch-assignment variables Delta_j, Delta_{l|j} are introduced, the E-step computes their expected values (probability profiles) under current parameters, and the M-step uses these as observation weights to refit the experts (weighted regressions) and as response vectors for multiple-logistic-regression fits of the internal gating nodes. Compared with CART it resembles linear-combination-split trees but is easier to optimize; its weakness is the lack of a method for learning a good tree topology (usually a fixed-depth tree, possibly from CART, is imposed), and the EM iterations can be slow to converge. A close cousin is the single-layer latent class model.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]