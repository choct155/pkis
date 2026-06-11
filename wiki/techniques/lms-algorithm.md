---
aliases: []
also_type: []
applies:
- linear-basis-function-model
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- normal-equations-pseudoinverse
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- signal-processing
id: pkis:technique:lms-algorithm
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
specializes:
- stochastic-gradient-descent
tags:
- online-learning
- stochastic-gradient
- sequential-learning
- adaptive-filtering
title: LMS Algorithm (Least-Mean-Squares)
understanding: 0
---

## Definition
A sequential (online) update rule for linear regression obtained by applying stochastic gradient descent to the per-sample squared error $E_n = \frac{1}{2}\{t_n - \mathbf{w}^T\boldsymbol{\phi}_n\}^2$:

$$\mathbf{w}^{(\tau+1)} = \mathbf{w}^{(\tau)} + \eta\,(t_n - \mathbf{w}^{(\tau)T}\boldsymbol{\phi}_n)\,\boldsymbol{\phi}_n$$

where $\eta$ is the learning rate and $\boldsymbol{\phi}_n = \boldsymbol{\phi}(x_n)$. Also known as the **Widrow-Hoff** rule.

### Why it matters
Enables regression on streaming or very large data sets without storing or inverting the full $N\times N$ Gram matrix. The update has the same form as a temporal-difference prediction error, linking regression learning to RL. Convergence requires $\eta$ to be small enough relative to the largest eigenvalue of the Gram matrix.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[normal-equations-pseudoinverse]] — contrasts-with: Sequential vs. batch solution to the same least-squares problem
- [[linear-basis-function-model]] — applies
- [[stochastic-gradient-descent]] — specializes
[To be populated during integration]