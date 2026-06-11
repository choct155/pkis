---
aliases: []
also_type: []
applies:
- distribution-shift
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
contrasts-with:
- multitask-learning
- meta-learning
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- machine-learning
id: pkis:framework:domain-generalization
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch19
tags:
- distribution-shift
- transfer-learning
- robustness
- out-of-distribution-generalization
title: Domain Generalization
understanding: 0
uses:
- hierarchical-bayesian-models
---

## Definition
Domain generalization (DG) trains a predictor on labeled data from $J$ source distributions (environments) $\{D^j\}_{j=1}^J$ so that it generalizes to an unseen target distribution $D^{J+1}$, with *no* labeled or unlabeled target data available at training time.

### Why it matters
Many real deployments face distribution shifts that cannot be anticipated at training time. DG formalizes this by assuming the target environment is one of infinitely many possible draws from a meta-distribution over environments, modeled hierarchically (e.g., population-level parameters shared across all $J+1$ environments). Methods include IRM, CORAL, GroupDRO, and vanilla ERM pooled across all environments.

### Empirical findings
Benchmark studies (DomainBed) have found that well-tuned ERM pooled across source domains is competitive with or superior to specialized DG algorithms on most benchmarks.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[meta-learning]] — contrasts-with
- [[hierarchical-bayesian-models]] — uses
- [[multitask-learning]] — contrasts-with
- [[distribution-shift]] — applies
[To be populated during integration]