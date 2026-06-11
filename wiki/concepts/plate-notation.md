---
aliases: []
also_type: []
applies:
- dag-factorization
- directed-graphical-models
- probabilistic-graphical-models
- bayesian-networks
- hierarchical-bayesian-models
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
- probabilistic-graphical-models
- machine-learning
extends:
- bayesian-networks
id: pkis:concept:plate-notation
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- bishop-prml-ch08
- murphy-pml1-intro-ch03
- murphy-pml2-advanced-ch04
tags:
- graphical-model
- notation
- iid
- Bayesian-network
- replication
title: Plate Notation
understanding: 0
uses:
- hierarchical-bayesian-models
- exchangeability
---

## Definition
**Plate notation** is a graphical shorthand for directed graphical models with repeated structure: a rectangular box (plate) labelled $N$ encloses a representative node $x_n$, indicating that there are $N$ i.i.d. copies of that node (and of any local structure inside the plate).

Instead of drawing $N$ identical subgraphs, a single plate compresses the representation; the label specifies the replication count.

### Why it matters
Plate notation is the standard compact representation used throughout modern probabilistic modelling literature (Bayesian networks, hierarchical models, VAEs, etc.). It makes model structure legible at a glance and maps directly onto vectorised probabilistic programming code. Parameters shared across all replicates (e.g., $\mathbf{w}$ in Bayesian regression) are drawn outside the plate, immediately conveying the conditional independence structure $p(t_1,\ldots,t_N,\mathbf{w}) = p(\mathbf{w})\prod_n p(t_n|\mathbf{w})$.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[bayesian-networks]] — extends
- [[hierarchical-bayesian-models]] — applies
- [[exchangeability]] — uses
- [[bayesian-networks]] — applies
- [[probabilistic-graphical-models]] — applies
- [[hierarchical-bayesian-models]] — uses
- [[directed-graphical-models]] — applies
- [[dag-factorization]] — applies
[To be populated during integration]