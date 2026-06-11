import { useEffect, useState } from 'react'

interface Props {
  slug: string
  title?: string
  onClose: () => void
}

// Full-screen viewer for full-page HTML explainers (kind: explainer). Mobile =
// edge-to-edge; desktop = centered max-width panel (see index.css). A ↗ pops the
// raw page out to a new tab. Esc closes.
export default function ExplainerOverlay({ slug, title, onClose }: Props) {
  const [t, setT] = useState(title || 'Explainer')
  const url = `/pkis-api/viz/${slug}.html`

  useEffect(() => {
    const onMsg = (e: MessageEvent) => {
      if (e.data?.type === 'viz-ready' && e.data.title) setT(e.data.title)
    }
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') onClose() }
    window.addEventListener('message', onMsg)
    window.addEventListener('keydown', onKey)
    return () => {
      window.removeEventListener('message', onMsg)
      window.removeEventListener('keydown', onKey)
    }
  }, [onClose])

  return (
    <div className="explainer-overlay">
      <div className="explainer-overlay-bar">
        <span className="explainer-overlay-title">{title || t}</span>
        <a className="explainer-overlay-pop" href={url} target="_blank" rel="noreferrer" title="Open in new tab">↗</a>
        <button className="explainer-overlay-close" onClick={onClose} title="Close (Esc)">✕</button>
      </div>
      <iframe
        className="explainer-overlay-frame"
        src={url}
        sandbox="allow-scripts allow-popups"
        title={title || t}
      />
    </div>
  )
}
