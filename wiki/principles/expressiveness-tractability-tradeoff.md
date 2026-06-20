---
aliases: []
also_type: []
coverage: 2
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- symbolic-subsymbolic
id: pkis:principle:expressiveness-tractability-tradeoff
knowledge_type: principle
maturity: settled
related_concepts:
- description-logic
- formal-ontology
- cyc-knowledge-base
- ontology-reasoning
sources:
- '[[lenat-marcus-cyc-trustworthy-2023]]'
- '[[delong-nsai-kg-survey-2024]]'
- allemang-semantic-web-ch15
- cimiano-ontology-nlp-ch02
tags:
- logic
- inference
- computational-complexity
- description-logic
- higher-order-logic
- owl
- cyc
- ontology
title: Expressiveness-Tractability Tradeoff
understanding: 0
---

The expressiveness-tractability tradeoff is the fundamental tension in knowledge representation and reasoning: richer logical languages (higher-order logic, full FOL) can represent arbitrarily complex knowledge but make inference computationally intractable, while more restricted languages (propositional logic, Horn clauses, Description Logic fragments, knowledge graphs) support efficient reasoning at the cost of expressive power; system design choices — DL profiles (EL, QL, RL), microtheory partitioning in Cyc, Datalog±, — are all responses to this tradeoff.

## Reading Path
- [[lenat-marcus-cyc-trustworthy-2023]] (unread) — articulates the tradeoff clearly: full HOL inference is too slow; knowledge graphs are fast but too inexpressive; Cyc microtheories as partial solution
- [[delong-nsai-kg-survey-2024]] (unread) — OWL 2 EL as a tractable DL fragment enabling polynomial-time reasoning for large biomedical KGs