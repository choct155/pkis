import { useEffect, useRef } from 'react'
import { getRelated } from '../lib/api'
import type { RelatedEntry } from '../types'

const TYPE_COLORS: Record<string, string> = {
  concept:   '#4f8ef7',
  technique: '#34c97a',
  result:    '#f5a623',
  framework: '#b06af5',
  problem:   '#e85c5c',
  principle: '#4ecdc4',
  source:    '#a8b3be',
}

interface CanvasNode {
  iri: string
  label: string
  type: string
  x: number
  y: number
  r: number
  isFocus: boolean
}

interface CanvasEdge {
  from: string
  to: string
}

function buildLayout(
  focusIri: string,
  focusTitle: string,
  focusType: string,
  related: RelatedEntry[]
): { nodes: CanvasNode[]; edges: CanvasEdge[] } {
  const nodes: CanvasNode[] = []
  const edges: CanvasEdge[] = []
  const MAX = 8
  const slice = related.slice(0, MAX)

  nodes.push({
    iri: focusIri,
    label: focusTitle,
    type: focusType,
    x: 0.5,
    y: 0.5,
    r: 18,
    isFocus: true,
  })

  slice.forEach((rel, i) => {
    const angle = (2 * Math.PI * i) / slice.length - Math.PI / 2
    nodes.push({
      iri: rel.iri,
      label: rel.canonical_title,
      type: rel.edge_type,
      x: 0.5 + 0.33 * Math.cos(angle),
      y: 0.5 + 0.38 * Math.sin(angle),
      r: 12,
      isFocus: false,
    })
    edges.push({ from: focusIri, to: rel.iri })
  })

  return { nodes, edges }
}

function drawGraph(
  canvas: HTMLCanvasElement,
  nodes: CanvasNode[],
  edges: CanvasEdge[],
  hoveredIri: string | null
) {
  const W = canvas.width
  const H = canvas.height
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.clearRect(0, 0, W, H)

  // Draw edges
  edges.forEach((e) => {
    const a = nodes.find((n) => n.iri === e.from)
    const b = nodes.find((n) => n.iri === e.to)
    if (!a || !b) return
    ctx.beginPath()
    ctx.moveTo(a.x * W, a.y * H)
    ctx.lineTo(b.x * W, b.y * H)
    ctx.strokeStyle = 'rgba(58,63,69,0.7)'
    ctx.lineWidth = 1
    ctx.stroke()
  })

  // Draw nodes
  nodes.forEach((n) => {
    const cx = n.x * W
    const cy = n.y * H
    const color = TYPE_COLORS[n.type] ?? '#6b7280'
    const isHovered = n.iri === hoveredIri

    // Glow for focus node
    if (n.isFocus) {
      ctx.beginPath()
      ctx.arc(cx, cy, n.r + 4, 0, Math.PI * 2)
      ctx.fillStyle = `${color}22`
      ctx.fill()
    }

    // Circle
    ctx.beginPath()
    ctx.arc(cx, cy, n.r, 0, Math.PI * 2)
    ctx.fillStyle = n.isFocus ? `${color}22` : 'rgba(20,22,24,0.9)'
    ctx.fill()
    ctx.strokeStyle = isHovered ? color : (n.isFocus ? color : `${color}88`)
    ctx.lineWidth = n.isFocus ? 2 : 1.5
    ctx.stroke()

    // Label
    const fontSize = n.isFocus ? 9 : 7
    const words = n.label.split(' ')
    const shortLabel =
      words.length > 2 ? words.slice(0, 2).join(' ') + '…' : n.label
    ctx.fillStyle = isHovered ? '#eef0f2' : color
    ctx.font = `${fontSize}px 'IBM Plex Mono', monospace`
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    ctx.fillText(shortLabel, cx, cy)
  })
}

interface Props {
  focusIri: string
  focusTitle: string
  focusType: string
  onNavigate: (iri: string) => void
}

export default function GraphMini({ focusIri, focusTitle, focusType, onNavigate }: Props) {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const nodesRef = useRef<CanvasNode[]>([])
  const hoveredRef = useRef<string | null>(null)

  useEffect(() => {
    let cancelled = false
    const canvas = canvasRef.current
    if (!canvas) return

    const observer = new ResizeObserver(() => {
      const W = canvas.parentElement?.clientWidth ?? 300
      const H = canvas.parentElement?.clientHeight ?? 200
      canvas.width = W
      canvas.height = H
      drawGraph(canvas, nodesRef.current, [], hoveredRef.current)
    })
    observer.observe(canvas.parentElement!)

    getRelated(focusIri, { max_hops: 1 }).then((related: RelatedEntry[]) => {
      if (cancelled) return
      const { nodes, edges } = buildLayout(focusIri, focusTitle, focusType, related)
      nodesRef.current = nodes
      const W = canvas.parentElement?.clientWidth ?? 300
      const H = canvas.parentElement?.clientHeight ?? 200
      canvas.width = W
      canvas.height = H
      drawGraph(canvas, nodes, edges, null)
    }).catch(() => {
      // silently fail — show empty canvas
    })

    return () => { cancelled = true; observer.disconnect() }
  }, [focusIri, focusTitle, focusType])

  const handleClick = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current
    if (!canvas) return
    const rect = canvas.getBoundingClientRect()
    const mx = e.clientX - rect.left
    const my = e.clientY - rect.top
    const W = canvas.width
    const H = canvas.height

    for (const n of nodesRef.current) {
      const cx = n.x * W
      const cy = n.y * H
      const dist = Math.hypot(mx - cx, my - cy)
      if (dist < n.r + 4 && !n.isFocus) {
        onNavigate(n.iri)
        return
      }
    }
  }

  const handleMouseMove = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current
    if (!canvas) return
    const rect = canvas.getBoundingClientRect()
    const mx = e.clientX - rect.left
    const my = e.clientY - rect.top
    const W = canvas.width
    const H = canvas.height
    let found: string | null = null
    for (const n of nodesRef.current) {
      if (n.isFocus) continue
      const dist = Math.hypot(mx - n.x * W, my - n.y * H)
      if (dist < n.r + 4) { found = n.iri; break }
    }
    if (found !== hoveredRef.current) {
      hoveredRef.current = found
      canvas.style.cursor = found ? 'pointer' : 'default'
    }
  }

  return (
    <div className="graph-mini-wrap">
      <canvas
        ref={canvasRef}
        className="graph-mini-canvas"
        onClick={handleClick}
        onMouseMove={handleMouseMove}
      />
      <div className="graph-mini-label">
        ego-network · {focusTitle.toLowerCase().split(' ').slice(0, 2).join(' ')}
      </div>
    </div>
  )
}
