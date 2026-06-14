---
date_created: '2026-06-13'
date_updated: '2026-06-14'
id: pkis:bridge-note:bn-20260613-cq-the-concept-dependency-distribution
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- query-coverage-as-expected-mass-of-c-q-on-encoded-conce
- retrieval-inference-tradeoff
- attention-mechanism
origin: conversation
proposed_edge_type: extends
rationale: 'C(q) is not directly computable but can be approximated via three strategies
  with distinct cost-quality tradeoffs. Corrected priority ordering (updated from
  initial incorrect version):


  Strategy 1 (day-one, highest cost): LLM decomposition. Prompt a model to decompose
  q into its constituent concept dependencies explicitly. Available immediately with
  no infrastructure requirements. Most expensive per query but the only option before
  any usage history or embedding infrastructure exists.


  Strategy 2 (default once embeddings exist): Embedding similarity. Embed q and compute
  cosine similarity against cached concept node embeddings. No model call required.
  Weakness: captures surface co-occurrence rather than structural dependency. First-order
  matches seed the frontier; graph traversal catches structural dependencies not surface-salient
  in q.


  Strategy 3 (mature system, lowest cost): Historical traversal patterns. Query logs
  recording which concept nodes were traversed in successful resolutions of similar
  queries. Cost at inference time is near-zero. Unavailable at day-zero; value compounds
  with usage history.


  Cost trajectory is monotonically decreasing as the system matures: expensive LLM
  decomposition day-one, cheap embedding lookup once infrastructure exists, near-zero
  historical lookup as logs accumulate. Increasing returns to scale on both retrieval
  efficiency and query routing efficiency simultaneously.


  All three strategies converge on a shared resolution step: mapping estimated concept
  dependencies back to nodes that actually exist in G. This is where coverage gaps
  surface and is the final step of the semantic bridging approximation problem.'
source_context: Conversation on tractable C(q) estimation for interactive example
  and pitch demonstration
status: unreviewed
tags:
- c-q-estimation
- strategy-ordering
- corrected
title: C(q) estimation — tractable strategy ordering for practical implementation
---

## Connection
C(q) — the concept dependency distribution induced by query q — is not directly computable but can be approximated via three strategies with distinct cost-quality tradeoffs. Practical priority ordering:

Strategy 1 (preferred where available): Historical traversal patterns. If query logs exist recording which concept nodes were traversed in successful resolutions of similar queries, P(c|q) can be estimated empirically from co-occurrence of concept nodes across query classes. Cost at inference time is near-zero — lookup only. Constraint: unavailable at day zero; value compounds with usage history. This is a desirable property for the cost argument: the system gets cheaper to operate over time.

Strategy 2 (default): Embedding similarity. Embed q and compute cosine similarity against cached concept node embeddings. Similarity score proxies P(c|q). No model call required; batch computation against cached embeddings is cheap. Weakness: captures surface co-occurrence rather than structural dependency — a concept may be necessary but surface-distant from q. First-order structural dependencies not surface-salient in q are caught by graph traversal once the embedding-matched nodes are retrieved.

Strategy 3 (fallback): LLM decomposition. Prompt a model to decompose q into its constituent concept dependencies explicitly. More expensive than strategies 1 and 2 but bounded — the decomposition prompt is small. Appropriate for novel queries with no embedding neighbors and no traversal history.

All three strategies converge on a shared resolution step: mapping estimated concept dependencies back to nodes that actually exist in G. This resolution step is where coverage gaps surface (concept needed but not encoded) and is the last mile of the semantic bridging approximation problem. It is not a separate problem from C(q) estimation — it is the final step of it. The claim to concept node existence is a prerequisite for coverage computation; the architecture must do this work regardless of which estimation strategy is used.

## Nodes Involved
- [[query-coverage-as-expected-mass-of-c-q-on-encoded-conce]]
- [[retrieval-inference-tradeoff]]
- [[attention-mechanism]]

## Integration Notes
Pending review.