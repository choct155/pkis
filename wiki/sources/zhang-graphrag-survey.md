---
id: "pkis:source:zhang-graphrag-survey"
aliases: []
title: "A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models"
authors: "Qinggang Zhang, Shengyuan Chen, Yuanchen Bei, Zheng Yuan, Huachi Zhou, Zijin Hong, Junnan Dong, Hao Chen, Yi Chang, Xiao Huang"
year: 2025
type: paper
domain: [knowledge-representation, deep-learning, symbolic-subsymbolic]
tags: [rag, knowledge-graphs, llm, survey, graph-theory, information-retrieval]
source_url: "https://github.com/DEEP-PolyU/Awesome-GraphRAG"
drive_id: "1J5MvXiTsp-Jb50i20kl2TCp3j19K4_-F"
drive_path: "PKIS/sources/papers/"
status: unread
date_added: 2026-05-20
concepts: [retrieval-augmented-generation, graph-rag, multi-hop-reasoning, graph-neural-networks, knowledge-graph-construction, in-context-learning, knowledge-graph]
---

## Summary

This survey provides a systematic analysis of Graph Retrieval-Augmented Generation (GraphRAG), a paradigm that extends standard RAG systems by replacing flat vector-database retrieval with graph-structured knowledge organization. The motivation is that traditional RAG fails on four critical fronts: (i) it cannot perform multi-hop reasoning because it only retrieves anchor-entity-adjacent chunks; (ii) it cannot faithfully represent distributed domain knowledge whose hierarchy is destroyed by chunking; (iii) it overwhelms fixed LLM context windows (2K–32K tokens) with undifferentiated retrieved text; and (iv) it scales poorly because domain-specific terms are sparse across large unstructured corpora.

GraphRAG addresses these by organizing knowledge as a graph at either the knowledge level (graphs as knowledge carriers — extracting or leveraging entity-relation KGs) or the index level (graphs for indexing — using graph structure to organize and retrieve text chunks), with a hybrid variant combining both. The paper taxonomizes retrieval techniques into five classes (similarity-based, logical-reasoning, GNN-based, LLM-based, RL-based) and knowledge integration strategies into fine-tuning (node, path, subgraph levels) and in-context learning (Graph-enhanced Chain-of-Thought and Collaborative KG Refinement). Domain applications reviewed span general QA, biomedical, legal, education, scientific research, and sports analytics, with prominent open-source systems including Microsoft GraphRAG, LightRAG, and MedGraphRAG.

## Key Knowledge Objects

- [[retrieval-augmented-generation]] (technique, high) — framework augmenting LLM generation with external knowledge retrieved at inference time
- [[graph-rag]] (technique, high — also framework) — GraphRAG: RAG variant using graph-structured knowledge organization and retrieval
- [[multi-hop-reasoning]] (concept, high) — reasoning that traverses multiple edges in a knowledge graph to answer complex queries
- [[graph-neural-networks]] (technique, high) — neural networks for graph-structured data via message-passing; key retrieval component in GraphRAG
- [[knowledge-graph-construction]] (technique, high) — automated extraction of structured KGs from text corpora via OIE and LLMs
- [[in-context-learning]] (technique, moderate — could be concept) — eliciting LLM capabilities through prompting with examples, without weight updates

## Key Extractions

1. **GraphRAG taxonomy (three categories):** Knowledge-based GraphRAG uses graphs as knowledge carriers (explicit entity-relation KGs, enabling logic-guided chain retrieval and multi-hop reasoning); Index-based GraphRAG uses graphs purely as indexing structures for organizing text chunks (preserving original content, more scalable); Hybrid GraphRAG combines both, linking KG nodes to their source text chunks for evidence-backed generation.

2. **Token efficiency claim:** "Research has shown that GraphRAG systems can generate LLM responses using 26% to 97% fewer tokens compared to traditional methods" — cited advantage over flat RAG in both speed and resource utilization.

