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
id: pkis:framework:lexicalized-pcfg
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch23
tags:
- nlp
- grammar
- augmented-grammar
- head-word
- smoothing
title: Lexicalized PCFG
understanding: 0
---

## Definition
An augmented context-free grammar that conditions rule probabilities on properties of the words in a phrase rather than syntactic categories alone, capturing distinctions a plain PCFG cannot -- e.g. preferring 'ate a banana' over 'ate a bandanna', or '[brown rice] and [black beans]' over the alternative bracketing. To control sparsity, probabilities depend only on the head of a phrase (the most important word: 'banana' heads 'a banana', 'ate' heads 'ate a banana'), written VP(v) -> Verb(v) NP(n) [P_1(v,n)]. The resulting head-pair tables are huge (5,000 verbs x 10,000 nouns = 50M entries) but mostly derived by smoothing and backoff (e.g. back off from P_1(v,n) to a verb-only model that still captures transitive vs intransitive preference). Categories can be further augmented with feature variables -- case, person, number -- to enforce subject-verb agreement and pronoun case (NP(Sbj,pn,n)), preventing overgeneration of nonsentences like 'I saw she' or 'Me ate a banana'. Lexicalized PCFGs (Charniak, 1997; Collins, 1999) combine the best of PCFGs and n-gram models.

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]