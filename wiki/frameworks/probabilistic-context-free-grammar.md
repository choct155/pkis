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
- knowledge-representation
- deep-learning
id: pkis:framework:probabilistic-context-free-grammar
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
specializes:
- language-model
tags:
- nlp
- grammar
- parsing
- syntax
- pcfg
title: Probabilistic Context-Free Grammar
understanding: 0
uses:
- phrase-structure
- compositionality
---

## Definition
A language model based on hierarchical syntactic structure: a set of rewrite rules, each annotated with a probability, that generate phrase-structure trees and assign a probability to each string. 'Context-free' means any rule applies in any context (a noun phrase rule is the same at the start of a sentence or later, and identical phrases get identical probabilities); a rule such as Adjs -> Adjective [0.80] | Adjective Adjs [0.20] partitions the probability mass over the right-hand-side alternatives. A PCFG can be learned from a treebank simply by counting how often each node-type expands a given way (with smoothing), though hand-built treebanks yield many idiosyncratic, overly flat rules. The CYK chart-parsing algorithm computes the most probable parse in O(n^3 m) time for grammars in Chomsky Normal Form. PCFGs were first investigated by Booth (1969) and Salomaa (1969); they capture hierarchical structure that atomic n-gram models miss, but the basic context-free form cannot express agreement, case, or head-word preferences without augmentation.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[compositionality]] — uses
- [[phrase-structure]] — uses
- [[language-model]] — specializes
[To be populated during integration]