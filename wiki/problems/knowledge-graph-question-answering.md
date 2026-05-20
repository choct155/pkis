---
title: "Knowledge Graph Question Answering (KGQA)"
knowledge_type: problem
also_type: []
domain: [knowledge-representation, deep-learning]
tags: [knowledge-graphs, multi-hop, question-answering, llm, benchmark, natural-language-understanding]
related_concepts: [knowledge-graph, multi-hop-reasoning, graph-rag, retrieval-augmented-generation]
sources: ["[[cheng-cograg]]", "[[liu-symagent]]", "[[cimiano-ontology-nlp]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 2
understanding: 0
maturity: evolving
---

The problem of answering natural language questions by traversing and reasoning over structured knowledge graphs, requiring multi-hop relational inference, entity linking, and often tolerance for KG incompleteness; benchmarked on datasets such as WebQSP, CWQ, HotpotQA, and MetaQA.

## Reading Path
- [[cheng-cograg]] (unread) — CogGRAG approach: cognitive decomposition + dual-level KG retrieval + self-verification; evaluated on HotpotQA, CWQ, WebQSP, GRBENCH
- [[liu-symagent]] (unread) — SymAgent approach: symbolic rule induction + ReAct agent loop + self-learning; evaluated on WebQSP, CWQ, MetaQA-3hop with incomplete KG setting
- [[cimiano-ontology-nlp-ch09]] (unread) — full symbolic NL-to-SPARQL QA pipeline; classical compositional baseline to neural KGQA approaches
