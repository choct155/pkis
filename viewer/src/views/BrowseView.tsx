import { useEffect, useState } from 'react'
import { getHealth, getFrontier, getReadingQueue, getStagedNodes } from '../lib/api'
import type { HealthMetrics, FrontierNode, QueueItem, NodeType, View, StagedNode } from '../types'
import NodeCard from '../components/NodeCard'

interface Props {
  typeFilter: NodeType | 'all'
  onSelectNode: (iri: string) => void
  onNavigate: (v: View) => void
}

// Frontier rows may omit node_type; fall back to the IRI segment so the type
// filter *filters* the cards rather than hiding all of them.
function typeOf(n: FrontierNode): string {
  if (n.node_type) return n.node_type
  const parts = n.iri.split(':')
  return parts.length >= 2 ? parts[1] : ''
}

export default function BrowseView({ typeFilter, onSelectNode, onNavigate }: Props) {
  const [health, setHealth]   = useState<HealthMetrics | null>(null)
  const [frontier, setFrontier] = useState<FrontierNode[]>([])
  const [queue, setQueue]     = useState<QueueItem[]>([])
  const [stagedCount, setStagedCount] = useState(0)
  const [loadingMain, setLoadingMain] = useState(true)

  useEffect(() => {
    let cancelled = false
    setLoadingMain(true)
    Promise.all([getHealth(), getFrontier(), getReadingQueue(), getStagedNodes({ limit: 500 })])
      .then(([h, f, q, s]: [HealthMetrics, FrontierNode[], QueueItem[], StagedNode[]]) => {
        if (cancelled) return
        setHealth(h)
        setFrontier(f)
        setQueue(q)
        setStagedCount(s.length)   // live count, not a limit:1 placeholder
        setLoadingMain(false)
      })
      .catch(() => { if (!cancelled) setLoadingMain(false) })
    return () => { cancelled = true }
  }, [])

  // Type filter applies ONLY to the frontier cards. The reading queue is sources
  // and is intentionally left unaffected by the node-type filter.
  const filteredFrontier = typeFilter === 'all'
    ? frontier
    : frontier.filter((f) => typeOf(f) === typeFilter)

  const prioritizedQueue = [...queue].sort((a, b) =>
    a.priority === 'high' && b.priority !== 'high' ? -1 :
    b.priority === 'high' && a.priority !== 'high' ? 1 : 0
  ).slice(0, 5)

  return (
    <div>
      {/* Staged nodes badge */}
      {stagedCount > 0 && (
        <div className="staged-badge" onClick={() => onNavigate('staged')}>
          <div className="staged-dot" />
          {stagedCount} staged node{stagedCount > 1 ? 's' : ''} awaiting review
        </div>
      )}

      {/* Stats row */}
      {loadingMain ? (
        <div className="loading-row">
          <div className="loading-spinner" /> loading stats…
        </div>
      ) : health && (
        <div className="stats-row">
          <div className="stat-card">
            <span className="stat-value">{health.total_nodes}</span>
            <span className="stat-label">nodes</span>
          </div>
          <div className="stat-card">
            <span className="stat-value">{health.total_sources}</span>
            <span className="stat-label">sources</span>
          </div>
          <div className="stat-card">
            <span className="stat-value">{health.queue_depth}</span>
            <span className="stat-label">queue</span>
          </div>
        </div>
      )}

      {/* Frontier */}
      <div className="section-label">frontier — needs attention</div>
      {filteredFrontier.length === 0 ? (
        <div className="empty-state">
          {typeFilter === 'all' ? 'nothing on the frontier' : `no ${typeFilter} nodes on the frontier`}
        </div>
      ) : (
        filteredFrontier.slice(0, 8).map((n) => (
          <NodeCard key={n.iri} node={n} onClick={onSelectNode} />
        ))
      )}

      {/* Reading queue (unaffected by type filter) */}
      {prioritizedQueue.length > 0 && (
        <>
          <div className="section-label">reading queue</div>
          {prioritizedQueue.map((item, i) => (
            <div key={i} className="queue-item" onClick={() => onNavigate('priority')}>
              <div className={`queue-priority prio-${item.priority}`} />
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
