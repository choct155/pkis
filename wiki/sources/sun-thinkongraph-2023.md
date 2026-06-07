---
aliases: []
authors: Jiashuo Sun, Chengjin Xu, Lumingyuan Tang, Saizhuo Wang, Chen Lin, Yeyun
  Gong, Lionel M. Ni, Heung-Yeung Shum, Jian Guo
chapter: null
concepts: []
date_added: '2026-05-31'
date_read: ''
date_updated: '2026-06-07'
doc_path: sources/sun-thinkongraph-2023/2307.07697.pdf
domain:
- knowledge-representation
- deep-learning
drive_id: ''
drive_path: ''
id: pkis:source:sun-thinkongraph-2023
isbn: ''
parent_book: ''
readwise_id: 01ksyzawhcpxr628p06e44zjpy
source_url: https://arxiv.org/abs/2307.07697
status: unread
tags:
- knowledge-graph
- graph-traversal
- beam-search
- question-answering
- LLM-grounding
- retrieval-augmented-generation
- think-on-graph
title: 'Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on
  Knowledge Graph'
toc_source: ''
type: paper
year: 2023
---

## Summary
Sun et al. (2023). Proposes iterative beam search over a knowledge graph to ground LLM reasoning for multi-hop question answering. The key architectural innovation is tight-coupling (LLM⊗KG): the LLM participates at every hop of traversal, scoring candidate relations and entities by relevance to the query and pruning the beam.

Three phases: initialization (LLM extracts topic entities from query), exploration (iterative LLM-scored beam search, depth D width N), reasoning (LLM determines whether to answer from current paths or continue traversal).

Demonstrates substantial improvements over flat RAG on multi-hop QA benchmarks (WebQSP, CWQ, HotpotQA). Introduces ToG-R variant that scores at relation-type level rather than entity instance level — competitive performance with substantially fewer LLM calls.

## Key Knowledge Objects
[To be identified during Librarian ingest]

## Key Extractions
[To be identified during Librarian ingest]

## Connection Candidates
[To be identified during Librarian ingest]

## Reading Notes
Empirical baseline for the variational-graph-traversal hypothesis. Read after policy gradient foundations are solid (Mohamed + Sutton-Barto Ch13). Proposes iterative beam search over a knowledge graph to ground LLM reasoning: at each hop the LLM scores available relations by relevance to the query and selects top-k; beam width and traversal depth are tunable. The traversal objective is a heuristic LLM relevance score — a point estimate with no uncertainty representation and no principled convergence criterion. Key gaps the hypothesis addresses: (1) Beam search implicitly collapses the ELBO entropy term to constant log k — traversal is purely fit-driven with no exploration pressure. (2) No convergence criterion — beam width and depth are ungrounded. (3) Heuristic relevance scorer is a point estimate; no uncertainty over paths. (4) No connection to particle filter literature or approximate posterior inference. Position in reading graph: target of variational-graph-traversal hypothesis; bridges knowledge-representation and bayesian-stats clusters.

## LLM-KG Paradigm Distinction
The paper distinguishes three paradigms:
LLM-only: reasoning entirely from parametric memory.
LLM⊕KG (loose coupling): static retrieval then generation. Fails when the retrieved subgraph is incomplete — if a required relation is missing, the LLM has nothing to work with.
LLM⊗KG (tight coupling): LLM participates at every traversal step. Can supplement missing graph knowledge from parametric memory at each hop. ToG is LLM⊗KG.

This distinction is the scope condition for the variational graph traversal hypothesis: VGT applies to LLM⊗KG paradigms only.

## Contamination Risk
High. Freebase and Wikidata are extensively covered in LLM pre-training data. ToG's benchmark performance may be partially inflated by the LLM having memorized answers that appear to come from graph traversal but are retrieved from parametric memory. This is a known critique in the literature and limits the interpretability of accuracy improvements on these specific benchmarks.

## ToG-R Significance
The paper introduces ToG-R as an efficiency variant that scores at relation-type level rather than entity instance level. The paper treats this as an efficiency tradeoff. From the VGT hypothesis perspective, ToG-R is theoretically cleaner: learning which relation types are useful for which query categories is a generalizable, interpretable parameter rather than a query-specific LLM judgment.

The empirical finding that ToG-R performs comparably to full ToG validates the tractability of the relation-type-level simplification in the VGT scoring matrix.

## Gaps Addressed by VGT Hypothesis
(1) Traversal objective is a heuristic point estimate with no uncertainty representation and no convergence criterion.
(2) Beam width and depth are empirically tuned — no principled guidance.
(3) Beam search collapses the ELBO entropy term to a constant (log k), making traversal purely fit-driven.
(4) No connection to particle filter literature or approximate posterior inference.
(5) ToG-R is identified as tractable but not connected to a learning objective.