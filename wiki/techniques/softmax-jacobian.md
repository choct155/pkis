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
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- calculus
id: pkis:technique:softmax-jacobian
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch10
tags:
- softmax
- Jacobian
- backpropagation
- gradient
- multiclass
title: Softmax Jacobian
understanding: 0
---

## Definition
For $\mu = \text{softmax}(a)$ with $\mu_c = \exp(a_c)/\sum_{c'}\exp(a_{c'})$, the $(c,j)$ entry of the Jacobian is
$$\frac{\partial\mu_c}{\partial a_j} = \mu_c(\delta_{cj} - \mu_j)$$
In matrix form: $\partial\mu/\partial a = \text{diag}(\mu) - \mu\mu^T$.

### Why it matters
This identity is the core building block for deriving gradients through any softmax layer: cross-entropy NLL gradient, Hessian of multinomial logistic regression, and backpropagation through classifier heads. The matrix $\text{diag}(\mu)-\mu\mu^T$ is positive semi-definite with rank $C-1$, confirming that the multinomial NLL is convex.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]