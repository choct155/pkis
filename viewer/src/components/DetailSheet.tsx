import { useEffect, useRef, useState } from 'react'
import { getNode, resolveSlug, resolveSlugs, sourceStatus, getSourceRelevance } from '../lib/api'
import type { SourceStatus } from '../lib/api'
import type { SourceRelevance } from '../types'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'
import { shareLink } from '../lib/share'
import type { FullNode, NodeType, RelatedNode, ReadingPathItem } from '../types'
import { TypeBadge, MaturityBadge } from './NodeCard'
import GraphMini from './GraphMini'
import VizPanel from './VizPanel'

const EDGE_PREDICATES = [
  'all', 'uses', 'generalizes', 'contrasts-with',
  'prerequisite-of', 'grounds', 'extends',
  'equivalent-in-context', 'commonly-confused-with', 'illustrated-by',
]

function Pips({ count, filled, variant, sheet }: {
  count: number; filled: number; variant?: 'understand'; sheet?: boolean
}) {
  const pipClass = sheet ? 'sheet-pip' : 'pip'
  const filledClass = sheet
    ? `sheet-pip on${variant === 'understand' ? ' u' : ''}`
    : `pip filled${variant === 'understand' ? ' understand' : ''}`
  return (
    <div className={sheet ? 'sheet-pips' : 'status-pips'}>
      {Array.from({ length: count }, (_, i) => (
        <div key={i} className={i < filled ? filledClass : pipClass} />
      ))}
    </div>
  )
}

function MarkdownBody({ md, onWiki }: { md: string; onWiki: (slug: string) => void }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => {
    renderMath(ref.current)
    // Open external body links (e.g. explainer URLs) in a new tab instead of
    // navigating away from the PWA.
    ref.current?.querySelectorAll('a[href]').forEach((a) => {
      a.setAttribute('target', '_blank')
      a.setAttribute('rel', 'noreferrer')
    })
    // Internal [[wikilinks]] (no href) navigate in-app: resolve slug → IRI.
    const cleanups: Array<() => void> = []
    const wikis = Array.from(
      ref.current?.querySelectorAll('a.wikilink') ?? []
    ) as HTMLElement[]
    wikis.forEach((a) => {
      const handler = (e: Event) => {
        e.preventDefault()
        const slug = a.dataset.slug
        if (slug) onWiki(slug)
      }
      a.addEventListener('click', handler)
      cleanups.push(() => a.removeEventListener('click', handler))
    })
    // One batch round-trip to dim wikilinks that point at no node yet (dangling).
    const slugs = [...new Set(wikis.map((a) => a.dataset.slug).filter(Boolean) as string[])]
    let cancelled = false
    if (slugs.length) {
      resolveSlugs(slugs)
        .then((map) => {
          if (cancelled) return
          wikis.forEach((a) => {
            if (a.dataset.slug && map[a.dataset.slug] == null) a.classList.add('dangling')
          })
        })
        .catch(() => { /* leave links un-dimmed on error */ })
    }
    return () => { cancelled = true; cleanups.forEach((fn) => fn()) }
  }, [md, onWiki])
  return (
    <div
      ref={ref}
      className="body-text"
      dangerouslySetInnerHTML={{ __html: html }}
    />
  )
}

function ConnectionsList({
  connections,
  onNavigate,
}: {
  connections: RelatedNode[]
  onNavigate: (iri: string) => void
}) {
  const [edgeFilter, setEdgeFilter] = useState('all')

  const filtered =
    edgeFilter === 'all'
      ? connections
      : connections.filter((c) => c.edge_type === edgeFilter)

  return (
    <>
      <div className="edge-filter-strip">
        {EDGE_PREDICATES.map((p) => (
          <div
            key={p}
            className={`edge-chip${edgeFilter === p ? ' active' : ''}`}
            onClick={() => setEdgeFilter(p)}
          >
            {p}
          </div>
        ))}
      </div>
      {filtered.length === 0 && (
        <div className="empty-state" style={{ padding: '12px 0', textAlign: 'left' }}>
          no connections
        </div>
      )}
      {filtered.map((c, i) => (
        <div key={i} className="conn-item" onClick={() => onNavigate(c.iri)}>
          <span className="conn-predicate">{c.edge_type}</span>
          <div className="conn-detail">
            <div className="conn-target">{c.title}</div>
          </div>
        </div>
      ))}
    </>
  )
}

