import type {
  SearchResult,
  FullNode,
  RelatedEntry,
  HealthMetrics,
  FrontierNode,
  QueueItem,
  StagedNode,
} from '../types';

const BASE = '/pkis-api';

async function post<T>(path: string, body: Record<string, unknown> = {}): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: res.statusText }));
    throw new Error((err as { error?: string }).error ?? res.statusText);
  }
  return res.json() as Promise<T>;
}

// ── Search ────────────────────────────────────────────────────────────────
export async function searchWiki(
  query: string,
  options: { domains?: string[]; node_types?: string[]; max_results?: number } = {}
): Promise<SearchResult[]> {
  return post<SearchResult[]>('/search', { query, ...options });
}

// ── Node ──────────────────────────────────────────────────────────────────
export async function getNode(iri: string): Promise<FullNode> {
  return post<FullNode>('/node', { iri });
}

// ── Related ───────────────────────────────────────────────────────────────
export async function getRelated(
  iri: string,
  options: { direction?: string; edge_types?: string[]; max_hops?: number } = {}
): Promise<RelatedEntry[]> {
  return post<RelatedEntry[]>('/related', { iri, ...options });
}

// ── Health ────────────────────────────────────────────────────────────────
export async function getHealth(): Promise<HealthMetrics> {
  return post<HealthMetrics>('/health');
}

// ── Frontier ──────────────────────────────────────────────────────────────
export async function getFrontier(): Promise<FrontierNode[]> {
  return post<FrontierNode[]>('/frontier');
}

// ── Reading graph ─────────────────────────────────────────────────────────
export async function getReadingGraph(
  options: {
    focus_concept?: string;
    focus_domain?: string;
    scope?: string;
    max_nodes?: number;
    min_edge_weight?: number;
  } = {}
): Promise<unknown> {
  return post('/reading-graph', options);
}

// ── Staged nodes ──────────────────────────────────────────────────────────
export async function getStagedNodes(
  options: { limit?: number; node_type?: string } = {}
): Promise<StagedNode[]> {
  return post<StagedNode[]>('/staged', options);
}

// ── Commit staged ─────────────────────────────────────────────────────────
export async function commitStaged(
  staged_id: string,
  action: string,
  edits?: Record<string, unknown>,
  confirmed_links?: unknown[]
): Promise<unknown> {
  return post('/staged/commit', { staged_id, action, edits, confirmed_links });
}

// ── Bridge note ───────────────────────────────────────────────────────────
export async function createBridgeNote(
  rationale: string,
  linked_node_refs: string[],
  proposed_edge_type: string,
  origin?: string,
  title?: string
): Promise<unknown> {
  return post('/bridge-note', { rationale, linked_node_refs, proposed_edge_type, origin, title });
}

// ── Source stub ───────────────────────────────────────────────────────────
export async function createSourceStub(
  title?: string,
  url?: string,
  notes?: string,
  authors?: string,
  year?: number,
  doi?: string,
  priority?: string
): Promise<unknown> {
  return post('/source-stub', { title, url, notes, authors, year, doi, priority });
}

// ── Queue ─────────────────────────────────────────────────────────────────
export async function getReadingQueue(): Promise<QueueItem[]> {
  return post<QueueItem[]>('/queue');
}

export async function addToQueue(
  reference: string,
  reason: string,
  priority: 'high' | 'normal' = 'normal',
  source_iri?: string
): Promise<unknown> {
  return post('/queue/add', { reference, reason, priority, source_iri });
}

// ── Save URL ──────────────────────────────────────────────────────────────
export async function saveUrl(
  url: string,
  slug?: string,
  push_to_readwise = true
): Promise<unknown> {
  return post('/save-url', { url, slug, push_to_readwise });
}

// ── Rebuild graph ─────────────────────────────────────────────────────────
export async function rebuildGraph(): Promise<unknown> {
  return post('/rebuild-graph');
}

// ── Detect concepts ───────────────────────────────────────────────────────
export async function detectConcepts(
  text: string,
  threshold = 0.6
): Promise<unknown> {
  return post('/detect-concepts', { text, threshold });
}
