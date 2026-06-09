---
aliases: []
also_type: []
applies:
- conditional-independence
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
id: pkis:result:graphoid-axioms
knowledge_type: result
maturity: evolving
needs_canonical_source: false
prerequisite-of:
- d-separation
related_concepts: []
sources:
- pearl-causality-ch01
tags:
- conditional-independence
- informational-relevance
- d-separation
- axioms
- probability-theory
title: Graphoid Axioms
understanding: 0
---

## Definition
A set of properties governing the conditional-independence (informational-relevance) relation $(X \perp\!\!\perp Y \mid Z)$, satisfied both by probabilistic independence and by graph separation — hence the abstract notion of a *graphoid*.

One-line intuition: irrelevance behaves lawfully — learning irrelevant facts cannot turn other irrelevant facts into relevant ones.

### The axioms
For disjoint variable sets,
$$\textbf{Symmetry:}\quad (X \perp\!\!\perp Y \mid Z) \Rightarrow (Y \perp\!\!\perp X \mid Z),$$
$$\textbf{Decomposition:}\quad (X \perp\!\!\perp YW \mid Z) \Rightarrow (X \perp\!\!\perp Y \mid Z),$$
$$\textbf{Weak union:}\quad (X \perp\!\!\perp YW \mid Z) \Rightarrow (X \perp\!\!\perp Y \mid ZW),$$
$$\textbf{Contraction:}\quad (X \perp\!\!\perp Y \mid Z)\,\&\,(X \perp\!\!\perp W \mid ZY) \Rightarrow (X \perp\!\!\perp YW \mid Z),$$
$$\textbf{Intersection:}\quad (X \perp\!\!\perp W \mid ZY)\,\&\,(X \perp\!\!\perp Y \mid ZW) \Rightarrow (X \perp\!\!\perp YW \mid Z).$$
Intersection holds only for strictly positive distributions; the first four hold generally (a *semi-graphoid*).

### Interpretation
Symmetry: if $Y$ tells us nothing new about $X$, then $X$ tells us nothing new about $Y$. Weak union and contraction jointly say that irrelevant information cannot alter the relevance status of other propositions. The same axioms hold when $(X \perp\!\!\perp Y \mid Z)$ is read as "$Z$ intercepts every path from $X$ to $Y$," which is exactly why graph separation can faithfully represent probabilistic independence.

### Why it matters
The graphoid axioms are the formal warrant for graphical models: they explain *why* a graph can encode the independencies of a distribution, underpinning d-separation and the entire reading-off of conditional independence from DAG topology.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[conditional-independence]] — applies
- [[d-separation]] — prerequisite-of
[To be populated during integration]