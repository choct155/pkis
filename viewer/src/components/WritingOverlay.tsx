import { useCallback, useEffect, useRef, useState } from 'react'
import { getNode } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'

const esc = (v: string) =>
  v.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')

// Standalone styles for the downloaded file. Deliberately independent of the
// app's theme: these documents get forwarded and printed, so they render light,
// on any device, with no network fetch.
const DOC_CSS = `
:root { color-scheme: light }
body { margin: 0; background: #fff; color: #1a1a1a;
  font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  -webkit-text-size-adjust: 100% }
article { max-width: 46rem; margin: 0 auto; padding: 3rem 1.5rem 6rem }
h1, h2, h3, h4 { line-height: 1.25; margin: 2.2em 0 .6em; font-weight: 650 }
h1 { font-size: 2rem; margin-top: 0 }
h2 { font-size: 1.4rem; padding-bottom: .3em; border-bottom: 1px solid #e5e5e5 }
h3 { font-size: 1.15rem }
h4 { font-size: 1rem }
p, ul, ol, blockquote, table, pre { margin: 0 0 1.1em }
ul, ol { padding-left: 1.4em }
li { margin: .3em 0 }
a { color: #0b5cad }
strong { font-weight: 650 }
blockquote { margin-left: 0; padding: .1em 0 .1em 1.1em;
  border-left: 3px solid #d8d8d8; color: #444 }
code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: .89em; background: #f4f4f5; padding: .15em .35em; border-radius: 3px }
pre { background: #f7f7f8; padding: 1em; border-radius: 6px; overflow-x: auto }
pre code { background: none; padding: 0 }
table { border-collapse: collapse; width: 100%; display: block; overflow-x: auto }
th, td { border: 1px solid #e0e0e0; padding: .5em .7em; text-align: left; vertical-align: top }
th { background: #f7f7f8; font-weight: 650 }
hr { border: 0; border-top: 1px solid #e5e5e5; margin: 2.4em 0 }
img { max-width: 100% }
@media print { article { max-width: none; padding: 0 } a { color: inherit } }
`

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

  // Re-pull the node so edits land while the overlay stays open — the writing
  // counterpart to the explainer overlay's cache-bust reload. Explainers bust a
  // published file's URL; here there is no file, so we just re-fetch the node.
  const load = useCallback(() => {
    setMd(null)
    setErr(null)
    getNode(iri)
      .then((n) => {
        setMd(n.content || '')
        const nt = n.frontmatter?.title
        if (nt) setT(nt)
      })
      .catch((e) => setErr(String(e)))
  }, [iri])

  useEffect(() => { load() }, [load])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') onClose() }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onClose])

  useEffect(() => { if (md != null) renderMath(ref.current) }, [md])

  // Explainers download a published, self-contained HTML file; a writing asset
  // has no such file, so build one from the rendered article. We snapshot the
  // live DOM rather than re-render the markdown, so any KaTeX output comes along
  // already typeset, and inline the styles so the file stands alone once saved.
  const doDownload = () => {
    const article = ref.current
    if (article == null) return
    // KaTeX's own CSS (and its font files) can't be inlined here, so when the
    // article actually contains math, link the app's stylesheets by absolute URL
    // — equations then typeset for a reader who is online, and degrade to plain
    // markup for one who isn't. Math-free documents stay fully self-contained.
    const sheets = article.querySelector('.katex')
      ? Array.from(document.querySelectorAll<HTMLLinkElement>('link[rel="stylesheet"]'))
          .map((l) => `<link rel="stylesheet" href="${esc(l.href)}">`).join('')
      : ''
    const doc = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(t)}</title>
${sheets}
<style>${DOC_CSS}</style>
</head>
<body><article>${article.innerHTML}</article></body>
</html>`
    const url = URL.createObjectURL(new Blob([doc], { type: 'text/html' }))
    const a = document.createElement('a')
    a.href = url
    a.download = `${iri.split(':').pop() || 'document'}.html`
    a.click()
    URL.revokeObjectURL(url)
  }


  return (
    <div className="explainer-overlay">
      <div className="explainer-overlay-bar">
        <span className="explainer-overlay-title">{t}</span>
        <button className="explainer-overlay-pop" onClick={load} title="Reload latest">⟳</button>
        <button className="explainer-overlay-pop" onClick={doDownload} disabled={md == null} title="Download HTML">⤓</button>
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
