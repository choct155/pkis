import { useEffect, useRef, useState } from 'react'
import { getNode } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'
import type { FullNode, NodeType, RelatedNode, ReadingPathItem } from '../types'
import { TypeBadge, MaturityBadge } from './NodeCard'
import GraphMini from './GraphMini'
import VizPanel from './VizPanel'

const EDGE_PREDICATES = [
  'all', 'uses', 'generalizes', 'contrasts-with',
  'prerequisite-of', 'grounds', 'extends',
  'equivalent-in-context', 'commonly-confused-with',
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

function MarkdownBody({ md }: { md: string }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => { renderMath(ref.current) }, [md])
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

// Citation + open-this-source links, shown when the node IS a source.
function SourceBlock({ fm, title }: { fm: Record<string, unknown>; title: string }) {
  const sourceUrl = (fm.source_url as string) || (fm.url as string) || ''
  const docPath   = (fm.doc_path as string) || ''
  const readwise  = (fm.readwise_id as string) || ''
  const authors   = (fm.authors as string) || ''
  const year      = (fm.year as string | number) ?? ''
  const doi       = (fm.doi as string) || ''
  const [copied, setCopied] = useState(false)

  const citation = [
    authors,
    year ? `(${year}).` : '',
    `${title}.`,
    doi ? `doi:${doi}` : (sourceUrl || ''),
  ].filter(Boolean).join(' ')

  const fileUrl = docPath ? `/docs/${docPath.replace(/^\/+/, '')}` : ''
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
        {fileUrl && <a className="source-link" href={fileUrl} target="_blank" rel="noreferrer">⤓ open file</a>}
        {readwiseUrl && <a className="source-link" href={readwiseUrl} target="_blank" rel="noreferrer">▤ readwise</a>}
        <span className="source-link as-btn" onClick={copy}>{copied ? '✓ copied' : '⎘ copy citation'}</span>
      </div>
    </div>
  )
}

// Sources this (non-source) node cites — navigable to each source node.
function SourcesList({ sources, onNavigate }: { sources: string[]; onNavigate: (iri: string) => void }) {
  return (
    <div className="body-section">
      <div className="body-section-title">sources to read</div>
      {sources.map((ref) => {
        const slug = wikilinkSlug(ref)
        return (
          <div key={slug} className="conn-item" onClick={() => onNavigate(`pkis:source:${slug}`)}>
            <span className="conn-predicate">source</span>
            <div className="conn-detail"><div className="conn-target">{slug}</div></div>
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
}

export default function DetailSheet({ iri, onClose, onNavigate, onEdit, onGraph }: Props) {
  const [node, setNode] = useState<FullNode | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    setError(null)
    setNode(null)
    getNode(iri).then((n: FullNode) => {
      if (!cancelled) { setNode(n); setLoading(false) }
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
  const content = node?.content ?? ''
  const connections = node?.related_nodes ?? []
  const readingPath = node?.reading_path ?? []
  const isSource = iri.startsWith('pkis:source:')
  const sources = Array.isArray(fm?.sources) ? (fm!.sources as string[]) : []

  // Split content into sections by ## headings
  function extractSection(md: string, heading: RegExp): string {
    const match = md.match(heading)
    if (!match || match.index === undefined) return ''
    const start = match.index + match[0].length
    const rest = md.slice(start)
    const nextHeading = rest.match(/\n##\s/)
    return nextHeading ? rest.slice(0, nextHeading.index).trim() : rest.trim()
  }

  const definitionMd = extractSection(content, /^## Definition\s*/m) || content.split('\n\n')[0]
  const intuitionMd  = extractSection(content, /^## Intuition\s*/m)

  return (
    <div className="sheet-overlay open">
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
              {/* Definition */}
              {definitionMd && (
                <div className="body-section">
                  <div className="body-section-title">definition</div>
                  <MarkdownBody md={definitionMd} />
                </div>
              )}

              {/* Source citation + links (when this node is a source) */}
              {isSource && fm && <SourceBlock fm={fm as Record<string, unknown>} title={title} />}

              {/* Visualization */}
              {viz && (
                <div className="body-section">
                  <div className="body-section-title">visualization</div>
                  <VizPanel slug={viz} />
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

              {/* Intuition */}
              {intuitionMd && (
                <div className="body-section">
                  <div className="body-section-title">intuition</div>
                  <MarkdownBody md={intuitionMd} />
                </div>
              )}

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
          <div className="action-btn" onClick={onGraph}>⬡ graph</div>
          <div className="action-btn primary" onClick={onEdit}>✎ edit</div>
        </div>
      </div>
    </div>
  )
}
