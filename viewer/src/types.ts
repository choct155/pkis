export type NodeType =
  | 'concept'
  | 'technique'
  | 'result'
  | 'framework'
  | 'problem'
  | 'principle'
  | 'source'
  | 'asset';

export type Maturity = 'settled' | 'evolving' | 'contested' | 'historical';

export type View = 'browse' | 'clusters' | 'priority' | 'graph' | 'explainers' | 'docs' | 'inbox' | 'ask' | 'lab';

// ── Natural-language ask (from /pkis-api/ask) ─────────────────────────────
export interface AskMessage {
  role: 'user' | 'assistant';
  content: string;
}
export interface Citation {
  slug: string;
  iri: string;
  title: string;
}
export interface AskResponse {
  answer: string;
  citations: Citation[];
  surfaced: string[];
  tier: 'reader' | 'owner';
  model: string;
  turns: number;
  usage: { input_tokens: number; output_tokens: number };
}

// A persisted chat turn (the subset we store/recall — no streaming flags).
export interface AskTurn {
  role: 'user' | 'assistant';
  content: string;
  citations?: Citation[];
  meta?: { model: string; turns: number };
}
export interface ConversationSummary {
  id: string;
  title: string;
  created_at: string;
  updated_at: string;
  turn_count: number;
  anchor: { type: string; ref: string } | null;
  deleted: boolean;
  shared?: boolean;
  share_token?: string | null;
}
export interface ConversationFull extends ConversationSummary {
  messages: AskTurn[];
  artifact: string | null;
}

// Public read-only content behind a capability link (/app/?s=<token>).
export interface SharedContent {
  kind: 'conversation';
  title: string;
  messages: AskTurn[];
  updated_at: string;
}

// ── Documentation (from /pkis-api/docs and /pkis-api/doc) ─────────────────
export interface DocMeta {
  key: string;
  title: string;
  category: string;
  path: string;
}
export interface Doc extends DocMeta {
  markdown: string;
}

// ── Proactive discovery (from /pkis-api/discovery) ────────────────────────
export interface DiscoveryCandidate {
  id: string;
  title: string;
  authors: string;
  year: number | null;
  venue: string;
  doi: string;
  url: string;
  abstract: string;
  cited_by: number;
  field: string;
  sim: number;
  score: number;
  prior_mult?: number;
  reason: string;
  status: 'pending' | 'accepted' | 'dismissed';
  channel: string;
  nearest_frontier: { iri: string; title: string; coverage: number; understanding: number; inbound_refs?: number };
  via_seeds?: string[];
  // ── enrichment (why-read-it intelligence) ──
  priority?: number;
  priority_note?: string;
  links?: { iri: string; title: string; type: string; score: number }[];
  clusters?: { slug: string; title: string; thesis: string; relevance: number }[];
  hypotheses?: { title: string; status: string; cluster: string }[];
  rationale?: { why?: string; gap?: string; fits?: string; questions?: string; agenda?: string };
}

export interface DiscoveryInbox {
  generated_at: string | null;
  channel: string | null;
  counts: Record<string, number>;
  candidates: DiscoveryCandidate[];
}

// ── Asset (from get_assets) — anything the owner authors ──────────────────
// `format` = how it renders: 'interactive' (HTML viz) | 'writing' (prose body).
// `kind` = open genre (governed by wiki/asset_kinds.json): explainer,
// visualization, position-paper, … filter the gallery by it.
export type AssetKind = 'explainer' | 'visualization';
export interface Asset {
  iri: string;
  title: string;
  kind: AssetKind | string;
  format: 'interactive' | 'writing' | string;
  viz: string;          // viz slug -> /pkis-api/viz/<slug>.html (interactive only)
  viz_title: string;    // the explainer's own <title> (or node title for writing)
  viz_url: string | null;
  domain: string[];
  illustrates: number;  // how many nodes link here via illustrated-by
  excerpt: string;
}

// ── Search result (from search_wiki / search_wiki_index) ──────────────────
export interface SearchResult {
  iri: string;
  canonical_title: string;
  domain: string[];
  node_type: string;
  coverage: number;
  understanding: number;
  one_line_summary: string;
  score?: number;
  maturity?: Maturity;
  tags?: string[];
}

// ── Retrieval lab (search profile comparison + metrics) ───────────────────
export interface TraceStage {
  name: string;
  kind: string;
  ms: number;
  n_out: number | null;
}
export interface SearchMetrics {
  coherence?: number;
  n_components?: number;
  n_in_graph?: number;
  redundancy?: number;
  diversity?: number;
}
export interface CompareColumn {
  profile_name: string;
  results: SearchResult[];
  trace: { stages: TraceStage[]; profile?: string; query?: string };
  metrics: SearchMetrics;
  retrieval_ms: number;
  eval_ms: number;
}
export interface CompareResponse {
  comparison_id: string;
  query: string;
  columns: CompareColumn[];
}
export interface QueryLogItem {
  query: string;
  query_norm: string;
  paradigm: string;
  count: number;
  last_seen: string;
}

// ── Full node (from get_node) ─────────────────────────────────────────────
export interface NodeFrontmatter {
  title: string;
  knowledge_type?: NodeType;
  type?: NodeType;          // some older nodes use "type" instead of "knowledge_type"
  domain: string[];
  tags: string[];
  coverage: number;
  understanding: number;
  maturity: Maturity;
  viz?: string;             // viz asset slug
  aliases?: string[];
  reading_path?: ReadingPathItem[];
  [key: string]: unknown;
}

