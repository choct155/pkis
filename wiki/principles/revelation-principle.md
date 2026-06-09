---
aliases: []
also_type: []
applies:
- mechanism-design
component_scores:
  implications: null
  justification: null
  statement: null
  violations: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- multi-agent-systems
- economics
id: pkis:principle:revelation-principle
knowledge_type: principle
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch18
tags:
- mechanism-design
- truthful
- incentive-compatibility
title: Revelation Principle
understanding: 0
---

## Definition
A foundational result of mechanism design (Myerson 1986): any mechanism can be transformed into an equivalent *truth-revealing* (incentive-compatible) mechanism that implements the same outcome. The transformed mechanism simulates the strategic behavior agents would have used in the original, so agents have no incentive to misreport. The practical upshot is that, without loss of generality, mechanism designers can restrict attention to direct truthful mechanisms — part of mechanism design is finding the truthful equivalent of a given mechanism.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[mechanism-design]] — applies
[To be populated during integration]