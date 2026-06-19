import { useEffect, useMemo, useRef, useState } from 'react'
import type { DocMeta, Doc } from '../types'
import { getDocs, getDoc } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'

// Mobile-first documentation reader. Lists the manifest grouped by category;
// tapping a doc loads and renders its markdown. Relative `.md` cross-links
// navigate within this view (resolved to manifest keys by filename).
export default function DocsView() {
  const [manifest, setManifest] = useState<DocMeta[] | null>(null)
  const [selected, setSelected] = useState<string | null>(null)
  const [doc, setDoc] = useState<Doc | null>(null)
  const [err, setErr] = useState<string | null>(null)        // fatal: manifest failed
  const [docErr, setDocErr] = useState<string | null>(null)  // scoped: one doc failed

  useEffect(() => {
    getDocs().then(setManifest).catch((e) => setErr(String(e)))
  }, [])

  useEffect(() => {
    if (!selected) { setDoc(null); setDocErr(null); return }
    setDoc(null); setDocErr(null)
    getDoc(selected).then(setDoc).catch((e) => setDocErr(String(e)))
  }, [selected])

  // filename (e.g. "USAGE.md") → manifest key, for resolving cross-links.
  const keyByFile = useMemo(() => {
    const m = new Map<string, string>()
    manifest?.forEach((d) => m.set(d.path.split('/').pop()!.toLowerCase(), d.key))
    return m
  }, [manifest])

  // Categories in first-seen manifest order.
  const categories = useMemo(() => {
    const order: string[] = []
    const byCat = new Map<string, DocMeta[]>()
    manifest?.forEach((d) => {
      if (!byCat.has(d.category)) { byCat.set(d.category, []); order.push(d.category) }
      byCat.get(d.category)!.push(d)
    })
    return order.map((c) => ({ category: c, docs: byCat.get(c)! }))
  }, [manifest])

  if (err) return <div className="empty-state">Couldn’t load docs: {err}</div>
  if (!manifest) return <div className="empty-state">Loading…</div>

  if (selected) {
    return (
      <div className="docs-view docs-reading">
        <div className="docs-bar">
          <button className="docs-back" onClick={() => setSelected(null)}>← all docs</button>
        </div>
        {docErr ? (
          <div className="empty-state">Couldn’t load this doc: {docErr}</div>
        ) : !doc ? (
          <div className="empty-state">Loading…</div>
        ) : (
          <article className="docs-article">
            <DocBody md={doc.markdown} keyByFile={keyByFile} onNavigate={setSelected} />
          </article>
        )}
      </div>
    )
  }

  return (
    <div className="docs-view">
      {categories.map(({ category, docs }) => (
        <section key={category} className="docs-section">
          <h3 className="docs-cat">{category}</h3>
          <div className="docs-list">
            {docs.map((d) => (
              <div key={d.key} className="docs-item node-card" onClick={() => setSelected(d.key)}>
                <span className="docs-item-title">{d.title}</span>
              </div>
            ))}
          </div>
        </section>
      ))}
    </div>
  )
}

function DocBody({
  md, keyByFile, onNavigate,
}: { md: string; keyByFile: Map<string, string>; onNavigate: (key: string) => void }) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => {
    renderMath(ref.current)
    ref.current?.querySelectorAll('a[href]').forEach((a) => {
      const href = a.getAttribute('href') || ''
      const file = href.split('#')[0].split('/').pop()?.toLowerCase() || ''
      const key = file.endsWith('.md') ? keyByFile.get(file) : undefined
      if (key) {
        // Internal doc cross-link → navigate within the Docs view.
        a.addEventListener('click', (e) => { e.preventDefault(); onNavigate(key) })
      } else if (/^https?:\/\//.test(href)) {
        a.setAttribute('target', '_blank')
        a.setAttribute('rel', 'noreferrer')
      }
    })
  }, [md, keyByFile, onNavigate])
  return <div ref={ref} className="body-text prose" dangerouslySetInnerHTML={{ __html: html }} />
}
