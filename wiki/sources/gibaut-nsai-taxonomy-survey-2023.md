---
id: "pkis:source:gibaut-nsai-taxonomy-survey-2023"
aliases: []
title: "Neurosymbolic AI and Its Taxonomy: A Survey"
authors: "Wandemberg Gibaut, Leonardo Pereira, Fabio Grassiotto, Alexandre Osorio, Eder Gadioli, Amparo Munoz, Sildolfo Gomes, Claudio Filipi Goncalves do Santos"
year: 2023
type: paper
domain: [symbolic-subsymbolic, deep-learning, knowledge-representation]
tags: [neurosymbolic, survey, taxonomy, logic-tensor-networks, neural-logic-machines, logical-boltzmann-machines, logical-neural-networks, inductive-logic-programming, fuzzy-logic]
source_url: "https://arxiv.org/abs/2305.08876"
drive_id: "1CJI-9K7RO7z3MVCVmzwht8Y3-O8PlHKu"
drive_path: "PKIS/sources/papers/Neurosymbolic AI and Its Taxonomy - A Survey - Gibaut, Pereira, Grassiotto et al.pdf"
status: unread
date_added: 2026-05-20
concepts: ["[[neurosymbolic-ai]]", "[[logic-tensor-networks]]", "[[logical-neural-networks]]", "[[neural-logic-machines]]", "[[logical-boltzmann-machines]]", "[[inductive-logic-programming]]"]
---

## Summary

This survey from Eldorado Institute of Technology covers neurosymbolic AI systems published from 2019 onward, focusing on Knowledge Representation, Learning, Reasoning, Explainability, and Applications. It provides a detailed technical treatment of five core frameworks: Logic Tensor Networks (LTN), Neural Logic Machines (NLM), Logical Neural Networks (LNN), Logical Boltzmann Machines (LBM), and the Neuro-Symbolic Concept Learner (NS-CL). The taxonomy is organized around how each framework handles knowledge representation (symbolic vs. distributed), learning (inductive logic programming, hybrid learning, curriculum learning), and reasoning (deductive, inductive, abductive). The paper grounds its framing in Physical Symbol System Hypothesis (Newell and Simon) and Kahneman's System 2 argument. A distinguishing contribution is the coverage of applications — bearing fault diagnosis (LTN), NLP entity linking (LNN), visual question answering (NS-CL), and reinforcement learning text games (LNN) — demonstrating that NSAI frameworks are moving beyond toy benchmarks. The survey also explicitly covers the connection between LTN's differentiable fuzzy logic and the broader Differentiable Fuzzy Logic (DFL) framework, and analyzes how LBMs exploit the equivalence between propositional logic satisfiability and energy minimization in Restricted Boltzmann Machines.

## Key Knowledge Objects

- [[neurosymbolic-ai]] (framework, high) — survey covers NSAI taxonomy, learning paradigms, reasoning, and applications
- [[logic-tensor-networks]] (technique, high) — Real Logic: fuzzy semantics (truth values in [0,1]) as differentiable first-order logic
- [[logical-neural-networks]] (technique, high) — LNN: truth bounds in FOL with bidirectional inference; weighted real-valued logic
- [[neural-logic-machines]] (technique, high) — NLM: probabilistic tensor representation for logic predicates; inductive relational learning
- [[logical-boltzmann-machines]] (technique, high) — LBM: maps propositional logic to energy minimization in Restricted Boltzmann Machines
- [[inductive-logic-programming]] (technique, high) — foundational NSAI learning paradigm; bottom-up and top-down approaches covered
- [[neuro-symbolic-concept-learner]] (technique, high) — NS-CL: perception + semantic parser + symbolic executor for visual QA without explicit supervision
- [[differentiable-fuzzy-logic]] (concept, high) — DFL: employs fuzzy logic with differentiable operators; LTNs as instances thereof
- [[physical-symbol-system-hypothesis]] (concept, moderate — could be principle) — Newell and Simon's foundational hypothesis about symbols as requirements for intelligence

## Key Extractions

1. **LTN Real Logic**: "Real Logic, simply put, is a way of representing symbolic knowledge so that it can be applied in a Machine Learning environment. Its main goal is to achieve a vector-based representation technique which should be shown adequately for integrating machine learning and symbolic reasoning in a grounded way." Truth values are in [0,1] (fuzzy), enabling gradient-based optimization of logical satisfiability.
2. **LNN bounds**: "The bounds of a universal quantifier node are set to the bounds of the grounding with the lowest upper bound, so that if all of its groundings are True then the universal statement is also True." LNN introduces both universal and existential quantifiers into weighted real-valued logic.
3. **LBM energy equivalence**: LBMs exploit "the equivalence between the logical satisfiability of formulas and the energy minimization in Restricted Boltzmann Machines." Each propositional logic formula is mapped to Strict Disjunctive Normal Form, with the knowledge base reflected in the RBM topology.
4. **NLM challenges addressed**: Lifted rule learning (generalizing beyond specific objects), high-order relational data with quantifiers, curse-of-dimensionality in rule learning, and minimal learning priors.
5. **NS-CL curriculum learning**: The system "starts by learning concepts or representations of individual objects from short questions on simple scenes... The next step is learning relational concepts by leveraging object-based concepts to interpret object referrals," mirroring developmental stages.

## Connection Candidates

- [[neurosymbolic-ai]] — extends: adds 2019-2023 application coverage and comparative taxonomy to prior surveys
- [[inductive-logic-programming]] — uses: ILP is the foundational learning paradigm for several NSAI frameworks
- [[graph-neural-networks]] — uses: NLM uses GNN-like architectures for relational learning; NS-CL uses GNNs for scene representation
- [[logic-tensor-networks]] — specializes: LTN is one specific instance of the differentiable fuzzy logic paradigm
- [[differentiable-fuzzy-logic]] — grounds: DFL provides the theoretical basis for LTN and other soft-constraint NSAI methods
