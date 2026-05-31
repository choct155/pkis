import type { SearchResult, FrontierNode, NodeType, Maturity } from '../types'

interface NodeCardData {
  iri: string
  title: string
  nodeType: string
  domain: string[]
  coverage: number
  understanding: number
  maturity?: Maturity
  description?: string
}

function toCardData(n: SearchResult | FrontierNode): NodeCardData {
  const isSearch = 'canonical_title' in n
  return {
    iri: n.iri,
    title: isSearch ? (n as SearchResult).canonical_title : (n as FrontierNode).canonical_title,
    nodeType: isSearch ? (n as SearchResult).node_type : ((n as FrontierNode).node_type ?? ''),
    domain: isSearch ? (n as SearchResult).domain : ((n as FrontierNode).domain ?? []),
    coverage: n.coverage,
    understanding: n.understanding,
    maturity: isSearch ? (n as SearchResult).maturity : (n as FrontierNode).maturity,
    description: isSearch
      ? (n as SearchResult).one_line_summary
      : undefined,
  }
}

function Pips({ count, filled, variant }: { count: number; filled: number; variant?: 'understand' }) {
  return (
    <div className="status-pips">
      {Array.from({ length: count }, (_, i) => (
        <div
          key={i}
          className={`pip${i < filled ? ` filled${variant === 'understand' ? ' understand' : ''}` : ''}`}
        />
      ))}
    </div>
  )
}

export function MaturityBadge({ maturity }: { maturity?: Maturity }) {
  if (!maturity) return null
  const cls = {
    settled: 'mat-settled',
    evolving: 'mat-evolving',
    contested: 'mat-contested',
    historical: 'mat-historical',
  }[maturity] ?? 'mat-evolving'
  return <span className={`maturity ${cls}`}>{maturity}</span>
}

export function TypeBadge({ type, sheet }: { type: string; sheet?: boolean }) {
  const cls = sheet
    ? `sheet-type-badge badge-${type || 'unknown'}`
    : 'card-type'
  return <span className={cls}>{type || '?'}</span>
}

interface Props {
  node: SearchResult | FrontierNode
  onClick: (iri: string) => void
}

export default function NodeCard({ node, onClick }: Props) {
  const d = toCardData(node)
  const nt = (d.nodeType || 'concept') as NodeType

  return (
    <div className={`node-card ${nt}`} onClick={() => onClick(d.iri)}>
      <div className="card-header">
        <span className="card-type">{nt}</span>
        <span className="card-title">{d.title}</span>
      </div>
      {d.description && <div className="card-desc">{d.description}</div>}
      <div className="card-meta">
        {d.domain.slice(0, 3).map((dm) => (
          <span key={dm} className="domain-tag">{dm}</span>
        ))}
        <div className="status-row">
          {d.coverage > 0 && (
            <div className="status-item">
              <span className="status-label">cov</span>
              <Pips count={5} filled={d.coverage} />
            </div>
          )}
          {d.understanding > 0 && (
            <div className="status-item">
              <span className="status-label">und</span>
              <Pips count={5} filled={d.understanding} variant="understand" />
            </div>
          )}
          <MaturityBadge maturity={d.maturity} />
        </div>
      </div>
    </div>
  )
}
