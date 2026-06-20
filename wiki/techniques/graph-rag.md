---
aliases: []
also_type:
- framework
coverage: 6
date_created: 2026-05-20
date_updated: '2026-06-20'
domain:
- knowledge-representation
- deep-learning
- symbolic-subsymbolic
id: pkis:technique:graph-rag
knowledge_type: technique
maturity: evolving
related_concepts:
- retrieval-augmented-generation
- knowledge-graph
- multi-hop-reasoning
- graph-neural-networks
- knowledge-graph-construction
- in-context-learning
sources:
- '[[zhang-graphrag-survey]]'
- '[[gulli-agentic-design-patterns]]'
- '[[banf-tripartite-graphrag]]'
- '[[cheng-cograg]]'
- '[[barron-legal-rag-nmf]]'
- '[[sequeda-kg-benchmark-llm-2023]]'
- 2307-07697-think-on-graph-deep
- arxivorg-thinkongraph
- edge-from-2024
- feng-cypherbench-2024
- procko-from-2026
- share-thinkongraph
- share-thinkongraph-1
tags:
- rag
- knowledge-graphs
- llm
- graph-theory
- multi-hop
- information-retrieval
title: Graph Retrieval-Augmented Generation
understanding: 0
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