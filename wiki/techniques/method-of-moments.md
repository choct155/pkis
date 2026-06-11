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
- statistics
id: pkis:technique:method-of-moments
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch04
tags:
- moments
- parameter-estimation
- consistency
- initialisation
title: Method of Moments (MOM)
understanding: 0
---

## Definition
$$\hat{\mu}_k = \frac{1}{N}\sum_{n=1}^{N} y_n^k, \qquad \text{solve } \mu_k(\theta) = \hat{\mu}_k \text{ for } k = 1,\ldots,K$$

MOM equates the first $K$ theoretical moments of the model to their empirical counterparts and solves the resulting system of equations for the $K$ unknown parameters.

### Why it matters
MOM is computationally simpler than MLE because it avoids optimising the NLL, which may lack a closed form. It is consistent but generally less statistically efficient than MLE (higher asymptotic variance). A key use case is initialising iterative MLE algorithms (e.g., EM for mixture models). MOM can occasionally produce inadmissible estimates (e.g., estimated support outside observed data range for the uniform distribution), a failure mode not shared by MLE.

### Limitations
For the Uniform$(\theta_1, \theta_2)$ distribution, MOM can yield $\hat{\theta}_2 < \max_n y_n$, which is logically inconsistent. The MLE instead uses order statistics: $\hat{\theta}_1 = y_{(1)},\, \hat{\theta}_2 = y_{(N)}$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]