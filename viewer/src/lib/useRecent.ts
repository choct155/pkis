import { useCallback, useEffect, useState } from 'react'

// Recently-viewed nodes, persisted to localStorage so the desktop context rail
// can offer a "jump back" list. Capped + de-duplicated, most-recent first.
export interface RecentNode { iri: string; title: string }

const KEY = 'pkis.recent'
const MAX = 8

function load(): RecentNode[] {
  try {
    const v = JSON.parse(localStorage.getItem(KEY) || '[]')
    return Array.isArray(v) ? v.filter((r) => r && r.iri) : []
  } catch {
    return []
  }
}

export function useRecent() {
  const [items, setItems] = useState<RecentNode[]>(load)

  // Keep multiple tabs in sync.
  useEffect(() => {
    const h = (e: StorageEvent) => { if (e.key === KEY) setItems(load()) }
    window.addEventListener('storage', h)
    return () => window.removeEventListener('storage', h)
  }, [])

  const record = useCallback((iri: string, title: string) => {
    if (!iri) return
    setItems((prev) => {
      const next = [{ iri, title: title || iri }, ...prev.filter((r) => r.iri !== iri)].slice(0, MAX)
      try { localStorage.setItem(KEY, JSON.stringify(next)) } catch { /* quota / private mode */ }
      return next
    })
  }, [])

  return { items, record }
}
