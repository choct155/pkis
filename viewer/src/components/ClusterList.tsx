import { useEffect, useState } from 'react'
import { getClusters } from '../lib/api'
import type { Cluster } from '../types'

interface Props {
  active: string
  onChange: (slug: string) => void   // select a cluster as a browse facet
  onAgenda: () => void                // jump to the Clusters research-agenda view
}

// Sidebar cluster picker: selecting a cluster sets it as a browse facet; the
// "agenda ↳" affordance opens the richer Clusters detail view.
export default function ClusterList({ active, onChange, onAgenda }: Props) {
  const [clusters, setClusters] = useState<Cluster[]>([])

  useEffect(() => {
    let cancelled = false
    getClusters().then((c) => { if (!cancelled) setClusters(c) }).catch(() => {})
    return () => { cancelled = true }
  }, [])

  if (clusters.length === 0) return null

  return (
    <div className="sidebar-section">
      <div className="sidebar-section-label">
        clusters
        <span className="sidebar-section-action" onClick={onAgenda}>agenda ↳</span>
      </div>
      {clusters.map((c) => (
        <div
          key={c.slug}
          className={`cluster-row${active === c.slug ? ' active' : ''}`}
          onClick={() => onChange(active === c.slug ? 'all' : c.slug)}
          title={c.title}
        >
          {c.title}
        </div>
      ))}
    </div>
  )
}
