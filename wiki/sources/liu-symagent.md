---
title: "SymAgent: Neural-Symbolic Self-Learning Agent over Knowledge Graphs"
authors: ["Ben Liu", "Jihai Zhang", "Fangquan Lin", "Cheng Yang", "Min Peng", "Wotao Yin"]
year: 2025
type: paper
domain: [knowledge-representation, symbolic-subsymbolic, deep-learning]
tags: [knowledge-graphs, llm, neural-symbolic, agents, self-learning, rule-induction, kgqa, reinforcement-learning, incomplete-kg, pomdp]
source_url: ""
drive_id: "1uIJYYOmWT4M-mxsQ42v3Vr-Uo5-aFtVK"
drive_path: "PKIS/sources/papers/liu-symagent.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[agentic-systems]]", "[[knowledge-graph]]", "[[knowledge-graph-question-answering]]", "[[multi-hop-reasoning]]"]
---

## Summary

Liu et al. propose SymAgent, a neural-symbolic agent framework for complex reasoning over knowledge graphs that addresses two key limitations of existing KG-LLM methods: (1) assumption that all answers are contained in the KG (ignoring KG incompleteness), and (2) treatment of KGs as static repositories rather than exploiting their implicit symbolic reasoning structure.

SymAgent consists of two modules. The Agent-Planner uses the LLM's inductive reasoning capability to extract symbolic rules (first-order logic rule bodies) from the KG by retrieving analogous seed questions, sampling BFS reasoning paths, and generalizing them into abstract rule templates. These rules serve as high-level plans aligning natural language questions with KG structural patterns. The Agent-Executor then engages in a ReAct-style thought-action-observation loop, invoking tools from a predefined action set: `getReasoningPath`, `searchNeighbor`, `wikiSearch` (with automatic `extractTriples` on return), and `finish`. When the KG lacks required triples, `wikiSearch` retrieves external documents and auto-extracts triples aligned with KG semantic granularity, facilitating dynamic KG expansion.

SymAgent is trained via a self-learning framework requiring only Q&A pairs: an online exploration phase synthesizes trajectories through environment interaction; self-reflection refines them; heuristic merging selects higher-reward trajectories; offline iterative policy updating fine-tunes the LLM on merged trajectories without teacher-model distillation. With Qwen2-7B as backbone, SymAgent outperforms GPT-4 across WebQSP, CWQ, and MetaQA-3hop by 37.19% Hits@1, 16.87% Accuracy, and 30.17% F1 on average.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — SymAgent is a hybrid neural-symbolic system: symbolic rules guide LLM planning, LLM reasoning executes rule-driven exploration
- [[agentic-systems]] (framework, high) — SymAgent implements a full agent loop (planner + executor with tool use, observation, self-learning)
- [[knowledge-graph-question-answering]] (problem, high) — the benchmark task SymAgent targets; multi-hop QA over Freebase and domain-specific KGs
- [[knowledge-graph]] (concept, high) — treated as a dynamic environment rather than a static repository; SymAgent both queries and expands the KG
- [[multi-hop-reasoning]] (concept, high) — symbolic rules capture multi-hop relational paths guiding efficient question decomposition

## Key Extractions

1. **Symbolic rule induction for planning**: Given a question, the Agent-Planner retrieves semantically similar seed questions, applies BFS to find closed relational paths in the KG connecting query entities to answer entities, and generalizes these paths into symbolic rule bodies. The LLM then selects the most plausible rule(s), providing structured planning rather than open-ended generation.
2. **KG as dynamic environment (POMDP)**: Complex reasoning is formalized as a Partially Observable Markov Decision Process over the KG. The agent interacts with the KG environment through multi-step action invocation, receiving observations as execution feedback.
3. **KG incompleteness handling**: When `searchNeighbor` returns no results, `wikiSearch` retrieves relevant Wikipedia documents; `extractTriples` automatically extracts KG-aligned triples from them, both answering the question and seeding KG updates. Augmenting RoG's KG with SymAgent-extracted triples demonstrably improves RoG performance.
4. **Self-learning without teacher distillation**: The framework synthesizes trajectory data through self-exploration and self-reflection with outcome-based rewards (recall of correct answers), then merges trajectories by taking the higher-reward version. Iterative fine-tuning on these self-synthesized trajectories outperforms distillation from GPT-4.
5. **Symbolic rules as semantic bridge**: LLMs are effective inductive reasoners but poor deductive reasoners. By deriving symbolic rules (which reflect KG structural patterns) and using them as planning scaffolds, SymAgent bridges the semantic gap between NL questions and KG entity/relation vocabulary.

## Connection Candidates

- [[neurosymbolic-ai]] — specializes: SymAgent implements a specific neurosymbolic architecture where symbolic KG rules guide neural LLM reasoning
- [[agentic-systems]] — extends: SymAgent adds symbolic rule induction (planner module) and self-learning to the basic ReAct agent paradigm
- [[knowledge-graph-question-answering]] — solves: SymAgent's primary benchmark task; outperforms prior methods across three KGQA datasets
- [[knowledge-graph]] — uses: KG serves as both the structured knowledge source and the dynamic environment the agent evolves
- [[multi-hop-reasoning]] — uses: symbolic rules explicitly represent multi-hop relational chains guiding the executor's navigation
- [[reinforcement-learning]] — uses: self-learning framework uses outcome-based rewards and iterative policy updating structurally similar to RL fine-tuning
