import { useMemo } from 'react'
import type { DocMeta } from '../types'

// The grouped doc list (category → docs) with active-doc highlighting. Pure
// content, no positioning — the parent decides whether it's a desktop sticky
// rail (DocsView) or the contents of the mobile nav drawer (NavDrawer).
export default function DocsTree({
  manifest, selected, onSelect,
}: {
  manifest: DocMeta[]
  selected: string | null
  onSelect: (key: string) => void
}) {
  const groups = useMemo(() => {
    const order: string[] = []
    const byCat = new Map<string, DocMeta[]>()
    manifest.forEach((d) => {
      if (!byCat.has(d.category)) { byCat.set(d.category, []); order.push(d.category) }
      byCat.get(d.category)!.push(d)
    })
    return order.map((c) => ({ category: c, docs: byCat.get(c)! }))
  }, [manifest])

  return (
    <nav className="doctree">
      <div className="doctree-head">Docs</div>
      {groups.map(({ category, docs }) => (
        <div key={category} className="doctree-group">
          <div className="doctree-cat">{category}</div>
          {docs.map((d) => (
            <div
              key={d.key}
              className={`doctree-item${d.key === selected ? ' active' : ''}`}
              onClick={() => onSelect(d.key)}
            >
              {d.title}
            </div>
          ))}
        </div>
      ))}
    </nav>
  )
}
