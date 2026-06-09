---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- statistical-learning
extends:
- vector-space
id: pkis:concept:analytic-geometry
knowledge_type: concept
maturity: settled
prerequisite-of:
- support-vector-machines
related_concepts:
- '[[linear-algebra]]'
- '[[principal-component-analysis]]'
- '[[support-vector-machines]]'
sources:
- '[[deisenroth-mml]]'
- '[[carrell-groups-matrices-vectors]]'
tags:
- mathematical-foundations
- linear-algebra
title: Analytic Geometry
understanding: 0
---

The geometric structure layered on top of linear algebra via inner products: lengths (norms), distances, angles, orthogonality, and projections — the vocabulary for understanding what optimization algorithms and dimensionality reduction methods are doing geometrically.

## Reading Path
- [[deisenroth-mml]] (unread) — primary treatment: inner products, norms, distances, orthogonality, projections, PCA geometry
- [[carrell-groups-matrices-vectors-ch06]] (unread) — inner product spaces, Hermitian forms, Gram–Schmidt, orthogonal complements
- [[carrell-groups-matrices-vectors-ch07]] (unread) — isometries and orthogonal mappings, projections, reflections

## Connections
- [[vector-space]] — extends: Ch. 3 adds inner products (norms, angles, distances) on top of the bare vector-space structure of Ch. 2.
- [[support-vector-machines]] — prerequisite-of: MML Ch.1: similarity and distance between vectors (analytic geometry, Ch.3) underpin the classification pillar; inner products / margins are the geometric basis for SVMs (Ch.12).