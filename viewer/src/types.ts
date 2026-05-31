export type NodeType =
  | 'concept'
  | 'technique'
  | 'result'
  | 'framework'
  | 'problem'
  | 'principle'
  | 'source';

export type Maturity = 'settled' | 'evolving' | 'contested' | 'historical';

export type View = 'browse' | 'graph' | 'queue' | 'staged';

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

// ── Queue item (from get_reading_queue) ──────────────────────────────────
export interface QueueItem {
  slug: string;
  priority: 'high' | 'normal';
  reason: string;
}

// ── Staged node (from get_staged_nodes) ──────────────────────────────────
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
