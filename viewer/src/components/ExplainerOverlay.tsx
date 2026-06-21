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
  // Cache-bust token: bumping it re-pulls the latest published explainer (the
  // iframe is keyed on it, so it remounts). Lets you watch edits land in PKIS
  // context after `explainer_publish.sh`, without closing/reopening the overlay.
  const [bust, setBust] = useState(0)
  const url = `/pkis-api/viz/${slug}.html${bust ? `?v=${bust}` : ''}`

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
        <button className="explainer-overlay-pop" onClick={() => setBust(Date.now())} title="Reload latest (re-pull after publishing)">⟳</button>
        <a className="explainer-overlay-pop" href={url} target="_blank" rel="noreferrer" title="Open in new tab">↗</a>
        <button className="explainer-overlay-close" onClick={onClose} title="Close (Esc)">✕</button>
      </div>
      <iframe
        key={bust}
        className="explainer-overlay-frame"
        src={url}
        sandbox="allow-scripts allow-popups"
        title={title || t}
      />
    </div>
  )
}
