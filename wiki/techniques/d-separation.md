---
aliases: []
also_type:
- result
coverage: 2
date_created: 2026-05-20
date_updated: 2026-05-20
domain:
- causal-analysis
- bayesian-stats
- knowledge-representation
id: pkis:technique:d-separation
knowledge_type: technique
maturity: settled
related_concepts:
- '[[directed-graphical-models]]'
- '[[structural-causal-models]]'
- '[[do-calculus]]'
- '[[probability-theory]]'
sources:
- '[[pearl-causality]]'
- '[[cunningham-causal-inference-mixtape]]'
tags:
- graph-theory
- conditional-independence
- bayesian-networks
- causality
title: d-Separation
understanding: 0
uses:
- conditional-independence
- strong-ignorability
---

## Reading Path
- [[pearl-causality-ch01]] (unread) — probabilistic graphical models; d-separation introduced as reading tool for DAGs
- [[cunningham-causal-inference-mixtape-ch04]] (unread) — practitioner treatment: blocking rules illustrated via confounders and colliders in econometric DAGs

A graphical criterion for determining all conditional independence relations encoded in a DAG. A path between X and Y is blocked by a set Z if it contains: (1) a chain X→M→Y or fork X←M→Y with M∈Z, or (2) a collider X→M←Y where M∉Z and no descendant of M∈Z. X and Y are d-separated by Z if every path between them is blocked — implying X⊥Y|Z under any distribution faithful to the graph. d-separation is Pearl's foundational contribution enabling Bayesian networks to encode and read off independence structure graphically without enumerating distributions.

## Connections
- [[strong-ignorability]] — uses: Pearl translates strong ignorability into a d-separation test: Z d-separates X from the parent-set surrogate W of {Y(0),Y(1)}.
- [[conditional-independence]] — uses