3. **Traditional RAG's four failure modes:** (i) no multi-hop reasoning — can only retrieve from anchor-entity-adjacent chunks; (ii) chunking destroys hierarchy — distributed domain knowledge loses its conceptual structure; (iii) LLM context window overflow — similarity retrieval lacks filtering, flooding the prompt; (iv) efficiency bottleneck — sparse domain terms force search across massive unstructured corpora.

4. **Knowledge-based GraphRAG approaches:** Two sub-lines — (a) constructing KGs from corpus using Open Information Extraction (classical OIE + LLM-based OIE), with methods ranging from relational triples to attributed KGs with community summaries (QUEST, Microsoft GraphRAG, LightRAG, GraphReader); (b) leveraging existing KGs (domain: UMLS, SPOKE, Lynx; general-purpose: Freebase, DBpedia) with LLM planners that perform beam search, relation path generation, or RL-based traversal (ToG, RoG, KnowGPT, SubgraphRAG).

5. **Five retrieval technique classes:** (a) Similarity-based: discrete string matching or embedding-space cosine similarity; (b) Logical reasoning-based: rule mining, inductive logic programming, constraint satisfaction (RoG, RuleRAG); (c) GNN-based: message-passing encoders for joint semantic + structural retrieval (GNN-RAG, SURGE); (d) LLM-based: LLMs as planners/navigators generating retrieval paths (Think-on-Graph, LightRAG, GraphRAG); (e) RL-based: sequential decision-making over graph traversal (KnowGPT, Spider).

6. **Knowledge integration via in-context learning — Graph-enhanced Chain-of-Thought:** Methods such as Think-on-Graph, Graph-CoT, MindMap, and Chain-of-Knowledge extend CoT prompting by grounding each reasoning step in graph-retrieved facts. The LLM iteratively queries the KG, retrieves a subgraph relevant to the current reasoning step, and chains inferences. Error accumulation remains an open challenge.

7. **Collaborative KG Refinement:** An alternative integration strategy where LLM-generated draft answers are post-hoc verified and corrected against the KG (KG-based Retrofitting, KELP, CogMG). CogMG additionally allows LLMs to identify missing KG triples, decompose them, and propose KG updates — creating a bidirectional augmentation loop.

## Connection Candidates

- [[knowledge-graph]] — uses: GraphRAG uses KGs as its primary knowledge carrier in knowledge-based variants; this source provides the richest treatment of KG utilization in the wiki so far
- [[rdf]] — uses: domain KGs leveraged by GraphRAG (SPOKE, UMLS, DBpedia) are commonly expressed in RDF or RDF-adjacent triple formats
- [[sparql]] — uses: logical-based retrievers generate structured rule queries over KGs analogous to SPARQL graph pattern matching
- [[neural-networks]] — extends: GNN-based retrievers specialize feedforward networks to graph-structured inputs via the message-passing mechanism
- [[backpropagation]] — uses: GNN encoders in retrieval are trained via backpropagation through graph-structured computation
- [[directed-graphical-models]] — contrasts-with: both use directed edges between entities, but KGs encode factual domain relationships while BNs encode probabilistic conditional dependencies
- [[em-algorithm]] — uses: knowledge graph completion methods (link prediction) involve EM-like alternation between entity embedding and relation optimization
- [[faceted-search]] — contrasts-with: faceted search provides filter-based KG exploration without reasoning; GraphRAG retrieval enables multi-hop inference over the same graph structures
- [[papadaki-rdf-analytics-survey]] — extends: prior source covers analytics over RDF KGs; this survey extends to LLM-augmented retrieval and generation over graph-structured knowledge

## Connection Candidates (new nodes → existing nodes)

- [[graph-rag]] extends [[retrieval-augmented-generation]]: GraphRAG is a specialized RAG variant
- [[graph-neural-networks]] extends [[neural-networks]]: GNNs generalize feedforward networks to graph-structured inputs
- [[knowledge-graph-construction]] uses [[knowledge-graph]]: construction produces KG instances
- [[multi-hop-reasoning]] prerequisite-of [[graph-rag]]: motivates the move from flat to graph retrieval