export interface FullNode {
  iri: string;
  frontmatter: NodeFrontmatter;
  content: string;          // raw markdown
  related_nodes: RelatedNode[];
  reading_path: ReadingPathItem[];
  component_scores: Record<string, number | null> | null;
}

export interface RelatedNode {
  iri: string;
  title: string;
  edge_type: string;
  direction: 'inbound' | 'outbound';
  viz?: string | null;   // present when the neighbor is a viz-bearing asset
  kind?: string | null;  // 'explainer' | 'visualization' (drives inline vs link)
}

export interface ReadingPathItem {
  source_iri?: string;
  source_title?: string;
  slug?: string;
  status?: 'read' | 'unread' | 'reading';
  note?: string;
}

// ── Related node (from get_related) ──────────────────────────────────────
export interface RelatedEntry {
  iri: string;
  canonical_title: string;
  edge_type: string;
  direction: 'inbound' | 'outbound';
  hop_count: number;
}

// ── Health metrics (from get_health_metrics) ──────────────────────────────
export interface HealthMetrics {
  total_nodes: number;
  total_sources: number;
  total_concepts: number;
  avg_coverage: number;
  avg_understanding: number;
  cross_domain_connections: number;
  queue_depth: number;
  stubs_awaiting_deepening: number;
  total_edges: number;
}

// ── Frontier node (from get_concept_frontier) ────────────────────────────
export interface FrontierNode {
  iri: string;
  canonical_title: string;
  coverage: number;
  understanding: number;
  inbound_refs: number;
  priority_score: number;
  node_type?: string;
  domain?: string[];
  maturity?: Maturity;
}

// A concept a source informs. is_gap marks an active-cluster frontier gap
// (load-bearing); cluster is set only then.
export interface QueueServes {
  concept: string;
  concept_iri: string;
  coverage: number;
  is_gap?: boolean;
  cluster?: string | null;
}

// ── Queue item (from get_reading_queue / cluster-priorities) ──────────────
export interface QueueItem {
  slug: string;
  reason: string;
  // B10: ordering is derived from the concept frontier; the manual high/normal tag
  // is demoted to an informational capture-time hint. The backend returns items
  // already ordered by frontier_score (un-ingested captures: null, sorted last).
  hint: 'high' | 'normal' | null;
  frontier_score: number | null;
  captured: string | null;
  title_full?: string | null;   // real source title (cluster-priorities enrichment)
  serves?: QueueServes[];        // gap concepts/clusters it advances
}

// ── Source research relevance (from /pkis-api/source-relevance) ───────────
export interface SourceRelevance {
  slug: string;
  serves: QueueServes[];
  frontier_score: number | null;
}

// ── Staged node (from get_staged_nodes) ──────────────────────────────────
export interface StagedLink {
  ref: string;            // the slug/fuzzy-ref the bridge note recorded
  iri: string | null;     // resolved canonical IRI, or null if it doesn't exist
  exists: boolean;
}
export interface StagedNode {
  staged_id: string;
  slug: string;
  node_type: string;
  staged_at: string;
  staged_by: string;
  title: string;
  review_status: string;
  description: string;
  review_url: string;
  // Bridge-note review context (empty for other staged types):
  rationale?: string;
  proposed_edge_type?: string;
  links?: StagedLink[];
}

// ── Research clusters (from get_clusters) ─────────────────────────────────
export interface ClusterHypothesis {
  slug: string;
  iri: string | null;
  title: string;
  status: string;
  role: string;
  is_frontier: boolean;
}

export interface ClusterDep {
  iri: string;
  title: string;
  type: string;
  predicate: string;
  coverage: number;
}

export interface Cluster {
  iri: string;
  slug: string;
  title: string;
  domain: string[];
  status: string;
  thesis: string;
  current_frontier: string;
  hypotheses: ClusterHypothesis[];
  frontier_hypotheses: string[];
  deps: ClusterDep[];
}

// ── Cluster priorities (from get_cluster_priorities) ──────────────────────
export interface GapNode {
  iri: string;
  title: string;
  type: string;
  coverage: number;
  understanding: number;
}

export interface ClusterPriorityGroup {
  cluster_slug: string;
  cluster_iri: string;
  cluster_title: string;
  lead_hypothesis: string | null;
  frontier_hypotheses: string[];
  gaps: GapNode[];
}

export interface ClusterPriorities {
  params: { cluster_proximity_weight: number; weight_source: string };
  clusters: ClusterPriorityGroup[];
  reading_queue: QueueItem[];
}

// ── Index node (from get_index) ───────────────────────────────────────────
export interface IndexNode {
  iri: string;
  canonical_title: string;
  domain: string[];
  node_type: string;
  coverage: number;
  understanding: number;
  date_updated: string;
}

// ── Domain counts (from get_domains) ──────────────────────────────────────
export interface DomainCount {
  domain: string;
  count: number;
}

// ── Reader (read+listen slice) ────────────────────────────────────────────
export interface ReaderSection {
  id: string;
  title: string;
  paper_md: string;
  narration: string;
  t_start: number;
  t_end: number;
  page?: number;            // 1-based PDF page this section starts on (for synced PDF view)
}

export interface ReaderPayload {
  slug: string;
  title: string;
  source_iri: string;
  audio_url: string;
  total_duration: number;
  sections: ReaderSection[];
  pdf_url?: string;         // original chapter PDF, when available
  pdf_pages?: number;
}

// ── App context ───────────────────────────────────────────────────────────
export interface AppState {
  view: View;
  selectedIri: string | null;
  captureOpen: boolean;
  editIri: string | null;
  typeFilter: NodeType | 'all';
  searchQuery: string;
  searchResults: SearchResult[] | null;
}
