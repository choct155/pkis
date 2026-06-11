---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
contrasts-with:
- late-iv
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- econometrics
- causal-inference
- statistics
id: pkis:concept:two-stage-least-squares
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
specializes:
- additive-unobserved-confounding
tags:
- instrumental-variables
- linear-model
- weak-instruments
- economics
- regression
title: Two-Stage Least Squares (2SLS)
understanding: 0
uses:
- instrumental-variables
- linear-regression
---

## Definition
Under the linear IV model
$$A_i = \alpha_0 + \alpha Z_i + \delta_A X_i + \xi_i^A, \qquad Y_i = \beta_0 + \beta A_i + \delta_Y X_i + \xi_i^Y,$$
the average treatment effect $\beta$ equals the ratio of the instrument-outcome coefficient to the instrument-treatment coefficient:
$$\hat{\beta}^{\text{2SLS}} = \frac{\hat{\beta\alpha}}{\hat{\alpha}}.$$
Practically, 2SLS is implemented by (1) regressing $A$ on $Z, X$ and taking fitted values $\hat{A}$; (2) regressing $Y$ on $\hat{A}, X$; the coefficient on $\hat{A}$ is $\hat{\beta}$.

### Why it matters
2SLS is the classical estimator for linear IV models and remains ubiquitous in economics. However, it requires linearity of both structural equations—an assumption that is hard to verify and frequently violated. Weak instrument relevance ($|\hat{\alpha}|$ small) causes standard errors to be severely underestimated, yielding spuriously significant estimates. Modern practice favors non-parametric IV or LATE-based approaches (see LATE-IV and additive-unobserved-confounding nodes) when linearity is doubtful.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[additive-unobserved-confounding]] — specializes
- [[late-iv]] — contrasts-with: 2SLS requires linearity; LATE requires monotonicity—complementary assumptions
- [[linear-regression]] — uses
- [[instrumental-variables]] — uses
[To be populated during integration]