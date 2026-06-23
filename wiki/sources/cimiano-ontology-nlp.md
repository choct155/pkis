---
abbrev: "OBI"
id: "pkis:source:cimiano-ontology-nlp"
aliases: ["Ontology-Based Interpretation of Natural Language"]
title: "[OBI Cimiano et al] Ontology-Based Interpretation of Natural Language"
authors: "Philipp Cimiano, Christina Unger, John McCrae"
year: 2014
type: book
domain: [knowledge-representation, symbolic-subsymbolic]
tags: [ontology, natural-language-processing, semantic-web, description-logic, sparql, rdf, owl, compositional-semantics, question-answering, lexicon]
source_url: ""
drive_id: "1QFL9U6fE9zo8jOAILFwqvs4xjDYags-w"
drive_path: "PKIS/sources/books/cimiano-ontology-nlp.pdf"
isbn: "978-3-031-01026-2"
toc_source: "manual"
status: unread
date_added: 2026-05-20
concepts: ["[[formal-ontology]]", "[[description-logic]]", "[[ontology-lexicon]]", "[[discourse-representation-theory]]", "[[lexicalized-tree-adjoining-grammar]]", "[[semantic-parsing]]", "[[sparql]]", "[[rdf]]", "[[ontology-reasoning]]", "[[knowledge-graph]]", "[[knowledge-graph-question-answering]]"]
---

## Summary

This book presents a principled, modular framework for ontology-based interpretation of natural language — a pipeline in which a formal domain ontology stands at the center of the NLP process rather than being an afterthought. The core argument is that a machine cannot robustly understand natural language without committing to a domain conceptualization: the ontology scopes and guides interpretation, fixing the type, structure, and granularity of the semantic representations being constructed.

The approach works through four interacting components. First, domain knowledge is formalized as a formal ontology expressed in Description Logic (OWL DL or OWL 2 DL). Second, an *ontology lexicon* in the *lemon* model specifies how ontology concepts, relations, and instances are realized in natural language — declaratively and theory-neutrally. Third, domain-specific grammars are automatically generated from the lexicon; these grammars use Lexicalized Tree Adjoining Grammars (LTAG) for syntactic representation and Dependency-based Underspecified Discourse Representation Structures (DUDES) for semantic composition. Fourth, ontological reasoning (via a DL reasoner) resolves ambiguities in parsed sentences by pruning readings inconsistent with ontology constraints.

