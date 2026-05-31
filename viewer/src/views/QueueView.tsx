import { useEffect, useState } from 'react'
import { getReadingQueue } from '../lib/api'
import type { QueueItem } from '../types'

interface Props {
  onSelectNode: (iri: string) => void
}

export default function QueueView({ onSelectNode }: Props) {
  const [queue, setQueue] = useState<QueueItem[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let cancelled = false
    setLoading(true)
    getReadingQueue().then((q: QueueItem[]) => {
      if (!cancelled) { setQueue(q); setLoading(false) }
    }).catch(() => { if (!cancelled) setLoading(false) })
    return () => { cancelled = true }
  }, [])

  const high   = queue.filter((q) => q.priority === 'high')
  const normal = queue.filter((q) => q.priority !== 'high')

  if (loading) {
    return (
      <div className="loading-row">
        <div className="loading-spinner" /> loading queue…
      </div>
    )
  }

  if (queue.length === 0) {
    return <div className="empty-state">queue is empty</div>
  }

  return (
    <div>
      {high.length > 0 && (
        <>
          <div className="section-label">high priority</div>
          {high.map((item, i) => (
            <QueueRow key={i} item={item} onSelect={onSelectNode} />
          ))}
        </>
      )}
      {normal.length > 0 && (
        <>
          <div className="section-label">normal</div>
          {normal.map((item, i) => (
            <QueueRow key={i} item={item} onSelect={onSelectNode} />
          ))}
        </>
      )}
    </div>
  )
}

function QueueRow({ item, onSelect }: { item: QueueItem; onSelect: (iri: string) => void }) {
  return (
    <div
      className="queue-item"
      onClick={() => onSelect(`pkis:source:${item.slug}`)}
    >
      <div className={`queue-priority prio-${item.priority}`} />
      <div className="queue-info">
        <div className="queue-title">{item.slug}</div>
        {item.reason && <div className="queue-reason">{item.reason}</div>}
      </div>
      <div className="queue-action">read →</div>
    </div>
  )
}
