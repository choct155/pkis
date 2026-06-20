---
aliases: []
also_type: []
component_scores:
  application: null
  limits: null
  primitives: null
  purpose: null
  scope: null
  structure: null
coverage: 0
date_created: '2026-06-20'
date_updated: '2026-06-20'
domain:
- knowledge-representation
- bayesian-stats
id: pkis:framework:multidimensional-retrieval-quality-framework
knowledge_type: framework
linked_nodes: []
maturity: evolving
needs_canonical_source: true
related_concepts: []
sources: []
tags:
- retrieval
- evaluation
- quality
- information-theory
- RAG
- graph-retrieval
- coverage
title: Multidimensional Retrieval Quality Framework
understanding: 0
---

## Definition
A seven-dimension framework for evaluating retrieval quality across architectures (vector search, inverted index, tree-structured hierarchical index, graph traversal). Developed to enable principled comparison of retrieval architectures in the context of AI-powered question answering over heterogeneous knowledge sources.

## Motivation

Standard RAG evaluation frameworks (RAGAS, ARES, RAGChecker) converge on three dimensions: context relevance, faithfulness, and answer relevance. These are necessary but insufficient for comparing retrieval architectures because they treat quality as a property of the output rather than of the retrieval mechanism. Two architectures can produce similar RAGAS scores via different mechanisms, with different failure modes and different scalability properties. A retrieval architecture comparison requires dimensions that are (a) computable without human annotation at scale and (b) sensitive to the structural differences between architectures.

## The Seven Dimensions

### 1. Coverage
Does the retrieved set contain the concept dependencies required to answer the query?

Formal definition: Coverage(q, S) = Σ_c P(c|q) · 𝟙[c ∈ S]

Maps to: context recall in RAGAS; eRAG's marginal contribution metric.
Computable: yes, via C(q) formalism and KSG estimation offline.
Architecture sensitivity: graph retrieval dominates vector search for concept-specific queries; vector search has higher recall on diffuse queries.

### 2. Concision
Does the retrieved set contain only what is necessary?

Formal definition: Concision(q, S) = Coverage(q, S) / tokens(S)

This is the efficiency metric Eff(q, S) from the coverage-per-token formalism. High coverage with low concision means correct but diluted content — the information is present but surrounded by noise.

Maps to: context precision and signal-to-noise ratio in RAGAS; conciseness in RAGChecker.
Computable: yes, directly from coverage and token count.
Architecture sensitivity: vector search systematically produces low concision due to semantic distance being a weak discriminator; graph traversal is concise by construction if the concept layer is well-specified.

### 3. Groundedness
Are the claims in the generated response supported by the retrieved content?

Distinct from accuracy: a claim can be true but not grounded in the retrieved content (the model hallucinated a correct fact), or grounded but factually incorrect (the retrieved content itself was wrong). These are different failure modes requiring different interventions.

Maps to: faithfulness in RAGAS; claim-level grounding in RAGChecker.
Computable: yes, via claim extraction and entailment checking against retrieved content. Does not require external ground truth.
Architecture sensitivity: graph retrieval improves groundedness by providing structured, traceable provenance; document retrieval makes provenance harder to attribute when multiple chunks contribute.

### 4. Accuracy
Are the claims factually correct against external ground truth?

The hardest dimension to automate. Requires either human annotation or a trusted reference corpus. Proxy: node hardening level λ(n,t) as a trustworthiness signal — well-hardened nodes backed by multiple high-quality sources are more likely to be accurate. Not a direct accuracy measure.

Maps to: correctness in RAGChecker; answer correctness in RAGAS 0.3.
Computable at scale: no without ground truth. Approximable via λ(n,t) as proxy.
Architecture sensitivity: graph retrieval improves accuracy indirectly through the hardening mechanism — nodes that survive repeated traversal and validation tend toward higher accuracy over time.

### 5. Validity
Are the retrieved facts well-formed — structurally appropriate for the domain and mutually compatible?

Two sub-dimensions:
- Structural validity: is the queried attribute formally defined for the entity type, including compositional types? Type violation example: coupon on a common equity share is invalid because coupon is not in the attribute schema for equity instruments.
- Compositional coherence: for composite entities (structured deals, LBOs), are retrieved facts about different components mutually consistent under the structure's constraints? A validity failure here is not a false claim but an incompatible assembly of individually valid claims.

Maps to: not explicitly formalized in RAGAS/ARES/RAGChecker — this is a gap in the existing literature.
Computable: yes, from the ontology schema for structural validity; from typed edge constraints for compositional coherence. Requires a well-specified concept layer.
Architecture sensitivity: only graph retrieval against a typed ontology can perform validity checking; document and vector retrieval have no structural validity signal.

