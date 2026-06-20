import { useEffect, useState } from 'react'
import { getClusterPriorities } from '../lib/api'
import type { ClusterPriorities, QueueItem } from '../types'

interface Props {
  onSelectNode: (iri: string) => void
}

// Priority = the ranked reading queue. Each source leads with WHY it's worth
// reading (the frontier-gap concepts/clusters it advances, or its capture reason)
// and a relevance bar from its frontier priority score. The by-cluster gap
// breakdown lives in the Clusters tab now.
export default function PriorityView({ onSelectNode }: Props) {
  const [data, setData] = useState<ClusterPriorities | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    getClusterPriorities()
      .then((d) => { if (!cancelled) { setData(d); setLoading(false) } })
      .catch(() => { if (!cancelled) setLoading(false) })
    return () => { cancelled = true }
  }, [])

  if (loading) return <div className="loading-row"><div className="loading-spinner" /> loading priority…</div>
  if (!data) return <div className="empty-state">could not load priorities</div>

  const queue = data.reading_queue
  const maxScore = Math.max(1, ...queue.map((q) => q.frontier_score || 0))

  return (
    <div>
      <div className="priority-caption">
        reading queue — ordered by research priority (which frontier gaps each source fills)
      </div>

      {queue.length === 0 && <div className="empty-state">reading queue is empty</div>}

      {queue.map((item, i) => (
        <div key={i} className="qrow" onClick={() => onSelectNode(`pkis:source:${item.slug}`)}>
          <RelevanceBar score={item.frontier_score} max={maxScore} />
          <div className="qrow-body">
            <div className="qrow-title">{item.title_full || item.slug}</div>
            <Why item={item} />
          </div>
          <div className="qrow-go">read →</div>
        </div>
      ))}
    </div>
  )
}

// "Why read it": the concept(s) it informs (frontier gaps flagged) → else reason.
function Why({ item }: { item: QueueItem }) {
  const serves = item.serves || []
  const more = serves.length > 1 ? <span className="qrow-more"> +{serves.length - 1} more</span> : null
  if (serves.length) {
    const s = serves[0]
    if (s.is_gap) {
      return (
        <div className="qrow-why">
          advances <span className="qrow-concept">{s.concept}</span>
          <span className="qrow-cov"> (cov {s.coverage})</span>
          {s.cluster && <> — frontier gap in <span className="qrow-cluster">{s.cluster}</span></>}
          {more}
        </div>
      )
    }
    return <div className="qrow-why">informs <span className="qrow-concept">{s.concept}</span>{more}</div>
  }
  if (item.reason) return <div className="qrow-why muted">{item.reason}</div>
  return <div className="qrow-why muted">captured — not yet linked to a concept</div>
}

// Relevance from the frontier priority score, normalized to the queue's top score.
function RelevanceBar({ score, max }: { score: number | null; max: number }) {
  if (score == null) return <div className="qrel none" title="captured, not yet scored" />
  const pct = Math.max(8, Math.round((score / max) * 100))
  return (
    <div className="qrel" title={`research priority score ${score}`}>
      <div className="qrel-track"><div className="qrel-fill" style={{ height: `${pct}%` }} /></div>
    </div>
  )
}
