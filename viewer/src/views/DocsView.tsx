import { useEffect, useMemo, useRef, useState } from 'react'
import type { DocMeta, Doc } from '../types'
import { getDoc } from '../lib/api'
import { renderMarkdown } from '../lib/markdown'
import { renderMath } from '../lib/katex'
import DocsTree from '../components/DocsTree'

// MkDocs-style documentation reader: a persistent doc tree (desktop left rail),
// the article (center), and an in-page table of contents (right) with scroll-spy.
// The doc tree + selection are owned by App so the mobile nav drawer can host the
// same tree; on mobile the rail is hidden and the drawer takes over.
//
// Heading anchors/ids are generated here (the shared markdown renderer emits
// plain <h2>/<h3>), which also powers the TOC and scroll-spy.

interface TocEntry { id: string; text: string; level: number }

interface Props {
  manifest: DocMeta[] | null
  selected: string | null
  onSelect: (key: string) => void
}

export default function DocsView({ manifest, selected, onSelect }: Props) {
  const [doc, setDoc] = useState<Doc | null>(null)
  const [docErr, setDocErr] = useState<string | null>(null)  // scoped: one doc failed
  const [toc, setToc] = useState<TocEntry[]>([])
  const [activeId, setActiveId] = useState<string | null>(null)

  const articleRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!selected) { setDoc(null); setDocErr(null); return }
    setDoc(null); setDocErr(null); setToc([]); setActiveId(null)
    getDoc(selected).then(setDoc).catch((e) => setDocErr(String(e)))
  }, [selected])

  // Navigate to a doc and scroll the article back to the top.
  function go(key: string) {
    onSelect(key)
    articleRef.current?.closest('.main')?.scrollTo({ top: 0 })
  }

  // filename (e.g. "USAGE.md") → manifest key, for resolving cross-links.
  const keyByFile = useMemo(() => {
    const m = new Map<string, string>()
    manifest?.forEach((d) => m.set(d.path.split('/').pop()!.toLowerCase(), d.key))
    return m
  }, [manifest])

  // Scroll-spy: highlight the TOC entry for the heading nearest the top of the
  // scroll container. Re-bound whenever the heading set changes.
  useEffect(() => {
    if (!toc.length) return
    const scroller = articleRef.current?.closest('.main') as HTMLElement | null
    if (!scroller) return
    const onScroll = () => {
      const top = scroller.getBoundingClientRect().top + 96
      let current = toc[0].id
      for (const h of toc) {
        const el = document.getElementById(h.id)
        if (el && el.getBoundingClientRect().top <= top) current = h.id
        else break
      }
      setActiveId(current)
    }
    onScroll()
    scroller.addEventListener('scroll', onScroll, { passive: true })
    return () => scroller.removeEventListener('scroll', onScroll)
  }, [toc])

  function tocClick(e: React.MouseEvent, id: string) {
    e.preventDefault()
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }

  if (!manifest) return <div className="empty-state">Loading…</div>

  return (
    <div className="docs-shell">
      {/* Desktop-only sticky rail; on mobile the doc tree lives in the nav drawer. */}
      <div className="docs-rail">
        <DocsTree manifest={manifest} selected={selected} onSelect={go} />
      </div>

      <article ref={articleRef} className="docs-article">
        {docErr ? (
          <div className="empty-state">Couldn’t load this doc: {docErr}</div>
        ) : !doc ? (
          <div className="empty-state">Loading…</div>
        ) : (
          <DocBody md={doc.markdown} keyByFile={keyByFile} onNavigate={go} onToc={setToc} />
        )}
      </article>

      <aside className="docs-toc">
        {toc.length > 0 && (
          <>
            <div className="docs-toc-label">On this page</div>
            <ul className="docs-toc-list">
              {toc.map((h) => (
                <li key={h.id} className={`docs-toc-l${h.level}`}>
                  <a
                    href={`#${h.id}`}
                    className={h.id === activeId ? 'active' : ''}
                    onClick={(e) => tocClick(e, h.id)}
                  >
                    {h.text}
                  </a>
                </li>
              ))}
            </ul>
          </>
        )}
      </aside>
    </div>
  )
}

// slugify heading text → a stable, URL-ish id.
function slugify(s: string): string {
  return s.toLowerCase().trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '') || 'section'
}

function DocBody({
  md, keyByFile, onNavigate, onToc,
}: {
  md: string
  keyByFile: Map<string, string>
  onNavigate: (key: string) => void
  onToc: (toc: TocEntry[]) => void
}) {
  const ref = useRef<HTMLDivElement>(null)
  const html = renderMarkdown(md)
  useEffect(() => {
    renderMath(ref.current)

    // Assign unique ids to h2/h3 and build the TOC.
    const seen = new Map<string, number>()
    const entries: TocEntry[] = []
    ref.current?.querySelectorAll('h2, h3').forEach((h) => {
      const text = h.textContent || ''
      let id = slugify(text)
      const n = seen.get(id) ?? 0
      seen.set(id, n + 1)
      if (n) id = `${id}-${n}`
      h.id = id
      entries.push({ id, text, level: h.tagName === 'H2' ? 2 : 3 })
    })
    onToc(entries)

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
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [md, keyByFile, onNavigate])
  return <div ref={ref} className="body-text prose" dangerouslySetInnerHTML={{ __html: html }} />
}
