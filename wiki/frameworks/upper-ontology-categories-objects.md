---
aliases: []
also_type: []
applies:
- knowledge-representation
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 1
date_created: '2026-06-09'
date_updated: '2026-06-09'
domain:
- knowledge-representation
id: pkis:framework:upper-ontology-categories-objects
knowledge_type: framework
maturity: evolving
needs_canonical_source: false
related_concepts: []
sources:
- russell-norvig-aima-ch10
specializes:
- formal-ontology
tags:
- ontology
- categories
- taxonomy
- inheritance
- natural-kinds
- substances
- first-order-logic
- ontological-engineering
title: Upper Ontology of Categories and Objects
understanding: 0
---

## Definition
An upper ontology is a domain-independent framework of the most general concepts — Categories, Objects, Substances, Events, Time, Space, Measures — from which any special-purpose ontology can be specialized by adding domain axioms. The convention (Russell & Norvig, AIMA Ch.10, Fig.10.1) draws general concepts at the top with specializations below, each link asserting that a lower concept is a specialization of an upper one; specializations need not be disjoint (a human is both an animal and an agent).

## Core constructs
- **Categories represented in FOL two ways**: as predicates (Basketball(b)) or, by reification, as objects (b ∈ Basketballs), enabling statements *about* categories (Dogs ∈ DomesticatedSpecies — a category of categories). Much reasoning happens at the category level even though interaction occurs at the level of individuals.
- **Taxonomic hierarchy**: Subset/subclass relations organize categories into a taxonomy; properties propagate by inheritance (apples inherit edibility from Food).
- **Category relations**: Disjoint, ExhaustiveDecomposition, and Partition (= disjoint exhaustive decomposition); categories defined by necessary-and-sufficient conditions (bachelor = unmarried adult male).
- **PartOf hierarchy**: transitive, reflexive part–whole structure distinct from subset; composite objects characterized by structural relations among parts; BunchOf (composite of definite parts but no structure) defined via logical minimization (the smallest object having the elements as parts).
- **Measures**: abstract measure objects with a units function (Length(L1)=Inches(1.5)=Centimeters(3.81)); the load-bearing property is ordering, not numerical value (basis of qualitative physics).
- **Natural kinds**: most real-world categories lack strict definitions (Wittgenstein's family resemblances, Quine's critique of 'bachelor'); handled by separating what holds of *all* instances from what holds of *typical* instances via a Typical(c) ⊆ c subclass.
- **Stuff vs. things**: count nouns (aardvarks) vs. mass nouns (butter); a substance is a category whose definition uses only *intrinsic* properties (preserved under subdivision — density, flavor), whereas a count noun's definition includes *extrinsic* properties (weight, shape).

## Status
General ontological engineering has had limited success; no top AI application uses a general ontology ("every ontology is a treaty" — Gruber). Existing large ontologies (CYC, DBpedia, SUMO, OpenCyc, Google Knowledge Graph) were built by hand-authoring, database import, text extraction, or crowdsourcing.

## Reading Path
- [[russell-norvig-aima-ch10]] — §10.1–10.2: general/upper ontology, categories, objects, substances, measures, natural kinds

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[formal-ontology]] — specializes: an upper ontology is a particular, most-general kind of formal ontology
- [[knowledge-representation]] — applies: an upper ontology is the content-level apparatus of KR — organizing what to represent
[To be populated during integration]