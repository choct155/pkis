---
date_created: '2026-06-13'
id: pkis:bridge-note:bn-20260613-the-standard-engineer-objection-to
integration_target: ''
knowledge_type: bridge-note
linked_nodes:
- concept-typed-nodes-dominate-document-nodes-on-coverage
- retrieval-inference-tradeoff
origin: conversation
proposed_edge_type: extends
rationale: 'The standard engineer objection to the document retrieval efficiency argument
  is that chunked embeddings replace full-document retrieval, improving the token
  cost denominator. This is absorbed directly into the existing formalism: a chunk
  is a document with smaller tokens(n). Eff(q, chunk) = I(q; chunk) / tokens(chunk)
  improves over Eff(q, document) because tokens(chunk) &lt;&lt; tokens(document).
  However, the numerator I(q; chunk) is still diluted because chunk boundaries are
  arbitrary with respect to concept boundaries — a chunk may contain partial concept
  explanations blended with irrelevant content. The efficiency ratio improves but
  does not converge to the concept node case, where token cost is bounded by concept
  scope rather than window size. The argument extends unchanged: concept nodes dominate
  chunked embeddings on Eff(q,n) for the same structural reason they dominate documents
  — concept boundary alignment, not token count, is the load-bearing property.'
source_context: Conversation on retrieval efficiency explainer — anticipated engineer
  objections
status: unreviewed
title: Document chunking is a partial efficiency improvement — not a solution to concept-boundary
  mismatch
---

## Connection
The standard engineer objection to the document retrieval efficiency argument is that chunked embeddings replace full-document retrieval, improving the token cost denominator. This is absorbed directly into the existing formalism: a chunk is a document with smaller tokens(n). Eff(q, chunk) = I(q; chunk) / tokens(chunk) improves over Eff(q, document) because tokens(chunk) &lt;&lt; tokens(document). However, the numerator I(q; chunk) is still diluted because chunk boundaries are arbitrary with respect to concept boundaries — a chunk may contain partial concept explanations blended with irrelevant content. The efficiency ratio improves but does not converge to the concept node case, where token cost is bounded by concept scope rather than window size. The argument extends unchanged: concept nodes dominate chunked embeddings on Eff(q,n) for the same structural reason they dominate documents — concept boundary alignment, not token count, is the load-bearing property.

## Nodes Involved
- [[concept-typed-nodes-dominate-document-nodes-on-coverage]]
- [[retrieval-inference-tradeoff]]

## Integration Notes
Pending review.