---
title: "Towards Cognitive AI Systems: A Survey and Prospective on Neuro-Symbolic AI"
authors: "Zishen Wan, Che-Kai Liu, Hanchen Yang, Chaojian Li, Haoran You, Yonggan Fu, Cheng Wan, Tushar Krishna, Yingyan Lin, Arijit Raychowdhury"
year: 2023
type: paper
domain: [symbolic-subsymbolic, deep-learning]
tags: [neurosymbolic, survey, cognitive-ai, hardware-architecture, system-profiling, taxonomy, probabilistic-reasoning]
source_url: ""
drive_id: "1cLUp9vohN0GllF3FnZB-JLxWoIyZYVW6"
drive_path: "PKIS/sources/papers/Towards Cognitive AI Systems - A Survey and Prospective on Neuro-Symbolic AI - Wan, Liu, Yang et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[kautz-nsai-taxonomy]]", "[[logic-tensor-networks]]", "[[logical-neural-networks]]", "[[neuro-vector-symbolic-architecture]]"]
---

## Summary

This Georgia Tech workshop paper provides the first systematic survey of NSAI from a *systems and hardware architecture* perspective, distinct from prior surveys that focus exclusively on algorithms. The paper categorizes recent NSAI algorithms using Kautz's six-type taxonomy (Symbolic[Neuro], Neuro|Symbolic, Neuro:Symbolic→Neuro, NeuroSymbolic, Neuro[Symbolic]) and then performs runtime profiling of three representative systems — Logical Neural Networks (LNN), Logic Tensor Networks (LTN), and Neuro-Vector Symbolic Architecture (NVSA) — on commodity hardware. Key finding: symbolic workloads are *not* negligible in compute latency and can dominate system runtime (NVSA's symbolic component accounts for 92.1% of total runtime due to sequential rule detection). The paper identifies five major research challenges: building ImageNet-like NSAI benchmark datasets, unifying neuro-symbolic-probabilistic models, developing modular software frameworks for logical reasoning, benchmarking diverse NSAI workloads, and designing novel hardware architectures with heterogeneous compute units suited to the irregular memory access and control-flow patterns of symbolic workloads. The work positions NSAI as the "third wave of AI" following expert systems and deep learning.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — primary subject; taxonomy, profiling, and architecture challenges
- [[kautz-nsai-taxonomy]] (concept, high) — Kautz's six-type classification of NSAI systems; foundational taxonomy used across the field
- [[logic-tensor-networks]] (technique, high) — LTN: symbolic logic rules as soft constraints via fuzzy logic on tensor representations
- [[logical-neural-networks]] (technique, high) — LNN: each neuron encodes a weighted real-valued logic formula; bidirectional inference
- [[neuro-vector-symbolic-architecture]] (technique, high) — NVSA: neural perception frontend + hyperdimensional symbolic reasoning backend
- [[inductive-logic-programming]] (technique, high) — ILP as foundational NSAI learning approach; differentiable ILP discussed
- [[probabilistic-logic-programming]] (technique, moderate — could be framework) — DeepProbLog and NeuPSL as probabilistic NSAI methods

## Key Extractions

1. **Kautz taxonomy**: Six types — Symbolic[Neuro] (AlphaGo), Neuro|Symbolic (NVSA, NeuPSL), Neuro:Symbolic→Neuro (LNN, differentiable ILP), NeuroSymbolic (LTN), Neuro[Symbolic] (GNN+attention).
2. **Runtime dominance finding**: "The symbolic workload dominates the NVSA's runtime, predominately due to the sequential and computational-intensive rule detection during the involved reasoning procedure" (92.1% of total runtime).
3. **Scaling bottleneck**: "When the test set size increases from 2×2 to 3×3, the symbolic workload runtime percentage only increases from 92.06% to 94.71%, but the total runtime of the NVSA model increases by 5.02×, indicating the potential scalability bottleneck of NSAI models."
4. **Hardware gap**: NSAI workloads feature "much greater heterogeneity in compute kernels, sparsity, irregularity in access patterns, and higher memory intensity than current DNN workloads," creating a divergence with hardware roadmaps optimized for matrix multiplication.
5. **Software fragmentation**: "Most NSAI system implementations create custom software for deduction for the particular logic used, which limits modularity and extensibility."

## Connection Candidates

- [[neurosymbolic-ai]] — extends: adds systems/hardware perspective to the existing algorithmic taxonomy
- [[graph-neural-networks]] — uses: GNNs with attention classified as Neuro[Symbolic] type 6 in Kautz taxonomy
- [[inductive-logic-programming]] — prerequisite-of: ILP understanding needed to evaluate differentiable NSAI approaches
- [[logic-tensor-networks]] — uses: LTN profiled as representative NeuroSymbolic system
- [[probabilistic-logic-programming]] — related: NeuPSL and DeepProbLog are classified NSAI variants
