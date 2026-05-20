---
title: "Neurosymbolic AI for Reasoning over Knowledge Graphs: A Survey"
authors: "Lauren Nicole DeLong, Ramon Fernández Mir, Jacques D. Fleuriot"
year: 2024
type: paper
domain: [symbolic-subsymbolic, knowledge-representation]
tags: [neurosymbolic, knowledge-graphs, survey, taxonomy, graph-neural-networks, link-prediction, inductive-logic-programming, markov-logic-networks, fuzzy-logic, description-logic, owl, interpretability]
source_url: ""
drive_id: "1utifPgiQcd6VCvvwS56lIHyN0arSEPOx"
drive_path: "PKIS/sources/papers/Neurosymbolic AI for Reasoning over Knowledge Graphs - A Survey - DeLong, Mir, Fleuriot.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[knowledge-graph]]", "[[knowledge-graph-completion]]", "[[graph-neural-networks]]", "[[description-logic]]", "[[markov-logic-networks]]", "[[inductive-logic-programming]]"]
---

## Summary

This University of Edinburgh survey is the first comprehensive treatment of neurosymbolic methods specifically designed for reasoning over knowledge graphs. The authors propose a three-category taxonomy: (1) **logically-informed embedding approaches** — use symbolic inference and deep learning sequentially (pre-trained rules inform embeddings); (2) **embedding approaches with logical constraints** — embeddings are learned subject to logical regularization during training; (3) **rule learning approaches** — logic rules are learned from the KG, often guided by neural scoring. The paper provides extensive background on the logic formalisms used (logic programming/Horn clauses, probabilistic logic/MLNs, fuzzy logic, description logics/OWL) and on GNN architectures as the dominant neural component. The taxonomy is structured around *architecture*: the order and integration of symbolic and neural modules. For each category, the paper analyzes five critical characteristics: interpretability, guided training via rules, encoding of underrepresented types, handling of long-range dependencies, and aggregation of heterogeneous information. Applications covered include drug discovery, social network recommendation, traffic forecasting, and COVID-19 KG completion. The paper concludes with prospective research directions: integrating temporal and spatial reasoning, addressing scalability in large KGs, and improving cross-domain generalization.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — survey of NSAI methods specifically for KG reasoning; new architecture-based taxonomy
- [[knowledge-graph]] (concept, high) — primary domain; covers KG structure, KG completion, and KGE methods
- [[knowledge-graph-completion]] (problem, high) — KGC (link prediction, relation prediction) as the central task motivating most surveyed methods
- [[graph-neural-networks]] (technique, high) — dominant neural component in KG neurosymbolic systems; GCN, R-GCN, GAT covered
- [[description-logic]] (concept, high) — DL-based ontologies (OWL, OWL 2 EL) provide semantic framework for KG reasoning
- [[markov-logic-networks]] (technique, high) — probabilistic FOL grounded over KG entities; key background method
- [[inductive-logic-programming]] (technique, high) — ILP (AMIE, FOIL, Aleph) for rule mining from KGs
- [[knowledge-graph-embedding]] (technique, high) — KGE methods (TransE, DistMult, ComplEx, RESCAL) as the neural component in categories 1 and 2
- [[logically-informed-embedding]] (technique, high) — category 1: pre-computed rules inform the embedding process sequentially

## Key Extractions

1. **Three-category taxonomy**: Logically-informed embeddings (neural and symbolic sequential), embeddings with logical constraints (symbolic regularization during neural training), rule learning approaches (logic rules learned/induced from neural scores).
2. **OWL 2 EL for scalability**: "OWL 2 EL, designed with biomedical ontologies in mind... EL means 'existential language', so in OWL 2 EL we can have existential but not universal quantification. These restrictions enable polynomial time reasoning, which is crucial for large knowledge bases."
3. **KGE comparison**: DeepWalk and node2vec use random walk co-occurrence; TransE represents relations as translations in embedding space; RESCAL, DistMult, ComplEx focus on relational information. DistMult decoder: `score_r(u,v) = eᵤᵀ Rᵣ eᵥ`.
4. **Kautz categories aligned**: Logically-informed embeddings and rule learning align with NEURO:SYMBOLIC→NEURO and NEURO;SYMBOLIC; constraint-based embeddings align with NEUROSYMBOLIC and NEURO[SYMBOLIC].
5. **Interpretability as central criterion**: "Rule-based approaches do not always achieve the same performance [as embedding methods], [but they] allow one to refer back to the rules which governed the algorithm to get a human-readable understanding of how and why certain predictions were made."

## Connection Candidates

- [[neurosymbolic-ai]] — specializes: focuses the general NSAI framework on KG reasoning tasks specifically
- [[knowledge-graph]] — uses: KGs are both the input data structure and the reasoning target for all surveyed methods
- [[knowledge-graph-completion]] — uses: KGC (especially link prediction) is the primary evaluation task
- [[graph-neural-networks]] — uses: GNNs (GCN, R-GCN, GAT) are the dominant neural encoder for KG nodes and edges
- [[description-logic]] — uses: DL-based ontologies provide the symbolic reasoning backbone for logically-informed embedding approaches
- [[markov-logic-networks]] — uses: MLNs ground probabilistic FOL over KG entities; bridge between logic programming and neural learning
- [[owl]] — uses: OWL and OWL 2 EL provide the semantic web standard for ontology-driven KG reasoning
