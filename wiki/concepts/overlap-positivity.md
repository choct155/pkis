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
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-20'
domain:
- causal-inference
- statistics
id: pkis:concept:overlap-positivity
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- average-treatment-effect
related_concepts: []
sources:
- murphy-pml2-advanced-ch36
- cunningham-causal-inference-mixtape-ch06
tags:
- positivity
- propensity-score
- identification
- ATE
- overlap
title: Overlap (Positivity) Condition
understanding: 0
uses:
- propensity-score
---

## Definition
A distribution $P$ on $(A, X)$ satisfies **overlap** (also called *positivity*) if
$$0 < P(A = 1 \mid X = x) < 1 \quad \forall x \in \mathrm{supp}(X).$$
**Strict overlap** strengthens this to
$$\epsilon < P(A = 1 \mid X = x) < 1 - \epsilon \quad \text{for some } \epsilon > 0.$$

Intuitively, every unit in the population must have a positive probability of receiving either treatment or control given their covariates.

### Why it matters
Overlap is a necessary condition for non-parametric identification of the ATE via confounder adjustment: the estimand $\tau = \mathbb{E}[\mathbb{E}[Y|A=1,X] - \mathbb{E}[Y|A=0,X]]$ is undefined at strata $x$ where $P(A=a|X=x)=0$. Practically, near-violations cause the IPTW variance to explode (terms $1/g(X)$ and $1/(1-g(X))$ become large), inflating confidence intervals and potentially misleading point estimates. Checking estimated propensity scores for extreme values is a standard diagnostic.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[propensity-score]] — uses: Overlap is checked via estimated propensity scores; violations manifest as extreme weights
- [[average-treatment-effect]] — prerequisite-of: Overlap is required for non-parametric identification of the ATE
[To be populated during integration]