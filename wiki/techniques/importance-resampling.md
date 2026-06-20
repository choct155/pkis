---
aliases: []
also_type: []
component_scores:
  alternatives: null
  conditions: null
  diagnostics: null
  failure_modes: null
  implementation: null
  operational_mechanism: null
  principled_mechanism: null
contrasts-with:
- rejection-sampling
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-20'
domain:
- bayesian-stats
- statistical-learning
extends:
- importance-sampling
id: pkis:technique:importance-resampling
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- gelman-bda3-ch10
- tanner-tools-statistical-inference-ch05
tags:
- monte-carlo
- sampling
- importance-weights
- resampling
- without-replacement
- posterior-inference
title: Importance Resampling (SIR)
understanding: 0
uses:
- importance-sampling
---

## Definition
A method for converting a weighted importance sample into an (approximately) equal-weight, independent sample from the target. Given S draws omega^1,...,omega^S from an approximate density g together with their importance weights w(omega^s) = q(omega^s|y)/g(omega^s), one draws k < S of them with probability proportional to the weights. Gelman, Carlin, Stern, Dunson, Vehtari, and Rubin (BDA3, ch. 10.4) recommend sampling WITHOUT replacement: when a few weights dominate, sampling with replacement repeatedly picks the same few points, whereas sampling without replacement yields a more desirable intermediate distribution between the proposal g and the target p. The resulting equal-weight sample is useful when downstream calculations require iid-like structure, e.g. as starting points for an iterative (MCMC) simulation, or for approximating mild modifications of a posterior (replacing a normal by a t in the 8-schools model, or leave-one-out cross-validation) by treating the original posterior as an approximation to the modified one. Introduced by Rubin (1987); for k = S, stratified/deterministic (Kitagawa) and residual (Liu) resampling have lower variance than simple random resampling.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[rejection-sampling]] — contrasts-with: Both yield (approximately) equal-weight samples but via resampling vs. accept/reject.
- [[importance-sampling]] — uses: Resampling probabilities are the importance weights.
- [[importance-sampling]] — extends: SIR turns weighted importance samples into approximately equal-weight independent draws.
[To be populated during integration]