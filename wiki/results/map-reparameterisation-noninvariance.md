---
aliases: []
also_type: []
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
- bayesian-inference
- statistical-estimation
id: pkis:result:map-reparameterisation-noninvariance
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch07
tags:
- MAP
- reparameterisation
- invariance
- change-of-variables
- point-estimation
title: MAP Estimate Non-Invariance Under Reparameterisation
understanding: 0
---

## Definition
Let $\hat{x} = \arg\max_x p_x(x)$ and $y = f(x)$ a smooth bijection. In general
$$\arg\max_y p_y(y) \neq f(\hat{x})$$
because the change-of-variables Jacobian $|df^{-1}/dy|$ deforms the density, shifting the mode.

### Why it matters
MAP estimation is not a coordinate-free operation: different parameterisations of the same model yield different point estimates, undermining the claim that MAP is a natural summary of the posterior. By contrast, (i) the MLE is invariant because it optimises a likelihood function (not a density), and (ii) full Bayesian posteriors are invariant because integration absorbs the Jacobian. This result motivates using the full posterior or, at minimum, working in a natural (e.g., unconstrained) parameterisation when applying Laplace or ADVI.

### Contrast with full Bayes
When computing posterior expectations $\mathbb{E}[g(\theta)|D]$, the change of variables is automatically accounted for by the integration measure, so results are parameterisation-invariant.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]