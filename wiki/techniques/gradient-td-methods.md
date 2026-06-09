---
aliases: []
also_type: []
applies:
- stochastic-gradient-descent
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- residual-gradient-algorithm
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- optimization
extends:
- semi-gradient-td
id: pkis:technique:gradient-td-methods
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch11
tags:
- off-policy
- projected-bellman-error
- sgd
- stable-off-policy
- two-time-scale
- gtd2
- tdc
title: Gradient-TD Methods (GTD2 and TDC)
understanding: 0
uses:
- bellman-error-vs-projected-bellman-error
---

## Definition
A family of true stochastic-gradient-descent methods that minimize the projected Bellman error (PBE), giving robust convergence even under off-policy training and nonlinear function approximation, at O(d) per-step cost. The PBE gradient (Eq. 11.27) is a product of three expectations whose first and last factors both depend on x_{t+1}, so naive sampling is biased. The trick is to estimate and store the product of the last two factors as a second weight vector v approximating E[x x^T]^{-1} E[rho delta x], learned by an importance-sampled LMS rule v_{t+1} = v_t + beta rho_t (delta_t - v_t^T x_t) x_t; the remaining factor is then sampled and combined with the stored v. Substituting v gives GTD2: w_{t+1} = w_t + alpha rho_t (x_t - gamma x_{t+1}) (x_t^T v_t). A few extra analytic steps before substitution give the slightly better TDC (TD(0) with gradient correction, a.k.a. GTD(0)): w_{t+1} = w_t + alpha rho_t (delta_t x_t - gamma x_{t+1} (x_t^T v_t)). Both are 'cascade' / two-time-scale algorithms: the secondary v-learner runs on a faster scale (beta -> 0, alpha/beta -> 0) and is assumed converged so the primary w-learner can rely on it. On Baird's counterexample TDC drives the PBE to zero (though the VE converges very slowly thereafter). Gradient-TD is the most well-understood and widely used stable off-policy method, with extensions to control (GQ), eligibility traces (GTD(lambda), GQ(lambda)), and nonlinear approximation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bellman-error-vs-projected-bellman-error]] — uses: Gradient-TD minimizes the projected Bellman error (PBE).
- [[semi-gradient-td]] — extends: TDC = semi-gradient TD plus a gradient-correction term using a second weight vector.
- [[residual-gradient-algorithm]] — contrasts-with: Both are true SGD methods but target the PBE vs the BE; Gradient-TD avoids the BE's learnability and double-sampling problems.
- [[stochastic-gradient-descent]] — applies: Gradient-TD performs true SGD on the projected Bellman error.
[To be populated during integration]