---
aliases: []
also_type: []
analogous-to:
- fisher-neyman-factorization
component_scores:
  conditions: null
  implications: null
  limitations: null
  proof_sketch: null
  statement: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- information-theory
- statistics
extends:
- sufficient-statistics
id: pkis:result:minimal-sufficient-statistic-dpi
knowledge_type: result
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml1-intro-ch06
tags:
- sufficient-statistic
- data-processing-inequality
- compression
- parameter-inference
title: Minimal Sufficient Statistic via Data Processing Inequality
understanding: 0
uses:
- data-processing-inequality
- mutual-information
---

## Definition
Given the Markov chain $\theta \to \mathcal{D} \to s(\mathcal{D})$, statistic $s$ is **sufficient** iff $\mathbb{I}(\theta; s(\mathcal{D})) = \mathbb{I}(\theta; \mathcal{D})$, i.e., no information about $\theta$ is lost. It is **minimal sufficient** if additionally it is a function of every other sufficient statistic:
$$\theta \to s(\mathcal{D}) \to s'(\mathcal{D}) \to \mathcal{D}$$
so $s$ maximally compresses $\mathcal{D}$ without losing information relevant to $\theta$.

This is a direct consequence of the data processing inequality: any further deterministic transformation $s'$ of the data can only decrease (or maintain) MI with $\theta$.

### Why it matters
The information-theoretic framing unifies the classical definition (Fisher–Neyman factorisation) with the operational idea of lossless compression of statistically relevant information. It clarifies why, e.g., for Bernoulli trials the count of successes $(N_1, N)$ is minimal sufficient: it preserves all MI with the parameter while discarding order information.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[fisher-neyman-factorization]] — analogous-to
- [[mutual-information]] — uses
- [[sufficient-statistics]] — extends
- [[data-processing-inequality]] — uses
[To be populated during integration]