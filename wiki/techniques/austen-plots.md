---
aliases: []
also_type: []
applies:
- confounding
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
id: pkis:technique:austen-plots
instantiates:
- sensitivity-analysis
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- sensitivity-analysis
- unobserved-confounding
- partial-R2
- observational-study
- bias
title: Austen Plots for Sensitivity Analysis
understanding: 0
uses:
- propensity-score
- aiptw-double-ml
---

## Definition
Austen plots (Veitch & Zaveri 2020) provide a non-parametric sensitivity analysis for unobserved confounding in observational studies. The sensitivity model posits
$$\tilde{g}(X,U)|X \sim \text{Beta}(g(X)(1/\alpha-1),\;(1-g(X))(1/\alpha-1))$$
$$\mathbb{E}[Y|A,X,U] = Q(A,X) + \delta\big(\mathrm{logit}\,\tilde{g}(X,U) - \mathbb{E}[\mathrm{logit}\,\tilde{g}(X,U)|A,X]\big),$$
where $\alpha \in [0,1]$ is the treatment-assignment influence of $U$ (equal to the partial $R^2$ of $U$ on $A$ given $X$) and $\delta$ governs outcome influence (reparameterised via partial $R^2_{Y,\text{par}}$). The induced bias is
$$\text{bias} = \frac{\delta}{1/\alpha - 1}\,\mathbb{E}\!\left[\frac{1}{g(X)}+\frac{1}{1-g(X)}\right].$$

The plot displays the iso-bias curve in $(\alpha, R^2_{Y,\text{par}})$ space alongside dots marking the measured influence of observed covariates, allowing domain experts to judge whether plausible unobserved confounders could overturn the study conclusion.

### Why it matters
Austen plots decouple sensitivity analysis from the observed-data modeling step: any ML estimator may be used for $\hat{Q}$ and $\hat{g}$, avoiding the parametric restrictions of classical approaches (e.g., Imbens' logistic/linear model). The partial-$R^2$ parameterisation is scale-free and directly calibratable against observed covariates.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[aiptw-double-ml]] — uses: Austen plots are compatible with any ML-based estimator for Q and g
- [[confounding]] — applies
- [[propensity-score]] — uses
- [[sensitivity-analysis]] — instantiates
[To be populated during integration]