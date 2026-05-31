import { useState, useRef, useEffect } from 'react'

interface Props {
  slug: string
}

export default function VizPanel({ slug }: Props) {
  const [open, setOpen] = useState(false)
  const [title, setTitle] = useState('Visualization')
  const [paused, setPaused] = useState(false)
  const iframeRef = useRef<HTMLIFrameElement>(null)

  useEffect(() => {
    const handler = (e: MessageEvent) => {
      if (e.data?.type === 'viz-ready') {
        setTitle(e.data.title ?? 'Visualization')
      }
    }
    window.addEventListener('message', handler)
    return () => window.removeEventListener('message', handler)
  }, [])

  const sendMsg = (msg: unknown) => {
    iframeRef.current?.contentWindow?.postMessage(msg, '*')
  }

  const handlePauseResume = () => {
    const next = !paused
    setPaused(next)
    sendMsg({ type: next ? 'pause' : 'resume' })
  }

  const handleReset = () => {
    setPaused(false)
    sendMsg({ type: 'reset' })
  }

  return (
    <>
      <div
        className={`viz-toggle${open ? ' open' : ''}`}
        onClick={() => setOpen((o) => !o)}
      >
        <span className="viz-toggle-icon">◈</span>
        <span className="viz-toggle-label">{title}</span>
        <span className="viz-toggle-chevron">▼</span>
      </div>

      {open && (
        <div className="viz-panel">
          <div className="viz-toolbar">
            <span className="viz-title">{title}</span>
            <button
              className={`viz-btn${!paused ? ' active' : ''}`}
              onClick={handlePauseResume}
            >
              {paused ? '▶ run' : '⏸ pause'}
            </button>
            <button className="viz-btn" onClick={handleReset}>
              ↺ reset
            </button>
          </div>
          <div className="viz-iframe-wrap">
            <iframe
              ref={iframeRef}
              className="viz-iframe"
              src={`/pkis-api/viz/${slug}.html`}
              sandbox="allow-scripts"
              title={title}
            />
          </div>
        </div>
      )}
    </>
  )
}
