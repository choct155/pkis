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
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- bayesian-stats
id: pkis:framework:the-bernoulli-urn
instantiates:
- sampling-distribution
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch03
tags:
- jaynes
- sampling-theory
- conceptual-device
- probability-as-logic
title: The Bernoulli Urn Model
understanding: 0
uses:
- principle-of-indifference
---

## Definition
The canonical conceptual device of elementary sampling theory: an urn holds $N$ labelled balls, $M$ red and $N-M$ white; balls are drawn blindfolded, their color recorded, and (in the basic case) set aside. From the principle of indifference applied to the equally-possible labelled balls, the **Bernoulli urn rule** follows: if proposition $A$ is true on a subset of $M$ balls, $P(A\mid B)=M/N$. This single rule, with the product and sum rules, generates the hypergeometric distribution, its symmetries, the binomial limit, and the forward/backward inference results.

Jaynes stresses that the urn probability is a description of *knowledge*, not a physical fact about the urn, and that 'verifying' $P(R_1\mid B)=M/N$ by experiment is a category error. The urn's analytic value is uneven: it is apt for survey sampling, radioactive counts, and quality control (literal finite populations), strained for agricultural or medical trials, and dangerously misleading for coin flips, temperatures, or commodity prices — where the 'hypothetical infinite population' is a figment that smuggles in unwarranted strict independence. Even when urn reasoning is conceptually inappropriate, the resulting distributions reappear in sophisticated analyses for purely mathematical reasons (Chapter 9), giving them a status independent of the urn picture.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[sampling-distribution]] — instantiates: the urn distributions are the chapter's worked examples of direct (sampling) probabilities P(D|H)
- [[principle-of-indifference]] — uses: Bernoulli urn rule P(A|B)=M/N is derived by applying the principle of indifference to the equally-possible labelled balls
[To be populated during integration]