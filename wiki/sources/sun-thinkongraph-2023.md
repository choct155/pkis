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
Although large language models (LLMs) have achieved significant success in various tasks, they often struggle with hallucination problems, especially in scenarios requiring deep and responsible reasoning. These issues could be partially addressed by introducing external knowledge graphs (KG) in LLM reasoning. In this paper, we propose a new LLM-KG integrating paradigm ``$\hbox{LLM}\otimes\hbox{KG}$'' which treats the LLM as an agent to interactively explore related entities and relations on KGs and perform reasoning based on the retrieved knowledge. We further implement this paradigm by introd…

## Key Knowledge Objects
[To be identified during Librarian ingest]

## Key Extractions
[To be identified during Librarian ingest]

## Connection Candidates
[To be identified during Librarian ingest]

## Reading Notes
Empirical baseline for the variational-graph-traversal hypothesis. Read after policy gradient foundations are solid (Mohamed + Sutton-Barto Ch13). Proposes iterative beam search over a knowledge graph to ground LLM reasoning: at each hop the LLM scores available relations by relevance to the query and selects top-k; beam width and traversal depth are tunable. The traversal objective is a heuristic LLM relevance score — a point estimate with no uncertainty representation and no principled convergence criterion. Key gaps the hypothesis addresses: (1) Beam search implicitly collapses the ELBO entropy term to constant log k — traversal is purely fit-driven with no exploration pressure. (2) No convergence criterion — beam width and depth are ungrounded. (3) Heuristic relevance scorer is a point estimate; no uncertainty over paths. (4) No connection to particle filter literature or approximate posterior inference. Position in reading graph: target of variational-graph-traversal hypothesis; bridges knowledge-representation and bayesian-stats clusters.