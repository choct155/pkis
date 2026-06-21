import { useEffect, useRef, useState } from 'react'
import { getNode } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'

interface Props {
  iri: string
  title?: string
  onClose: () => void
}

// Full-screen reader for `format: writing` assets (position papers, notes, …).
// Renders the asset node's markdown body, reusing the explainer-overlay chrome
// and the Docs prose styles. Esc closes.
export default function WritingOverlay({ iri, title, onClose }: Props) {
  const [md, setMd] = useState<string | null>(null)
  const [err, setErr] = useState<string | null>(null)
  const [t, setT] = useState(title || 'Document')
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    getNode(iri)
      .then((n) => {
        setMd(n.content || '')
        const nt = n.frontmatter?.title
        if (nt) setT(nt)
      })
      .catch((e) => setErr(String(e)))
  }, [iri])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') onClose() }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onClose])

  useEffect(() => { if (md != null) renderMath(ref.current) }, [md])

  return (
    <div className="explainer-overlay">
      <div className="explainer-overlay-bar">
        <span className="explainer-overlay-title">{t}</span>
        <button className="explainer-overlay-close" onClick={onClose} title="Close (Esc)">✕</button>
      </div>
      <div className="writing-overlay-scroll">
        {err ? (
          <div className="empty-state">Couldn’t load: {err}</div>
        ) : md == null ? (
          <div className="empty-state">Loading…</div>
        ) : (
          <article
            ref={ref}
            className="body-text prose writing-article"
            dangerouslySetInnerHTML={{ __html: renderMarkdown(md) }}
          />
        )}
      </div>
    </div>
  )
}
