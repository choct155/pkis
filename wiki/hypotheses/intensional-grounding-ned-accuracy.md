---
aliases: []
cluster_membership:
- intensional-grounding
date_created: 2026-05-30
date_updated: '2026-06-30'
dependent_nodes:
- node: '[[named-entity-disambiguation]]'
  node_type: technique
  rationale: Addressing this hypothesis requires implementing and evaluating NED systems
- node: '[[transformer-attention-mechanisms]]'
  node_type: technique
  rationale: The umbrella thesis claims ontological structure operates through attention
    redistribution — testing this requires understanding attention mechanisms
- node: '[[ontology]]'
  node_type: concept
  rationale: Ontological class definitions are the independent variable in this hypothesis
domain:
- knowledge-representation
- deep-learning
evidence_nodes: []
id: pkis:hypothesis:intensional-grounding-ned-accuracy
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: intensional-grounding
research_program_role: direct-test
status: open
tags:
- named-entity-disambiguation
- ontology
- intensional-grounding
title: Token-to-Ontological-Class Distance Predicts NED/NER Accuracy
uses:
- named-entity-disambiguation
- transformer-attention-mechanisms
- formal-ontology
---

## Formal Statement
Token-to-ontological-class distance — measured as the semantic distance between a surface token and its candidate ontological class assignments in the embedding space — predicts NED/NER accuracy: entities with closer token-to-class distance are resolved correctly at higher rates than those with greater distance.

## Motivation
If ontological structure operates through attention weight redistribution, then the degree to which a token is already semantically proximate to its correct ontological class in the model's representation should predict whether the model resolves it correctly. This is a clean, testable operationalization of the umbrella thesis.

## Current Evidence
Experimental platform identified: OpGraph (a private, local operational-graph system) is being instrumented as the live test bed. Design: every Librarian capture draft that requires human correction in the review workbench produces a single ground-truth label per entity mention. Six resolution strategies are then run as parallel offline voters against the same historical utterances and that single ground truth, decoupled from the live operational resolution path (which uses a separate fast default-or-waterfall policy for production use, informed by but not blocking on the comparative results). Ground truth is established once per mention; all strategies are scored against it asynchronously, which keeps the comparative program off the synchronous capture path — important while running CPU-only pending a GPU upgrade.

The six strategies under comparison, in increasing order of reliance on intensional/structural signal vs. lexical signal: (1) alias lookup — exact/fuzzy match against a maintained alias registry (lexical/extensional baseline); (2) fuzzy string similarity (Levenshtein/Jaro-Winkler) — lexical, generalizes slightly beyond exact alias match; (3) structural/graph priors — using existing edges, roles, and organizational context as evidence (the most direct operationalization of intensional/ontological-class distance); (4) vector/embedding similarity — semantic but not explicitly ontological; (5) LLM-as-resolver — given mention, context, and a candidate shortlist, ask a local model to resolve; (6) implicit instantiation from context/co-occurrence — inferring entity identity (or, in the hardest variant, inferring that an entity exists at all) from contextual and co-occurrence signal without requiring an explicit alias or lexical match, particularly for indirect referring expressions ("my boss", "the budget owner") that have no lexical overlap with any stored alias.

Strategy (6) carries particular priority: a colleague holds the explicit prior that context/co-occurrence-driven implicit instantiation will outperform alias-based resolution specifically, motivating early instrumentation to test this empirically rather than letting the disagreement sit unresolved. Strategies (3) and (6) are the most direct tests of this hypothesis's core claim (intensional/structural signal predicts resolution accuracy); (1) and (2) serve as the lexical/extensional baseline the hypothesis predicts will underperform, particularly on indirect referring expressions where lexical methods cannot work in principle.

## Open Questions
Comparative design questions raised during OpGraph instrumentation: (1) Is implicit instantiation (strategy 6) limited to resolving a mention to an EXISTING entity via context, or does it extend to inferring that an entity exists at all with no explicit mention? The latter is a distinct and harder capability (entity creation from implicit signal, not just entity resolution) — needs to be scoped explicitly before scoring, since conflating the two would muddy the comparison. (2) How is ground truth established for mentions where even the human reviewer is uncertain which existing entity is meant — does this produce a discard category, a soft/probabilistic label, or a forced choice? (3) Stratify comparison by mention type (explicit named mention vs. indirect referring expression) since the hypothesis predicts the lexical/intensional gap should be largest specifically for indirect expressions — confirm this stratification is built into the scoring design from the start rather than added post hoc. (4) Need an explicit owner/process for collecting, organizing, and analyzing this comparative data on an ongoing basis — not just one-off scoring runs (see new Lab Assistant agent role, both in OpGraph and as a PKIS Lab Mode counterpart).

## Connections
- [[formal-ontology]] — uses: Ontological class definitions are the independent variable; the [[ontology]] reference resolves to the materialized formal-ontology node.
- [[transformer-attention-mechanisms]] — uses: Token-to-class distance is operationalized through the attention mechanism the hypothesis claims as the channel.
- [[named-entity-disambiguation]] — uses: NED/NER is the task whose accuracy the hypothesis predicts from token-to-class distance.
- [[intensional-grounding]] — belongs-to: this is a constituent hypothesis of the Intensional Grounding cluster

## Task Grounding
Mechanism claim: token-to-ontological-class distance predicts NED/NER accuracy.

Task outcome claim: providing explicit intensional structure at inference time improves entity disambiguation accuracy on private markets documents, measured by NED/NER F1 against ground-truth entity resolution.

Deployment context: financial data manufacturing where entity disambiguation errors propagate through downstream analytics and are costly to correct manually.

Why the scale foil fails at the task level: Scale-based disambiguation relies on distributional similarity in pre-training data. Private markets entities are sparse in pre-training corpora, surface form variation is high (fund names, GP names, portfolio company abbreviations), and new entities appear continuously. Ontological class membership provides normative constraints that are robust to surface form variation and do not require pre-training exposure.