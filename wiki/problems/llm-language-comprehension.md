---
id: "pkis:problem:llm-language-comprehension"
aliases: []
title: "LLM Language Comprehension"
knowledge_type: problem
also_type: []
domain: [symbolic-subsymbolic, deep-learning]
tags: [llm, language-comprehension, compositionality, benchmarking, nlp, evaluation]
related_concepts: ["[[compositionality]]", "[[moravecs-paradox]]", "[[inductive-bias]]", "[[neurosymbolic-ai]]"]
sources: ["[[dentella-ai-language-comprehension-2024]]", "[[murphy-llm-linguistic-structure-2025]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: contested
---

The open problem of whether large language models genuinely comprehend language — in the sense of compositionally mapping syntactic structure to meaning — or whether they are pattern-matching surface statistics without access to underlying semantic structure. Dentella et al. (2024) provide empirical evidence for the latter: LLMs perform at chance on 40 simple comprehension questions that humans answer at ceiling, exhibiting distinctly non-human error patterns (irrelevant elaborations, contradictory outputs). Murphy et al. (2025) extend this to structural linguistics: o3 fails to represent phrase structure, center-embedding, and other hallmarks of compositional syntax.

## Reading Path
- [[dentella-ai-language-comprehension-2024]] (unread) — primary empirical source; 7 LLMs × 40 simple comprehension questions; n=26,680 datapoints; LLMs at chance, humans at ceiling; LLM errors qualitatively non-human; foundational demonstration of the comprehension gap
- [[murphy-llm-linguistic-structure-2025]] (unread) — extends to structural linguistics; 26 linguistic probes on o3; failures at phrase structure generalization, center-embedding, Escher sentences, and graded acceptability judgments; structural failure goes beyond surface statistics
