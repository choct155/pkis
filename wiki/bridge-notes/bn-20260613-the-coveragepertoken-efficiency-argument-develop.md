---
date_created: '2026-06-13'
id: pkis:bridge-note:bn-20260613-the-coveragepertoken-efficiency-argument-develop
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- concept-typed-nodes-dominate-document-nodes-on-coverage
- bn-20260613-the-retrieval-efficiency-argument-has
- retrieval-inference-tradeoff
origin: conversation
proposed_edge_type: extends
rationale: 'The coverage-per-token efficiency argument developed for concept nodes
  extends structurally intact to the instance layer. The parallelism is exact.


  At the concept layer: a query induces C(q), a distribution over concept dependencies.
  Typed concept nodes achieve higher Eff(q,n) = I(q;n)/tokens(n) than documents because
  P(k|concept node) is narrow and concept-boundary-aligned. The semantic bridging
  problem is resolving query tokens to canonical concept node IRIs.


  At the instance layer: a query induces I(q), a distribution over instance dependencies
  — specific entities, their properties, and their relationships. Typed instance nodes
  with canonical entity resolution achieve higher Eff(q,n) than documents decorated
  with unresolved entity mentions, because P(k|instance node) is narrow and entity-boundary-aligned.
  The semantic bridging problem is resolving entity mentions to canonical instance
  IRIs — the entity resolution problem.


  The set logic vs. graph argument transfers exactly to the instance layer. Document
  tagging with entity mentions is set membership: this document mentions JPMorgan.
  An instance graph encodes typed directed relationships: JPMorgan Asset Management
  [LP] —committed_to→ Fund X [commitment_date: Y, amount: Z]. Set membership tells
  you something is present; the graph tells you how it relates, in what capacity,
  and with what properties. The information content difference is the same as the
  typed edge argument at the concept layer.


  Entity resolution is the instance-layer analog of concept disambiguation. The same
  entity — JPMorgan Chase — appears under dozens of surface forms across documents
  (JPMorgan, JP Morgan, JPMorgan AM, JPMorgan Asset Management, specific line-of-business
  names). Without canonical instance nodes, queries over entity relationships return
  inconsistent, incomplete results. With canonical instance nodes, the graph enforces
  entity identity across all document references.


  Cost dynamics differ: instance graphs are typically larger, more volatile, and require
  update pipelines (entity extraction, resolution, deduplication, incremental refresh)
  that concept graphs do not need at the same frequency. The construction cost per
  node is higher and the amortization horizon may differ. However, the structural
  efficiency argument — Eff(q, instance node) > Eff(q, document) for entity-scoped
  queries — holds by the same mechanism.


  The two-layer thesis is therefore:

  - Concept layer — Coverage(q, G_concept): typed concept nodes dominate documents
  on Eff(q,n) due to concept-boundary alignment.

  - Instance layer — Coverage(q, G_instance): typed instance nodes with canonical
  entity resolution dominate document entity tags on Eff(q,n) due to entity-boundary
  alignment and relationship typing.


  The layers are separable and independently valuable. Concept layer can be implemented
  first; instance layer adds incremental value on top. Both layers together support
  the full query space: conceptual questions (what is X, how does X relate to Y) and
  factual questions (what is the value of property P for entity E).'
source_context: Conversation on general audience explainer design — two-layer thesis
  connecting concept and instance graph efficiency
status: unreviewed
title: Instance layer efficiency thesis — structural parallel to concept layer coverage-per-token
  argument
---

## Connection
The coverage-per-token efficiency argument developed for concept nodes extends structurally intact to the instance layer. The parallelism is exact.

At the concept layer: a query induces C(q), a distribution over concept dependencies. Typed concept nodes achieve higher Eff(q,n) = I(q;n)/tokens(n) than documents because P(k|concept node) is narrow and concept-boundary-aligned. The semantic bridging problem is resolving query tokens to canonical concept node IRIs.

At the instance layer: a query induces I(q), a distribution over instance dependencies — specific entities, their properties, and their relationships. Typed instance nodes with canonical entity resolution achieve higher Eff(q,n) than documents decorated with unresolved entity mentions, because P(k|instance node) is narrow and entity-boundary-aligned. The semantic bridging problem is resolving entity mentions to canonical instance IRIs — the entity resolution problem.

The set logic vs. graph argument transfers exactly to the instance layer. Document tagging with entity mentions is set membership: this document mentions JPMorgan. An instance graph encodes typed directed relationships: JPMorgan Asset Management [LP] —committed_to→ Fund X [commitment_date: Y, amount: Z]. Set membership tells you something is present; the graph tells you how it relates, in what capacity, and with what properties. The information content difference is the same as the typed edge argument at the concept layer.

Entity resolution is the instance-layer analog of concept disambiguation. The same entity — JPMorgan Chase — appears under dozens of surface forms across documents (JPMorgan, JP Morgan, JPMorgan AM, JPMorgan Asset Management, specific line-of-business names). Without canonical instance nodes, queries over entity relationships return inconsistent, incomplete results. With canonical instance nodes, the graph enforces entity identity across all document references.

Cost dynamics differ: instance graphs are typically larger, more volatile, and require update pipelines (entity extraction, resolution, deduplication, incremental refresh) that concept graphs do not need at the same frequency. The construction cost per node is higher and the amortization horizon may differ. However, the structural efficiency argument — Eff(q, instance node) > Eff(q, document) for entity-scoped queries — holds by the same mechanism.

The two-layer thesis is therefore:
- Concept layer — Coverage(q, G_concept): typed concept nodes dominate documents on Eff(q,n) due to concept-boundary alignment.
- Instance layer — Coverage(q, G_instance): typed instance nodes with canonical entity resolution dominate document entity tags on Eff(q,n) due to entity-boundary alignment and relationship typing.

The layers are separable and independently valuable. Concept layer can be implemented first; instance layer adds incremental value on top. Both layers together support the full query space: conceptual questions (what is X, how does X relate to Y) and factual questions (what is the value of property P for entity E).

## Nodes Involved
- [[concept-typed-nodes-dominate-document-nodes-on-coverage]]
- [[bn-20260613-the-retrieval-efficiency-argument-has]]
- [[retrieval-inference-tradeoff]]

## Integration Notes
Pending review.