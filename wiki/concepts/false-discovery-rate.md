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
- statistical-learning
- bayesian-stats
id: pkis:concept:false-discovery-rate
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- hastie-esl-ch18
tags:
- multiple-testing
- fdr
- benjamini-hochberg
- feature-selection
- genomics
title: False Discovery Rate (FDR)
understanding: 0
---

## Definition
An error criterion for large-scale multiple hypothesis testing: FDR = E(V/R), the expected proportion of false rejections V among the R hypotheses called significant (with V/R taken as 0 when R=0). Unlike the family-wise error rate (FWER = Pr(V ≥ 1)), which controls the probability of any false positive and becomes crippling for large M, the FDR controls the expected fraction of mistakes among discoveries, making it far less conservative and well suited to screening thousands of genes. The Benjamini–Hochberg (BH) procedure orders the p-values p_(1) ≤ ··· ≤ p_(M), finds L = max{j : p_(j) < α·j/M}, and rejects the L smallest; under independence it guarantees FDR ≤ (M0/M)α ≤ α. An equivalent plug-in / permutation estimate is FDR̂ = Ê(V)/Ê(R), working directly with the test statistics rather than p-values. The positive FDR, pFDR = E(V/R | R>0), has a clean Bayesian reading: pFDR(Γ) = Pr(H0 true | statistic falls in rejection region Γ) under a two-group mixture t_j ~ π₀F₀ + (1−π₀)F₁. Localized versions — the q-value (smallest FDR over rejection regions rejecting t_j) and the local FDR Pr(Z_j=0 | t_j=t₀) — give per-feature significance.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]