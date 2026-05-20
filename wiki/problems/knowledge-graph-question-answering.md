---
title: "Knowledge Graph Question Answering (KGQA)"
knowledge_type: problem
also_type: []
domain: [knowledge-representation, deep-learning]
tags: [knowledge-graphs, multi-hop, question-answering, llm, benchmark, natural-language-understanding]
related_concepts: [knowledge-graph, multi-hop-reasoning, graph-rag, retrieval-augmented-generation]
sources: ["[[cheng-cograg]]", "[[liu-symagent]]", "[[cimiano-ontology-nlp]]", "[[kg-evaluation-bloomberg-2024]]", "[[sequeda-kg-benchmark-llm-2023]]", "[[sequeda-kg-trust-llm-2025]]", "[[radhakrishnan-datagemma-2024]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 7
understanding: 0
maturity: evolving
---

The problem of answering natural language questions by traversing and reasoning over structured knowledge graphs, requiring multi-hop relational inference, entity linking, and often tolerance for KG incompleteness; benchmarked on datasets such as WebQSP, CWQ, HotpotQA, and MetaQA.

## Reading Path
- [[cheng-cograg]] (unread) — CogGRAG approach: cognitive decomposition + dual-level KG retrieval + self-verification; evaluated on HotpotQA, CWQ, WebQSP, GRBENCH
- [[liu-symagent]] (unread) — SymAgent approach: symbolic rule induction + ReAct agent loop + self-learning; evaluated on WebQSP, CWQ, MetaQA-3hop with incomplete KG setting
- [[cimiano-ontology-nlp-ch09]] (unread) — full symbolic NL-to-SPARQL QA pipeline; classical compositional baseline to neural KGQA approaches
- [[kg-evaluation-bloomberg-2024]] (unread) — demand-side KG evaluation framing; competency questions as fitness-for-purpose assessment; enterprise perspective on what KGQA needs to deliver
- [[sequeda-kg-benchmark-llm-2023]] (unread) — primary empirical benchmark: 16.7% (SQL) vs. 54.2% (SPARQL/KG) accuracy for GPT-4 zero-shot on enterprise insurance schema; 4-quadrant complexity classification; SQL collapses to 0% for high schema complexity
- [[sequeda-kg-trust-llm-2025]] (unread) — position paper: three trust roles of KGs in enterprise QA (query validation, explainability, governed data access); conceptual follow-on to the 2023 benchmark
- [[radhakrishnan-datagemma-2024]] (unread) — KGQA over public statistical data: NL → Data Commons query decomposition into variable/place/attribute components; RIG and RAG architectures for grounding LLM answers in a 2.5T-triple statistics KG
