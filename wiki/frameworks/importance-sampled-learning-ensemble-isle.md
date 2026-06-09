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
- optimization
generalizes:
- bagging
- random-forests
- gradient-boosting
id: pkis:framework:importance-sampled-learning-ensemble-isle
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch16
specializes:
- ensemble-learning
tags:
- ensemble-methods
- boosting
- bagging
- random-forests
- lasso
- importance-sampling
- subsampling
title: Importance Sampled Learning Ensemble (ISLE)
understanding: 0
uses:
- lasso
- importance-sampling
---

## Definition
A two-stage framework (Friedman & Popescu, 2003) that reconceives ensemble construction as numerical quadrature of an unknown target written as an integral f(x) = ∫ β(γ) b(x;γ) dγ over a continuum of basis functions b(x;γ) indexed by γ ∈ Γ (for trees, γ indexes split variables, split-points, and node values). Stage 1 induces a finite dictionary T_L = {b(x;γ_1),...,b(x;γ_M)} by sampling γ via importance sampling — favoring relevant regions where the loss-based relevance measure Q(γ) = min_{c0,c1} Σ L(y_i, c0 + c1 b(x_i;γ)) is small. Randomness is injected through subsampling: each base learner is fit on a subsample S_m(η) of N·η observations (typically without replacement). The characteristic width σ = E_S[Q(γ) - Q(γ*)] of the sampling scheme trades off diversity against relevance — too narrow makes the b(x;γ_m) look alike, too wide admits many irrelevant members. A memory parameter ν ∈ [0,1] in the update f_m = f_{m-1} + ν b(x;γ_m) controls how strongly the procedure avoids previously-found members. Stage 2 post-processes the dictionary by fitting a lasso path α(λ) = argmin_α Σ L[y_i, α_0 + Σ α_m T_m(x_i)] + λ Σ |α_m|, yielding a sparse, parsimonious reweighting. Algorithm 16.2 unifies familiar schemes as special cases: bagging (η=1 with replacement, ν=0), random forests (similar plus random split-variable selection), gradient boosting with shrinkage (η=1, ν=learning rate, but often insufficient width σ), and stochastic gradient boosting (the exact recipe). Recommended defaults: ν=0.1, η≤1/2 (and η~1/√N for large N). Empirically, lasso post-processing of a random forest on the spam data reduced 1000 trees to ~40 while matching gradient boosting; ISLE typically preserves accuracy while producing far more parsimonious models. RuleFit (rule-ensembles) is the rule-based instantiation built on top of ISLE.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[gradient-boosting]] — generalizes: (stochastic) gradient boosting with shrinkage is the exact recipe with subsample η and memory ν
- [[random-forests]] — generalizes: random forests arise as a subsampling special case with random split-variable selection
- [[bagging]] — generalizes: bagging is the special case η=1 (with replacement), ν=0 of Algorithm 16.2
- [[importance-sampling]] — uses: dictionary members are drawn by importance sampling over the basis-function index space Γ
- [[lasso]] — uses: stage-2 post-processing fits a lasso path over the induced dictionary
- [[ensemble-learning]] — specializes: ISLE is a concrete two-stage instantiation of the ensemble-learning framework
[To be populated during integration]