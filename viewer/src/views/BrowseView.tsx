import { useEffect, useState } from 'react'
import { getHealth, getFrontier, getReadingQueue, getStagedNodes } from '../lib/api'
import type { HealthMetrics, FrontierNode, QueueItem, SearchResult, NodeType, View, StagedNode } from '../types'
import NodeCard from '../components/NodeCard'

interface Props {
  typeFilter: NodeType | 'all'
  searchResults: SearchResult[] | null
  onSelectNode: (iri: string) => void
  onNavigate: (v: View) => void
}

export default function BrowseView({ typeFilter, searchResults, onSelectNode, onNavigate }: Props) {
  const [health, setHealth]   = useState<HealthMetrics | null>(null)
  const [frontier, setFrontier] = useState<FrontierNode[]>([])
  const [queue, setQueue]     = useState<QueueItem[]>([])
  const [stagedCount, setStagedCount] = useState(0)
  const [loadingMain, setLoadingMain] = useState(true)

  useEffect(() => {
    let cancelled = false
    setLoadingMain(true)
    Promise.all([getHealth(), getFrontier(), getReadingQueue(), getStagedNodes({ limit: 1 })])
      .then(([h, f, q, s]: [HealthMetrics, FrontierNode[], QueueItem[], StagedNode[]]) => {
        if (cancelled) return
        setHealth(h)
        setFrontier(f)
        setQueue(q)
        setStagedCount(s.length)
        setLoadingMain(false)
      })
      .catch(() => { if (!cancelled) setLoadingMain(false) })
    return () => { cancelled = true }
  }, [])

  // If we have search results, show those instead
  if (searchResults !== null) {
    const filtered = typeFilter === 'all'
      ? searchResults
      : searchResults.filter((r) => r.node_type === typeFilter)

    return (
      <div>
        <div className="section-label">
          search results {filtered.length > 0 ? `· ${filtered.length}` : ''}
        </div>
        {filtered.length === 0 && (
          <div className="empty-state">no results</div>
        )}
        {filtered.map((r) => (
          <NodeCard key={r.iri} node={r} onClick={onSelectNode} />
        ))}
      </div>
    )
  }

  const filteredFrontier = typeFilter === 'all'
    ? frontier
    : frontier.filter((f) => f.node_type === typeFilter)

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
      {filteredFrontier.length > 0 && (
        <>
          <div className="section-label">frontier — needs attention</div>
          {filteredFrontier.slice(0, 5).map((n) => (
            <NodeCard key={n.iri} node={n} onClick={onSelectNode} />
          ))}
        </>
      )}

      {/* Reading queue */}
      {prioritizedQueue.length > 0 && (
        <>
          <div className="section-label">reading queue</div>
          {prioritizedQueue.map((item, i) => (
            <div
              key={i}
              className="queue-item"
              onClick={() => onNavigate('queue')}
            >
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
