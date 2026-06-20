---
aliases: []
also_type: []
analogous-to:
- entropy
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-08'
date_updated: '2026-06-20'
domain:
- statistical-learning
id: pkis:result:exponential-family-ml-maxent-duality
instantiates:
- maximum-entropy-principle
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- mackay-itila-ch22
- lange-applied-probability-ch16
specializes:
- maximum-likelihood-estimation
tags:
- exponential-family
- maximum-likelihood
- maximum-entropy
- moment-matching
- lagrange-multipliers
- sufficient-statistics
title: ML–MaxEnt Duality for Exponential Families
understanding: 0
uses:
- sufficient-statistics
- lagrange-multipliers
- maximum-entropy-principle
---

## Definition
For an exponential-family model
$$P(x\mid\mathbf w) = \frac{1}{Z(\mathbf w)}\exp\!\Big(\sum_k w_k f_k(x)\Big),$$
the maximum-likelihood parameters $\mathbf w_{\text{ML}}$ satisfy a **moment-matching** condition: the expected value of every feature under the fitted model equals its empirical average,
$$\langle f_k\rangle_{P(x\mid\mathbf w_{\text{ML}})} = \langle f_k\rangle_{\text{Data}} = \frac1N\sum_n f_k(x^{(n)}).$$
This drops out of differentiating the log likelihood, the only subtlety being $\frac{\partial}{\partial w_k}\ln Z(\mathbf w) = \langle f_k\rangle_{P(x\mid\mathbf w)}$ — the log-partition function's gradient is the model's feature mean.

### The duality with maximum entropy
Separately, the **maximum-entropy** distribution that maximizes $H = \sum_x P(x)\log\tfrac1{P(x)}$ subject to constraints $\langle f_k\rangle_{P} = F_k$ has, by Lagrange multipliers (one per constraint plus normalization), *exactly* the exponential-family form $P(x) = \tfrac1Z\exp(\sum_k w_k f_k(x))$. Setting $F_k = \langle f_k\rangle_{\text{Data}}$ makes the two problems coincide: **maximum-likelihood fitting of an exponential family is identical to maximum-entropy fitting under empirical-moment constraints.**

### Why it matters
This is the conceptual hub of generalized linear models, logistic regression, Boltzmann machines, and maxent NLP models: feature expectations are the sufficient statistics, and learning is just matching them. MacKay nonetheless cautions against using maxent to *assign priors* or solve inference problems — for inference, Bayes' theorem is the correct tool.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[maximum-entropy-principle]] — uses
- [[maximum-entropy-principle]] — instantiates: ML fitting of an exponential family equals maxent under empirical-moment constraints.
- [[entropy]] — analogous-to: Maximum-entropy distributions under moment constraints are exponential families, the maxent counterpart of the ML fit.
- [[lagrange-multipliers]] — uses: The maxent side of the duality derives the exponential form via one Lagrange multiplier per moment constraint.
- [[sufficient-statistics]] — uses: The empirical feature-averages that ML must match are the sufficient statistics of the exponential family.
- [[maximum-likelihood-estimation]] — specializes: The moment-matching condition is the ML estimating equation specialized to the exponential family.
[To be populated during integration]