function ReadingPath({ items }: { items: ReadingPathItem[] }) {
  return (
    <>
      {items.map((item, i) => {
        const status = item.status ?? 'unread'
        const title = item.source_title ?? item.slug ?? '—'
        return (
          <div key={i} className="conn-item">
            <span className={`rp-status rp-${status}`}>{status}</span>
            <div className="conn-detail">
              <div className="conn-target" style={{ color: 'var(--text)' }}>{title}</div>
              {item.note && <div className="conn-note">{item.note}</div>}
            </div>
          </div>
        )
      })}
    </>
  )
}

function wikilinkSlug(ref: string): string {
  return ref.replace(/^\[\[/, '').replace(/\]\]$/, '').split('|')[0].trim()
}

// Parse a book node's "## Chapters" section into {slug,label} entries.
// Lines look like:  - [[mackay-itila-ch06]] — Ch. 6: About Inference
function parseChapters(content: string): { slug: string; label: string }[] {
  const m = content.match(/\n##[ \t]+Chapters[ \t]*\n([\s\S]*?)(?=\n##\s|$)/i)
  if (!m) return []
  const out: { slug: string; label: string }[] = []
  for (const line of m[1].split('\n')) {
    const lm = line.match(/\[\[([^\]|]+)(?:\|[^\]]*)?\]\]\s*(?:[—\-–:]\s*(.*))?/)
    if (lm) out.push({ slug: lm[1].trim(), label: (lm[2] || '').trim() })
  }
  return out
}

// Book → chapters: navigable list parsed from the "## Chapters" wikilinks.
function ChaptersList({ chapters, onNavigate }: {
  chapters: { slug: string; label: string }[]; onNavigate: (iri: string) => void
}) {
  return (
    <div className="body-section">
      <div className="body-section-title">chapters</div>
      {chapters.map((c) => (
        <div key={c.slug} className="conn-item" onClick={() => onNavigate(`pkis:source:${c.slug}`)}>
          <span className="conn-predicate">chapter</span>
          <div className="conn-detail"><div className="conn-target">{c.label || c.slug}</div></div>
        </div>
      ))}
    </div>
  )
}

// Chapter → book: a clickable chip pointing at the containing book.
function ParentBookNav({ parentBook, onNavigate }: {
  parentBook: string; onNavigate: (iri: string) => void
}) {
  const slug = parentBook.split(':').pop() || parentBook
  return (
    <div className="conn-item" style={{ marginBottom: 4 }} onClick={() => onNavigate(parentBook)}>
      <span className="conn-predicate">📖 in book</span>
      <div className="conn-detail"><div className="conn-target">{slug}</div></div>
    </div>
  )
}

