import { useEffect, useState } from 'react'
import { getClusterPriorities } from '../lib/api'
import type { ClusterPriorities } from '../types'

interface Props {
  onSelectNode: (iri: string) => void
}

export default function PriorityView({ onSelectNode }: Props) {
  const [data, setData] = useState<ClusterPriorities | null>(null)
  const [loading, setLoading] = useState(true)
  const [collapsed, setCollapsed] = useState<Record<string, boolean>>({})

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    getClusterPriorities()
      .then((d) => { if (!cancelled) { setData(d); setLoading(false) } })
      .catch(() => { if (!cancelled) setLoading(false) })
    return () => { cancelled = true }
  }, [])

  if (loading) {
    return (
      <div className="loading-row">
        <div className="loading-spinner" /> loading priority…
      </div>
    )
  }
  if (!data) {
    return <div className="empty-state">could not load priorities</div>
  }

  const toggle = (slug: string) => setCollapsed((c) => ({ ...c, [slug]: !c[slug] }))

  return (
    <div>
      <div className="priority-caption">
        reading priority by research cluster — coverage gaps blocking each frontier
        <span className="priority-weight">
          proximity weight {data.params.cluster_proximity_weight} · {data.params.weight_source}
        </span>
      </div>

      {data.clusters.map((g) => {
        const isCollapsed = collapsed[g.cluster_slug]
        return (
          <div key={g.cluster_slug} className="prio-group">
            <div className="prio-group-head" onClick={() => toggle(g.cluster_slug)}>
              <span className="prio-caret">{isCollapsed ? '▸' : '▾'}</span>
              <span className="prio-cluster-title">{g.cluster_title}</span>
              {g.lead_hypothesis && (
                <span className="prio-lead">lead: {g.lead_hypothesis.replace(g.cluster_slug + '-', '')}</span>
              )}
              <span className="prio-gap-count">{g.gaps.length}</span>
            </div>
            {!isCollapsed && g.gaps.map((gap) => (
              <div key={gap.iri} className="gap-row" onClick={() => onSelectNode(gap.iri)}>
                <span className="card-type">{gap.type}</span>
                <span className="gap-title">{gap.title}</span>
                <CovBar coverage={gap.coverage} />
              </div>
            ))}
            {!isCollapsed && g.gaps.length === 0 && (
              <div className="gap-empty">no materialized dependencies</div>
            )}
          </div>
        )
      })}

      {data.reading_queue.length > 0 && (
        <>
          <div className="section-label">reading queue · sources · {data.reading_queue.length}</div>
          {data.reading_queue.slice(0, 30).map((item, i) => (
            <div
              key={i}
              className="queue-item"
              onClick={() => onSelectNode(`pkis:source:${item.slug}`)}
            >
              <div className={`queue-priority prio-${item.hint ?? 'normal'}`} />
              <div className="queue-info">
                <div className="queue-title">{item.slug}</div>
                {item.reason && <div className="queue-reason">{item.reason}</div>}
              </div>
              <div className="queue-action">read →</div>
            </div>
          ))}
        </>
      )}
    </div>
  )
}

function CovBar({ coverage }: { coverage: number }) {
  const pct = Math.min(100, (coverage / 6) * 100)
  const tone = coverage <= 1 ? 'gap-low' : coverage <= 3 ? 'gap-mid' : 'gap-ok'
  return (
    <span className={`cov-bar ${tone}`} title={`coverage ${coverage}`}>
      <span className="cov-bar-fill" style={{ width: `${pct}%` }} />
    </span>
  )
}
