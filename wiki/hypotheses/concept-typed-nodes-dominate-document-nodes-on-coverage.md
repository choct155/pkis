---
aliases: []
cluster_membership:
- retrieval-inference-tradeoff
date_created: '2026-06-13'
date_updated: '2026-06-13'
dependent_nodes:
- node: pkis:research-cluster:retrieval-inference-tradeoff
  node_type: research-cluster
  rationale: Core cluster this hypothesis belongs to
- node: pkis:concept:mutual-information
  node_type: concept
  rationale: Efficiency metric is defined in terms of mutual information
- node: pkis:concept:conditional-entropy
  node_type: concept
  rationale: Coverage completeness is characterized via conditional entropy
domain:
- knowledge-representation
- bayesian-stats
evidence_nodes: []
id: pkis:hypothesis:concept-typed-nodes-dominate-document-nodes-on-coverage
iks_link: null
knowledge_type: hypothesis
origin: research-program
research_program_cluster: retrieval-inference-tradeoff
research_program_role: direct-test
status: open
tags:
- coverage-per-token
- efficiency
- document-retrieval
- concept-nodes
- cost-model
title: Concept-Typed Nodes Dominate Document Nodes on Coverage-Per-Token Efficiency
---

## Formal Statement
Define Coverage-Per-Token Efficiency for a retrieved node n against query q as:

Efficiency(q, n) = I(q; n) / tokens(n)

where I(q; n) is the mutual information between query q and node n — the reduction in uncertainty about C(q) from retrieving n — and tokens(n) is the token cost of consuming n.

For a concept-typed node c and a document node d covering the same concept:

E[Efficiency(q, c)] > E[Efficiency(q, d)]

because: (1) I(q; c) ≈ I(q; d) when d contains concept c, but I(q; c) >> I(q; d) in expectation across queries since documents contain substantial irrelevant content; and (2) tokens(c) << tokens(d) by construction — concept nodes are scoped to a single knowledge unit while documents are multi-concept artifacts of arbitrary length.

The efficiency gap widens as document length increases and query scope narrows, both of which are the dominant trends at organizational scale.

## Motivation
Document retrieval achieves acceptable raw coverage on concepts it contains, but pays full document token cost regardless of how much of the document is relevant to the query. For a narrow query against a long document, the vast majority of tokens consumed contribute zero mutual information with q. Concept nodes eliminate this waste structurally — their token cost is bounded and their information content is scoped to a single knowledge unit. This is not a model quality argument — it holds regardless of model capability. It is an architectural efficiency argument: documents are the wrong granularity for concept-scoped queries.

## Current Evidence
Qualitative: PKIS operational experience confirms that pulling a concept node returns scoped, relevant content without irrelevant surrounding material. The PE multiple example illustrates the failure mode: a blog post referencing PE multiple requires consuming substantial irrelevant content to extract the concept definition. Formal quantification against a query benchmark is an open empirical question.

## Open Questions
How do we construct a query benchmark that samples representatively from C(q) distributions across organizational query types? What is the empirical distribution of tokens(d) / I(q;d) for document retrieval at our query volumes? How does efficiency degrade as graph coverage of C(q) decreases — i.e. what is the cost of coverage gaps?

## Connections
- [[retrieval-inference-tradeoff]] — belongs-to: constituent hypothesis of the retrieval-inference-tradeoff cluster