// Citation + open-this-source links, shown when the node IS a source.
// "Research relevance" for a source: the frontier-gap concepts it advances (the
// "why am I reading this"). Quiet if the source isn't linked to any gap yet.
function SourceRelevancePanel({ slug, onNavigate }: { slug: string; onNavigate: (iri: string) => void }) {
  const [rel, setRel] = useState<SourceRelevance | null>(null)
  useEffect(() => { getSourceRelevance(slug).then(setRel).catch(() => {}) }, [slug])
  if (!rel || (!rel.serves.length && rel.frontier_score == null)) return null
  return (
    <div className="body-section relevance-section">
      <div className="body-section-label">
        research relevance{rel.frontier_score != null && <span className="rel-score"> · priority {rel.frontier_score}</span>}
      </div>
      {rel.serves.length === 0 ? (
        <div className="rel-empty">Not yet linked to any concept — a Librarian pass will connect it to the concepts it supports.</div>
      ) : (
        <div className="rel-list">
          <div className="rel-why">Reading this informs:</div>
          {rel.serves.map((s) => (
            <div key={s.concept_iri} className={`rel-row${s.is_gap ? ' gap' : ''}`} onClick={() => onNavigate(s.concept_iri)}>
              <span className="rel-concept">{s.concept}</span>
              <span className="rel-cov">coverage {s.coverage}</span>
              {s.is_gap && s.cluster && <span className="rel-cluster">⚡ frontier gap · {s.cluster}</span>}
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

function SourceBlock({ fm, title, iri }: { fm: Record<string, unknown>; title: string; iri: string }) {
  const sourceUrl = (fm.source_url as string) || (fm.url as string) || ''
  const docPath   = (fm.doc_path as string) || ''
  const readwise  = (fm.readwise_id as string) || ''
  const authors   = (fm.authors as string) || ''
  const year      = (fm.year as string | number) ?? ''
  const doi       = (fm.doi as string) || ''
  const [copied, setCopied] = useState(false)
  const [derivedPdf, setDerivedPdf] = useState('')

  // When no explicit doc_path, fall back to the split-chapter PDF convention
  // (/docs/sources/<slug>/<slug>.pdf) so the original document — figures and all
  // — is one tap away. HEAD-check so the link only appears when the file exists.
  const slug = iri.split(':').pop() || ''
  useEffect(() => {
    if (docPath || !slug) return
    let cancelled = false
    const url = `/docs/sources/${slug}/${slug}.pdf`
    fetch(url, { method: 'HEAD' })
      .then((r) => { if (!cancelled && r.ok) setDerivedPdf(url) })
      .catch(() => { /* not served */ })
    return () => { cancelled = true }
  }, [slug, docPath])

  const citation = [
    authors,
    year ? `(${year}).` : '',
    `${title}.`,
    doi ? `doi:${doi}` : (sourceUrl || ''),
  ].filter(Boolean).join(' ')

  const fileUrl = docPath ? `/docs/${docPath.replace(/^\/+/, '')}` : derivedPdf
  const readwiseUrl = readwise ? `https://read.readwise.io/read/${readwise}` : ''

  const copy = () => {
    navigator.clipboard?.writeText(citation).then(() => {
      setCopied(true); setTimeout(() => setCopied(false), 1500)
    }).catch(() => { /* noop */ })
  }

  return (
    <div className="body-section">
      <div className="body-section-title">source</div>
      <div className="citation">{citation}</div>
      <div className="source-links">
        {sourceUrl && <a className="source-link" href={sourceUrl} target="_blank" rel="noreferrer">↗ open url</a>}
        {fileUrl && <a className="source-link" href={fileUrl} target="_blank" rel="noreferrer">📄 open original</a>}
        {readwiseUrl && <a className="source-link" href={readwiseUrl} target="_blank" rel="noreferrer">▤ readwise</a>}
        <span className="source-link as-btn" onClick={copy}>{copied ? '✓ copied' : '⎘ copy citation'}</span>
      </div>
    </div>
  )
}

// Sources this (non-source) node cites — navigable, with a 'read' affordance when
// the source is actually readable, and dimmed when it isn't ingested yet.
function SourcesList({ sources, onNavigate }: { sources: string[]; onNavigate: (iri: string) => void }) {
  const slugs = sources.map(wikilinkSlug)
  const [status, setStatus] = useState<Record<string, SourceStatus>>({})
  useEffect(() => {
    let cancelled = false
    sourceStatus([...new Set(slugs)])
      .then((m) => { if (!cancelled) setStatus(m) })
      .catch(() => { /* leave un-annotated on error */ })
    return () => { cancelled = true }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [slugs.join('|')])

  return (
    <div className="body-section">
      <div className="body-section-title">sources to read</div>
      {sources.map((ref) => {
        const slug = wikilinkSlug(ref)
        const st = status[slug]
        const dangling = st ? st.iri === null : false
        return (
          <div
            key={slug}
            className={`conn-item source-row${dangling ? ' dangling' : ''}`}
            onClick={() => { if (st?.iri) onNavigate(st.iri) }}
          >
            <span className="conn-predicate">{dangling ? 'not ingested' : 'source'}</span>
            <div className="conn-detail"><div className="conn-target">{slug}</div></div>
            {st?.readable && st.read_url && (
              <a
                className="read-link"
                href={st.read_url}
                target="_blank"
                rel="noreferrer"
                onClick={(e) => e.stopPropagation()}
              >▶ read</a>
            )}
          </div>
        )
      })}
    </div>
  )
}

interface Props {
  iri: string
  onClose: () => void
  onNavigate: (iri: string) => void
  onEdit: () => void
  onGraph: () => void
  onListen: (slug: string) => void
  onOpenExplainer: (slug: string, title?: string) => void
}

export default function DetailSheet({ iri, onClose, onNavigate, onEdit, onGraph, onListen, onOpenExplainer }: Props) {
  const [node, setNode] = useState<FullNode | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [toast, setToast] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError(null)
    setNode(null)
    getNode(iri).then((n: FullNode & { error?: string }) => {
      if (cancelled) return
      // The backend returns 200 + {error} (and no frontmatter) for a missing node —
      // treat that as an error instead of rendering a blank shell titled with the IRI.
      if (n?.error || !n?.frontmatter) {
        setError(n?.error || `Node not found: ${iri}`); setLoading(false)
      } else {
        setNode(n); setLoading(false)
      }
    }).catch((e: unknown) => {
      if (!cancelled) { setError(String(e)); setLoading(false) }
    })
    return () => { cancelled = true }
  }, [iri])

  const fm = node?.frontmatter
  const nodeType = (fm?.knowledge_type ?? fm?.type ?? 'concept') as NodeType
  const coverage = fm?.coverage ?? 0
  const understanding = fm?.understanding ?? 0
  const maturity = fm?.maturity
  const title = fm?.title ?? iri
  const domain = fm?.domain ?? []
  const viz = fm?.viz
  const ownKind = (fm?.kind as string) || undefined
  const content = node?.content ?? ''
  const connections = node?.related_nodes ?? []

  // Surfaces to render: this node's own viz (asset nodes) plus any asset linked
  // via `illustrated-by`. visualization → inline; explainer → open full-screen.
  const vizItems: { slug: string; kind: string; title: string }[] = []
  const seenViz = new Set<string>()
  const addViz = (slug?: string | null, kind?: string | null, ttl?: string) => {
    if (!slug || seenViz.has(slug)) return
    seenViz.add(slug)
    vizItems.push({ slug, kind: kind || 'explainer', title: ttl || slug })
  }
  if (viz) addViz(viz, ownKind, title)
  connections.forEach((c) => {
    if (c.edge_type === 'illustrated-by' && c.viz) addViz(c.viz, c.kind, c.title)
  })
  const readingPath = node?.reading_path ?? []
  const isSource = iri.startsWith('pkis:source:')
  const sources = Array.isArray(fm?.sources) ? (fm!.sources as string[]) : []
  // Book ↔ chapter navigation: a book lists its chapters in "## Chapters";
  // a chapter points back via the parent_book frontmatter.
  const chapters = isSource ? parseChapters(content) : []
  const parentBook = (fm?.parent_book as string) || ''

  // Render the FULL node body for every node type — all sections (Definition,
  // Intuition, Why it matters, anatomy, mechanism, Formal Statement, Thesis…).
  // (Previously only Definition+Intuition surfaced, so the rest of every node
  // was authored-but-invisible in the viewer.)
  //
  // Strip ONLY sections that are also rendered structurally below, to avoid
  // duplication: the "## Connections" section (structural block always shows),
  // and "## Reading Path" but only when structured reading_path data exists —
  // when it's empty, the markdown section is the only copy, so keep it. The
  // anchored heading match leaves prose like "## Connections Beyond HMC" intact.
  function stripSection(md: string, name: string): string {
    return md.replace(
      new RegExp(`\\n##[ \\t]+${name}[ \\t]*(?=\\n|$)[\\s\\S]*?(?=\\n##\\s|$)`, 'i'),
      ''
    )
  }
  let fullBody = stripSection(content, 'Connections')
  if (readingPath.length > 0) fullBody = stripSection(fullBody, 'Reading Path')
  // The chapter wikilinks render as a navigable block below, so drop the raw
  // "## Chapters" list from the prose to avoid a dead, duplicated copy.
  if (chapters.length > 0) fullBody = stripSection(fullBody, 'Chapters')
  fullBody = fullBody.trim()

  return (
    <div className="sheet-overlay open">
      {toast && <div className="toast">{toast}</div>}
      <div className="sheet-backdrop" onClick={onClose} />
      <div className="sheet">
        <div className="sheet-handle" />

        {/* ── HEADER ── */}
        <div className="sheet-header">
          <div className="sheet-type-row">
            <TypeBadge type={nodeType} sheet />
            {domain.slice(0, 2).map((d) => (
              <span key={d} className="domain-tag">{d}</span>
            ))}
          </div>
          <div className="sheet-title">{title}</div>
          <div className="sheet-status-row">
            <div className="sheet-status-item">
              <span className="sheet-status-label">coverage</span>
              <Pips count={5} filled={coverage} sheet />
            </div>
            <div className="sheet-status-item">
              <span className="sheet-status-label">understanding</span>
              <Pips count={5} filled={understanding} variant="understand" sheet />
            </div>
            <MaturityBadge maturity={maturity} />
          </div>
        </div>

        {/* ── BODY ── */}
        <div className="sheet-body">
          {loading && (
            <div className="loading-row">
              <div className="loading-spinner" /> loading node…
            </div>
          )}
          {error && <div style={{ color: 'var(--red)', fontSize: 12 }}>{error}</div>}

          {!loading && node && (
            <>
              {/* Chapter → containing book (navigable) */}
              {parentBook && <ParentBookNav parentBook={parentBook} onNavigate={onNavigate} />}

              {/* Full node body — every section, with its own ## headings */}
              {fullBody && (
                <div className="body-section">
                  <MarkdownBody
                    md={fullBody}
                    onWiki={(slug) => resolveSlug(slug).then((target) => {
                      if (target) onNavigate(target)
                      else { setToast('“' + slug + '” isn’t a node yet'); setTimeout(() => setToast(null), 1800) }
                    })}
                  />
                </div>
              )}

              {/* Book → chapters (navigable) */}
              {chapters.length > 0 && (
                <ChaptersList chapters={chapters} onNavigate={onNavigate} />
              )}

              {/* Source citation + links (when this node is a source) */}
              {isSource && fm && <SourceBlock fm={fm as Record<string, unknown>} title={title} iri={iri} />}

              {/* Why read it: the frontier-gap concepts this source advances. */}
              {isSource && <SourceRelevancePanel slug={iri.split(':').pop() || ''} onNavigate={onNavigate} />}

              {/* Explainers & visualizations: viz-kind inline, explainer-kind as
                  a full-screen link (cramming a full HTML page inline is unreadable). */}
              {vizItems.length > 0 && (
                <div className="body-section">
                  <div className="body-section-title">
                    {vizItems.some((v) => v.kind === 'visualization') ? 'visualization' : 'explainer'}
                  </div>
                  {vizItems.map((v) =>
                    v.kind === 'visualization' ? (
                      <VizPanel key={v.slug} slug={v.slug} />
                    ) : (
                      <div key={v.slug} className="explainer-link" onClick={() => onOpenExplainer(v.slug, v.title)}>
                        <span className="explainer-link-icon">◈</span>
                        <span className="explainer-link-title">{v.title}</span>
                        <span className="explainer-link-open">open →</span>
                      </div>
                    )
                  )}
                </div>
              )}

              {/* Ego-network mini graph */}
              <div className="body-section">
                <div className="body-section-title">graph</div>
                <GraphMini
                  focusIri={iri}
                  focusTitle={title}
                  focusType={nodeType}
                  onNavigate={onNavigate}
                />
              </div>

              {/* Sources to read (when this node cites sources) */}
              {!isSource && sources.length > 0 && (
                <SourcesList sources={sources} onNavigate={onNavigate} />
              )}

              {/* Connections */}
              <div className="body-section">
                <div className="body-section-title">connections</div>
                <ConnectionsList connections={connections} onNavigate={onNavigate} />
              </div>

              {/* Reading path */}
              {readingPath.length > 0 && (
                <div className="body-section">
                  <div className="body-section-title">reading path</div>
                  <ReadingPath items={readingPath} />
                </div>
              )}
            </>
          )}
        </div>

        {/* ── ACTIONS ── */}
        <div className="sheet-actions">
          <div className="action-btn" onClick={onClose}>← back</div>
          {isSource && (
            <div className="action-btn" onClick={() => onListen(iri.split(':').pop() || '')}>▶ listen</div>
          )}
          <div className="action-btn"
            onClick={() => { void shareLink(`/app/?n=${iri.split(':').pop()}`, title) }}>↗ share</div>
          <div className="action-btn" onClick={onGraph}>⬡ graph</div>
          <div className="action-btn primary" onClick={onEdit}>✎ edit</div>
        </div>
      </div>
    </div>
  )
}
