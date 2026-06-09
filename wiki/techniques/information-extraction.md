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
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
- deep-learning
id: pkis:technique:information-extraction
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- relation-extraction
- open-ie
- knowledge-acquisition
title: Information Extraction
understanding: 0
---

## Definition
The process of acquiring structured knowledge by skimming text for occurrences of particular classes of objects and the relationships among them -- e.g. extracting addresses (street/city/state/zip) from web pages, or storm reports (temperature/wind/precipitation) from weather text. Well-structured source text (tables) yields to simple techniques like regular expressions; free-form text requires hidden Markov models, conditional random fields, rule-based learning, or (recently) recurrent neural networks exploiting word embeddings. Closed extraction targets a fixed relation schema; open information extraction (e.g. TextRunner) extracts over an open, expanding set of relations. Bootstrapping methods -- cotraining (Blum and Mitchell, 1998) / DIPRE (Brin, 1998) -- simultaneously learn extraction templates and example instances from a handful of seeds, scaling to systems like KnowItAll and the never-ending learner NELL. Extraction can also exploit geometric/layout structure (lists, tables, charts in HTML or PDF) rather than linguistic structure.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]