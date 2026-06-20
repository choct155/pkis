---
aliases: []
also_type: []
coverage: 3
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- symbolic-subsymbolic
- deep-learning
- knowledge-representation
id: pkis:concept:compositionality
knowledge_type: concept
maturity: contested
related_concepts:
- '[[phrase-structure]]'
- '[[variable-binding]]'
- '[[inductive-bias]]'
- '[[neurosymbolic-ai]]'
sources:
- '[[marcus-dl-critical-appraisal-2018]]'
- '[[murphy-llm-linguistic-structure-2025]]'
- '[[dentella-ai-language-comprehension-2024]]'
- cimiano-ontology-nlp-ch03
- gulli-agentic-design-patterns-ch29
tags:
- syntax
- semantics
- language
- nlp
- meaning
- hierarchical-structure
- frege-principle
title: Compositionality
understanding: 0
---

The principle that the meaning of a complex expression is fully determined by the meanings of its constituent parts and the syntactic rules used to combine them (Frege's compositionality principle). In language, this means hierarchically structured expressions built from words according to phrase structure rules yield meanings in a rule-governed, generative way. Compositionality is claimed to be absent or severely limited in current large language models, which appear to process sequential statistical patterns rather than hierarchically composed meanings.

## Reading Path
- [[marcus-dl-critical-appraisal-2018]] (unread) — §3.3: DL's flat, non-hierarchical representations fail to capture recursive compositional structure; contrast with symbolic AI
- [[murphy-llm-linguistic-structure-2025]] (unread) — direct empirical tests of o3's compositional syntax-semantics; primary evidence of LLM failure on compositionality
- [[dentella-ai-language-comprehension-2024]] (unread) — behavioral benchmark showing LLMs fail at compositionally simple comprehension questions; argues failure stems from lack of a compositional operator