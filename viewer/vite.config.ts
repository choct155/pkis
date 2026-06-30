import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  // Web build is served by nginx under '/app/'; the native (Capacitor) build
  // loads index.html from the WebView root, so it needs a relative base.
  // Build for native with `CAP_BUILD=1 npm run build`.
  base: process.env.CAP_BUILD ? '' : '/app/',
  plugins: [react()],
  build: {
    outDir: 'app/dist',
    emptyOutDir: true,
  },
  server: {
    proxy: {
      '/pkis-api': 'http://127.0.0.1:5000',
    },
  },
})
