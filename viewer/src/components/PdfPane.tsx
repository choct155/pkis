import { useCallback, useEffect, useRef, useState } from 'react'
import type { TouchEvent as RTouchEvent, TouchList as RTouchList } from 'react'
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

const MIN_ZOOM = 0.6
const MAX_ZOOM = 6

// A mobile-usable PDF pane: pdf.js renders to a canvas fit to width, but the user
// can ZOOM (buttons + pinch) and PAN — the app's viewport disables browser
// pinch-zoom, so the pane owns it. A transparent text layer over the canvas keeps
// text selectable for section-level annotation.
export default function PdfPane({ url, page, onSelectText, onLoaded }: Props) {
  const wrapRef = useRef<HTMLDivElement>(null)
  const pageRef = useRef<HTMLDivElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const textRef = useRef<HTMLDivElement>(null)
  const docRef = useRef<PDFDocumentProxy | null>(null)
  const taskRef = useRef<RenderTask | null>(null)
  const [ready, setReady] = useState(false)
  const [err, setErr] = useState(false)
  const [zoom, setZoom] = useState(1)        // multiplier on top of fit-to-width
  // Live pinch state: scale the page via CSS during the gesture (cheap), then
  // re-render crisp on release.
  const pinch = useRef<{ startDist: number; startZoom: number; live: number } | null>(null)

  // Load (and cache) the document once per URL.
  useEffect(() => {
    let cancelled = false
    setReady(false); setErr(false); setZoom(1)
    const loading = pdfjs.getDocument(url)
    loading.promise.then((doc) => {
      if (cancelled) { doc.destroy(); return }
      docRef.current = doc
      onLoaded?.(doc.numPages)
      setReady(true)
    }).catch(() => { if (!cancelled) setErr(true) })
    return () => { cancelled = true; loading.destroy(); docRef.current = null }
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
    const fitScale = Math.max(0.3, avail / base.width)
    const scale = fitScale * zoom
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
    if (pageRef.current) pageRef.current.style.transform = ''   // clear any pinch transform
  }, [page, zoom])

  useEffect(() => { if (ready) renderPage() }, [ready, page, zoom, renderPage])

  // Re-fit on resize / orientation change (debounced via rAF).
  useEffect(() => {
    let raf = 0
    const onResize = () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(() => renderPage()) }
    window.addEventListener('resize', onResize)
    window.addEventListener('orientationchange', onResize)
    return () => {
      window.removeEventListener('resize', onResize)
      window.removeEventListener('orientationchange', onResize)
      cancelAnimationFrame(raf)
    }
  }, [renderPage])

  const clamp = (z: number) => Math.min(MAX_ZOOM, Math.max(MIN_ZOOM, z))
  const zoomBy = (f: number) => setZoom((z) => clamp(z * f))

  // ── Pinch-to-zoom (the app disables native pinch) ──────────────────────
  const dist = (t: RTouchList) => Math.hypot(t[0].clientX - t[1].clientX, t[0].clientY - t[1].clientY)
  const onTouchStart = (e: RTouchEvent) => {
    if (e.touches.length === 2) {
      pinch.current = { startDist: dist(e.touches), startZoom: zoom, live: zoom }
    }
  }
  const onTouchMove = (e: RTouchEvent) => {
    if (e.touches.length === 2 && pinch.current) {
      e.preventDefault()
      const ratio = dist(e.touches) / pinch.current.startDist
      const live = clamp(pinch.current.startZoom * ratio)
      pinch.current.live = live
      // Cheap visual feedback: scale the already-rendered page; re-render on release.
      if (pageRef.current) pageRef.current.style.transform = `scale(${live / zoom})`
    }
  }
  const onTouchEnd = () => {
    if (pinch.current) {
      const live = pinch.current.live
      pinch.current = null
      setZoom(live)                       // commit → crisp re-render (clears transform)
      return
    }
    const t = window.getSelection?.()?.toString().trim()
    if (t && t.length > 1) onSelectText(t)
  }
  const handleMouseUp = () => {
    const t = window.getSelection?.()?.toString().trim()
    if (t && t.length > 1) onSelectText(t)
  }

  return (
    <div className="reader-pdf-wrap">
      <div
        className="reader-pdf-scroll"
        ref={wrapRef}
        onMouseUp={handleMouseUp}
        onTouchStart={onTouchStart}
        onTouchMove={onTouchMove}
        onTouchEnd={onTouchEnd}
      >
        {!ready && !err && <div className="reader-pdf-loading"><div className="loading-spinner" /> loading pdf…</div>}
        {err && <div className="reader-pdf-loading">couldn’t load the original pdf</div>}
        <div className="reader-pdf-page" ref={pageRef}>
          <canvas ref={canvasRef} />
          <div className="textLayer" ref={textRef} />
        </div>
      </div>
      {ready && !err && (
        <div className="reader-pdf-zoom">
          <button onClick={() => zoomBy(1 / 1.25)} aria-label="zoom out">−</button>
          <button onClick={() => setZoom(1)} aria-label="fit width" className="fit">{Math.round(zoom * 100)}%</button>
          <button onClick={() => zoomBy(1.25)} aria-label="zoom in">+</button>
        </div>
      )}
    </div>
  )
}
