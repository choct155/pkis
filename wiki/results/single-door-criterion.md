---
aliases: []
also_type: []
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- econometrics
id: pkis:result:single-door-criterion
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch05
tags:
- identification
- d-separation
- direct-effect
- regression
- linear-sem
title: Single-Door Criterion for Direct Effects
understanding: 0
---

## Definition
Pearl's Theorem 5.3.1. Let G be a path diagram in which alpha is the path coefficient on the link X->Y, and let G_alpha be G with that edge deleted. The coefficient alpha is identifiable if there exists a set Z of variables such that (i) Z contains no descendant of Y, and (ii) Z d-separates X from Y in G_alpha; then alpha equals the partial regression coefficient r_YX.Z (i.e., the coefficient of X in the regression of Y on X and Z). Conversely, if Z fails these conditions, r_YX.Z is not a consistent estimand of alpha (except on a measure-zero set). This gives a purely graphical answer to two classical SEM questions — what constitutes an adequate set of regressors, and when a regression coefficient consistently estimates a path coefficient. It differs from the back-door criterion in that Z must block ALL paths from X to Y in G_alpha (including indirect ones), not only back-door paths; it identifies a direct effect rather than a total effect.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]