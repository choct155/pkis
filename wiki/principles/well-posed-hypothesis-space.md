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
- bayesian-stats
id: pkis:principle:well-posed-hypothesis-space
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- jaynes-probability-ch18
tags:
- jaynes
- foundations
- prior-information
- principle-of-indifference
- ill-posed
title: Well-Posed Hypothesis Space
understanding: 0
---

## Definition
Probability theory cannot give a definite answer unless asked a definite question: every inference problem must begin with an explicit enumeration of the hypothesis space — the mutually exclusive, exhaustive propositions under consideration — as part of its boundary conditions. To say 'I don't know what the possible propositions are' is mathematically equivalent to saying 'I don't know what problem I want to solve.' Crucially, 'no evidence' is not a free-floating notion: what matters is what it means *to the robot*, i.e. which hypotheses it has been told to consider. Admitting a third proposition where there were two already changes the prior information.

### Why it matters
This principle dissolves the classic objections to Laplace's rule of succession. The 'elephants on Mars' paradox (N=n=0 giving probability 1/2 to mutually exclusive elephant-counts, hence a contradiction) is a misapplication: enumerating 137 distinct ways for $A$ to be false versus one way to be true gives prior $1/138$, not $1/2$. More generally, every famous 'absurdity' (solidified hydrogen, the boy and his grandfather, Jeffreys's feathered animals) arises from either ignoring highly relevant prior information or mis-specifying the hypothesis space. The remedy is the same: state the prior information not in words but in equations — the prior probabilities actually used — before the problem is well-posed.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]