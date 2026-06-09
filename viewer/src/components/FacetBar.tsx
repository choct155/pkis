import type { NodeType } from '../types'

interface Props {
  typeFilter: NodeType | 'all'
  domainFilter: string
  clusterFilter: string
  onClearType: () => void
  onClearDomain: () => void
  onClearCluster: () => void
}

// The "unified" surface: shows every active browse facet (domain × type ×
// cluster) as a removable pill so the combined filter is legible at a glance.
// Renders nothing when no facet is active.
export default function FacetBar({
  typeFilter, domainFilter, clusterFilter,
  onClearType, onClearDomain, onClearCluster,
}: Props) {
  const pills: { key: string; label: string; onClear: () => void }[] = []
  if (domainFilter !== 'all') pills.push({ key: 'd', label: `domain: ${domainFilter}`, onClear: onClearDomain })
  if (typeFilter !== 'all') pills.push({ key: 't', label: `type: ${typeFilter}`, onClear: onClearType })
  if (clusterFilter !== 'all') pills.push({ key: 'c', label: `cluster: ${clusterFilter}`, onClear: onClearCluster })

  if (pills.length === 0) return null

  return (
    <div className="facet-bar">
      {pills.map((p) => (
        <span key={p.key} className="facet-pill" onClick={p.onClear}>
          {p.label} <span className="facet-pill-x">×</span>
        </span>
      ))}
      {pills.length > 1 && (
        <span
          className="facet-clear-all"
          onClick={() => { onClearType(); onClearDomain(); onClearCluster() }}
        >
          clear all
        </span>
      )}
    </div>
  )
}
