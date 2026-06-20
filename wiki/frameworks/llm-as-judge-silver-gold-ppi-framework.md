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
id: pkis:framework:llm-as-judge-silver-gold-ppi-framework
knowledge_type: framework
linked_nodes: []
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- angelopoulos-predictionpowered-2023
- angelopoulos-ppi-2023
- saadfalcon-ares-2024
tags:
- evaluation
- LLM-judge
- silver-gold
- PPI
- cost-reduction
- measurement
- continuous-assessment
title: LLM-as-Judge Silver/Gold Calibration Framework (PPI)
understanding: 0
---

## Definition
A general-purpose measurement architecture for reducing the cost of continuous quality assessment in any system where ground truth is expensive to obtain but machine predictions are cheap. The framework separates the measurement problem into two components: a high-volume silver signal from an automated judge (LLM, model, or heuristic) and a small gold set of human-verified labels used to measure and correct the judge's systematic error.

## Core Structure

**Silver signal**: Large-scale automated judgments. Cheap, scalable, systematically biased. Source: LLM-as-a-judge, model predictions, heuristic classifiers.

**Gold set**: Small human-annotated sample drawn from the same population. Expensive, assumed reliable, used exclusively for bias estimation — not for direct metric computation.

**Statistical framework**: Prediction-Powered Inference (PPI / PPI++, Angelopoulos et al. 2023). The gold set measures the silver judge's systematic error. That error is subtracted from the silver-based estimate to produce a provably unbiased metric with variance reduced by the silver sample size. Each additional silver judgment reduces variance without introducing new bias. The power-tuning coefficient λ in PPI++ guarantees the combined estimator is never worse than the gold-only baseline.

## Formal Estimator

Let μ be the true metric value, f(X) the silver judge prediction, Y the gold label:

θ_PPI = (1/n) Σ_gold Y_i  −  (1/N) Σ_silver f(X_i)  +  (1/N) Σ_silver f(X_i)  [corrected for bias]

More precisely (PPI++): θ_PPI++ = mean(Y_gold) − λ·(mean(f(X_gold)) − mean(f(X_silver)))

where λ is chosen to minimize variance. When λ=0: gold-only estimator. When λ=1: standard PPI. PPI++ adapts λ from pilot data.

## Key Properties

- Provably unbiased regardless of silver judge quality (as long as gold set is unbiased)
- Variance reduction proportional to silver sample size — more silver = tighter CIs, no new bias
- Never worse than gold-only estimator (PPI++ guarantee)
- Works for any metric expressible as an expectation over instance-level judgments
- Extends to sub-instance annotations (PRECISE extension for ranking metrics like Precision@K)

## Cost Reduction Profile

Empirical findings across applications:
- PRECISE: 95% cost reduction with N_gold=30 and N_silver=3,000 vs N_silver=60,000
- RocketEval: 50x cost reduction with small fine-tuned judge (0.965 correlation with GPT-4o)
- ARES: valid evaluation with a few hundred human annotations across eight knowledge-intensive tasks

## Applications in This Research Program

**Accuracy dimension**: Silver = LLM binary extraction judgment. Gold = human verification of extraction correctness. PPI++ debiases the LLM-based accuracy estimate at scale. See accuracy estimation computational brief.

**Retrieval quality dimensions (Coverage, Concision, Groundedness, Structural Coherence, Structural Relevance)**: Silver = LLM judgment on each dimension per retrieved set. Gold = expert annotation of the same sample. PPI++ produces unbiased dimension scores continuously.

**Hardening signal calibration**: Silver = traversal frequency and Reliability(τ) from logs. Gold = human validation of edge quality on a sample. PPI++ estimates how well the log-based signal tracks true edge reliability.

**Ontology quality assessment**: Silver = automated structural checks (inseparability, class granularity). Gold = ontologist review on a sample. PPI++ calibrates the automated signal.

## Why This Is Load-Bearing

Without this framework, continuous quality assessment requires either: (a) human annotation of every judgment — operationally infeasible at scale, or (b) pure automated assessment — systematically biased with no correction mechanism. PPI++ is the bridge: it makes automated assessment statistically valid by anchoring it to a small but persistent gold investment. The gold set is not wasted — it is the calibration instrument that makes all silver estimates trustworthy.

## Relationship to Gödel / Measurement Architecture

The silver signal cannot be self-certifying — it requires external grounding. The gold set provides that external anchor. PPI++ makes the anchor as small as possible while preserving statistical validity. This is the operational resolution to the measurement circularity problem identified in the C(q) estimation bridge note.

## Open Questions

- What is the minimum gold set size required per quality dimension for the PPI++ CI to be actionable (< ±0.03)?
- How frequently does the gold set need refreshing as the silver judge's error distribution shifts (concept drift)?
- Can the gold set be shared across multiple quality dimensions or does each require independent annotation?
- What is the optimal allocation of a fixed annotation budget across dimensions given their different variance profiles?

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]