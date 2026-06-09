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
contrasts-with:
- phrase-structure
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
id: pkis:framework:dependency-grammar
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- grammar
- syntax
- parsing
- universal-dependencies
title: Dependency Grammar
understanding: 0
---

## Definition
A syntactic formalism that represents structure as a set of binary head-dependent relations between lexical items, without positing syntactic constituents (phrases). Dependency and phrase-structure grammars are largely notational variants -- a phrase-structure tree annotated with phrase heads yields the dependency tree, and a dependency tree converts back by introducing categories -- so neither is more powerful; the choice is one of naturalness. Phrase-structure trees suit fixed-word-order languages like English; dependency trees suit free-word-order languages like Latin, where order is governed by pragmatics rather than syntactic position. Carried to its extreme, lexicalization yields dependency grammar with no syntactic categories at all, only relations between words. The formalism's modern popularity stems largely from the Universal Dependencies project, an open treebank defining a shared relation set across 70+ languages.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[phrase-structure]] — contrasts-with
[To be populated during integration]