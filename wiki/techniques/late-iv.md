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
- additive-unobserved-confounding
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- causal-inference
- econometrics
- statistics
id: pkis:technique:late-iv
instantiates:
- local-average-treatment-effect
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
tags:
- instrumental-variables
- non-compliance
- monotonicity
- compliers
- causal-identification
title: Local Average Treatment Effect (LATE) via IV
understanding: 0
uses:
- instrumental-variables
- aiptw-double-ml
---

## Definition
Given a binary instrument $Z$, binary treatment $A$, and outcome $Y$, the **Local Average Treatment Effect** (LATE, also *Complier Average Causal Effect*) is defined as
$$\text{LATE} = \mathbb{E}[Y|\mathrm{do}(A=1),\text{complier}] - \mathbb{E}[Y|\mathrm{do}(A=0),\text{complier}],$$
where *compliers* are units who take treatment iff assigned ($A_i(Z=1)=1, A_i(Z=0)=0$).

Under the IV assumptions (relevance, unconfoundedness, exclusion restriction) and **instrument monotonicity** (no defiers), LATE is identified as
$$\tau^{\text{LATE}} = \frac{\mathbb{E}[\mathbb{E}[Y|X,Z=1]-\mathbb{E}[Y|X,Z=0]]}{\mathbb{E}[P(A=1|X,Z=1)-P(A=1|X,Z=0)]},$$
the ratio of the reduced-form effect (instrument$\to$outcome) to the first-stage effect (instrument$\to$treatment). A double-ML estimator using cross-fitted nuisance functions $\hat{\mu}(z,x)$, $\hat{m}(z,x)$, $\hat{p}(x)$ achieves $\sqrt{n}$-asymptotic normality under the product-rate condition.

### Why it matters
LATE extends IV identification to settings with heterogeneous treatment effects and without functional-form assumptions, at the cost of estimating only a sub-population effect (compliers). It is the standard target in randomised trials with non-compliance and in natural-experiment designs (e.g., judge fixed effects).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[additive-unobserved-confounding]] — contrasts-with: LATE uses monotonicity while additive confounding uses no-interaction; both supplement IV assumptions
- [[aiptw-double-ml]] — uses: Double-ML LATE estimator uses same cross-fitting and influence-function approach
- [[local-average-treatment-effect]] — instantiates
- [[instrumental-variables]] — uses
[To be populated during integration]