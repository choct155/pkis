---
aliases: []
also_type: []
analogous-to:
- control-variates
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
- simulation
- numerical-methods
extends:
- monte-carlo-integration
id: pkis:technique:antithetic-sampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch11
specializes:
- quasi-monte-carlo
tags:
- variance-reduction
- negative-correlation
- paired-samples
- MC-efficiency
title: Antithetic Sampling
understanding: 0
---

## Definition
For each base sample $u_i\sim\text{Unif}(0,1)$, form the antithetic pair $u'_i=1-u_i$; the estimator averages $f(u_i)$ and $f(u'_i)$:
$$\hat{\theta}_{anti} = \frac{1}{2N}\sum_{i=1}^N [f(u_i)+f(u'_i)]$$

Variance is reduced relative to $2N$ independent samples when $\text{Cov}[f(u),f(1-u)]<0$, i.e., when $f$ is monotone.

### Why it matters
Exploits the negative correlation between paired samples to reduce variance at zero extra computational cost beyond function evaluations. Particularly effective for monotone integrands. Can achieve similar variance reduction to control variates without requiring knowledge of a correlated baseline function.

### Connection to QMC
Antithetic sampling is a simple special case of the broader idea behind quasi-Monte Carlo: constructing negatively correlated or space-filling sample sequences to reduce estimator variance below the $O(1/\sqrt{N})$ i.i.d. rate.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[quasi-monte-carlo]] — specializes
- [[control-variates]] — analogous-to
- [[monte-carlo-integration]] — extends
[To be populated during integration]