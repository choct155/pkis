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
contrasts-with:
- the-kernel-trick
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- reinforcement-learning
- statistical-learning
generalizes:
- coarse-coding
- kernel-smoothing
id: pkis:technique:radial-basis-function-network
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- sutton-reinforcement-2018-ch09
specializes:
- linear-function-approximation-rl
tags:
- feature-construction
- rbf
- gaussian
- function-approximation
title: Radial Basis Function Network
understanding: 0
uses:
- gaussian-mixture-models
---

## Definition
A linear function approximator whose features are radial basis functions—the continuous-valued generalization of coarse coding. Each feature has a graded (typically Gaussian) response x_i(s) = exp(−‖s − c_i‖² / 2σ_i²) depending only on the distance from the state to the feature's center c_i relative to its width σ_i, taking any value in [0,1]. Learning the weights uses the standard linear SGD/semi-gradient update (Eqs. 9.7–9.8); if the centers and widths are also adapted, the method becomes nonlinear and can fit targets more precisely at the cost of computational complexity and manual tuning. RBFs produce smooth, differentiable approximations, an advantage that rarely matters in practice; in more than two dimensions they typically add cost without improving on tile coding because graded activations near tile edges are hard to control.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[the-kernel-trick]] — contrasts-with
- [[gaussian-mixture-models]] — uses
- [[kernel-smoothing]] — generalizes
- [[linear-function-approximation-rl]] — specializes: an RBF network with fixed centers/widths is a linear approximator over RBF features
- [[coarse-coding]] — generalizes: RBFs are the continuous-valued generalization of binary coarse-coding features
[To be populated during integration]