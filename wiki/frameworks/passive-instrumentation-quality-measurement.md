---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-20'
date_updated: '2026-06-20'
domain:
- bayesian-stats
- knowledge-representation
id: pkis:framework:passive-instrumentation-quality-measurement
knowledge_type: framework
linked_nodes: []
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- angelopoulos-predictionpowered-2023
- angelopoulos-ppi-2023
tags:
- measurement
- instrumentation
- passive-signal
- quality-assessment
- client-side
- production-side
- cost-reduction
title: Passive Instrumentation Strategy for Quality Measurement
understanding: 0
illustrated-by:
- accuracy-calibration-explainer
---

## Definition
A measurement strategy class that exploits existing production and client-side processes as passive quality measurement instruments, avoiding or minimizing active annotation campaigns. The core principle: identify processes already running in production whose outputs are correlated with latent quality variables, instrument them cheaply, and apply statistical models that connect the observable signal to the quality dimension of interest.

## Motivation

Active annotation campaigns are expensive, slow, and produce point-in-time snapshots. Production systems emit continuous signals correlated with quality that go unmeasured if the instrumentation perimeter is defined too narrowly. The passive instrumentation strategy extends the measurement perimeter to capture these signals, reducing the cost of continuous quality assessment from O(human annotations per time period) to O(instrumentation investment + small periodic gold calibration set).

## General Structure

Every passive measurement instrument has three components:

**Signal source**: a production or client-side process already running, emitting observable outputs at low marginal cost once instrumented. Must be correlated with at least one latent quality dimension.

**Statistical model**: maps the observable signal to the latent quality variable with a known or estimable error structure. Must be estimable from a small gold set and must admit asymptotic verification — consistency, efficiency, valid confidence intervals under standard econometric conditions.

**Instrumentation investment**: the minimal logging, tagging, and pipeline modifications needed to make the signal collectible and interpretable. Often the binding constraint — not the statistical framework but whether the production system emits recoverable signals.

## Signal Inventory

### Production-side signals (data creation layer)

| Signal | Quality dimension | Statistical model | Notes |
|---|---|---|---|
| LLM binary extraction judgment | Accuracy | Confusion matrix + PPI++ | Silver/gold calibration framework |
| Bond attribute revision events | Accuracy (pipeline errors) | NHPP mixture of exponentials | Passive; market participants as annotators |
| Revision revert events | Accuracy (false corrections) | Filter from NHPP signal | Drop reverted revisions as noise |
| Traversal frequency by edge type | Reliability(τ) | Empirical P(ΔCoverage > θ | c1, τ) | Hardening signal for traversal ranking |
| Node retrieval frequency | Coverage gap detection | λ(n,t) hardening weight | Accumulates evidence for hardening |
| LLM confidence scores | Accuracy proxy | Calibration against gold | Cheap but indirect |

### Client-side signals (application layer)

| Signal | Quality dimension | Statistical model | Notes |
|---|---|---|---|
| Query reformulation rate | Coverage | Missing mass estimator on C(q) | User rephrasing = retrieval didn't satisfy C(q) |
| Time-on-task for research workflows | Coherence + Coverage composite | Survival model on task duration | Fast close = well-structured, complete payload |
| Document open rate post-retrieval | Relevance | Logistic regression on open/no-open | High retrieval + low open = ranking wrong |
| Downstream workflow actions | Relevance (highest quality) | Attribution model | Causal attribution hard; partial credit possible |
| Session depth (queries per session) | Coverage | Count model | Deep sessions suggest coverage gaps in early retrievals |
| Explicit feedback (ratings, flags) | Composite | Direct label; PPI++ if sparse | Rare but high-value; use as gold anchor |

## Prioritization Criterion

Instrument production processes that are simultaneously:

1. **High correlation** with load-bearing quality dimensions — instruments that are only weakly correlated with the target dimension produce wide CIs even with large signal volume
2. **Cheap to instrument** — signals already partially logged are preferred; new instrumentation requires engineering investment
3. **Good asymptotic properties** — the statistical model connecting signal to quality variable must converge quickly with small gold sets and produce valid CIs under standard regularity conditions
4. **Causally interpretable** — the signal should have a plausible mechanism connecting it to the quality dimension, not just a correlational relationship that may break under distribution shift

## Instrumentation Design Principle

Application developers make logging decisions based on product requirements. If they don't know that query reformulation rate is a coverage metric and document open rate is a relevance metric, they will log what is convenient for the product dashboard and miss the signals most valuable for quality measurement. Quality measurement requirements must be communicated to application teams as first-class instrumentation requirements — not as a post-hoc analytics request.

This creates a coordination requirement between the measurement team (QMI) and the application development team. The investment is low — adding events to an existing logging pipeline — but the coordination must happen before the application ships, not after.

## Relationship to PPI Framework

Passive signals are the silver layer in the PPI++ framework. Every passive signal source listed above produces cheap, scalable, systematically biased measurements of a quality dimension. The PPI++ calibration step — small gold set estimating the signal's systematic error — is the same across all of them. The passive instrumentation framework and the LLM-as-judge silver/gold framework are instances of the same statistical architecture applied to different signal sources.

## Relationship to Hardening Framework

Client-side signals provide a second hardening channel beyond traversal frequency. Query reformulation events that follow concept-layer traversal are evidence that the traversal did not satisfy C(q) — a negative hardening signal for the traversed edges. Fast task closure after concept-layer retrieval is a positive hardening signal. The hardening weight λ(n,t) should in principle incorporate both production-side and client-side evidence, though the attribution model for client-side signals is more complex.

## Open Questions

- What is the minimum signal volume required for each client-side instrument to produce actionable CIs at the quality dimension level?
- How do you handle the attribution problem for downstream workflow actions — connecting a research action to a specific retrieval event in a multi-step workflow?
- What is the optimal instrumentation investment allocation across signal sources given a fixed engineering budget?
- How do client-side signal distributions shift as the user base evolves, and how does that affect the stability of the statistical models?
- Can the gold calibration set be shared across multiple passive instruments for the same quality dimension, or does each require independent calibration?

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]