import { useCallback, useEffect, useRef, useState } from 'react'
import * as pdfjs from 'pdfjs-dist'
import workerSrc from 'pdfjs-dist/build/pdf.worker.min.js?url'
import 'pdfjs-dist/web/pdf_viewer.css'   // text-layer span positioning + selection
import type { PDFDocumentProxy, RenderTask } from 'pdfjs-dist'

// pdf.js renders the page text off the main thread; point it at the bundled worker.
pdfjs.GlobalWorkerOptions.workerSrc = workerSrc

interface Props {
  url: string
  page: number                       // controlled: the page to display (1-based)
  onSelectText: (text: string) => void
  onLoaded?: (numPages: number) => void
}

// A buttery PDF pane: pdf.js renders straight to a canvas (no iframe reload on
// page change) with a transparent, selectable text layer over it so highlighting
// text in the original document drives section-level annotation.
export default function PdfPane({ url, page, onSelectText, onLoaded }: Props) {
  const wrapRef = useRef<HTMLDivElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const textRef = useRef<HTMLDivElement>(null)
  const docRef = useRef<PDFDocumentProxy | null>(null)
  const taskRef = useRef<RenderTask | null>(null)
  const [ready, setReady] = useState(false)
  const [err, setErr] = useState(false)

  // Load (and cache) the document once per URL.
  useEffect(() => {
    let cancelled = false
    setReady(false); setErr(false)
    const loading = pdfjs.getDocument(url)
    loading.promise.then((doc) => {
      if (cancelled) { doc.destroy() ; return }
      docRef.current = doc
      onLoaded?.(doc.numPages)
      setReady(true)
    }).catch(() => { if (!cancelled) setErr(true) })
    return () => {
      cancelled = true
      loading.destroy()
      docRef.current = null
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [url])

  // Render the current page to canvas + overlay a selectable text layer.
  const renderPage = useCallback(async () => {
    const doc = docRef.current, canvas = canvasRef.current, wrap = wrapRef.current
    if (!doc || !canvas || !wrap) return
    const n = Math.min(Math.max(1, page), doc.numPages)
    const pg = await doc.getPage(n)
    const avail = wrap.clientWidth - 16
    const base = pg.getViewport({ scale: 1 })
    const scale = Math.max(0.3, avail / base.width)
    const viewport = pg.getViewport({ scale })
    const dpr = window.devicePixelRatio || 1
    const ctx = canvas.getContext('2d')
    if (!ctx) return

    canvas.width = Math.floor(viewport.width * dpr)
    canvas.height = Math.floor(viewport.height * dpr)
    canvas.style.width = `${Math.floor(viewport.width)}px`
    canvas.style.height = `${Math.floor(viewport.height)}px`

    if (taskRef.current) { try { taskRef.current.cancel() } catch { /* superseded */ } }
    const task = pg.render({
      canvasContext: ctx,
      viewport,
      transform: dpr !== 1 ? [dpr, 0, 0, dpr, 0, 0] : undefined,
    })
    taskRef.current = task
    try { await task.promise } catch { return /* cancelled by a newer render */ }

    const tdiv = textRef.current
    if (tdiv) {
      tdiv.innerHTML = ''
      tdiv.style.width = `${Math.floor(viewport.width)}px`
      tdiv.style.height = `${Math.floor(viewport.height)}px`
      tdiv.style.setProperty('--scale-factor', String(scale))
      const tc = await pg.getTextContent()
      pdfjs.renderTextLayer({ textContentSource: tc, container: tdiv, viewport })
    }
    wrap.scrollTop = 0
  }, [page])

  useEffect(() => { if (ready) renderPage() }, [ready, page, renderPage])

  // Re-fit on resize (debounced via rAF).
  useEffect(() => {
    let raf = 0
    const onResize = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(() => renderPage()) }
    window.addEventListener('resize', onResize)
    return () => { window.removeEventListener('resize', onResize); cancelAnimationFrame(raf) }
  }, [renderPage])

  const handleSelect = () => {
    const t = window.getSelection?.()?.toString().trim()
    if (t && t.length > 1) onSelectText(t)
  }

  return (
    <div className="reader-pdf-scroll" ref={wrapRef} onMouseUp={handleSelect} onTouchEnd={handleSelect}>
      {!ready && !err && <div className="reader-pdf-loading"><div className="loading-spinner" /> loading pdf…</div>}
      {err && <div className="reader-pdf-loading">couldn’t load the original pdf</div>}
      <div className="reader-pdf-page">
        <canvas ref={canvasRef} />
        <div className="textLayer" ref={textRef} />
      </div>
    </div>
  )
}
