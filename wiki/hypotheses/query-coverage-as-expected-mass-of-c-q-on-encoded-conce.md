---
aliases: []
cluster_membership:
- retrieval-inference-tradeoff
date_created: '2026-06-13'
date_updated: '2026-06-13'
dependent_nodes: []
domain:
- knowledge-representation
- bayesian-stats
evidence_nodes: []
id: pkis:hypothesis:query-coverage-as-expected-mass-of-c-q-on-encoded-conce
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: retrieval-inference-tradeoff
research_program_role: direct-test
status: open
tags:
- coverage
- query-distribution
- concept-retrieval
- sufficiency
- information-theoretic
title: Query Coverage as Expected Mass of C(q) on Encoded Concept Nodes
---

## Formal Statement
Let C(q) be a probability distribution over all concepts, where P(c|q) represents the contribution of concept c to answering query q. Let G be a graph with encoded concept nodes.

Define coverage of q by G as:

Coverage(q, G) = Σ_c P(c|q) · 1[c ∈ G]

Each concept node in G is a Bernoulli trial against C(q) — it either covers a concept in the support of P(c|q) or it does not.

Define marginal information gain from adding concept node c to retrieved set S as:

ΔI(q; c | S) = I(q; c, S) − I(q; S)

Retrieval proceeds by adding nodes in order of marginal gain until ΔI(q; c | S) < ε for some sufficiency threshold ε.

The architectural claim: a multipartite concept graph achieves higher Coverage(q, G) at lower expected token cost than a document graph, because concept nodes are scoped to individual units in C(q) while documents spread probability mass across many concepts simultaneously, most irrelevant to q.

## Motivation
C(q) is not directly observable — it must be approximated via semantic bridging from query tokens to concept nodes. This approximation is a separable problem from coverage computation itself. Conditional on the bridging step resolving correctly, coverage is computable as the mass of C(q) falling on encoded nodes. The sufficiency threshold ε is a design parameter that trades completeness against token cost — setting it appropriately is an empirical question about the query distribution.

## Current Evidence
Qualitative: the PE multiple example demonstrates that C(q) for even a simple financial query spans multiple concepts — PE ratio definition, index membership, company-metric linkage — none of which co-occur cleanly in any single document. Formal: C(q) approximation via semantic distance to concept nodes is standard in entity-linking literature. Quantification against organizational query distribution is an open empirical problem.

## Open Questions
How do we estimate P(c|q) in practice — is this a learned distribution or derived from semantic distance? What is the right sufficiency threshold ε for organizational QA tasks? How does Coverage(q, G) degrade gracefully when G has gaps — does the model recover the missing mass from world knowledge reliably?

## Connections
- [[retrieval-inference-tradeoff]] — belongs-to: constituent hypothesis of the retrieval-inference-tradeoff cluster