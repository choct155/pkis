import type {
  SearchResult,
  FullNode,
  RelatedEntry,
  HealthMetrics,
  FrontierNode,
  QueueItem,
  StagedNode,
  Cluster,
  ClusterPriorities,
  IndexNode,
  DomainCount,
  ReaderPayload,
  Asset,
  DocMeta,
  Doc,
  AskMessage,
  AskResponse,
  AskTurn,
  ConversationSummary,
  ConversationFull,
} from '../types';

const BASE = '/pkis-api';

export class ApiError extends Error {
  status: number;
  constructor(message: string, status: number) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
  }
}

async function post<T>(path: string, body: Record<string, unknown> = {}): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: res.statusText }));
    throw new ApiError((err as { error?: string }).error ?? res.statusText, res.status);
  }
  return res.json() as Promise<T>;
}

async function get<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`, { method: 'GET' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ error: res.statusText }));
    throw new ApiError((err as { error?: string }).error ?? res.statusText, res.status);
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

// ── Ask (natural-language Q&A + graph traversal over the wiki) ────────────
// Stateless + multi-turn: send the full conversation each call. The server
// runs the shared "ask brain" (retrieve → traverse → cited synthesis).
export async function ask(messages: AskMessage[]): Promise<AskResponse> {
  return post<AskResponse>('/ask', { messages });
}

// Streaming ask over SSE. The server forwards engine events as `data:` frames:
//   status → a tool turn began (drop any partial answer shown this turn)
//   delta  → a chunk of answer text
//   done   → final payload (answer, citations, …)
//   error  → a server-side failure
// Returns when the stream completes. Throws ApiError on a non-OK response
// (e.g. 429 rate-limit) so the caller can surface the message.
export interface AskStreamHandlers {
  onStatus?: (text: string) => void;
  onDelta?: (text: string) => void;
  onDone?: (res: AskResponse) => void;
  onError?: (message: string) => void;
}
export async function askStream(messages: AskMessage[], h: AskStreamHandlers): Promise<void> {
  const res = await fetch(`${BASE}/ask/stream`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ messages }),
  });
  if (!res.ok || !res.body) {
    const err = await res.json().catch(() => ({ error: res.statusText }));
    throw new ApiError((err as { error?: string }).error ?? res.statusText, res.status);
  }
  const reader = res.body.getReader();
  const dec = new TextDecoder();
  let buf = '';
  for (;;) {
    const { value, done } = await reader.read();
    if (done) break;
    buf += dec.decode(value, { stream: true });
    let i: number;
    // SSE frames are separated by a blank line.
    while ((i = buf.indexOf('\n\n')) >= 0) {
      const frame = buf.slice(0, i);
      buf = buf.slice(i + 2);
      const line = frame.split('\n').find((l) => l.startsWith('data:'));
      if (!line) continue;
      let ev: { type: string; text?: string; error?: string } & Partial<AskResponse>;
      try { ev = JSON.parse(line.slice(5).trim()); } catch { continue; }
      if (ev.type === 'status') h.onStatus?.(ev.text ?? '');
      else if (ev.type === 'delta') h.onDelta?.(ev.text ?? '');
      else if (ev.type === 'done') h.onDone?.(ev as AskResponse);
      else if (ev.type === 'error') h.onError?.(ev.error ?? 'stream error');
    }
  }
}

// ── Conversation persistence (signed-in, per-user) ────────────────────────
export async function listConversations(): Promise<ConversationSummary[]> {
  const r = await get<{ conversations: ConversationSummary[] }>('/conversations');
  return r.conversations ?? [];
}
export async function getConversation(id: string): Promise<ConversationFull> {
  return get<ConversationFull>(`/conversation/${id}`);
}
// Auto-save (create or update). Returns the (possibly new) id.
export async function saveConversation(
  messages: AskTurn[], id?: string | null, title?: string,
): Promise<{ id: string; title: string; created: boolean }> {
  return post('/conversations', { id: id ?? undefined, messages, title });
}
export async function renameConversation(id: string, title: string): Promise<void> {
  await post(`/conversation/${id}/rename`, { title });
}
export async function deleteConversation(id: string, deleted = true): Promise<void> {
  await post(`/conversation/${id}/delete`, { deleted });
}

// ── Node ──────────────────────────────────────────────────────────────────
export async function getNode(iri: string): Promise<FullNode> {
  return post<FullNode>('/node', { iri });
}

// Resolve a bare node slug (from a body [[wikilink]]) to its canonical IRI.
// Returns null for a dangling link (no such node).
export async function resolveSlug(slug: string): Promise<string | null> {
  const r = await post<{ iri: string | null }>('/resolve', { slug });
  return r.iri ?? null;
}

// Batch-resolve many slugs at once → {slug: iri|null}. Used to dim dangling
// wikilinks with a single round-trip per node body.
export async function resolveSlugs(slugs: string[]): Promise<Record<string, string | null>> {
  if (!slugs.length) return {};
  const r = await post<{ map: Record<string, string | null> }>('/resolve', { slugs });
  return r.map ?? {};
}

export interface SourceStatus {
  iri: string | null;      // null = not ingested (dangling)
  readable: boolean;
  read_url: string | null; // external url or in-app PDF path
  has_reader: boolean;
}

// Readability of cited sources → so the viewer can offer a 'read' link and dim
// un-ingested sources. One round-trip per node's source list.
export async function sourceStatus(slugs: string[]): Promise<Record<string, SourceStatus>> {
  if (!slugs.length) return {};
  const r = await post<{ map: Record<string, SourceStatus> }>('/source-status', { slugs });
  return r.map ?? {};
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

// ── Index (browse all nodes of a type) ────────────────────────────────────
export async function getIndex(
  node_type?: string,
  domain?: string,
  cluster?: string
): Promise<IndexNode[]> {
  return post<IndexNode[]>('/index', { node_type, domain, cluster });
}

// ── Reader (read+listen) ──────────────────────────────────────────────────
export async function getReader(slug: string): Promise<ReaderPayload> {
  return post<ReaderPayload>(`/reader/${slug}`);
}

export async function saveReaderAnnotation(a: {
  slug: string; section_id: string; text: string; note?: string; kind?: 'note' | 'bridge';
}): Promise<unknown> {
  return post('/reader-annotate', a);
}

export async function buildReader(slug: string): Promise<{ status: string; slug: string; arxiv_id?: string }> {
  return post('/reader-build', { slug });
}

export async function getReaderStatus(slug: string): Promise<{ state: string }> {
  try {
    const r = await fetch(`/pkis-api/reader/${slug}/status`);
    if (r.status === 404) return { state: 'none' };          // genuinely not built
    if (!r.ok) return { state: 'unknown' };                  // 5xx / outage — not "none"
    return (await r.json()) as { state: string };
  } catch {
    return { state: 'unknown' };                             // network error — retryable
  }
}

// ── Domains (facet) ───────────────────────────────────────────────────────
export async function getDomains(): Promise<DomainCount[]> {
  return post<DomainCount[]>('/domains');
}

// ── Assets (interactive explainers + visualizations) ──────────────────────
export async function getAssets(kind?: string): Promise<Asset[]> {
  return post<Asset[]>('/assets', kind ? { kind } : {});
}

// ── Documentation ─────────────────────────────────────────────────────────
export async function getDocs(): Promise<DocMeta[]> {
  return post<DocMeta[]>('/docs');
}

export async function getDoc(key: string): Promise<Doc> {
  return post<Doc>('/doc', { key });
}

// ── Research clusters ─────────────────────────────────────────────────────
export async function getClusters(): Promise<Cluster[]> {
  return post<Cluster[]>('/clusters');
}

// ── Cluster priorities (frontier gaps grouped by cluster) ─────────────────
export async function getClusterPriorities(): Promise<ClusterPriorities> {
  return post<ClusterPriorities>('/cluster-priorities');
}

// ── Staged nodes ──────────────────────────────────────────────────────────
export async function getStagedNodes(
  options: { limit?: number; node_type?: string } = {}
): Promise<StagedNode[]> {
  return post<StagedNode[]>('/staged', options);
}

// ── Commit staged ─────────────────────────────────────────────────────────
// Edit a LIVE node (frontmatter fields and/or full body), commit + push. Write-gated.
export async function editNode(
  iri: string,
  opts: { frontmatter_updates?: Record<string, unknown>; content?: string; commit_message?: string }
): Promise<{ status: string; git_pushed?: boolean }> {
  return post('/edit', { iri, ...opts });
}

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

// ── Auth (WorkOS sealed session) ──────────────────────────────────────────
export interface AuthState { authenticated: boolean; user_id?: string; role: string }

export async function getAuth(): Promise<AuthState> {
  try {
    const r = await fetch(`${BASE}/auth/me`, { credentials: 'same-origin' });
    if (!r.ok) return { authenticated: false, role: 'reader' };
    return (await r.json()) as AuthState;
  } catch {
    return { authenticated: false, role: 'reader' };
  }
}

// Owner-only administrative inbox (wiki/inbox.md). Throws ApiError(401/403) if the
// caller isn't the owner — the session cookie carries the role.
export async function getInbox(): Promise<{ markdown: string }> {
  const r = await fetch(`${BASE}/inbox`, { credentials: 'same-origin' });
  if (!r.ok) {
    const err = await r.json().catch(() => ({ error: r.statusText }));
    throw new ApiError((err as { error?: string }).error ?? r.statusText, r.status);
  }
  return r.json() as Promise<{ markdown: string }>;
}

export async function logout(): Promise<void> {
  await fetch(`${BASE}/auth/logout`, { method: 'POST', credentials: 'same-origin' });
}

export function signInUrl(returnTo = '/app/'): string {
  return `${BASE}/auth/login?return=${encodeURIComponent(returnTo)}`;
}

// ── Upload document ───────────────────────────────────────────────────────
export async function uploadDocument(
  filename: string,
  content_b64: string,
  slug?: string,
  push_to_readwise = false
): Promise<{ slug: string; doc_url: string; source_auto_created?: boolean; readwise_url?: string }> {
  return post('/upload-document', { filename, content_b64, slug, push_to_readwise });
}

// ── Proactive discovery ───────────────────────────────────────────────────
export async function getDiscovery(
  status: 'pending' | 'accepted' | 'dismissed' = 'pending',
  limit = 50
): Promise<import('../types').DiscoveryInbox> {
  return post('/discovery', { status, limit });
}

export async function discoveryAct(
  id: string,
  action: 'accept' | 'dismiss',
  reason_chip?: string,
  note?: string
): Promise<{ action: string; source_slug?: string; queued?: boolean }> {
  return post('/discovery/act', { id, action, reason_chip, note });
}
