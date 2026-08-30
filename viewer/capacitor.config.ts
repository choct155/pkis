import type { CapacitorConfig } from '@capacitor/cli'

// PKIS native shell config. The React/Vite UI is built to `app/dist/` (webDir)
// and bundled into the APK; the Flask backend is reached over the network
// (LAN/emulator in dev, VPN/HTTPS in prod) via VITE_API_BASE_URL — not served
// from here. Build the web bundle for native with `CAP_BUILD=1 npm run build`
// so Vite emits relative asset paths (base '') instead of the web '/app/' base.
const config: CapacitorConfig = {
  appId: 'com.pkis.app',
  appName: 'PKIS',
  webDir: 'app/dist',
  // Load the UI from the LIVE site instead of the bundled webDir, so frontend
  // deploys reach the phone on next launch — no APK rebuild for UI changes ever
  // again. The WebView origin becomes pkis.clowderpack.dev, so API calls to
  // /pkis-api are same-origin (no CapacitorHttp cross-origin workaround needed) and
  // auth still uses the native Bearer/PKCE flow (isNative() is a platform check, not
  // origin-based). index.html is served no-store, so each launch pulls the latest.
  // The bundled webDir remains only as a build artifact; server.url takes over.
  server: {
    url: 'https://pkis.clowderpack.dev/app/',
    cleartext: false,
  },
  plugins: {
    // The UI is served from https://localhost inside the WebView, but the API may
    // be plain HTTP on the LAN — a mixed-content + cross-origin request the WebView
    // blocks. CapacitorHttp patches window.fetch to make the call from native code,
    // sidestepping both. Cleartext (HTTP) is still gated by the Android network
    // security config; prod should use HTTPS.
    CapacitorHttp: {
      enabled: true,
    },
  },
}

export default config
