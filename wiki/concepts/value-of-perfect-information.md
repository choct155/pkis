---
aliases: []
also_type: []
component_scores:
  application: null
  boundary: null
  definition: null
  dependents: null
  formal_statement: null
  prerequisites: null
  scope: null
  transfer: null
coverage: 1
date_created: '2026-06-11'
date_updated: '2026-06-11'
domain:
- decision theory
- economics
- AI
id: pkis:concept:value-of-perfect-information
instantiates:
- statistical-decision-theory
knowledge_type: concept
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- murphy-pml2-advanced-ch34
specializes:
- value-of-information
tags:
- information value
- influence diagram
- MEU
- experimental design
title: Value of Perfect Information (VPI)
understanding: 0
uses:
- influence-diagram
---

## Definition
$$\text{VPI}(S) = \text{MEU}(\mathcal{G} + S \to D) - \text{MEU}(\mathcal{G})$$

The VPI of a random variable $S$ is the increase in maximum expected utility (MEU) obtained when the agent can observe $S$ before making decision $D$, compared with the base case where $S$ is unobserved. It is computed by adding an information arc from $S$ to the relevant decision node in the influence diagram and recomputing the MEU.

### Why it matters
VPI quantifies how much it is worth paying (in utility units) to acquire a measurement. Since VPI $\geq 0$ always, observing more information never hurts in expectation. It guides optimal data-collection decisions, experimental design, and sensor placement in robotics.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[statistical-decision-theory]] — instantiates
- [[value-of-information]] — specializes
- [[influence-diagram]] — uses
[To be populated during integration]