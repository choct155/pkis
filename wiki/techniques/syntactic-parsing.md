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
id: pkis:technique:syntactic-parsing
knowledge_type: technique
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- parsing
- cyk
- chart-parser
- shift-reduce
- beam-search
title: Syntactic Parsing
understanding: 0
---

## Definition
The process of analyzing a string of words to recover its phrase structure under a grammar -- a search for a valid parse tree whose leaves are the words. Pure top-down or bottom-up search repeats effort and backtracks (e.g. command vs question sentences sharing their first ten words), so dynamic programming stores analyzed substrings in a chart (chart parsing). The CYK algorithm is a probabilistic bottom-up chart parser requiring Chomsky Normal Form, using O(n^2 m) space and O(n^3 m) time and returning the most probable parse. A* search with an admissible heuristic can find the most probable parse faster on average; beam search keeps only the b most probable partial parses and (carefully implemented) runs in O(n) time, usually finding the best parse. A beam parser with b=1 is a deterministic parser, of which shift-reduce parsing -- choosing at each word to shift onto a constituent stack or reduce by a rule -- is the popular instance. Modern neural parsers (Parsey McParseface, Stanford, Berkeley, spaCy) reach ~95% accuracy on Penn Treebank / WSJ.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]