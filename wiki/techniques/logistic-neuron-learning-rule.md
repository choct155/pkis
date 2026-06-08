---
aliases: []
also_type: []
applies:
- single-neuron-classifier
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-08'
domain:
- deep-learning
- statistical-learning
id: pkis:technique:logistic-neuron-learning-rule
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- backpropagation
related_concepts: []
sources:
- mackay-itila-ch39
specializes:
- gradient-descent
tags:
- delta-rule
- error-correction
- stochastic-gradient-descent
- cross-entropy
- online-learning
- weight-decay
title: Logistic-Neuron Gradient-Descent Learning Rule
understanding: 0
uses:
- cross-entropy-loss
- regularization
---

## Definition
The learning rule that trains a logistic single neuron by descending the cross-entropy (relative-entropy) error
$$G(\mathbf{w}) = -\sum_n \big[t^{(n)}\ln y^{(n)} + (1-t^{(n)})\ln(1-y^{(n)})\big],$$
where $t^{(n)}\in\{0,1\}$ are targets and $y^{(n)}=y(\mathbf{x}^{(n)};\mathbf{w})$. The gradient takes a strikingly clean form because the sigmoid's derivative cancels the logarithm:
$$\frac{\partial G}{\partial w_j} = -\sum_n (t^{(n)}-y^{(n)})\,x_j^{(n)}.$$

### The delta (error-correction) rule
Defining the error signal $e=t-y$, the **on-line** update presents examples one at a time:
$$\Delta w_i = \eta\, e\, x_i,$$
with learning rate $\eta$ (often $\eta_0/\tau$). This is stochastic gradient descent; accumulating $\sum_n$ before updating gives **batch** gradient descent. The weight change is proportional to the prediction error times the input — the Hebb-like signature of the rule.

### Overfitting and weight decay
On linearly separable data $G$ has no finite minimizer and $\|\mathbf{w}\|\to\infty$, sharpening the boundary (overfitting). A weight-decay regularizer $E_W=\tfrac12\sum_i w_i^2$ gives $M=G+\alpha E_W$, adding $-\eta\alpha w_i$ to each update and shrinking weights toward zero.

### Why it matters
This is the prototype of all neural-net training: the error-times-input update and the cancellation that makes it dimensionless-clean reappear as the base case of backpropagation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[backpropagation]] — prerequisite-of: The single-neuron error-times-input gradient is the base case generalized by backpropagation to multilayer nets.
- [[regularization]] — uses: Weight decay (L2) is added to the error to curb overfitting on linearly separable data.
- [[cross-entropy-loss]] — uses: The objective minimized is the cross-entropy / relative-entropy error between targets and neuron outputs.
- [[gradient-descent]] — specializes: On-line (delta) and batch updates are stochastic and full-batch gradient descent on the cross-entropy error.
- [[single-neuron-classifier]] — applies: The learning rule trains the single-neuron classifier by adjusting its weights.
[To be populated during integration]