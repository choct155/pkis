import React, { useEffect, useState } from 'react'
import ReactDOM from 'react-dom/client'
import { Capacitor } from '@capacitor/core'
import { SendIntent } from 'send-intent'
import App from './App'
import ShareView from './views/ShareView'
import ShareIngestView from './views/ShareIngestView'
import type { ShareInput } from './lib/shareClassify'
import './index.css'

// Lightweight routing via query params (no router dep). A `?s=<token>` link renders the
// public, read-only ShareView. On native, a share from the Android share sheet renders
// the ShareIngestView review card.
const shareToken = new URLSearchParams(window.location.search).get('s')

// Service workers are DISABLED (a prior cache-first SW poisoned the app shell).
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations()
    .then((regs) => regs.forEach((r) => r.unregister()))
    .catch(() => {})
}

interface Intent { title?: string; description?: string; url?: string; type?: string }
const toShareInput = (i: Intent): ShareInput =>
  ({ title: i.title, text: i.description, url: i.url, type: i.type })

function Root() {
  const [share, setShare] = useState<ShareInput | null>(null)

  useEffect(() => {
    if (!Capacitor.isNativePlatform()) return
    const check = () =>
      SendIntent.checkSendIntentReceived()
        .then((i) => { if (i && (i.url || i.title || i.description)) setShare(toShareInput(i as Intent)) })
        .catch(() => {})
    check()                                             // cold start via a share
    window.addEventListener('sendIntentReceived', check) // shared while already running
    return () => window.removeEventListener('sendIntentReceived', check)
  }, [])

  if (shareToken) return <ShareView token={shareToken} />
  if (share) {
    const done = () => { setShare(null); try { SendIntent.finish() } catch { /* web/no-op */ } }
    return <ShareIngestView input={share} onDone={done} />
  }
  return <App />
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>,
)
