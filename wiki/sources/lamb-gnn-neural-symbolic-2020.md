---
id: "pkis:source:lamb-gnn-neural-symbolic-2020"
aliases: []
title: "Graph Neural Networks Meet Neural-Symbolic Computing: A Survey and Perspective"
authors: "Luis C. Lamb, Artur d'Avila Garcez, Marco Gori, Marcelo O.R. Prates, Pedro H.C. Avelar, Moshe Y. Vardi"
year: 2020
type: paper
domain: [symbolic-subsymbolic, deep-learning, knowledge-representation]
tags: [neurosymbolic, graph-neural-networks, survey, logic-tensor-networks, kautz-taxonomy, combinatorial-optimization, message-passing, relational-reasoning, attention-mechanisms]
source_url: "https://arxiv.org/abs/2003.00330"
drive_id: "1H88GHk0hs5-NH3qLK5Ytmh6gG9qF3acY"
drive_path: "PKIS/sources/papers/Graph Neural Networks Meet Neural-Symbolic Computing - A Survey and Perspective - Lamb, Garcez, Gori et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[graph-neural-networks]]", "[[neurosymbolic-ai]]", "[[logic-tensor-networks]]", "[[kautz-nsai-taxonomy]]", "[[graph-convolutional-networks]]", "[[message-passing-neural-networks]]"]
---

## Summary

This IJCAI 2020 survey by Lamb, Garcez, Gori et al. reviews the relationship between Graph Neural Networks (GNNs) and Neural-Symbolic Computing (NSC), arguing that GNNs are a natural model of neural-symbolic computation. The paper opens with Kautz's six-type taxonomy, locating GNNs as Type 1 (Symbolic Neuro Symbolic: input/output are symbolic) while Logic Tensor Networks are Type 5 (NeuroSymbolic: symbolic rules as soft constraints via tensor embeddings). The technical core covers: (1) Logic Tensor Networks and their tensorization approach to FOL; (2) Pointer Networks as attention-based combinatorial reasoners; (3) Graph Convolutional Networks (GCNs) as attention layers over non-Euclidean data; (4) Graph Attention Networks (GATs); (5) GNNs for combinatorial optimization (SAT, TSP, graph coloring). The paper argues that the permutation invariance and structural flexibility of GNNs make them natural candidates for Type 6 (Neuro[Symbolic]) systems — capable of true symbolic reasoning inside a neural engine. The attention mechanism emerges as the critical bridge: GNN-with-attention can encode symbolic rules by selectively aggregating relevant neighbors, enabling soft reasoning about graph-structured symbolic expressions. The paper concludes with a research agenda for combining GNNs with NSC for sound and explainable AI systems.

## Key Knowledge Objects

- [[graph-neural-networks]] (technique, high) — primary subject; GCN, GAT, GNN for combinatorial optimization
- [[neurosymbolic-ai]] (framework, high) — GNNs positioned as natural neural-symbolic computing models
- [[logic-tensor-networks]] (technique, high) — LTN: tensorization of FOL as soft constraints; Type 5 NSC
- [[kautz-nsai-taxonomy]] (concept, high) — six-type taxonomy used to position GNNs within NSC landscape
- [[graph-convolutional-networks]] (technique, high) — GCN as generalization of CNNs to non-Euclidean data; core GNN building block
- [[message-passing-neural-networks]] (technique, high) — the iterative neighborhood aggregation paradigm underlying GNNs
- [[combinatorial-optimization-with-gnns]] (technique, moderate — could be problem) — GNNs applied to SAT, TSP, graph coloring; neural approach to NP-hard combinatorial problems
- [[pointer-networks]] (technique, high) — attention-based architecture for combinatorial problems; inputs and outputs are sets

## Key Extractions

1. **GNNs as Type 1 NSC**: "The origin of GNNs can be traced back to neural-symbolic computing (NSC) in that both sought to enrich the vector representations in the inputs of neural networks, first by accepting tree structures and then graphs more generally." According to Kautz's taxonomy, GNNs are Type 1 neural-symbolic.
2. **GCN formulation**: `x_i^(k+1) = σ( Σ_{j∈N(i)∪{i}} θ_k · x_j^(k) / √(deg(i)·deg(j)) )` — each node aggregates linearly-transformed, degree-normalized representations from its neighborhood.
3. **Permutation invariance**: "NSC architectures often combine the key design concepts from convolutional networks and attention-based architectures to enforce permutation invariance over the elements of a set or the nodes of a graph."
4. **Attention-symbolic bridge**: "Attention mechanisms can be leveraged to incorporate symbolic rules into GNN models, enabling selective attention to pertinent symbolic information in the graph." This positions GNNs as candidates for Type 6 (full symbolic reasoning in a neural engine).
5. **Tensorization as Type 5**: Logic Tensor Networks embed FOL symbols (constants, predicates, rules) as real-valued tensors, acting as soft constraints (regularizers) on the network's loss function — Type 5 in Kautz taxonomy.

## Connection Candidates

- [[graph-neural-networks]] — extends: places GNNs within the neural-symbolic framework; new applications in combinatorial reasoning
- [[neurosymbolic-ai]] — uses: GNNs are proposed as the architectural basis for Type 6 neural-symbolic systems
- [[logic-tensor-networks]] — uses: LTNs as the canonical Type 5 NSC example; FOL tensorization approach
- [[message-passing-neural-networks]] — specializes: GCN/GAT implement specific message-passing strategies
- [[knowledge-graph]] — uses: relational reasoning over KG-structured data is a core GNN application domain
- [[inductive-bias]] — uses: GNN permutation invariance is a structural inductive bias enabling graph-level generalization
