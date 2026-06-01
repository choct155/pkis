---
aliases: []
cross_cluster_dependencies:
- structured-validation-truth-discovery
- retrieval-inference-tradeoff
- evaluation-infrastructure
date_created: 2026-05-30
date_updated: '2026-06-01'
domain:
- bayesian-stats
- knowledge-representation
frontier_hypotheses:
- ontological-provenance-enables-conflict-resolution
hypotheses:
- ontological-provenance-enables-conflict-resolution
- source-credibility-as-latent-variable
id: pkis:research-cluster:composite-credibility
knowledge_type: research-cluster
origin: research-program
status: active
tags:
- provenance
- source-credibility
- conflict-resolution
- confidence-calibration
- auditability
title: Composite Credibility
uses:
- bayesian-inference
- probabilistic-graphical-models
- calibration
---

## Thesis
When a composite response draws from multiple sources of varying reliability, ontological provenance — knowing which source contributed which component and what the ontological relationship between components is — enables principled conflict detection, resolution, and confidence communication that heuristic aggregation cannot provide.

## Summary
Conflict resolution requires source credibility weights (learnable from agreement history), the specific property type (some properties are more stable), and temporal context. All of this is ontologically representable and can be formalized as a Bayesian inference over the true value given source reports. The provenance attribution requirement maps directly to auditability as a non-functional requirement.

## Research Program Context
Stage 8 (Result Construction) primary cluster. Strong overlap with Structured Validation & Truth Discovery — both deal with cross-source conflict resolution but at different pipeline stages and granularities.

## Constituent Hypotheses
- **ontological-provenance-enables-conflict-resolution** — Ontological provenance enables more accurate cross-source conflict resolution than heuristic credibility weighting
- **source-credibility-as-latent-variable** — Treating source credibility as a latent variable estimated from agreement patterns produces better-calibrated resolution than static weights

## Current Frontier
Anchored to `bayesian-inference`, `probabilistic-graphical-models`, and `calibration`. Lead hypothesis **`ontological-provenance-enables-conflict-resolution`**: ontological provenance beats heuristic credibility weighting for cross-source conflict resolution. Supporting: **`source-credibility-as-latent-variable`** (credibility as a latent variable from agreement patterns → better calibration than static weights). Coverage gaps: `bayesian-inference`, `probabilistic-graphical-models`, `calibration` are sourceless stubs.

## Connections
- [[calibration]] — uses: evaluating resolution quality requires calibration assessment
- [[probabilistic-graphical-models]] — uses: the truth-discovery literature is rooted in PGMs
- [[bayesian-inference]] — uses: conflict resolution is formalized as Bayesian inference over the true value
- [[bayesian-inference]] — uses: conflict resolution is formalized as Bayesian inference over the true value
- [[probabilistic-graphical-models]] — uses: the truth discovery literature is rooted in PGMs
- [[calibration]] — uses: evaluating resolution quality requires calibration assessment