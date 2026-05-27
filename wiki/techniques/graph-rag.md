---
id: "pkis:technique:graph-rag"
aliases: []
title: "Graph Retrieval-Augmented Generation"
knowledge_type: technique
also_type: [framework]
domain: [knowledge-representation, deep-learning, symbolic-subsymbolic]
tags: [rag, knowledge-graphs, llm, graph-theory, multi-hop, information-retrieval]
related_concepts: [retrieval-augmented-generation, knowledge-graph, multi-hop-reasoning, graph-neural-networks, knowledge-graph-construction, in-context-learning]
sources: ["[[zhang-graphrag-survey]]", "[[gulli-agentic-design-patterns]]", "[[banf-tripartite-graphrag]]", "[[cheng-cograg]]", "[[barron-legal-rag-nmf]]", "[[sequeda-kg-benchmark-llm-2023]]"]
date_created: 2026-05-20
date_updated: 2026-05-20
coverage: 6
understanding: 0
maturity: evolving
---

## Reading Path
- [[zhang-graphrag-survey]] (unread) — primary theoretical treatment; full taxonomy and retrieval technique survey
- [[gulli-agentic-design-patterns-ch14]] (unread) — practical coverage; GraphRAG within the agentic knowledge retrieval pattern
- [[banf-tripartite-graphrag]] (unread) — tripartite variant with concept-anchored graph construction; formulates prompt assembly as node classification via Markov Random Fields
- [[cheng-cograg]] (unread) — CogGRAG: cognitive decomposition, dual-level retrieval, and self-verification for KGQA
- [[barron-legal-rag-nmf]] (unread) — legal domain instantiation combining VS, KG, and NMF-based latent topic retrieval
- [[sequeda-kg-benchmark-llm-2023]] (unread) — structured KG-as-schema RAG variant: OWL ontology injected as context enables SPARQL generation; contrasts with graph-traversal GraphRAG in that query is formal (SPARQL) rather than generative

A specialization of RAG that replaces flat vector-database retrieval with graph-structured knowledge organization, enabling multi-hop reasoning, explicit entity-relation retrieval, and structure-aware knowledge integration into LLM generation.

Classification note: assigned as technique but also functions as framework — GraphRAG defines a paradigm (knowledge organization → graph retrieval → knowledge integration) organizing concepts, techniques, and results into a coherent architecture; the three-way taxonomy (knowledge-based, index-based, hybrid) further structures the design space.
