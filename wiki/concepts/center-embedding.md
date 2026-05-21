---
title: "Center-Embedding"
knowledge_type: concept
also_type: []
domain: [symbolic-subsymbolic, knowledge-representation]
tags: [syntax, recursion, working-memory, generative-grammar, linguistic-complexity]
related_concepts: ["[[phrase-structure]]", "[[compositionality]]", "[[variable-binding]]"]
sources: ["[[murphy-llm-linguistic-structure-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 1
understanding: 0
maturity: settled
---

A syntactic construction in which a clause is embedded in the middle of another clause, requiring the parser to maintain multiple open syntactic dependencies simultaneously. Classic example: "The doctor [the nurse [the hospital had hired] met] saw John." Center-embedding tests a hallmark of recursive hierarchical syntax; humans can parse modest depths with effort, but performance degrades with deeper embedding due to working memory limits. Murphy et al. (2025) find that o3 fails to correctly assess grammaticality of center-embedded structures, hallucinating words in syntactic trees and missing the recursive dependency structure.

## Reading Path
- [[murphy-llm-linguistic-structure-2025]] (unread) — §3.4 directly tests center-embedding acceptability; documents o3's failure to detect ungrammaticality from a missing verb and its hallucinated pronominal elements in tree representation