A worked application throughout is a question answering system over RDF/SPARQL data for a soccer domain. Chapter 8 shows how temporal expressions are handled via a reusable *time ontology* module; Chapter 9 demonstrates how composed semantic representations are translated to SPARQL queries and executed against an RDF knowledge base. The book is published in the Springer *Synthesis Lectures on Human Language Technologies* series (Lecture #24) and covers the OWL and RDF standards extensively as shared vocabulary between NLP and Semantic Web communities.

## Key Knowledge Objects

- [[formal-ontology]] (concept, high) — explicit, formal, shared conceptualization of a domain; the axiomatized logical theory at the center of interpretation
- [[description-logic]] (concept, high) — family of decidable fragments of FOL underlying OWL/OWL 2 ontology languages; ALC, SHOIN(D), SROIQ(D)
- [[ontology-lexicon]] (concept, high) — declarative specification of how ontology vocabulary is verbalized in natural language; the lemon model is the primary instantiation
- [[discourse-representation-theory]] (framework, high) — formal theory of natural language semantics based on discourse referents and conditions; extended as DUDES for ontology alignment
- [[lexicalized-tree-adjoining-grammar]] (framework, moderate — could be technique) — grammar formalism using elementary trees with lexical anchors; used for syntactic representations aligned to ontology
- [[semantic-parsing]] (technique, high) — translating natural language sentences into formal meaning representations (SPARQL, logical form) aligned to a target ontology or KB
- [[sparql]] (technique, high) — already exists; used as the target formal query language in the NL QA pipeline
- [[ontology-reasoning]] (technique, high) — already exists; DL reasoning over OWL ontologies used here for ambiguity resolution
- [[knowledge-graph-question-answering]] (problem, high) — already exists; ch9 instantiates the full pipeline for NL QA over RDF/SPARQL
- [[rdf]] (concept, high) — already exists; the data representation standard underpinning the QA application
- [[knowledge-graph]] (concept, high) — already exists; RDF knowledge bases constitute the structured data queried in ch9

## Key Extractions

1. **Core architecture:** "Our approach to ontology-based interpretation of natural language puts an ontology at the center of the interpretation process, in order to scope and guide that process in a principled fashion. The level of representational granularity at which the meaning of natural language is captured is not driven by language, but by the semantic distinctions made in an ontology." (ch1, §1.1)

2. **lemon model:** The *Lexicon Model for Ontologies* (lemon) provides a theory-neutral, RDF-publishable declarative specification of the lexicon-ontology interface. A lexicon engineer unfamiliar with grammar formalisms or formal semantics can create a lemon lexicon purely by specifying how words correspond to ontology entities — the domain-specific grammar is then automatically generated from this lexicon. (ch4)

3. **Description logic hierarchy:** The book covers three DL fragments for OWL — ALC (basic, no nominals/concrete domains), OWL DL (SHOIN(D), adds nominals and concrete domains), and OWL 2 DL (SROIQ(D), adds role chaining and reflexive/transitive/asymmetric role axioms). OWL 2 DL is the recommended standard for expressive domain ontologies. (ch2, §2.3)

4. **Ambiguity resolution via reasoning:** Ontological type constraints can automatically prune inconsistent readings of syntactically ambiguous sentences. For example, if "won" can be a transitive verb over entities of type Team but not Person, the reasoner eliminates the reading where a player is the winning agent. Ambiguities are represented either by full enumeration of alternatives or by underspecification (ch7, §7.2).

5. **DUDES composition:** DUDES (Dependency-based Underspecified Discourse Representation Structures) pairs syntactic (LTAG) and semantic (DRT) representations, enabling compositional construction of ontology-aligned meanings from lexical entries through grammatical combination. (ch3, §3.6)

6. **QA pipeline over SPARQL:** A natural language question is parsed and compositionally interpreted into a DUDES; the DUDES is then mapped to a SPARQL SELECT query; the query is executed against an RDF triplestore; and answers are returned as bindings. The key challenge is entity linking (mapping NL mentions to RDF URIs) and handling incompleteness of the knowledge base. (ch9)

7. **Guarino's formal definition of ontology:** An ontology is "a logical theory accounting for the intended meaning of a formal vocabulary, i.e., its ontological commitment to a particular conceptualization of the world." Crucially, an ontology rules out *unintended* model-theoretic interpretations — its models should correspond precisely to situations possible within the target conceptualization. (ch2, §2.1)

## Chapters
- [[cimiano-ontology-nlp-ch01]] — Ch. 1 — Introduction
- [[cimiano-ontology-nlp-ch02]] — Ch. 2 — Ontologies
- [[cimiano-ontology-nlp-ch03]] — Ch. 3 — Linguistic Formalisms
- [[cimiano-ontology-nlp-ch04]] — Ch. 4 — Ontology Lexica
- [[cimiano-ontology-nlp-ch05]] — Ch. 5 — Grammar Generation
- [[cimiano-ontology-nlp-ch06]] — Ch. 6 — Putting Everything Together
- [[cimiano-ontology-nlp-ch07]] — Ch. 7 — Ontological Reasoning for Ambiguity Resolution
- [[cimiano-ontology-nlp-ch08]] — Ch. 8 — Temporal Interpretation
- [[cimiano-ontology-nlp-ch09]] — Ch. 9 — Ontology-Based Interpretation for Question Answering
- [[cimiano-ontology-nlp-ch10]] — Ch. 10 — Conclusion
## Connection Candidates

- [[ontology-reasoning]] — extends: this book extends the basic Datalog/chase view of ontological reasoning to DL-based OWL reasoning for disambiguation; the reasoner here is a tableau-based DL reasoner rather than a Datalog chase engine
- [[sparql]] — uses: the NL interpretation pipeline ultimately produces SPARQL queries as its output representation; SPARQL is both the target language and the interface to the RDF data layer
- [[rdf]] — uses: the domain knowledge base and all ontology resources (lemon lexicon, time ontology) are published in RDF; RDF is the shared data model
- [[knowledge-graph-question-answering]] — grounds: this book provides the formal compositional semantics pipeline underlying NL QA; contrasts with neural KGQA by being fully rule-based and interpretable
- [[neurosymbolic-ai]] — specializes: the pipeline is a classical symbolic NLP system; it represents the symbolic end of the neurosymbolic spectrum (no neural components), relevant as baseline/contrast
- [[knowledge-graph]] — uses: the domain ontology + RDF data constitute the knowledge graph; the interpretation pipeline is the NL interface to that graph
- [[linked-open-data]] — uses: ch1 §1.3 discusses the Semantic Web and LOD as the context into which this approach scales; lemon lexica are published as LOD resources
