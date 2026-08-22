import { useEffect, useState } from 'react'
import { shareLink } from '../lib/share'

interface Props {
  slug: string
  title?: string
  onClose: () => void
}

// Full-screen viewer for full-page HTML explainers (kind: explainer). Mobile =
// edge-to-edge; desktop = centered max-width panel (see index.css). Esc closes.
export default function ExplainerOverlay({ slug, title, onClose }: Props) {
  const [t, setT] = useState(title || 'Explainer')
  const [toast, setToast] = useState<string | null>(null)
  // Cache-bust token: bumping it re-pulls the latest published explainer (the
  // iframe is keyed on it, so it remounts). Lets you watch edits land in PKIS
  // context after `explainer_publish.sh`, without closing/reopening the overlay.
  const [bust, setBust] = useState(0)
  // Clean, shareable URL (no cache-bust) — the /pkis-api/viz endpoint is public,
  // so this link works for colleagues who aren't signed in.
  const shareUrl = `/pkis-api/viz/${slug}.html`
  const url = `${shareUrl}${bust ? `?v=${bust}` : ''}`

  const flash = (m: string) => { setToast(m); setTimeout(() => setToast(null), 2000) }
  const doShare = async () => {
    const r = await shareLink(shareUrl, title || t)   // native sheet on mobile → clipboard fallback
    if (r === 'copied') flash('Link copied')
    else if (r === 'shared') flash('Shared')
    else if (r === 'failed') flash('Could not share')
  }

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
      {toast && <div className="explainer-overlay-toast">{toast}</div>}
      <div className="explainer-overlay-bar">
        <span className="explainer-overlay-title">{title || t}</span>
        <button className="explainer-overlay-pop" onClick={() => setBust(Date.now())} title="Reload latest (re-pull after publishing)">⟳</button>
        {/* Share via the OS sheet (reliable in the Android app, where target=_blank
            silently no-ops) with a clipboard fallback on desktop. */}
        <button className="explainer-overlay-pop" onClick={doShare} title="Share link">↗ share</button>
        {/* Download the self-contained HTML so it can be saved / sent as a file. */}
        <a className="explainer-overlay-pop" href={url} download={`${slug}.html`} title="Download HTML">⤓</a>
        <button className="explainer-overlay-close" onClick={onClose} title="Close (Esc)">✕</button>
      </div>
      <iframe
        key={bust}
        className="explainer-overlay-frame"
        src={url}
        // First-party, owner-authored HTML from our own origin. allow-same-origin
        // is required so interactive explainers that use storage / same-origin
        // fetch actually run (without it they render blank or half-broken).
        sandbox="allow-scripts allow-same-origin allow-popups allow-downloads"
        title={title || t}
      />
    </div>
  )
}
