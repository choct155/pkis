---
title: "Phrase Structure"
knowledge_type: concept
also_type: []
domain: [symbolic-subsymbolic, knowledge-representation]
tags: [syntax, grammar, linguistics, hierarchical-structure, constituency, generative-grammar]
related_concepts: ["[[compositionality]]", "[[center-embedding]]", "[[discourse-representation-theory]]", "[[lexicalized-tree-adjoining-grammar]]"]
sources: ["[[murphy-llm-linguistic-structure-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

The hierarchical organization of sentences into nested syntactic constituents (noun phrases, verb phrases, clauses) according to phrase structure rules in a generative grammar. Phrase structure encodes the recursive compositional structure of language: a sentence is built from phrases, each recursively assembled from smaller units according to rules like S → NP VP, NP → Det N, etc. Murphy et al. (2025) demonstrate that o3 fails to generalize basic phrase structure rules: it incorrectly judges ungrammatical strings built from novel pseudowords as grammatical, and its syntactic tree representations are inconsistent with actual string structure.

## Reading Path
- [[murphy-llm-linguistic-structure-2025]] (unread) — §3.2 and §3.4 directly test phrase structure generalization and center-embedding; empirical demonstration that o3 cannot represent multi-step phrase structure dependencies
