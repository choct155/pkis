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
- machine-learning
id: pkis:technique:partition-function-chaining
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch11
tags:
- partition-function
- bayesian-model-comparison
- importance-sampling
- thermodynamic-integration
title: Partition Function Estimation by Chaining
understanding: 0
---

## Definition
To estimate the normalisation constant $Z_M$ of a complex distribution $p_M(z) \propto \exp(-E_M(z))$, introduce a sequence of intermediate distributions $p_1, p_2, \ldots, p_M$ with interpolating energies
$$E_\alpha(z) = (1-\alpha)E_1(z) + \alpha E_M(z), \quad \alpha \in [0,1],$$
where $Z_1$ is analytically known. The target partition function is obtained via telescoping:
$$\frac{Z_M}{Z_1} = \frac{Z_2}{Z_1}\cdot\frac{Z_3}{Z_2}\cdots\frac{Z_M}{Z_{M-1}},$$
with each ratio estimated by importance sampling or MCMC on adjacent distributions.

### Why it matters
Direct estimation of $Z_M/Z_1$ by importance sampling fails when the two distributions are very different. Chaining reduces the problem to a sequence of easier ratio estimates between closely matched neighbours. This is the computational basis for thermodynamic integration and annealed importance sampling used in Bayesian model comparison.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]