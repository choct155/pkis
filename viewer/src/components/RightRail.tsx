import { useEffect, useState } from 'react'
import { getClusters } from '../lib/api'
import type { Cluster } from '../types'
import type { RecentNode } from '../lib/useRecent'

interface Props {
  recent: RecentNode[]
  onSelectNode: (iri: string) => void
  onCluster: (slug: string) => void   // browse a cluster as a facet
  onAgenda: () => void                 // open the full Clusters view
}

// Desktop-only context rail (CSS-hidden below the wide breakpoint). Surfaces the
// active research agenda — what's being worked on right now, richer than the
// sidebar's flat cluster list — plus a jump-back list of recently-viewed nodes.
export default function RightRail({ recent, onSelectNode, onCluster, onAgenda }: Props) {
  const [clusters, setClusters] = useState<Cluster[]>([])

  useEffect(() => {
    let cancelled = false
    getClusters().then((c) => { if (!cancelled) setClusters(c) }).catch(() => {})
    return () => { cancelled = true }
  }, [])

  // The agenda is the *active* clusters; fall back to the first few if none are
  // explicitly flagged active, so the rail is never empty when clusters exist.
  const active = clusters.filter((c) => c.status === 'active')
  const agenda = (active.length ? active : clusters).slice(0, 6)

  return (
    <aside className="right-rail">
      {agenda.length > 0 && (
        <div className="rail-section">
          <div className="rail-section-label">
            agenda
            <span className="rail-section-action" onClick={onAgenda}>all ↳</span>
          </div>
          {agenda.map((c) => (
            <div key={c.slug} className="rail-agenda-item" onClick={() => onCluster(c.slug)} title={c.thesis || c.title}>
              <div className="rail-agenda-title">{c.title}</div>
              {c.current_frontier && (
                <div className="rail-agenda-frontier">{c.current_frontier}</div>
              )}
            </div>
          ))}
        </div>
      )}

      <div className="rail-section">
        <div className="rail-section-label">recently viewed</div>
        {recent.length === 0 ? (
          <div className="rail-empty">nodes you open show up here</div>
        ) : (
          recent.map((r) => (
            <div key={r.iri} className="rail-recent-item" onClick={() => onSelectNode(r.iri)} title={r.title}>
              {r.title}
            </div>
          ))
        )}
      </div>
    </aside>
  )
}
