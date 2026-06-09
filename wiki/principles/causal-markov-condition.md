---
aliases: []
also_type: []
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- causal-analysis
- bayesian-stats
- knowledge-representation
id: pkis:principle:causal-markov-condition
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- pearl-causality-ch02
tags:
- markov-condition
- screening-off
- common-cause
- reichenbach
- independent-disturbances
- interactive-fork
title: Markov Condition (Causal Markov Assumption)
understanding: 0
---

## Definition
The assumption that, in a complete causal model, each variable is independent of all its nondescendants given its parents (direct causes). It follows from Pearl's definition of a causal model: assigning each X_i a mechanism x_i=f_i(pa_i,u_i) with mutually *independent* disturbances u_i renders the model Markovian (Theorem 1.4.1). The condition encodes Reichenbach's common-cause principle and its corollaries: 'no correlation without causation', 'causes screen off their effects', 'no action at a distance'. Pearl treats it as a *convention demarcating complete from incomplete models* rather than a law of Nature: aggregating microscopic detail into macroscopic variables introduces disturbances, and a parent set PA_i is deemed complete only when no omitted cause influences two modeled variables at once; if it does, the shared disturbance breaks the Markov property and must be promoted to an explicit *latent* node, restoring it. Alleged macroscopic counterexamples (Cartwright, Lemmer) are, Pearl argues, interactive forks (Salmon) reducible to Markovian latent structures -- the interactive fork of Fig 2.6(a) is emulated by the latent structure of Fig 2.6(b), observationally and experimentally indistinguishable -- and they propose no alternative model from which interventions could be predicted. Only quantum phenomena exhibit genuinely non-latent associations. The condition is the object minimized in inferred-causation semantics and is also implicit in the Bayesian discovery approach via parameter independence.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]