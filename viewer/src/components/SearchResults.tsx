import type { SearchResult, NodeType } from '../types'
import NodeCard from './NodeCard'

function typeFromIri(iri: string): string {
  const parts = iri.split(':')
  return parts.length >= 2 ? parts[1] : ''
}

interface Props {
  results: SearchResult[]
  typeFilter: NodeType | 'all'
  onSelectNode: (iri: string) => void
}

export default function SearchResults({ results, typeFilter, onSelectNode }: Props) {
  const filtered = typeFilter === 'all'
    ? results
    : results.filter((r) => (r.node_type || typeFromIri(r.iri)) === typeFilter)

  return (
    <div>
      <div className="section-label">
        search results{filtered.length > 0 ? ` · ${filtered.length}` : ''}
      </div>
      {filtered.length === 0 && <div className="empty-state">no results</div>}
      {filtered.map((r) => (
        <NodeCard key={r.iri} node={r} onClick={onSelectNode} />
      ))}
    </div>
  )
}
