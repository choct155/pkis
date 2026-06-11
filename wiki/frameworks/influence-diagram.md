---
aliases: []
also_type: []
applies:
- statistical-decision-theory
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- decision theory
- probabilistic graphical models
- AI
extends:
- directed-graphical-models
- bayesian-networks
id: pkis:framework:influence-diagram
instantiates:
- decision-network-influence-diagram
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
tags:
- decision theory
- graphical models
- utility
- policy
- sequential decisions
title: Influence Diagram (Decision Diagram)
understanding: 0
uses:
- variable-elimination
---

## Definition
An influence diagram extends a directed probabilistic graphical model by introducing two additional node types:
- **Decision nodes** (rectangles): variables whose values are chosen by the agent.
- **Utility nodes** (diamonds): scalar-valued functions of their parents, representing payoffs.

Chance nodes (ovals) represent random variables as in ordinary Bayesian networks. **Information arcs** into a decision node indicate which variables are observed before the decision is made. The optimal policy is computed by backward induction through the diagram, equivalent to variable elimination on the joint probability–utility surface.

$$\text{MEU}(\mathcal{G}) = \max_{\pi} \mathbb{E}_{p(h,x;\pi)}[U(h, \pi(x))]$$

### Why it matters
Provides a graphical, modular language for specifying multi-stage decision problems under uncertainty, bridging Bayesian networks and decision theory. Optimal policies can be computed automatically via modified variable elimination, and the formalism naturally accommodates value of information calculations.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[variable-elimination]] — uses
- [[bayesian-networks]] — extends
- [[statistical-decision-theory]] — applies
- [[decision-network-influence-diagram]] — instantiates
- [[directed-graphical-models]] — extends
[To be populated during integration]