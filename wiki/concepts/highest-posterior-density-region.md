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
- frequentist-confidence-interval
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- bayesian-statistics
- statistics
id: pkis:concept:highest-posterior-density-region
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch03
specializes:
- credible-interval
tags:
- HPD
- HDI
- credible-interval
- posterior-summary
- uncertainty-quantification
title: Highest Posterior Density (HPD) Region
understanding: 0
uses:
- posterior-geometry-coordinate-systems
---

## Definition
The $100(1-\alpha)\%$ **highest posterior density (HPD) region** is the smallest set $C_\alpha$ such that
$$\int_{C_\alpha} p(\theta|D)\,d\theta = 1-\alpha,\quad C_\alpha=\{\theta : p(\theta|D)\geq p^*\}$$
where $p^*$ is the largest threshold satisfying the coverage constraint.

In one dimension the HPD region is called a **highest density interval (HDI)**. Every point inside $C_\alpha$ has higher posterior density than every point outside; this is the defining property that distinguishes it from a central credible interval.

### Why it matters
For skewed or multimodal posteriors, the HPD region is narrower than the central interval while maintaining the same probability mass, and it has the direct Bayesian interpretation that the true parameter lies in the region with probability $1-\alpha$ given the observed data. This contrasts with the frequentist confidence interval, whose coverage statement is about repeated-sampling properties, not the specific observed dataset.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[posterior-geometry-coordinate-systems]] — uses
- [[frequentist-confidence-interval]] — contrasts-with
- [[credible-interval]] — specializes
[To be populated during integration]