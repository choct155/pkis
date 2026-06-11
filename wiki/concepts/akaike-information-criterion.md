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
date_updated: '2026-06-11'
domain:
- statistics
- machine-learning
- model-selection
id: pkis:concept:akaike-information-criterion
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch05
tags:
- model-selection
- information-criterion
- AIC
- KL-divergence
- prediction
title: Akaike Information Criterion (AIC)
understanding: 0
---

## Definition
$$L_{\text{AIC}}(m) = -2\log p(D|\hat{\theta},m) + 2D_m$$

where $D_m$ is the number of free parameters. Derived from a frequentist approximation to the expected out-of-sample KL divergence (Kullback–Leibler divergence from the true model to the fitted model).

### Why it matters
AIC penalises model complexity less heavily than BIC (the penalty is $2D_m$ vs $D_m\log N$), so it tends to select larger models, especially for moderate $N$. Unlike BIC, AIC is not consistent (it does not converge to the true model) but it is **efficient** — it asymptotically selects the model that minimises prediction error when the true model is not in the candidate set. The AIC/BIC trade-off captures the broader bias–variance trade-off: AIC prioritises predictive accuracy; BIC prioritises parsimony.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]