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
- causal-inference
- statistics
id: pkis:technique:iptw-estimator
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- propensity-score
- weighting
- ATE
- confounding
- double-robustness
title: Inverse Probability of Treatment Weighting (IPTW)
understanding: 0
---

## Definition
Given treatment $A \in \{0,1\}$, outcome $Y$, covariates $X$, and propensity score $g(x)=P(A=1|X=x)$, the **IPTW estimator** of the ATE exploits the identity
$$\tau = \mathbb{E}\!\left[\frac{YA}{g(X)} - \frac{Y(1-A)}{1-g(X)}\right]$$
to define
$$\hat{\tau}^{\text{IPTW}} \triangleq \frac{1}{n}\sum_i \frac{Y_i A_i}{\hat{g}(X_i)} - \frac{Y_i(1-A_i)}{1-\hat{g}(X_i)},$$
where $\hat{g}$ is estimated by any proper-scoring-rule supervised learner (e.g., logistic regression, gradient boosting).

The self-normalised (Hajek) version is $\hat{\tau}^{\text{h-IPTW}} \triangleq \bar{Y}_1^w - \bar{Y}_0^w$ where each group mean is weighted by $1/\hat{g}$ or $1/(1-\hat{g})$ and normalised.

### Why it matters
IPTW re-weights observations so that the empirical distributions of $X$ in the treated and control groups match the marginal $P(X)$, removing confounding bias without requiring a model for the outcome. Its consistency relies on correct specification of $g$, whereas outcome regression relies on correct specification of $Q(a,x)=\mathbb{E}[Y|A=a,X=x]$. These complementary requirements motivate doubly robust estimators.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]