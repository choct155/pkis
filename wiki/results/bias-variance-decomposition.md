---
aliases: []
also_type: []
applies:
- linear-basis-function-model
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
- statistics
extends:
- bias-variance-tradeoff
id: pkis:result:bias-variance-decomposition
instantiates:
- mean-square-value-error
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch03
tags:
- overfitting
- model-complexity
- frequentist
- expected-loss
title: Bias-Variance Decomposition of Expected Squared Loss
understanding: 0
uses:
- overfitting-and-underfitting
- regularization
---

## Definition
For a squared-loss regression problem, the expected loss decomposes as:

$$\mathbb{E}[L] = (\text{bias})^2 + \text{variance} + \text{noise}$$

$$(\text{bias})^2 = \int \{\mathbb{E}_{\mathcal{D}}[y(x;\mathcal{D})] - h(x)\}^2 p(x)\,dx$$

$$\text{variance} = \int \mathbb{E}_{\mathcal{D}}[\{y(x;\mathcal{D}) - \mathbb{E}_{\mathcal{D}}[y(x;\mathcal{D})]\}^2]\,p(x)\,dx$$

$$\text{noise} = \int \{h(x)-t\}^2 p(x,t)\,dx\,dt$$

where $h(x)=\mathbb{E}[t|x]$ is the regression function (Bayes-optimal predictor) and $y(x;\mathcal{D})$ is the learned predictor on dataset $\mathcal{D}$.

### Why it matters
Provides a frequentist account of the over-fitting phenomenon: high-capacity models have low bias but high variance; regularisation trades one for the other. Motivates ensemble methods (averaging reduces variance) and the Bayesian alternative (posterior averaging avoids the tradeoff by integrating over parameters).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mean-square-value-error]] — instantiates
- [[regularization]] — uses
- [[overfitting-and-underfitting]] — uses
- [[linear-basis-function-model]] — applies
- [[bias-variance-tradeoff]] — extends: Provides the formal mathematical derivation of the bias-variance tradeoff
[To be populated during integration]