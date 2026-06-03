// PKIS SW kill-switch.
// The previous service worker was cache-first over the HTML shell, which served a
// stale index.html pointing at asset hashes that later deploys removed -> blank screen.
// This version unregisters itself, clears all caches, and reloads open clients so the
// app loads fresh from the network. No fetch handler => it never serves cached content.
self.addEventListener('install', () => {
  self.skipWaiting()
})

self.addEventListener('activate', (event) => {
  event.waitUntil((async () => {
    try {
      const keys = await caches.keys()
      await Promise.all(keys.map((k) => caches.delete(k)))
      await self.registration.unregister()
      const clients = await self.clients.matchAll({ type: 'window' })
      clients.forEach((c) => c.navigate(c.url))
    } catch (e) {
      /* best effort */
    }
  })())
})
