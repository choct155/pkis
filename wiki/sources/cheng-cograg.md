---
id: "pkis:source:cheng-cograg"
aliases: []
title: "Human Cognition Inspired RAG with Knowledge Graph for Complex Problem Solving"
authors: ["Yao Cheng", "Yibo Zhao", "Jiapeng Zhu", "Yao Liu", "Xing Sun", "Xiang Li"]
year: 2025
type: paper
domain: [knowledge-representation, deep-learning]
tags: [rag, knowledge-graphs, kgqa, llm, multi-hop, question-decomposition, self-verification, mind-map, chain-of-thought]
source_url: "https://arxiv.org/abs/2503.06567"
drive_id: "12K0S3harw8J97jzSCUxJ4yQ1Wkw8TciB"
drive_path: "PKIS/sources/papers/cheng-cograg.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[graph-rag]]", "[[retrieval-augmented-generation]]", "[[knowledge-graph]]", "[[multi-hop-reasoning]]", "[[knowledge-graph-question-answering]]"]
---

## Summary

Cheng et al. present CogGRAG (Cognition-inspired Graph RAG), a GraphRAG framework for Knowledge Graph Question Answering (KGQA) that draws on human cognitive strategies of problem decomposition and self-verification. The paper identifies two key failure modes of prior graph-based RAG: (1) error propagation in iterative retrieval/reasoning chains, and (2) lack of self-verification mechanisms. CogGRAG addresses both through a three-stage pipeline: Decomposition, Retrieval, and Reasoning with Self-Verification.

In the Decomposition stage, a complex question is recursively broken into a structured mind map — a tree of sub-questions with "Continue/End" state labels — using the LLM in a top-down fashion. The Retrieval stage operates at two granularity levels: local (entities and triples per sub-question) and global (cross-question subgraph relationships). Retrieved triples are pruned via cosine similarity against extracted keys. In the Reasoning stage, a dual-process framework employs one LLM for bottom-up reasoning (answering sub-questions from leaves to root) and a separate LLM for self-verification (checking consistency of each intermediate answer, triggering re-thinking when errors are detected).

Experiments on HotpotQA, CWQ, WebQSP, and GRBENCH (domain-specific KGs) with three backbone LLMs (LLaMA2-13B, LLaMA3-8B, Qwen2.5-7B) show CogGRAG outperforms baselines in most settings. Ablation confirms all three components — decomposition, global retrieval, and self-verification — contribute meaningfully. A hallucination analysis shows CogGRAG reduces hallucinations by prompting "I don't know" for insufficient information.

## Key Knowledge Objects

- [[graph-rag]] (technique, high) — CogGRAG is a specialized GraphRAG framework for KGQA; extends standard GraphRAG with cognitive decomposition and self-verification
- [[multi-hop-reasoning]] (concept, high) — core capability enabled by the mind-map decomposition and cross-question global retrieval
- [[knowledge-graph-question-answering]] (problem, high) — the specific task CogGRAG addresses; multi-hop QA over structured KGs
- [[knowledge-graph]] (concept, high) — Wikidata and domain-specific KGs used as structured external knowledge source
- [[retrieval-augmented-generation]] (technique, high) — foundational framework extended by graph-structured retrieval

## Key Extractions

1. **Mind map decomposition**: Complex questions are recursively decomposed top-down into a tree of sub-questions; each node carries a "Continue/End" state determining further decomposition. This structured hierarchical representation enables more precise retrieval than flat single-query approaches.
2. **Two-level retrieval (local + global)**: Local retrieval extracts entities and triples per sub-question; global retrieval extracts subgraphs representing cross-question relationships. Pruning via cosine similarity (threshold ε = 0.7) retains only relevant triples, reducing noise.
3. **Dual-process self-verification**: A reasoning LLM (LLMres) generates answers bottom-up; a separate verification LLM (LLMver) checks logical consistency against accumulated reasoning path. Errors trigger re-thinking rather than propagating forward.
4. **Error propagation avoidance**: Unlike iterative approaches (Think-on-Graph, Graph-CoT) where one wrong step corrupts all subsequent steps, CogGRAG's pre-built mind map allows re-verification at each level independently.
5. **Hallucination reduction via abstention**: When insufficient information is available, CogGRAG explicitly prompts "I don't know" rather than generating incorrect answers; this reduces hallucination rate while increasing missing-answer rate — a deliberate precision-recall tradeoff.

## Connection Candidates

- [[graph-rag]] — extends: adds cognitive decomposition (mind map), dual-level retrieval, and self-verification to basic GraphRAG
- [[multi-hop-reasoning]] — uses: mind map construction explicitly structures multi-hop reasoning paths as hierarchical question chains
- [[knowledge-graph-question-answering]] — the problem this technique addresses
- [[in-context-learning]] — uses: retrieved KG triples fed to LLM as structured in-context knowledge
- [[agentic-systems]] — contrasts-with: CogGRAG is pipeline-based (not agentic loop-based), though shares decomposition/verification patterns with agents
