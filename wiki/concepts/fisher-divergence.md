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
- information-theory
- machine-learning
id: pkis:concept:fisher-divergence
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch24
tags:
- score-matching
- divergence
- information-geometry
- EBM
title: Fisher Divergence
understanding: 0
---

## Definition
$$D_F(p \| q) = E_{p(x)}\!\left[\frac{1}{2}\|\nabla_x \log p(x) - \nabla_x \log q(x)\|^2\right]$$

The Fisher divergence (also called relative Fisher information) measures the discrepancy between two distributions via their score functions rather than their densities. It is $\geq 0$ with equality iff $p = q$ (under regularity conditions).

### Why it matters
Fisher divergence is the objective minimised by score matching—its key advantage being that the intractable normalizing constant cancels. It is related to KL divergence through de Bruijn's identity: $\tfrac{d}{dt}D_{KL}(q_t\|p_t) = -\tfrac{1}{2}D_F(q_t\|p_t)$, which links score matching (minimising $D_F$) to contrastive divergence (approximately minimising $D_{KL}$). Fisher divergence also underlies Langevin dynamics convergence analysis.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]