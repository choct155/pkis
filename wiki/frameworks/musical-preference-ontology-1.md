---
aliases:
- music taste framework
- musical preference profile
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 0
date_created: '2026-06-28'
date_updated: '2026-06-28'
domain:
- knowledge-representation
- personal-epistemology
- music
id: pkis:framework:musical-preference-ontology-1
instantiates:
- exploration-exploitation-tradeoff
knowledge_type: framework
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- music
- ontology
- personal-epistemology
- taste
- agent-instructions
- discovery
- mcmc-analogy
title: Musical Preference Ontology
understanding: 0
uses:
- preference-elicitation
---

## Definition
A lightweight personal ontology for articulating musical preference with enough precision to instruct AI agents to discover and retrieve music. Developed inductively from exemplars through structured conversation, the framework distinguishes primary dimensions (properties that directly drive preference), contextual dimensions (properties that enrich the experience without being primary drivers), and navigational heuristics (priors for efficient exploration of the preference space).

Primary dimensions: kinetic character, spaciousness, craft density, mastery legibility.
Contextual dimensions: genealogical depth, conceptual reach.
Navigational heuristics: creative ecosystem membership, exploration/exploitation calibration.

The framework treats music discovery as a posterior estimation problem — the latent variable is preference, the exemplar set is the observed data, and agent instructions operationalize a proposal distribution that balances exploitation of known high-density regions with calibrated exploratory moves into adjacent lower-density territory. This connects directly to MCMC framing (Metropolis-Hastings) as a model for how taste discovery works over time.

Key distinctions developed in the framework:
- Craft density is an objective property of the work; mastery legibility is relational (listener-dependent).
- Utility fit (how well a track serves the current context) is separable from intrinsic regard (how much the work is valued independent of context).
- Kinetic character is explicitly situational — a query parameter varying with listening context, not a fixed preference.
- Creative ecosystem is a navigational heuristic, not a sonic property — it operates as a high-value prior for discovery.

Primary listening contexts mapped to dimension weights: walking/city ambulation (high kinetic character, high mastery legibility, craft density), focused desk work (spaciousness, moderate kinetic energy, instrumental), analytic/reading (intrinsic regard, conceptual reach, tolerates static kinetic character).

Mastery legibility is highest in: rap/hip-hop, West African music, spiritual/avant-garde jazz (Sun Ra/Coltrane/Heliocentric lineage).

## Reading Path
[To be populated when a canonical source is attached]

## Connections
- [[exploration-exploitation-tradeoff]] — instantiates: graph-gaps: wire orphan
- [[preference-elicitation]] — uses: graph-gaps: wire orphan
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]