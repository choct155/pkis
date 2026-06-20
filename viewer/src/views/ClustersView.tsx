import { useEffect, useState } from 'react'
import { getClusters } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import type { Cluster } from '../types'

interface Props {
  onSelectNode: (iri: string) => void
  onDomain: (d: string) => void          // cross-link: browse a domain
  onBrowseCluster: (slug: string) => void // browse a cluster's nodes as a facet
}

export default function ClustersView({ onSelectNode, onDomain, onBrowseCluster }: Props) {
  const [clusters, setClusters] = useState<Cluster[]>([])
  const [loading, setLoading] = useState(true)
  const [selected, setSelected] = useState<Cluster | null>(null)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    getClusters()
      .then((c) => { if (!cancelled) { setClusters(c); setLoading(false) } })
      .catch(() => { if (!cancelled) setLoading(false) })
    return () => { cancelled = true }
  }, [])

  if (loading) {
    return (
      <div className="loading-row">
        <div className="loading-spinner" /> loading clusters…
      </div>
    )
  }

  if (selected) {
    return (
      <ClusterDetail
        cluster={selected}
        onBack={() => setSelected(null)}
        onSelectNode={onSelectNode}
        onDomain={onDomain}
        onBrowseCluster={onBrowseCluster}
      />
    )
  }

  if (clusters.length === 0) {
    return <div className="empty-state">no research clusters</div>
  }

  return (
    <div>
      <div className="section-label">research clusters · {clusters.length}</div>
      {clusters.map((c) => (
        <div key={c.iri} className="cluster-card" onClick={() => setSelected(c)}>
          <div className="cluster-card-head">
            <span className="cluster-title">{c.title}</span>
            {c.status !== 'active' && <span className="cluster-status">{c.status}</span>}
            <span
              className="cluster-browse"
              onClick={(e) => { e.stopPropagation(); onBrowseCluster(c.slug) }}
              title="Browse this cluster's nodes"
            >browse →</span>
          </div>
          <div className="cluster-card-meta">
            {c.domain.slice(0, 3).map((d) => (
              <span
                key={d}
                className="domain-tag clickable"
                onClick={(e) => { e.stopPropagation(); onDomain(d) }}
              >{d}</span>
            ))}
            <span className="cluster-counts">
              {c.hypotheses.length} hyp · frontier {c.frontier_hypotheses.length}
            </span>
          </div>
        </div>
      ))}
    </div>
  )
}

function ClusterDetail({ cluster, onBack, onSelectNode, onDomain, onBrowseCluster }: {
  cluster: Cluster
  onBack: () => void
  onSelectNode: (iri: string) => void
  onDomain: (d: string) => void
  onBrowseCluster: (slug: string) => void
}) {
  return (
    <div className="cluster-detail">
      <div className="cluster-detail-bar">
        <div className="cluster-back" onClick={onBack}>← clusters</div>
        <span className="cluster-browse" onClick={() => onSelectNode(cluster.iri)}>open cluster node →</span>
        <span className="cluster-browse" onClick={() => onBrowseCluster(cluster.slug)}>browse nodes →</span>
      </div>
      <h2 className="cluster-detail-title">{cluster.title}</h2>
      <div className="cluster-card-meta">
        {cluster.domain.map((d) => (
          <span key={d} className="domain-tag clickable" onClick={() => onDomain(d)}>{d}</span>
        ))}
      </div>

      {cluster.thesis && (
        <>
          <div className="section-label">thesis</div>
          <div className="prose" dangerouslySetInnerHTML={{ __html: renderMarkdown(cluster.thesis) }} />
        </>
      )}

      <div className="section-label">constituent hypotheses · {cluster.hypotheses.length}</div>
      {cluster.hypotheses.map((h) => (
        <div
          key={h.slug}
          className={`hyp-row${h.is_frontier ? ' frontier' : ''}${h.iri ? '' : ' missing'}`}
          onClick={() => h.iri && onSelectNode(h.iri)}
        >
          <div className="hyp-row-head">
            {h.is_frontier && <span className="frontier-pill">frontier</span>}
            <span className="hyp-title">{h.title}</span>
          </div>
          <div className="hyp-meta">
            {h.role && <span className="hyp-role">{h.role}</span>}
            <span className={`hyp-status status-${h.status}`}>{h.status}</span>
          </div>
        </div>
      ))}

      {cluster.deps.length > 0 && (
        <>
          <div className="section-label">depends on · {cluster.deps.length}</div>
          {cluster.deps.map((d) => (
            <div key={d.iri} className="dep-row" onClick={() => onSelectNode(d.iri)}>
              <span className={`card-type`}>{d.type}</span>
              <span className="dep-title">{d.title}</span>
              <span className="dep-cov">cov {d.coverage}</span>
            </div>
          ))}
        </>
      )}

      {cluster.current_frontier && (
        <>
          <div className="section-label">current frontier</div>
          <div className="prose" dangerouslySetInnerHTML={{ __html: renderMarkdown(cluster.current_frontier) }} />
        </>
      )}
    </div>
  )
}