### 6. Structural Coherence
Does the retrieved node set hang together as a connected explanatory structure?

Formal definition: a retrieved set S is structurally coherent if every node in S is reachable from every other node in S via typed edges within S (the induced subgraph is connected).

Distinct from groundedness (which concerns response-to-context support) and from relevance (which concerns query-to-content distance). Coherence is a property of the internal structure of the retrieved set.

Maps to: partially in RAGAS answer coherence, but that is a generation-quality judgment not a structural computation. Our formulation is a structural graph property, not an LLM judgment.
Computable: yes, from graph adjacency within the retrieved set. O(|S|²) in the worst case but tractable for realistic retrieved set sizes.
Architecture sensitivity: graph retrieval produces structurally coherent retrieved sets by construction if the traversal algorithm follows typed edges. Document retrieval and vector search produce structurally incoherent sets by default — individually relevant but disconnected passages.

### 7. Structural Relevance
Are the retrieved concepts reachable from the query's anchor concepts via semantically appropriate typed edges within bounded path length?

Formal definition: Relevance(c, q) = 𝟙[∃ path from anchor(q) to c via semantically appropriate typed edges within depth d]

Key property: handles discovery queries correctly. A concept that has never been retrieved before but is structurally reachable from the query's anchor concepts is relevant — the graph encodes the relationship even if no historical traversal exists. This resolves the sample selection bias and non-stationarity problems that afflict empirically-derived relevance metrics.

Relevance amortization: the relevance judgment encoded in each edge was made once at graph construction time and is reused at inference time across all queries that touch the neighborhood. This is a third amortization layer distinct from node content amortization and traversal signal amortization.

Maps to: partially in MIGRASCOPE's marginal contribution metric, but our formulation is graph-specific and handles non-stationarity differently.
Computable: yes, from graph topology and path traversal. Does not require historical query patterns.
Architecture sensitivity: only graph retrieval can compute structural relevance. Vector search computes semantic proximity, which approximates relevance but conflates it with surface similarity.

## Architecture Quality Profiles

| Dimension | Inverted Index | Vector Search | Tree (RAPTOR) | Graph Traversal |
|---|---|---|---|---|
| Coverage | Variable (vocab-dependent) | Moderate-high | High (multi-hop) | High (concept-specific) |
| Concision | High when it works | Low | Moderate | High |
| Groundedness | High (exact match) | Moderate | Moderate | High (traceable) |
| Accuracy | High (exact) | Moderate | Moderate | Depends on λ(n,t) |
| Validity | None | None | None | Full (if ontology exists) |
| Structural Coherence | None | None | Within-document only | Full |
| Structural Relevance | None | Approximate | Approximate | Full |

## Automated Measurement Strategy

Dimensions computable without human annotation: Coverage, Concision, Groundedness (via entailment), Structural Coherence, Structural Relevance. These five dimensions constitute the automated quality signal.

Dimensions requiring ground truth or proxy: Accuracy (requires external reference or λ(n,t) proxy). Validity (requires a well-specified ontology schema — computable once the schema exists).

The two-tier measurement strategy from the edge contribution attribution bridge note applies here: use the five automated dimensions continuously, use accuracy validation periodically on a sample with human annotation, use samples to calibrate λ(n,t) as an accuracy proxy.

## Relationship to MIGRASCOPE

MIGRASCOPE (2026) provides information-theoretic metrics for retrieval quality, redundancy, synergy, and marginal contribution. Its marginal contribution metric is the closest existing analog to our Structural Relevance dimension. The key difference: MIGRASCOPE's metrics are agnostic to graph structure and operate on retrieved document sets. Our framework extends the information-theoretic approach specifically to the graph retrieval setting, adding the structural dimensions (Validity, Structural Coherence, Structural Relevance) that are only definable when a typed concept graph exists.

## Open Questions

- What is the right path depth bound d for structural relevance — does it depend on query type?
- How should the framework handle queries that span multiple query types (e.g., a screening query that requires a prior fan-out step)?
- Can compositional coherence (validity sub-dimension) be checked efficiently for large structured deal graphs?
- What is the empirical correlation between structural coherence and human judgments of answer quality?
- How should the framework weight the seven dimensions for an aggregate quality score — are they equally important or does the right weighting depend on query class?

## Reading Path
[To be populated when a canonical source is attached]

## Connections
[To be populated during integration]

## Needs Canonical Source
This stub was created without a source. Suggested references:

**Already in corpus:**
[none in corpus]

**External candidates (Semantic Scholar):**
[none found]