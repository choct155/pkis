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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- statistical-learning
id: pkis:concept:latent-structure-projection
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch02
specializes:
- latent-variable-models
tags:
- latent-variable
- bidirected-edge
- semi-markovian
- verma-projection
- structure-learning
title: Latent Structure Projection
understanding: 0
---

## Definition
A canonical, finite normal form for latent-variable causal structures that makes causal discovery with unobserved confounders tractable. When Nature hides variables, the observed distribution P-hat need no longer be stable relative to the observable set O, and the space of compatible latent structures is unbounded. The projection theorem (Verma 1993) tames this: for every latent structure L there exists a dependency-equivalent *projection* L[O] in which every unobservable node is a parentless root with exactly two observed, nonadjacent children -- and at least one projection always exists. Such a projection is drawn as a *bidirected graph* over only the observed variables, where each bidirected link a<->b stands for an implicit shared hidden cause a<-L->b. This reduces the search from an infinite space of latent DAGs to graphs of finite, well-defined structure, and renders the semantic definition of inferred causation operational: a distinguished link in the projection of any minimal model of P-hat signals a causal path in every minimal model, and these links are recoverable by the IC* algorithm. The construction underlies the marked-pattern edge taxonomy and the modern treatment of semi-Markovian causal models. A caveat noted by Verma-Pearl: some latent structures impose *numerical* (non-independence) constraints -- later termed dormant independencies (Tian-Pearl 2002, Shpitser-Pearl 2008) -- so projection captures the independence-equivalence class but not every observable constraint.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[latent-variable-models]] — specializes: A projection is a canonical two-children-root normal form of a latent-variable causal model.
[To be populated during integration]