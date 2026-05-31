// PKIS PWA Service Worker — app shell cache
const CACHE = 'pkis-v1'
const APP_SHELL = [
  '/app/',
  '/app/index.html',
]

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(APP_SHELL))
  )
  self.skipWaiting()
})

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  )
  self.clients.claim()
})

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url)

  // Never cache API calls
  if (url.pathname.startsWith('/pkis-api')) return

  // Cache-first for static assets
  e.respondWith(
    caches.match(e.request).then((cached) => {
      if (cached) return cached
      return fetch(e.request).then((res) => {
        if (res.ok && e.request.method === 'GET') {
          const clone = res.clone()
          caches.open(CACHE).then((c) => c.put(e.request, clone))
        }
        return res
      }).catch(() => caches.match('/app/index.html'))
    })
  )
})
